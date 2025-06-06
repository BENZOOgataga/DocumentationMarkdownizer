# Markdownizer - Documentation to Markdown Converter

A robust Python tool that converts documentation pages to clean Markdown format, handling JavaScript-rendered content using Selenium WebDriver. **NEW in v1.2.0**: Multi-page documentation scraping!

## 🚀 Features

- **JavaScript Support**: Handles dynamically loaded content using Selenium Chrome WebDriver
- **Smart Content Extraction**: Automatically identifies and extracts main documentation content
- **🆕 Multi-Page Scraping**: Scrape entire documentation sites with automatic link discovery
- **Intelligent Link Detection**: Automatically finds and follows documentation links
- **Clean Output**: Removes navigation, ads, headers, footers, and other unwanted elements
- **File Management**: Intelligent handling of existing output files with auto-numbering
- **Flexible Output**: Custom output paths and filenames
- **Production Ready**: Comprehensive error handling, logging, and validation
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📦 Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd Markdownizer
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **System Requirements:**
   - Python 3.7+
   - Google Chrome browser
   - Internet connection (for ChromeDriver auto-download)

## 🎯 Usage

### Single Page Conversion (Original Mode)
```bash
# Convert a single documentation page
python src/main.py https://docs.example.com/api

# Convert with custom filename
python src/main.py https://docs.example.com/api -o my-docs.md

# Convert to specific directory
python src/main.py https://docs.example.com/api --output-path="./documentation"
```

### 🆕 Multi-Page Documentation Scraping
```bash
# Scrape entire documentation (up to 50 pages by default)
python src/main.py https://docs.example.com/guide --multi-page

# Scrape with custom limits and output directory
python src/main.py https://docs.example.com --multi-page --max-pages 100 --output-path="./full-docs"

# Scrape with custom rate limiting (slower, more respectful)
python src/main.py https://docs.example.com --multi-page --rate-limit 2.0
```

### Command Line Options

#### Basic Options:
- `-o, --output FILENAME`: Specify output filename (single page only)
- `--output-path PATH`: Specify output directory
- `--verbose, -v`: Enable detailed logging
- `--force, -f`: Overwrite existing files without prompting

#### Multi-Page Options:
- `--multi-page`: Enable multi-page scraping mode
- `--max-pages NUMBER`: Maximum pages to scrape (default: 50)
- `--same-domain-only`: Only scrape pages from same domain (default: true)
- `--rate-limit SECONDS`: Delay between requests (default: 1.0)

#### Browser Options:
- `--wait SECONDS`: Wait time for page loading (default: 5)
- `--timeout SECONDS`: Maximum wait time (default: 30)
- `--no-headless`: Run browser visibly for debugging

## 🌟 Real-World Examples

### Single Page Examples
```bash
# Convert React documentation
python src/main.py https://react.dev/learn/your-first-component -o react-component-guide.md

# Convert API reference with debug mode
python src/main.py https://api.example.com/reference --no-headless --verbose
```

### Multi-Page Examples
```bash
# Scrape complete React documentation
python src/main.py https://react.dev/learn --multi-page --max-pages 30 --output-path="./react-docs"

# Scrape Vue.js guide with respectful rate limiting
python src/main.py https://vuejs.org/guide/ --multi-page --rate-limit 2.0 --max-pages 25

# Scrape API documentation
python src/main.py https://docs.example.com/api --multi-page --max-pages 15 --output-path="./api-docs"

# Scrape with maximum verbosity for debugging
python src/main.py https://docs.complex-site.com --multi-page --verbose --no-headless
```

## 📁 Output Structure

### Single Page Mode
```
./
├── output.md              # Default output
├── custom-name.md          # Custom filename
└── output_1.md            # Auto-numbered if file exists
```

### Multi-Page Mode
```
./docs-example-com_docs/    # Auto-generated directory
├── index.md               # Generated index with links
├── getting-started.md     # Individual pages
├── api-reference.md
├── tutorial-basics.md
└── advanced-concepts.md
```

## 🔧 How Multi-Page Scraping Works

1. **Starting Point**: Begins with the provided URL
2. **Link Discovery**: Extracts documentation links from navigation, sidebars, and content
3. **Intelligent Filtering**: Only follows links that appear to be documentation pages
4. **Content Extraction**: Converts each page to clean Markdown
5. **File Organization**: Saves files with meaningful names based on page titles
6. **Index Generation**: Creates an index.md file linking all scraped pages

### Supported Documentation Patterns
- `/docs/`, `/guide/`, `/tutorial/`, `/reference/`
- `/api/`, `/manual/`, `/help/`, `/documentation/`
- Navigation links, sidebar links, table of contents
- Same-domain links (configurable)

