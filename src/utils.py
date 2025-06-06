import re
from urllib.parse import urljoin, urlparse

def clean_html(html_content):
    # Function to clean up HTML content
    # This can include removing scripts, styles, or any unwanted tags
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    return str(soup)

def format_markdown(content):
    # Function to format the content into Markdown
    # This can include adding headers, lists, etc.
    # For simplicity, we will just return the content as is for now
    return content.strip()

def is_valid_url(url):
    """Check if URL is valid"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def get_page_title(soup):
    """Extract page title from soup"""
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.get_text().strip()
    
    h1_tag = soup.find('h1')
    if h1_tag:
        return h1_tag.get_text().strip()
        
    return "Documentation Page"

def sanitize_filename(filename):
    """Sanitize filename for Windows"""
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove excessive dots and spaces
    filename = re.sub(r'\.+', '.', filename)
    filename = filename.strip('. ')
    return filename

def make_absolute_urls(soup, base_url):
    """Convert relative URLs to absolute URLs"""
    for tag in soup.find_all(['a', 'img', 'link']):
        for attr in ['href', 'src']:
            if tag.get(attr):
                tag[attr] = urljoin(base_url, tag[attr])
    return soup