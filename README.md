# Markdownizer - Documentation to Markdown Converter

A robust Python tool that converts documentation pages to clean Markdown format, handling JavaScript-rendered content using Selenium WebDriver.

## 🚀 Features

- **JavaScript Support**: Handles dynamically loaded content using Selenium Chrome WebDriver
- **Smart Content Extraction**: Automatically identifies and extracts main documentation content
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

### Basic Usage
```bash
# Convert a documentation page
python src/main.py https://docs.example.com/api

# Convert with custom filename
python src/main.py https://docs.example.com/api -o my-docs.md

# Convert to specific directory
python src/main.py https://docs.example.com/api --output-path="./documentation"
```

### Advanced Options
```bash
python src/main.py <URL> [OPTIONS]
```

#### Command Line Options:
- `-o, --output FILENAME`: Specify output filename
- `--output-path PATH`: Specify output directory
- `--wait SECONDS`: Wait time for page loading (default: 5)
- `--timeout SECONDS`: Maximum wait time (default: 30)
- `--no-headless`: Run browser visibly for debugging
- `--verbose, -v`: Enable detailed logging
- `--force, -f`: Overwrite existing files without prompting

### Real-World Examples

```bash
# Convert API documentation with extended wait time
python src/main.py https://api.example.com/docs --wait 10 --output-path="./api-docs"

# Debug problematic page with visible browser
python src/main.py https://complex-site.com/docs --no-headless --verbose

# Batch convert to organized directory structure
python src/main.py https://docs.react.dev/learn --output-path="./docs/react" -o react-tutorial.md

# Force overwrite existing file
python src/main.py https://vue-docs.com/guide --force -o vue-guide.md

# Convert with auto-generated filename
python src/main.py https://docs.python.org/3/tutorial/ --output-path="./python-docs"
```

## 📁 File Management

### Output File Handling
- **Auto-numbering**: If `output.md` exists, creates `output_1.md`, `output_2.md`, etc.
- **Custom paths**: Use `--output-path` to organize files in directories
- **Safe overwrites**: Prompts before overwriting unless `--force` is used
- **Auto-naming**: Generates filenames from page titles when not specified

### Examples:
```bash
# These will create numbered files if they exist:
python src/main.py https://site1.com/docs  # → output.md
python src/main.py https://site2.com/docs  # → output_1.md  
python src/main.py https://site3.com/docs  # → output_2.md

# Organized output:
python src/main.py https://react.dev/docs --output-path="./docs/react"
python src/main.py https://vue.js.org/guide --output-path="./docs/vue"
```

## 🏗️ Project Structure

```
Markdownizer/
├── src/
│   ├── main.py          # CLI interface and main logic
│   ├── scraper.py       # Web scraping with Selenium
│   ├── converter.py     # HTML to Markdown conversion
│   └── utils.py         # Utility functions
├── requirements.txt     # Python dependencies
├── README.md           # This documentation
└── .gitignore          # Git ignore rules
```

## 🔧 How It Works

1. **Web Scraping**: Uses Selenium WebDriver to load pages and execute JavaScript
2. **Content Detection**: Intelligently identifies main content areas
3. **Content Cleaning**: Removes navigation, ads, and unwanted elements
4. **Markdown Conversion**: Converts clean HTML to well-formatted Markdown
5. **File Management**: Handles output paths and prevents file conflicts

## 🎛️ Supported Sites

- **Documentation Platforms**: GitBook, Docusaurus, VuePress, Sphinx
- **API References**: Swagger/OpenAPI, Postman docs, custom API documentation
- **Framework Docs**: React, Vue, Angular, Django, Flask documentation
- **Technical Resources**: MDN, W3Schools, Stack Overflow documentation
- **Wiki Pages**: GitHub wikis, Confluence, MediaWiki

## 🐛 Troubleshooting

### Common Issues

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

**Permission Errors:**
```bash
# Check directory permissions
python src/main.py <URL> --output-path="/path/with/write/access"
```

**Content Quality Issues:**
```bash
# Use verbose mode to see what's happening
python src/main.py <URL> --verbose --no-headless
```

### Debug Mode

```bash
# Run with maximum verbosity and visible browser
python src/main.py <URL> --no-headless --verbose --wait 10
```

## 🚀 Production Usage

### Batch Processing
```bash
# Create a script for multiple URLs
#!/bin/bash
URLS=(
    "https://docs.react.dev/learn"
    "https://vuejs.org/guide/"
    "https://angular.io/guide/setup-local"
)

for url in "${URLS[@]}"; do
    python src/main.py "$url" --output-path="./docs" --force
done
```

### CI/CD Integration
```yaml
# GitHub Actions example
- name: Convert Documentation
  run: |
    python src/main.py ${{ env.DOC_URL }} \
      --output-path="./generated-docs" \
      --force --verbose
```

## 📊 Performance Tips

- Use `--wait` appropriately for your target sites
- Set reasonable `--timeout` values for slow sites
- Use `--headless` (default) for better performance
- Consider batch processing for multiple pages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🔄 Changelog

### v2.0.0 (Production Ready)
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