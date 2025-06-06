# Configuration Guide

Complete guide to configuring and customizing Markdownizer for your specific needs.

## 📋 Table of Contents

- [Command Line Options](#command-line-options)
- [Environment Variables](#environment-variables)
- [Chrome Configuration](#chrome-configuration)
- [Site-Specific Settings](#site-specific-settings)
- [Performance Tuning](#performance-tuning)
- [Custom Patterns](#custom-patterns)

## ⚙️ Command Line Options

### Core Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `url` | | str | Required | URL to scrape |
| `--output` | `-o` | str | `output.md` | Output filename (single page) |
| `--output-path` | | str | `.` | Output directory |
| `--verbose` | `-v` | flag | False | Enable verbose logging |
| `--force` | `-f` | flag | False | Overwrite without prompting |

### Multi-Page Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--multi-page` | flag | False | Enable multi-page scraping |
| `--max-pages` | int | 50 | Maximum pages to scrape |
| `--rate-limit` | float | 1.0 | Delay between requests (seconds) |
| `--same-domain-only` | flag | True | Only scrape same domain |

### Browser Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--wait` | int | 5 | Page load wait time (seconds) |
| `--timeout` | int | 30 | Maximum page load timeout |
| `--no-headless` | flag | False | Show browser (debugging) |

### Usage Examples

```bash
# Basic configuration
python src/main.py https://docs.example.com/api \
  --output="api-reference.md" \
  --output-path="./documentation" \
  --verbose

# Multi-page with custom settings
python src/main.py https://docs.example.com/guide \
  --multi-page \
  --max-pages=25 \
  --rate-limit=2.0 \
  --output-path="./complete-guide"

# Debugging configuration
python src/main.py https://problematic-site.com/docs \
  --no-headless \
  --verbose \
  --wait=15 \
  --timeout=120
```

## 🌍 Environment Variables

Set these environment variables to customize default behavior:

### General Settings

```bash
# Default wait time for page loading
export MARKDOWNIZER_WAIT_TIME="10"

# Default output directory
export MARKDOWNIZER_OUTPUT_DIR="./scraped-docs"

# Default rate limit for multi-page scraping
export MARKDOWNIZER_RATE_LIMIT="2.0"

# Default maximum pages
export MARKDOWNIZER_MAX_PAGES="30"

# Enable verbose logging by default
export MARKDOWNIZER_VERBOSE="true"
```

### Chrome Settings

```bash
# Custom Chrome binary path
export CHROME_BINARY_PATH="/usr/bin/google-chrome"

# Custom ChromeDriver path
export CHROMEDRIVER_PATH="/usr/local/bin/chromedriver"

# Chrome user data directory
export CHROME_USER_DATA_DIR="/tmp/chrome-markdownizer"
```

### Platform-Specific Examples

**Windows:**
```cmd
set MARKDOWNIZER_WAIT_TIME=10
set MARKDOWNIZER_OUTPUT_DIR=C:\Users\%USERNAME%\Documents\scraped-docs
set CHROME_BINARY_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
```

**macOS:**
```bash
export MARKDOWNIZER_WAIT_TIME=10
export MARKDOWNIZER_OUTPUT_DIR="$HOME/Documents/scraped-docs"
export CHROME_BINARY_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

**Linux:**
```bash
export MARKDOWNIZER_WAIT_TIME=10
export MARKDOWNIZER_OUTPUT_DIR="$HOME/scraped-docs"
export CHROME_BINARY_PATH="/usr/bin/google-chrome"
```

## 🌐 Chrome Configuration

### Default Chrome Options

Markdownizer automatically configures Chrome with these options:

```python
# Performance options
--no-sandbox
--disable-dev-shm-usage
--disable-gpu
--disable-images
--disable-plugins

# Stability options
--disable-web-security
--allow-running-insecure-content
--disable-extensions

# Memory options
--disable-background-timer-throttling
--disable-renderer-backgrounding
--disable-backgrounding-occluded-windows
```

### Custom Chrome Options

Create a configuration file to customize Chrome options:

```python
# config/chrome_options.py
CUSTOM_CHROME_OPTIONS = [
    '--disable-blink-features=AutomationControlled',
    '--disable-infobars',
    '--disable-notifications',
    '--disable-popup-blocking',
    '--disable-translate',
    '--disable-features=VizDisplayCompositor',
]
```

### User Agent Configuration

Default user agent for bot detection avoidance:

```python
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
```

Custom user agent:
```bash
export MARKDOWNIZER_USER_AGENT="Mozilla/5.0 (Custom Bot) Markdownizer/1.2.0"
```

## 🎯 Site-Specific Settings

### Documentation Site Presets

Create presets for common documentation platforms:

#### GitBook Sites
```bash
# GitBook typically needs longer wait times
python src/main.py https://docs.gitbook.com \
  --multi-page \
  --wait=8 \
  --rate-limit=2.0 \
  --max-pages=40
```

#### Sphinx Documentation
```bash
# Sphinx sites usually have good structure
python src/main.py https://docs.python.org/3/ \
  --multi-page \
  --wait=5 \
  --rate-limit=1.0 \
  --max-pages=50
```

#### Docusaurus Sites
```bash
# React-based, may need more wait time
python src/main.py https://docusaurus.io/docs \
  --multi-page \
  --wait=10 \
  --rate-limit=1.5 \
  --max-pages=30
```

#### VuePress Sites
```bash
# Vue-based documentation
python src/main.py https://vuepress.vuejs.org/guide/ \
  --multi-page \
  --wait=8 \
  --rate-limit=1.5 \
  --max-pages=25
```

### API Documentation Settings

#### Swagger/OpenAPI
```bash
# API docs often load slowly
python src/main.py https://petstore.swagger.io/v2/swagger.json \
  --wait=15 \
  --timeout=60 \
  --verbose
```

#### Postman Documentation
```bash
# Postman docs are JavaScript-heavy
python src/main.py https://documenter.getpostman.com/view/... \
  --wait=12 \
  --timeout=90 \
  --no-headless  # For debugging
```

## 🚀 Performance Tuning

### Speed Optimization

**Fast Scraping (Less Respectful):**
```bash
python src/main.py https://docs.example.com \
  --multi-page \
  --rate-limit=0.5 \
  --wait=3 \
  --max-pages=20
```

**Balanced Performance:**
```bash
python src/main.py https://docs.example.com \
  --multi-page \
  --rate-limit=1.5 \
  --wait=5 \
  --max-pages=30
```

**Respectful Scraping:**
```bash
python src/main.py https://docs.example.com \
  --multi-page \
  --rate-limit=3.0 \
  --wait=8 \
  --max-pages=50
```

### Memory Optimization

For large documentation sites:

```bash
# Process in smaller chunks
python src/main.py https://huge-docs.com/section1 \
  --multi-page \
  --max-pages=25 \
  --output-path="./docs/section1"

python src/main.py https://huge-docs.com/section2 \
  --multi-page \
  --max-pages=25 \
  --output-path="./docs/section2"
```

### Network Optimization

```bash
# For slow networks
export MARKDOWNIZER_WAIT_TIME=20
export MARKDOWNIZER_TIMEOUT=180

# For fast networks
export MARKDOWNIZER_WAIT_TIME=3
export MARKDOWNIZER_TIMEOUT=30
```

## 🔍 Custom Patterns

### URL Pattern Customization

Modify `multi_scraper.py` to customize URL patterns:

```python
# Custom documentation patterns
doc_patterns = [
    r'/docs?/',
    r'/guide/',
    r'/tutorial/',
    r'/reference/',
    r'/api/',
    r'/manual/',
    r'/help/',
    r'/documentation/',
    r'/wiki/',          # Custom: Wiki pages
    r'/knowledge/',     # Custom: Knowledge base
    r'/faq/',          # Custom: FAQ sections
]

# Custom exclusion patterns
exclude_patterns = [
    r'/search',
    r'/login',
    r'/register',
    r'/contact',
    r'/download',
    r'/install',
    r'\.pdf$',
    r'\.zip$',
    r'/admin/',        # Custom: Admin pages
    r'/dashboard/',    # Custom: Dashboard pages
    r'/settings/',     # Custom: Settings pages
]
```

### Content Selector Customization

Modify `converter.py` for site-specific content extraction:

```python
# Custom content selectors for specific sites
site_specific_selectors = {
    'docs.example.com': ['.custom-content', '.main-docs'],
    'api.example.com': ['#api-content', '.api-documentation'],
    'help.example.com': ['.help-content', '.support-docs'],
}

def extract_main_content(self, soup, url=None):
    if url:
        domain = urlparse(url).netloc
        if domain in site_specific_selectors:
            for selector in site_specific_selectors[domain]:
                content = soup.select_one(selector)
                if content:
                    return content
    
    # Fall back to default extraction
    return self.default_extract_main_content(soup)
```

## 📝 Configuration Files

### Create Configuration Files

**config.json:**
```json
{
  "default_wait_time": 8,
  "default_rate_limit": 2.0,
  "default_max_pages": 40,
  "chrome_options": [
    "--disable-blink-features=AutomationControlled",
    "--disable-infobars"
  ],
  "site_presets": {
    "gitbook": {
      "wait_time": 10,
      "rate_limit": 2.5,
      "max_pages": 30
    },
    "sphinx": {
      "wait_time": 5,
      "rate_limit": 1.0,
      "max_pages": 50
    }
  }
}
```

**settings.py:**
```python
# Default settings
DEFAULT_SETTINGS = {
    'wait_time': 5,
    'timeout': 30,
    'rate_limit': 1.0,
    'max_pages': 50,
    'headless': True,
    'verbose': False,
}

# Site-specific settings
SITE_SETTINGS = {
    'docs.python.org': {
        'wait_time': 3,
        'rate_limit': 0.5,
        'max_pages': 100,
    },
    'react.dev': {
        'wait_time': 8,
        'rate_limit': 2.0,
        'max_pages': 25,
    },
}
```

## 🔧 Advanced Configuration

### Custom Output Formatting

```python
# Custom filename generation
def custom_filename_generator(url, soup):
    # Extract section and page information
    section = extract_section_from_url(url)
    title = extract_title_from_soup(soup)
    return f"{section}_{sanitize_filename(title)}.md"
```

### Custom Link Filtering

```python
def custom_link_filter(url, base_url):
    # Custom logic to determine if URL should be scraped
    if 'deprecated' in url.lower():
        return False
    if 'v1' in url and 'v2' in base_url:
        return False
    return True
```

### Custom Content Processing

```python
def custom_content_processor(markdown_content, url):
    # Add custom headers
    header = f"<!-- Source: {url} -->\n"
    header += f"<!-- Scraped: {datetime.now().isoformat()} -->\n\n"
    
    # Custom formatting
    processed_content = process_code_blocks(markdown_content)
    processed_content = fix_relative_links(processed_content, url)
    
    return header + processed_content
```

## 🎯 Best Practice Configurations

### Development/Testing
```bash
# Quick testing with minimal impact
python src/main.py https://docs.example.com \
  --multi-page \
  --max-pages=5 \
  --rate-limit=3.0 \
  --verbose \
  --no-headless
```

### Production/Batch Processing
```bash
# Respectful production scraping
python src/main.py https://docs.example.com \
  --multi-page \
  --max-pages=50 \
  --rate-limit=2.0 \
  --timeout=120 \
  --force
```

### Debugging Problematic Sites
```bash
# Maximum debugging information
python src/main.py https://problematic-site.com \
  --no-headless \
  --verbose \
  --wait=20 \
  --timeout=180 \
  --max-pages=3
```

This configuration guide provides comprehensive options for customizing Markdownizer to work optimally with different types of documentation sites and use cases.