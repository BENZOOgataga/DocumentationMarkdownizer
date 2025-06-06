# Troubleshooting Guide

Comprehensive guide to solving common issues with Markdownizer.

## 📋 Table of Contents

- [Installation Issues](#installation-issues)
- [Chrome/WebDriver Problems](#chromewebdriver-problems)
- [Scraping Issues](#scraping-issues)
- [Content Quality Problems](#content-quality-problems)
- [Performance Issues](#performance-issues)
- [Network and Timeout Issues](#network-and-timeout-issues)
- [File and Permission Issues](#file-and-permission-issues)
- [Multi-Page Specific Issues](#multi-page-specific-issues)

## 🔧 Installation Issues

### Python Version Problems

**Problem:** `SyntaxError` or `python command not found`

**Solution:**
```bash
# Check Python version
python --version
# Should be 3.7 or higher

# Try python3 if python doesn't work
python3 --version

# Install Python if needed
# Windows: Download from python.org
# macOS: brew install python3
# Ubuntu: sudo apt-get install python3
```

### Dependency Installation Failures

**Problem:** `pip install` fails or packages not found

**Solution:**
```bash
# Update pip first
python -m pip install --upgrade pip

# Install dependencies with verbose output
pip install -r requirements.txt --verbose

# Try with user flag if permission issues
pip install -r requirements.txt --user

# Use virtual environment (recommended)
python -m venv markdownizer-env
source markdownizer-env/bin/activate  # macOS/Linux
markdownizer-env\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Module Import Errors

**Problem:** `ModuleNotFoundError: No module named 'selenium'`

**Solution:**
```bash
# Verify installation
pip list | grep selenium

# Reinstall if missing
pip uninstall selenium
pip install selenium

# Check if using correct Python/pip
which python
which pip

# Use specific Python version
python3 -m pip install selenium
```

## 🌐 Chrome/WebDriver Problems

### ChromeDriver Issues

**Problem:** `[WinError 193] %1 is not a valid Win32 application`

**Solution:**
```bash
# Clear ChromeDriver cache
# Windows:
rmdir /s "%USERPROFILE%\.wdm"
# macOS/Linux:
rm -rf ~/.wdm

# Reinstall webdriver-manager
pip uninstall webdriver-manager
pip install webdriver-manager

# Manual ChromeDriver installation if needed
# 1. Check Chrome version: chrome://version
# 2. Download matching ChromeDriver from chromedriver.chromium.org
# 3. Add to PATH or specify location
```

**Problem:** `SessionNotCreatedException: session not created`

**Solution:**
```bash
# Update Chrome browser to latest version
# Windows: chrome://settings/help
# macOS: Chrome → About Google Chrome
# Linux: sudo apt-get update && sudo apt-get upgrade google-chrome-stable

# Clear Chrome user data
rm -rf /tmp/chrome-markdownizer  # Linux/macOS
rmdir /s "C:\temp\chrome-markdownizer"  # Windows

# Try with different Chrome options
python src/main.py <URL> --no-headless --verbose
```

### Chrome Binary Not Found

**Problem:** `WebDriverException: chrome not reachable`

**Solution:**
```bash
# Set Chrome binary path
# Windows:
set CHROME_BINARY_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
# macOS:
export CHROME_BINARY_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Linux:
export CHROME_BINARY_PATH="/usr/bin/google-chrome"

# Install Chrome if missing
# Windows: Download from google.com/chrome
# macOS: brew install --cask google-chrome
# Ubuntu: wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
```

### Headless Mode Issues

**Problem:** Different behavior between headless and non-headless mode

**Solution:**
```bash
# Debug with visible browser first
python src/main.py <URL> --no-headless --verbose

# If working in non-headless, try these headless options:
# Add to scraper.py:
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')
```

## 🔍 Scraping Issues

### JavaScript Not Loading

**Problem:** Page shows "Please enable JavaScript" or content is missing

**Solution:**
```bash
# Increase wait time
python src/main.py <URL> --wait 15 --timeout 60

# Use debug mode to see what's happening
python src/main.py <URL> --no-headless --verbose

# Try multiple waits
python src/main.py <URL> --wait 20 --verbose
```

**Advanced Solution:**
```python
# In scraper.py, add after page load:
self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
self.driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
```

### Page Load Timeouts

**Problem:** `TimeoutException: Message: timeout`

**Solution:**
```bash
# Increase timeout values
python src/main.py <URL> --timeout 120 --wait 30

# Check network connectivity
ping google.com

# Try with simpler sites first
python src/main.py https://example.com --verbose
```

### Authentication Required

**Problem:** Site requires login or shows 403/401 errors

**Current Limitation:** Markdownizer doesn't support authentication

**Workarounds:**
1. Use publicly accessible documentation URLs
2. Find alternative documentation sources
3. Manual login then get direct content URLs

### Bot Detection

**Problem:** Site detects and blocks the scraper

**Solution:**
```bash
# Use more realistic delays
python src/main.py <URL> --multi-page --rate-limit 5.0 --wait 10

# Try different user agent (modify scraper.py):
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

# Use non-headless mode
python src/main.py <URL> --no-headless
```

## 📄 Content Quality Problems

### Empty or Minimal Content

**Problem:** Output file is nearly empty or contains very little content

**Diagnosis:**
```bash
# Use verbose mode to see what's extracted
python src/main.py <URL> --verbose --no-headless

# Check if JavaScript is needed
# Look at page source vs rendered content
```

**Solutions:**
```bash
# Increase wait time for JavaScript
python src/main.py <URL> --wait 15

# Try different content selectors
# Modify converter.py content_selectors list

# Debug with browser inspection
python src/main.py <URL> --no-headless
# Manually inspect page structure
```

### Unwanted Content Included

**Problem:** Output includes navigation, ads, or other unwanted elements

**Solution:**
```python
# Modify converter.py to add more exclusion patterns
unwanted_patterns = [
    r'advertisement', r'ads?', r'cookie', r'popup', r'modal',
    r'navigation', r'sidebar', r'footer', r'header',
    r'social', r'share', r'newsletter'  # Add your patterns
]
```

### Poor Markdown Formatting

**Problem:** Markdown output is poorly formatted or broken

**Solutions:**
```bash
# Try different HTML to Markdown settings
# Modify converter.py:
self.h2t.body_width = 0  # No line wrapping
self.h2t.unicode_snob = True
self.h2t.escape_snob = True
```

### Missing Code Blocks

**Problem:** Code examples are not properly formatted

**Solution:**
```python
# In converter.py, enhance code block detection:
def preserve_code_blocks(self, soup):
    for code in soup.find_all(['pre', 'code']):
        code['class'] = code.get('class', []) + ['preserve-formatting']
```

## ⚡ Performance Issues

### Slow Scraping

**Problem:** Scraping takes too long

**Solutions:**
```bash
# Reduce wait times (if content loads properly)
python src/main.py <URL> --wait 3 --rate-limit 0.5

# Disable images and plugins (modify scraper.py):
chrome_options.add_argument('--disable-images')
chrome_options.add_argument('--disable-plugins')

# Use fewer pages for testing
python src/main.py <URL> --multi-page --max-pages 10
```

### High Memory Usage

**Problem:** High RAM consumption during large scraping jobs

**Solutions:**
```bash
# Process in smaller batches
python src/main.py <URL> --multi-page --max-pages 25
# Then process next section separately

# Use more aggressive cleanup (modify multi_scraper.py):
# Add garbage collection after each page
import gc
gc.collect()
```

### CPU Usage Issues

**Problem:** High CPU usage

**Solutions:**
```bash
# Increase rate limiting
python src/main.py <URL> --multi-page --rate-limit 3.0

# Use headless mode (if not already)
python src/main.py <URL>  # Headless is default

# Reduce concurrent operations
# Modify scraper to use lower Chrome process priority
```

## 🌐 Network and Timeout Issues

### Slow Network Connections

**Problem:** Timeouts on slow connections

**Solution:**
```bash
# Increase all timeout values
python src/main.py <URL> --wait 30 --timeout 180 --rate-limit 5.0

# Set environment variables for defaults
export MARKDOWNIZER_WAIT_TIME=20
export MARKDOWNIZER_TIMEOUT=120
```

### Intermittent Network Failures

**Problem:** Random network failures during scraping

**Solution:**
```python
# Add retry logic to scraper.py:
def scrape_with_retry(self, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            return self.scrape_page(url)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))  # Exponential backoff
                continue
            raise e
```

### DNS Resolution Issues

**Problem:** Cannot resolve domain names

**Solution:**
```bash
# Test DNS resolution
nslookup docs.example.com

# Try different DNS servers
# Windows: ipconfig /flushdns
# macOS: sudo dscacheutil -flushcache
# Linux: sudo systemctl restart systemd-resolved

# Use IP address if DNS fails
python src/main.py http://93.184.216.34/docs  # example.com IP
```

## 📁 File and Permission Issues

### Permission Denied Errors

**Problem:** Cannot write to output directory

**Solution:**
```bash
# Check directory permissions
ls -la ./  # Linux/macOS
dir       # Windows

# Create directory with proper permissions
mkdir -p ./output
chmod 755 ./output  # Linux/macOS

# Use different output directory
python src/main.py <URL> --output-path="$HOME/Documents/markdownizer"

# Run with appropriate permissions (not recommended as admin/root)
```

### File Path Too Long (Windows)

**Problem:** `OSError: [Errno 36] File name too long`

**Solution:**
```bash
# Use shorter output paths
python src/main.py <URL> --output-path="C:\md"

# Enable long path support (Windows 10):
# Group Policy: Computer Configuration → Administrative Templates → System → Filesystem → Enable Win32 long paths
```

### File Already Open Errors

**Problem:** Cannot overwrite file that's open in another program

**Solution:**
```bash
# Close file in other applications
# Use force flag
python src/main.py <URL> -o filename.md --force

# Use different filename
python src/main.py <URL> -o filename-new.md
```

## 🔗 Multi-Page Specific Issues

### Too Many/Few Pages Found

**Problem:** Multi-page mode finds wrong number of pages

**Diagnosis:**
```bash
# Use verbose mode to see discovered URLs
python src/main.py <URL> --multi-page --verbose --max-pages 5
```

**Solutions:**
```python
# Modify URL patterns in multi_scraper.py:
# Add site-specific patterns
doc_patterns = [
    r'/docs?/',
    r'/guide/',
    r'/tutorial/',
    r'/your-custom-pattern/',  # Add custom patterns
]

# Add to exclusion patterns
exclude_patterns = [
    r'/search',
    r'/login',
    r'/your-exclusion-pattern/',  # Add custom exclusions
]
```

### Infinite Loop in Link Discovery

**Problem:** Scraper keeps finding same URLs

**Solution:**
```python
# Enhanced duplicate detection in multi_scraper.py:
def normalize_url(self, url):
    # Remove query parameters and fragments
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip('/')
```

### Index File Issues

**Problem:** Generated index file is incomplete or broken

**Solution:**
```bash
# Regenerate index manually if needed
# Check output directory structure
ls -la ./output-directory/

# Verify file names are valid
# Check for special characters in filenames
```

## 🆘 General Debugging Steps

### Step 1: Verify Basic Functionality

```bash
# Test with simple site
python src/main.py https://example.com --verbose

# Test Chrome/WebDriver
python src/main.py https://httpbin.org/html --no-headless
```

### Step 2: Isolate the Problem

```bash
# Test single page vs multi-page
python src/main.py <URL> --verbose
python src/main.py <URL> --multi-page --max-pages 1 --verbose

# Test with/without headless
python src/main.py <URL> --no-headless --verbose
```

### Step 3: Gather Debug Information

```bash
# Full verbose output
python src/main.py <URL> --verbose --no-headless --wait 10 2>&1 | tee debug.log

# System information
python --version
pip list | grep -E "(selenium|beautifulsoup|html2text)"
google-chrome --version  # or chrome --version
```

### Step 4: Check Common Solutions

1. **Clear caches:** ChromeDriver, pip, browser
2. **Update everything:** Python packages, Chrome, ChromeDriver
3. **Try different settings:** Wait times, timeouts, rate limits
4. **Test with simpler sites:** Verify basic functionality

### Step 5: Get Help

When reporting issues, include:

```bash
# Environment information
echo "OS: $(uname -a)"
echo "Python: $(python --version)"
echo "Chrome: $(google-chrome --version)"
echo "Pip packages:"
pip list | grep -E "(selenium|beautifulsoup|html2text|webdriver-manager)"

# Command used
echo "Command: python src/main.py <URL> [options]"

# Error output
echo "Error output:" && python src/main.py <URL> --verbose 2>&1
```

## 📞 Getting Additional Help

If these solutions don't resolve your issue:

1. **Check [FAQ](faq.md)** for common questions
2. **Search [GitHub Issues](https://github.com/YOUR_USERNAME/Markdownizer/issues)**
3. **Create a new issue** with:
   - Complete error message
   - Environment information
   - Steps to reproduce
   - Expected vs actual behavior

Remember: Most issues are related to Chrome/WebDriver setup, network connectivity, or site-specific quirks that can be resolved with configuration adjustments.