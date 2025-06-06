import re
import logging
from pathlib import Path
from urllib.parse import urljoin, urlparse

def setup_logging(level=logging.INFO):
    """Setup logging configuration"""
    logging.basicConfig(
        level=level,
        format='%(message)s',
        handlers=[logging.StreamHandler()]
    )

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
    """Sanitize filename for cross-platform compatibility"""
    # Remove HTML tags if any
    filename = re.sub(r'<[^>]+>', '', filename)
    
    # Replace invalid characters with underscore
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # Replace multiple spaces/underscores with single underscore
    filename = re.sub(r'[_\s]+', '_', filename)
    
    # Remove leading/trailing dots, spaces, underscores
    filename = filename.strip('. _')
    
    # Ensure filename is not empty and not too long
    if not filename:
        filename = "document"
    
    if len(filename) > 50:
        filename = filename[:50]
    
    return filename

def get_safe_output_path(base_path, force=False):
    """Get a safe output path, handling existing files"""
    base_path = Path(base_path)
    
    # If force is True or file doesn't exist, return as-is
    if force or not base_path.exists():
        return base_path
    
    # Generate numbered filename
    stem = base_path.stem
    suffix = base_path.suffix
    parent = base_path.parent
    
    counter = 1
    while True:
        new_path = parent / f"{stem}_{counter}{suffix}"
        if not new_path.exists():
            return new_path
        counter += 1
        
        # Safety check to prevent infinite loop
        if counter > 1000:
            raise ValueError("Too many existing files with similar names")

def make_absolute_urls(soup, base_url):
    """Convert relative URLs to absolute URLs"""
    for tag in soup.find_all(['a', 'img', 'link']):
        for attr in ['href', 'src']:
            if tag.get(attr):
                tag[attr] = urljoin(base_url, tag[attr])
    return soup

def validate_output_directory(path_str):
    """Validate and create output directory if needed"""
    try:
        path = Path(path_str)
        path.mkdir(parents=True, exist_ok=True)
        
        # Test write permissions
        test_file = path / '.write_test'
        test_file.touch()
        test_file.unlink()
        
        return path
    except PermissionError:
        raise ValueError(f"Permission denied: Cannot write to directory '{path_str}'")
    except OSError as e:
        raise ValueError(f"Invalid directory path '{path_str}': {e}")

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024**2:
        return f"{size_bytes/1024:.1f} KB"
    elif size_bytes < 1024**3:
        return f"{size_bytes/(1024**2):.1f} MB"
    else:
        return f"{size_bytes/(1024**3):.1f} GB"