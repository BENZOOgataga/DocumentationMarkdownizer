import html2text
from markdownify import markdownify
import re

class DocumentationConverter:
    def __init__(self):
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # No line wrapping
        
    def extract_main_content(self, soup):
        """Extract main documentation content from soup"""
        # Common selectors for documentation content
        content_selectors = [
            'main',
            '[role="main"]',
            '.content',
            '.documentation',
            '.docs-content',
            '.main-content',
            'article',
            '.markdown-body',
            '.rst-content'
        ]
        
        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break
                
        # If no main content found, use body but remove nav, header, footer
        if not main_content:
            main_content = soup.find('body')
            if main_content:
                # Remove navigation, headers, footers, sidebars
                for tag in main_content.find_all(['nav', 'header', 'footer', 'aside']):
                    tag.decompose()
                for tag in main_content.find_all(class_=re.compile(r'nav|menu|sidebar|header|footer')):
                    tag.decompose()
                    
        return main_content
        
    def clean_html(self, soup_element):
        """Clean HTML content before conversion"""
        if not soup_element:
            return None
            
        # Remove script and style tags
        for tag in soup_element.find_all(['script', 'style']):
            tag.decompose()
            
        # Remove common unwanted elements
        unwanted_classes = ['advertisement', 'ads', 'cookie', 'popup', 'modal']
        for class_name in unwanted_classes:
            for tag in soup_element.find_all(class_=re.compile(class_name, re.I)):
                tag.decompose()
                
        return soup_element
        
    def convert_to_markdown(self, soup):
        """Convert BeautifulSoup object to Markdown"""
        if not soup:
            return "Error: No content found or page failed to load properly."
            
        # Extract main content
        main_content = self.extract_main_content(soup)
        
        if not main_content:
            return "Error: Could not find main content on the page."
            
        # Clean the HTML
        cleaned_content = self.clean_html(main_content)
        
        if not cleaned_content:
            return "Error: Content cleaning failed."
            
        # Convert to markdown using html2text
        markdown_content = self.h2t.handle(str(cleaned_content))
        
        # Clean up the markdown
        markdown_content = self.clean_markdown(markdown_content)
        
        return markdown_content
        
    def clean_markdown(self, markdown_text):
        """Clean up the converted markdown"""
        # Remove excessive blank lines
        markdown_text = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_text)
        
        # Remove trailing whitespace
        lines = [line.rstrip() for line in markdown_text.split('\n')]
        
        return '\n'.join(lines).strip()