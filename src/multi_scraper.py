import time
import logging
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs
from collections import deque
from typing import Set, List, Tuple, Optional
from scraper import DocumentationScraper
from converter import DocumentationConverter
from utils import sanitize_filename, get_safe_output_path

class MultiPageScraper:
    def __init__(self, base_url: str, output_dir: Path, max_pages: int = 50, 
                 same_domain_only: bool = True, respect_robots: bool = True):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.max_pages = max_pages
        self.same_domain_only = same_domain_only
        self.respect_robots = respect_robots
        self.visited_urls: Set[str] = set()
        self.failed_urls: Set[str] = set()
        self.queue = deque([base_url])
        self.scraped_count = 0
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        self.scraper = DocumentationScraper()
        self.converter = DocumentationConverter()
        
        # URL patterns for documentation sites
        self.doc_patterns = [
            r'/docs?/',
            r'/guide/',
            r'/tutorial/',
            r'/reference/',
            r'/api/',
            r'/manual/',
            r'/help/',
            r'/documentation/',
        ]
        
        # Patterns to exclude
        self.exclude_patterns = [
            r'/search',
            r'/login',
            r'/register',
            r'/contact',
            r'/download',
            r'/install',
            r'\.pdf$',
            r'\.zip$',
            r'\.tar\.gz$',
            r'#',  # Fragment-only URLs
        ]
        
    def is_valid_doc_url(self, url: str) -> bool:
        """Check if URL is a valid documentation page"""
        parsed_url = urlparse(url)
        
        # Same domain check
        if self.same_domain_only:
            base_domain = urlparse(self.base_url).netloc
            if parsed_url.netloc != base_domain:
                return False
        
        # Check if URL matches documentation patterns
        url_path = parsed_url.path.lower()
        
        # Must match at least one doc pattern
        doc_match = any(re.search(pattern, url_path) for pattern in self.doc_patterns)
        
        # Must not match exclude patterns
        exclude_match = any(re.search(pattern, url.lower()) for pattern in self.exclude_patterns)
        
        return doc_match and not exclude_match
    
    def extract_links_from_soup(self, soup, current_url: str) -> List[str]:
        """Extract valid documentation links from soup"""
        links = []
        
        # Common selectors for navigation links in documentation
        nav_selectors = [
            'nav a[href]',
            '.sidebar a[href]',
            '.navigation a[href]',
            '.toc a[href]',
            '.menu a[href]',
            '.docs-nav a[href]',
            '.doc-nav a[href]',
            '.side-nav a[href]',
            'aside a[href]',
            '[class*="nav"] a[href]',
            '[class*="menu"] a[href]',
            '[class*="sidebar"] a[href]',
        ]
        
        # Also get links from main content area
        content_selectors = [
            'main a[href]',
            'article a[href]',
            '.content a[href]',
            '.main-content a[href]',
            '.docs-content a[href]',
        ]
        
        all_selectors = nav_selectors + content_selectors
        
        for selector in all_selectors:
            for link in soup.select(selector):
                href = link.get('href')
                if href:
                    # Convert relative URLs to absolute
                    absolute_url = urljoin(current_url, href)
                    
                    # Clean URL (remove fragments, query params that aren't needed)
                    parsed = urlparse(absolute_url)
                    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                    
                    if self.is_valid_doc_url(clean_url) and clean_url not in self.visited_urls:
                        links.append(clean_url)
        
        return list(set(links))  # Remove duplicates
    
    def generate_filename(self, url: str, soup) -> str:
        """Generate a filename for the scraped page"""
        # Try to get page title
        title = ""
        if soup:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text().strip()
            elif soup.find('h1'):
                title = soup.find('h1').get_text().strip()
        
        # Fallback to URL path
        if not title:
            parsed_url = urlparse(url)
            path_parts = [p for p in parsed_url.path.split('/') if p]
            if path_parts:
                title = path_parts[-1] or path_parts[-2] if len(path_parts) > 1 else "index"
            else:
                title = "index"
        
        # Clean and sanitize filename
        filename = sanitize_filename(title)
        
        # Ensure uniqueness
        return get_safe_output_path(self.output_dir / f"{filename}.md").name
    
    def scrape_single_page(self, url: str) -> Tuple[bool, Optional[str], Optional[List[str]]]:
        """Scrape a single page and return success status, content, and found links"""
        try:
            self.logger.info(f"📄 Scraping: {url}")
            
            # Scrape the page
            soup = self.scraper.scrape_page(url, wait_time=3, timeout=30)
            
            if not soup:
                self.logger.warning(f"⚠️  Failed to scrape: {url}")
                return False, None, []
            
            # Convert to markdown
            markdown_content = self.converter.convert_to_markdown(soup)
            
            if not markdown_content or "Error:" in markdown_content:
                self.logger.warning(f"⚠️  Conversion failed for: {url}")
                return False, None, []
            
            # Extract links for further crawling
            links = self.extract_links_from_soup(soup, url)
            
            # Generate filename and save
            filename = self.generate_filename(url, soup)
            output_path = self.output_dir / filename
            
            # Add source URL as comment at the top
            final_content = f"<!-- Source: {url} -->\n\n{markdown_content}"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            self.logger.info(f"✅ Saved: {filename} ({len(markdown_content)} chars)")
            return True, filename, links
            
        except Exception as e:
            self.logger.error(f"❌ Error scraping {url}: {str(e)}")
            return False, None, []
    
    def run(self, wait_between_requests: float = 1.0) -> dict:
        """Run the multi-page scraping process"""
        self.logger.info(f"🚀 Starting multi-page scrape from: {self.base_url}")
        self.logger.info(f"📁 Output directory: {self.output_dir}")
        self.logger.info(f"📄 Max pages: {self.max_pages}")
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        scraped_files = []
        start_time = time.time()
        
        try:
            while self.queue and self.scraped_count < self.max_pages:
                current_url = self.queue.popleft()
                
                if current_url in self.visited_urls:
                    continue
                
                self.visited_urls.add(current_url)
                
                # Scrape the page
                success, filename, new_links = self.scrape_single_page(current_url)
                
                if success:
                    self.scraped_count += 1
                    scraped_files.append({
                        'url': current_url,
                        'filename': filename,
                        'path': str(self.output_dir / filename)
                    })
                    
                    # Add new links to queue
                    for link in new_links:
                        if link not in self.visited_urls and link not in self.queue:
                            self.queue.append(link)
                            self.logger.debug(f"➕ Added to queue: {link}")
                else:
                    self.failed_urls.add(current_url)
                
                # Progress update
                if self.scraped_count % 5 == 0:
                    self.logger.info(f"📊 Progress: {self.scraped_count}/{self.max_pages} pages scraped")
                
                # Rate limiting
                if wait_between_requests > 0:
                    time.sleep(wait_between_requests)
                    
        except KeyboardInterrupt:
            self.logger.info("⚠️  Scraping interrupted by user")
        except Exception as e:
            self.logger.error(f"❌ Unexpected error during scraping: {str(e)}")
        finally:
            self.scraper.close()
        
        # Generate summary
        elapsed_time = time.time() - start_time
        summary = {
            'scraped_count': self.scraped_count,
            'failed_count': len(self.failed_urls),
            'total_time': elapsed_time,
            'files': scraped_files,
            'failed_urls': list(self.failed_urls)
        }
        
        self.logger.info(f"🎉 Scraping completed!")
        self.logger.info(f"📊 Statistics:")
        self.logger.info(f"   ✅ Scraped: {summary['scraped_count']} pages")
        self.logger.info(f"   ❌ Failed: {summary['failed_count']} pages")
        self.logger.info(f"   ⏱️  Time: {elapsed_time:.1f} seconds")
        
        return summary
    
    def generate_index_file(self, summary: dict):
        """Generate an index file listing all scraped pages"""
        index_content = "# Documentation Index\n\n"
        index_content += f"Generated on {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        index_content += f"**Total pages scraped:** {summary['scraped_count']}\n"
        index_content += f"**Time taken:** {summary['total_time']:.1f} seconds\n\n"
        
        if summary['files']:
            index_content += "## Scraped Pages\n\n"
            for file_info in summary['files']:
                relative_path = Path(file_info['filename'])
                index_content += f"- [{file_info['filename']}](./{relative_path})\n"
                index_content += f"  - Source: {file_info['url']}\n\n"
        
        if summary['failed_urls']:
            index_content += "## Failed URLs\n\n"
            for url in summary['failed_urls']:
                index_content += f"- {url}\n"
        
        index_path = self.output_dir / "index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        self.logger.info(f"📋 Generated index file: {index_path}")