## 🏗️ Project Structure

```
Markdownizer/
├── src/
│   ├── main.py           # CLI interface and orchestration
│   ├── scraper.py        # Single-page web scraping
│   ├── multi_scraper.py  # 🆕 Multi-page scraping logic
│   ├── converter.py      # HTML to Markdown conversion
│   └── utils.py          # Utility functions
├── requirements.txt      # Python dependencies
├── CHANGELOG.md         # Detailed version history
└── README.md           # This documentation
```

## 🎛️ Supported Sites

### Documentation Platforms
- **GitBook**: Full site scraping with navigation
- **Docusaurus**: React-based documentation sites
- **VuePress**: Vue-powered documentation
- **Sphinx**: Python documentation standard
- **MkDocs**: Markdown-based documentation

### Framework Documentation
- **React**: Complete guide and API reference scraping
- **Vue.js**: Full documentation scraping
- **Angular**: Comprehensive guide extraction
- **Django/Flask**: Python web framework docs

### API Documentation
- **Swagger/OpenAPI**: Complete API reference
- **Postman**: API documentation collections
- **Custom API docs**: Most documentation formats

## 🐛 Troubleshooting

### Multi-Page Scraping Issues

**Too many/few pages found:**
```bash
# Adjust max-pages limit
python src/main.py <URL> --multi-page --max-pages 100

# Use verbose mode to see what links are being found
python src/main.py <URL> --multi-page --verbose
```

**Rate limiting concerns:**
```bash
# Increase delay between requests
python src/main.py <URL> --multi-page --rate-limit 3.0
```

**Wrong pages being scraped:**
```bash
# Check the patterns in multi_scraper.py and adjust if needed
# Use --verbose to see which URLs are being processed
```

### Single Page Issues

**ChromeDriver Problems:**
```bash
# Clear cache and reinstall
rmdir /s "%USERPROFILE%\.wdm"  # Windows
rm -rf ~/.wdm                   # macOS/Linux
pip install --upgrade webdriver-manager
```

**JavaScript Not Loading:**
```bash
# Increase wait time
python src/main.py <URL> --wait 15 --timeout 60

# Use debug mode
python src/main.py <URL> --no-headless --verbose
```

## 🚀 Production Usage

### Automated Documentation Backup
```bash
#!/bin/bash
# Backup multiple documentation sites
SITES=(
    "https://docs.react.dev/learn"
    "https://vuejs.org/guide/"
    "https://docs.python.org/3/tutorial/"
)

for site in "${SITES[@]}"; do
    python src/main.py "$site" --multi-page --max-pages 50 --force
done
```

### CI/CD Integration
```yaml
# GitHub Actions example
- name: Scrape Documentation
  run: |
    python src/main.py ${{ env.DOC_URL }} \
      --multi-page --max-pages 30 \
      --output-path="./scraped-docs" \
      --force --verbose
```

## 📊 Performance Tips

### Multi-Page Scraping
- Start with lower `--max-pages` values to test
- Use `--rate-limit` to be respectful to servers
- Monitor with `--verbose` for the first run
- Use `--same-domain-only` to avoid external links

### Single Page
- Use `--wait` appropriately for your target sites
- Set reasonable `--timeout` values for slow sites
- Use `--headless` (default) for better performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🔄 Changelog

### v1.2.0 - Multi-Page Documentation Scraping
- ✨ **NEW**: Multi-page documentation scraping with `--multi-page` flag
- ✨ **NEW**: Intelligent link discovery and filtering for documentation sites
- ✨ **NEW**: Automatic index file generation with links to all scraped pages
- ✨ **NEW**: Rate limiting and respectful scraping with `--rate-limit`
- ✨ **NEW**: Configurable maximum page limits with `--max-pages`
- ✨ **NEW**: Same-domain filtering to prevent external link following
- 🔧 Enhanced CLI with multi-page specific options
- 🔧 Improved filename generation from page titles
- 🔧 Better error handling for batch operations
- 📖 Updated documentation with comprehensive examples

### v1.1.0 (Production Ready)
- ✅ Added intelligent file management with auto-numbering
- ✅ Implemented custom output paths with `--output-path`
- ✅ Added comprehensive error handling and logging
- ✅ Enhanced command-line interface with more options
- ✅ Improved content extraction and cleaning
- ✅ Added timeout and retry mechanisms
- ✅ Cross-platform compatibility improvements
- ✅ Production-ready stability and error recovery

### v1.0.0
- Initial release with basic Selenium support
- Simple HTML to Markdown conversion
- Basic file output functionality
