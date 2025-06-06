# API Reference

Complete technical documentation for Markdownizer's internal APIs and classes.

## 📋 Table of Contents

- [Core Classes](#core-classes)
- [Main Module](#main-module)
- [Scraper Module](#scraper-module)
- [Multi-Scraper Module](#multi-scraper-module)
- [Converter Module](#converter-module)
- [Utils Module](#utils-module)

## 🏗️ Core Classes

### DocumentationScraper

Main class for single-page web scraping using Selenium.

```python
class DocumentationScraper:
    def __init__(self, headless=True)
    def setup_driver(self)
    def scrape_page(self, url, wait_time=5, timeout=30)
    def close(self)
```

#### Methods

**`__init__(headless=True)`**
- **Parameters:**
  - `headless` (bool): Run browser in headless mode
- **Description:** Initialize the scraper with browser options

**`setup_driver()`**
- **Returns:** None
- **Raises:** Exception if ChromeDriver setup fails
- **Description:** Configure and initialize Chrome WebDriver

**`scrape_page(url, wait_time=5, timeout=30)`**
- **Parameters:**
  - `url` (str): URL to scrape
  - `wait_time` (int): Seconds to wait for page load
  - `timeout` (int): Maximum wait time
- **Returns:** BeautifulSoup object or None
- **Description:** Scrape a single page and return parsed HTML

**`close()`**
- **Description:** Clean up WebDriver resources

#### Example Usage

```python
from scraper import DocumentationScraper

scraper = DocumentationScraper(headless=True)
try:
    soup = scraper.scrape_page("https://docs.example.com", wait_time=10)
    if soup:
        print("Successfully scraped page")
finally:
    scraper.close()
```

### MultiPageScraper

Advanced class for multi-page documentation scraping.

```python
class MultiPageScraper:
    def __init__(self, base_url, output_dir, max_pages=50, 
                 same_domain_only=True, respect_robots=True)
    def is_valid_doc_url(self, url)
    def extract_links_from_soup(self, soup, current_url)
    def generate_filename(self, url, soup)
    def scrape_single_page(self, url)
    def run(self, wait_between_requests=1.0)
    def generate_index_file(self, summary)
```

#### Constructor Parameters

- `base_url` (str): Starting URL for scraping
- `output_dir` (Path): Directory to save files
- `max_pages` (int): Maximum pages to scrape (default: 50)
- `same_domain_only` (bool): Restrict to same domain (default: True)
- `respect_robots` (bool): Respect robots.txt (default: True)

#### Methods

**`is_valid_doc_url(url)`**
- **Parameters:** `url` (str): URL to validate
- **Returns:** bool
- **Description:** Check if URL matches documentation patterns

**`extract_links_from_soup(soup, current_url)`**
- **Parameters:**
  - `soup`: BeautifulSoup object
  - `current_url` (str): Current page URL
- **Returns:** List[str] of found URLs
- **Description:** Extract documentation links from page

**`run(wait_between_requests=1.0)`**
- **Parameters:** `wait_between_requests` (float): Delay between requests
- **Returns:** dict with scraping summary
- **Description:** Execute the complete multi-page scraping process

#### Example Usage

```python
from multi_scraper import MultiPageScraper
from pathlib import Path

scraper = MultiPageScraper(
    base_url="https://docs.example.com/guide",
    output_dir=Path("./docs"),
    max_pages=25,
    same_domain_only=True
)

summary = scraper.run(wait_between_requests=2.0)
scraper.generate_index_file(summary)
```

### DocumentationConverter

Converts HTML content to clean Markdown.

```python
class DocumentationConverter:
    def __init__(self)
    def extract_main_content(self, soup)
    def clean_html(self, soup_element)
    def convert_to_markdown(self, soup)
    def clean_markdown(self, markdown_text)
```

#### Methods

**`extract_main_content(soup)`**
- **Parameters:** `soup`: BeautifulSoup object
- **Returns:** BeautifulSoup element or None
- **Description:** Find and extract main documentation content

**`clean_html(soup_element)`**
- **Parameters:** `soup_element`: BeautifulSoup element
- **Returns:** Cleaned BeautifulSoup element
- **Description:** Remove unwanted HTML elements

**`convert_to_markdown(soup)`**
- **Parameters:** `soup`: BeautifulSoup object
- **Returns:** str (Markdown content)
- **Description:** Convert HTML to clean Markdown

#### Example Usage

```python
from converter import DocumentationConverter

converter = DocumentationConverter()
markdown = converter.convert_to_markdown(soup)
print(f"Converted {len(markdown)} characters")
```

## 📁 Module Reference

### main.py

Main entry point and CLI interface.

#### Functions

**`main()`**
- **Description:** Main entry point, handles CLI arguments and orchestrates conversion

**`run_multi_page_scraping(args, logger)`**
- **Parameters:**
  - `args`: Parsed command line arguments
  - `logger`: Logger instance
- **Description:** Execute multi-page scraping workflow

**`run_single_page_conversion(args, logger)`**
- **Parameters:**
  - `args`: Parsed command line arguments  
  - `logger`: Logger instance
- **Description:** Execute single page conversion workflow

**`determine_output_path(output_arg, output_path_arg, soup, force, logger)`**
- **Returns:** Path object for output file
- **Description:** Determine final output file path with conflict resolution

### scraper.py

Single-page web scraping functionality.

#### Key Features

- Selenium WebDriver management
- Chrome options optimization
- JavaScript content waiting
- Error handling and recovery
- Resource cleanup

#### Configuration Options

```python
# Chrome options for better performance
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-images')  # Faster loading
```

### multi_scraper.py

Multi-page documentation scraping engine.

#### Link Discovery Patterns

**Documentation URL Patterns:**
```python
doc_patterns = [
    r'/docs?/',
    r'/guide/',
    r'/tutorial/',
    r'/reference/',
    r'/api/',
    r'/manual/',
    r'/help/',
    r'/documentation/',
]
```

**Excluded Patterns:**
```python
exclude_patterns = [
    r'/search',
    r'/login',
    r'/register',
    r'/contact',
    r'/download',
    r'\.pdf$',
    r'\.zip$',
]
```

#### Link Extraction Selectors

**Navigation Selectors:**
```python
nav_selectors = [
    'nav a[href]',
    '.sidebar a[href]',
    '.navigation a[href]',
    '.toc a[href]',
    '.menu a[href]',
    '.docs-nav a[href]',
]
```

### converter.py

HTML to Markdown conversion with intelligent content extraction.

#### Content Selectors

**Main Content Selectors (in priority order):**
```python
content_selectors = [
    'main',
    '[role="main"]',
    '.content',
    '.documentation',
    '.docs-content',
    'article',
    '.markdown-body',
]
```

#### Cleaning Rules

**Unwanted Elements:**
- Script and style tags
- Navigation elements
- Advertisements
- Social media widgets
- Cookie notices

### utils.py

Utility functions for file management, URL handling, and path operations.

#### Key Functions

**`sanitize_filename(filename)`**
- **Parameters:** `filename` (str): Raw filename
- **Returns:** str (sanitized filename)
- **Description:** Create cross-platform safe filenames

**`get_safe_output_path(base_path, force=False)`**
- **Parameters:**
  - `base_path` (Path): Desired output path
  - `force` (bool): Overwrite without numbering
- **Returns:** Path (safe output path)
- **Description:** Handle file conflicts with auto-numbering

**`setup_logging(level=logging.INFO)`**
- **Parameters:** `level`: Logging level
- **Description:** Configure application logging

## 🔧 Configuration

### Environment Variables

```bash
# Chrome binary location (if non-standard)
export CHROME_BINARY_PATH="/path/to/chrome"

# Default wait time
export MARKDOWNIZER_WAIT_TIME="5"

# Default output directory
export MARKDOWNIZER_OUTPUT_DIR="./output"
```

### Chrome Options

```python
# Performance optimizations
chrome_options.add_argument('--disable-images')
chrome_options.add_argument('--disable-plugins')
chrome_options.add_argument('--disable-javascript-harmony-shipping')

# Stability options
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
```

## 🚨 Error Handling

### Exception Types

**`WebDriverException`**
- Selenium WebDriver errors
- Chrome/ChromeDriver issues
- Browser crashes

**`TimeoutException`**
- Page load timeouts
- Element wait timeouts
- Network delays

**`PermissionError`**
- File system permission issues
- Directory creation failures
- File write errors

**`ValueError`**
- Invalid URL formats
- Invalid configuration values
- Parameter validation errors

### Error Recovery

```python
try:
    soup = scraper.scrape_page(url)
except TimeoutException:
    logger.warning(f"Timeout for {url}, retrying...")
    soup = scraper.scrape_page(url, wait_time=15)
except WebDriverException as e:
    logger.error(f"WebDriver error: {e}")
    scraper.setup_driver()  # Reinitialize
```

## 📊 Performance Considerations

### Memory Management

- WebDriver instance reuse in multi-page mode
- Efficient BeautifulSoup parsing
- Proper resource cleanup
- Large file handling

### Network Optimization

- Rate limiting to respect servers
- Connection reuse
- Timeout configuration
- Retry mechanisms

### Processing Optimization

- Lazy loading support
- Efficient CSS selectors
- Minimal DOM traversal
- Optimized regular expressions

## 🔗 Integration Examples

### As a Library

```python
from scraper import DocumentationScraper
from converter import DocumentationConverter

def convert_documentation(url):
    scraper = DocumentationScraper()
    converter = DocumentationConverter()
    
    try:
        soup = scraper.scrape_page(url)
        if soup:
            return converter.convert_to_markdown(soup)
    finally:
        scraper.close()
    
    return None
```

### Batch Processing

```python
from multi_scraper import MultiPageScraper
from pathlib import Path

def batch_convert(urls, output_base):
    for i, url in enumerate(urls):
        output_dir = Path(output_base) / f"site_{i}"
        scraper = MultiPageScraper(url, output_dir, max_pages=20)
        summary = scraper.run(wait_between_requests=2.0)
        scraper.generate_index_file(summary)
```

### Custom Content Filters

```python
class CustomConverter(DocumentationConverter):
    def extract_main_content(self, soup):
        # Custom content extraction logic
        custom_content = soup.select_one('.custom-docs-content')
        if custom_content:
            return custom_content
        return super().extract_main_content(soup)
```

This API reference provides complete technical documentation for integrating and extending Markdownizer's functionality.