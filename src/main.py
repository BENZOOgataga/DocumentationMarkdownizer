import argparse
import os
import sys
import logging
from pathlib import Path
from scraper import DocumentationScraper
from converter import DocumentationConverter
from multi_scraper import MultiPageScraper
from utils import sanitize_filename, get_safe_output_path, setup_logging

def main():
    parser = argparse.ArgumentParser(
        description='Convert documentation page(s) to Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single page conversion
  python src/main.py https://docs.example.com/api
  python src/main.py https://docs.example.com/api -o custom-name.md
  
  # Multi-page documentation scraping
  python src/main.py https://docs.example.com/guide --multi-page --max-pages 20
  python src/main.py https://docs.example.com --multi-page --output-path="./full-docs"
  
  # Advanced options
  python src/main.py https://docs.example.com/api --wait 10 --no-headless
        """
    )
    
    parser.add_argument('url', help='URL of the documentation page to convert')
    
    # Output options
    parser.add_argument('-o', '--output', 
                       help='Output filename (single page mode only)')
    parser.add_argument('--output-path', 
                       help='Output directory path (default: current directory)')
    
    # Multi-page options
    parser.add_argument('--multi-page', action='store_true',
                       help='Enable multi-page documentation scraping')
    parser.add_argument('--max-pages', type=int, default=50,
                       help='Maximum number of pages to scrape in multi-page mode (default: 50)')
    parser.add_argument('--same-domain-only', action='store_true', default=True,
                       help='Only scrape pages from the same domain (default: True)')
    parser.add_argument('--rate-limit', type=float, default=1.0,
                       help='Delay between requests in seconds (default: 1.0)')
    
    # Browser options
    parser.add_argument('--wait', type=int, default=5,
                       help='Wait time for page to load in seconds (default: 5)')
    parser.add_argument('--timeout', type=int, default=30,
                       help='Maximum time to wait for page load in seconds (default: 30)')
    parser.add_argument('--no-headless', action='store_true',
                       help='Run browser in non-headless mode for debugging')
    
    # Other options
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--force', '-f', action='store_true',
                       help='Overwrite existing output file without prompting')
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    logger = logging.getLogger(__name__)
    
    try:
        # Validate URL
        if not args.url.startswith(('http://', 'https://')):
            logger.error("❌ Invalid URL. Please provide a URL starting with http:// or https://")
            sys.exit(1)
        
        if args.multi_page:
            # Multi-page mode
            run_multi_page_scraping(args, logger)
        else:
            # Single page mode
            run_single_page_conversion(args, logger)
            
    except KeyboardInterrupt:
        logger.info("\n⚠️  Operation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        if args.verbose:
            logger.exception("Full error traceback:")
        sys.exit(1)

def run_multi_page_scraping(args, logger):
    """Run multi-page documentation scraping"""
    logger.info(f"🚀 Starting multi-page scraping from: {args.url}")
    
    # Determine output directory
    if args.output_path:
        output_dir = Path(args.output_path)
    else:
        # Generate directory name from URL
        from urllib.parse import urlparse
        parsed_url = urlparse(args.url)
        dir_name = sanitize_filename(f"{parsed_url.netloc}_docs")
        output_dir = Path(dir_name)
    
    # Check if directory exists and handle accordingly
    if output_dir.exists() and not args.force:
        if any(output_dir.iterdir()):  # Directory not empty
            response = input(f"⚠️  Directory '{output_dir}' exists and is not empty. Continue? (y/N): ")
            if response.lower() != 'y':
                logger.info("❌ Operation cancelled by user.")
                return
    
    # Initialize multi-page scraper
    multi_scraper = MultiPageScraper(
        base_url=args.url,
        output_dir=output_dir,
        max_pages=args.max_pages,
        same_domain_only=args.same_domain_only
    )
    
    # Run scraping
    summary = multi_scraper.run(wait_between_requests=args.rate_limit)
    
    # Generate index file
    multi_scraper.generate_index_file(summary)
    
    # Final summary
    logger.info(f"🎉 Multi-page scraping completed!")
    logger.info(f"📁 Output directory: {output_dir}")
    logger.info(f"📄 Pages scraped: {summary['scraped_count']}")
    logger.info(f"📋 Index file: {output_dir / 'index.md'}")

def run_single_page_conversion(args, logger):
    """Run single page conversion (original functionality)"""
    logger.info(f"🚀 Starting single page conversion of: {args.url}")
    
    # Initialize scraper and converter
    scraper = DocumentationScraper(headless=not args.no_headless)
    converter = DocumentationConverter()
    
    try:
        # Scrape the page
        logger.info("🔍 Scraping page content...")
        soup = scraper.scrape_page(args.url, wait_time=args.wait, timeout=args.timeout)
        
        if not soup:
            logger.error("❌ Failed to scrape the page content.")
            sys.exit(1)
        
        # Convert to markdown
        logger.info("🔄 Converting HTML to Markdown...")
        markdown_content = converter.convert_to_markdown(soup)
        
        if not markdown_content or "Error:" in markdown_content:
            logger.error(f"❌ Conversion failed: {markdown_content}")
            sys.exit(1)
        
        # Determine output file path
        output_path = determine_output_path(
            args.output, 
            args.output_path, 
            soup, 
            args.force,
            logger
        )
        
        if not output_path:
            logger.error("❌ Could not determine output path.")
            sys.exit(1)
        
        # Write to file
        write_output_file(output_path, markdown_content, logger)
        
        logger.info(f"✅ Conversion completed successfully!")
        logger.info(f"📄 Output saved to: {output_path}")
        logger.info(f"📊 File size: {os.path.getsize(output_path)} bytes")
        
    finally:
        scraper.close()

def determine_output_path(output_arg, output_path_arg, soup, force, logger):
    """Determine the final output file path"""
    
    # Set base directory
    if output_path_arg:
        base_dir = Path(output_path_arg)
        base_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"📁 Using output directory: {base_dir}")
    else:
        base_dir = Path.cwd()
    
    # Determine filename
    if output_arg:
        filename = output_arg
        if not filename.endswith('.md'):
            filename += '.md'
    else:
        # Generate filename from page title
        page_title = get_page_title_from_soup(soup)
        filename = sanitize_filename(page_title) + '.md'
        logger.info(f"📝 Generated filename from page title: {filename}")
    
    # Get safe output path (handles existing files)
    output_path = get_safe_output_path(base_dir / filename, force)
    
    if output_path != base_dir / filename:
        logger.info(f"📄 File already exists, using: {output_path.name}")
    
    # Confirm overwrite if file exists and force is not set
    if output_path.exists() and not force:
        response = input(f"⚠️  File '{output_path}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            logger.info("❌ Operation cancelled by user.")
            return None
    
    return output_path

def get_page_title_from_soup(soup):
    """Extract page title from BeautifulSoup object"""
    # Try multiple selectors for title
    title_selectors = ['title', 'h1', '[data-title]', '.title', '.page-title']
    
    for selector in title_selectors:
        element = soup.select_one(selector)
        if element:
            title = element.get_text().strip()
            if title:
                return title[:50]  # Limit length
    
    return "documentation"

def write_output_file(output_path, content, logger):
    """Write content to output file with error handling"""
    try:
        # Ensure directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write file with UTF-8 encoding
        with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        
        logger.debug(f"✅ Successfully wrote {len(content)} characters to {output_path}")
        
    except PermissionError:
        logger.error(f"❌ Permission denied: Cannot write to {output_path}")
        raise
    except OSError as e:
        logger.error(f"❌ OS Error while writing file: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Unexpected error while writing file: {e}")
        raise

if __name__ == "__main__":
    main()