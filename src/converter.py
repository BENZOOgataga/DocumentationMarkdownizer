import html2text
import re
import logging
from bs4 import BeautifulSoup

class DocumentationConverter:
    def __init__(self):
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # No line wrapping
        self.h2t.unicode_snob = True
        self.h2t.escape_snob = True
        self.logger = logging.getLogger(__name__)
        
    def extract_main_content(self, soup):
        """Extract main documentation content from soup"""
        # Common selectors for documentation content (ordered by preference)
        content_selectors = [
            'main',
            '[role="main"]',
            '.content',
            '.documentation',
            '.docs-content',
            '.main-content',
            'article',
            '.markdown-body',
            '.rst-content',
            '.page-content',
            '.container .content',
            '#content',
            '#main-content'
        ]
        
        main_content = None
        for selector in content_selectors:
            elements = soup.select(selector)
            if elements:
                # Choose the element with most content
                main_content = max(elements, key=lambda x: len(x.get_text()))
                self.logger.debug(f"📍 Found main content using selector: {selector}")
                break
                
        # Fallback: use body but remove unwanted elements
        if not main_content:
            self.logger.debug("📍 Using body as fallback, removing unwanted elements")
            main_content = soup.find('body')
            if main_content:
                # Remove navigation, headers, footers, sidebars
                unwanted_selectors = [
                    'nav', 'header', 'footer', 'aside',
                    '[class*="nav"]', '[class*="menu"]', '[class*="sidebar"]',
                    '[class*="header"]', '[class*="footer"]', '[id*="nav"]',
                    '[id*="menu"]', '[id*="sidebar"]', '[id*="header"]',
                    '[id*="footer"]', '.advertisement', '.ads', '.cookie',
                    '.popup', '.modal', '.overlay'
                ]
                
                for selector in unwanted_selectors:
                    for element in main_content.select(selector):
                        element.decompose()
                        
        return main_content
        
    def clean_html(self, soup_element):
        """Clean HTML content before conversion"""
        if not soup_element:
            return None
            
        # Remove script and style tags
        for tag in soup_element.find_all(['script', 'style', 'noscript']):
            tag.decompose()
            
        # Remove comments
        from bs4 import Comment
        comments = soup_element.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()
            
        # Remove common unwanted elements
        unwanted_patterns = [
            r'advertisement', r'ads?', r'cookie', r'popup', r'modal',
            r'overlay', r'banner', r'promo', r'social', r'share',
            r'newsletter', r'subscription'
        ]
        
        for pattern in unwanted_patterns:
            for tag in soup_element.find_all(class_=re.compile(pattern, re.I)):
                tag.decompose()
            for tag in soup_element.find_all(id=re.compile(pattern, re.I)):
                tag.decompose()
                
        # Clean up empty elements
        for tag in soup_element.find_all():
            if not tag.get_text(strip=True) and not tag.find(['img', 'br', 'hr']):
                tag.decompose()
                
        return soup_element
        
    def convert_to_markdown(self, soup):
        """Convert BeautifulSoup object to Markdown"""
        if not soup:
            return "Error: No content found or page failed to load properly."
            
        # Extract main content
        main_content = self.extract_main_content(soup)
        
        if not main_content:
            self.logger.warning("⚠️  Could not find main content, using entire page")
            main_content = soup
            
        # Clean the HTML
        cleaned_content = self.clean_html(main_content)
        
        if not cleaned_content:
            return "Error: Content cleaning failed."
            
        # Check if content is substantial
        text_content = cleaned_content.get_text(strip=True)
        if len(text_content) < 100:
            self.logger.warning("⚠️  Extracted content seems very short")
            
        # Convert to markdown using html2text
        try:
            markdown_content = self.h2t.handle(str(cleaned_content))
        except Exception as e:
            self.logger.error(f"❌ HTML to Markdown conversion failed: {e}")
            return f"Error: Markdown conversion failed - {str(e)}"
        
        # Clean up the markdown
        markdown_content = self.clean_markdown(markdown_content)
        
        self.logger.debug(f"✅ Converted to Markdown ({len(markdown_content)} characters)")
        return markdown_content
        
    def clean_markdown(self, markdown_text):
        """Clean up the converted markdown"""
        if not markdown_text:
            return ""
        
        # Remove excessive blank lines (more than 2 consecutive)
        markdown_text = re.sub(r'\n\s*\n\s*\n+', '\n\n', markdown_text)
        
        # Clean up code blocks
        markdown_text = re.sub(r'```\s*\n\s*```', '', markdown_text)
        
        # Remove trailing whitespace from lines
        lines = [line.rstrip() for line in markdown_text.split('\n')]
        
        # Remove leading/trailing empty lines
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
            
        return '\n'.join(lines).strip()