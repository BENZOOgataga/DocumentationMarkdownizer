# Markdownizer - Documentation to Markdown Converter

A Python tool that converts documentation pages to clean Markdown format, handling JavaScript-rendered content using Selenium WebDriver.

## Features

- **JavaScript Support**: Handles dynamically loaded content using Selenium Chrome WebDriver
- **Smart Content Extraction**: Automatically identifies and extracts main documentation content
- **Clean Output**: Removes navigation, ads, headers, footers, and other unwanted elements
- **Flexible Configuration**: Customizable wait times for slow-loading pages
- **Headless Operation**: Runs without visible browser window by default
- **Debug Mode**: Option to run with visible browser for troubleshooting

## Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Chrome Browser**: Ensure Google Chrome is installed on your system
3. **ChromeDriver**: The tool automatically downloads and manages ChromeDriver

## Usage

### Basic Usage
```bash
python src/main.py <URL>
```

### Advanced Options
```bash
python src/main.py <URL> [OPTIONS]
```

#### Options:
- `-o, --output FILE`: Specify output file path (default: output.md)
- `--wait SECONDS`: Wait time for page to load (default: 5)
- `--no-headless`: Run browser in visible mode for debugging

## Examples

### Basic Conversion
```bash
# Convert a documentation page to output.md
python src/main.py https://docs.example.com/api-reference

# Convert with custom output file
python src/main.py https://docs.example.com/guide -o my-guide.md
```

### Advanced Usage
```bash
# Convert slow-loading page with extended wait time
python src/main.py https://docs.example.com/complex-page --wait 10

# Debug mode with visible browser
python src/main.py https://docs.example.com/troublesome-page --no-headless

# Complete example with all options
python src/main.py https://docs.example.com/api --wait 8 -o api-docs.md
```

### Real-World Examples
```bash
# Convert Pterodactyl API documentation
python src/main.py https://dashflo.net/docs/api/pterodactyl/v1/ -o pterodactyl-api.md

# Convert React documentation
python src/main.py https://reactjs.org/docs/getting-started.html -o react-getting-started.md

# Convert Vue.js guide with longer wait time
python src/main.py https://vuejs.org/guide/ --wait 8 -o vue-guide.md

# Convert MDN documentation
python src/main.py https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide --wait 6 -o js-guide.md
```

## Project Structure

```
Markdownizer/
├── src/
│   ├── main.py          # Main entry point and CLI interface
│   ├── scraper.py       # Web scraping logic with Selenium
│   ├── converter.py     # HTML to Markdown conversion
│   ├── utils.py         # Utility functions
│   └── output.md        # Default output file
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## How It Works

1. **Web Scraping**: Uses Selenium WebDriver to load the page and execute JavaScript
2. **Content Extraction**: Identifies main content areas using common CSS selectors
3. **Cleaning**: Removes unwanted elements like navigation, ads, and scripts
4. **Conversion**: Converts clean HTML to Markdown using html2text
5. **Output**: Saves formatted Markdown to specified file

## Supported Page Types

- **Documentation Sites**: GitBook, Docusaurus, VuePress, etc.
- **API References**: Swagger, Postman, custom API docs
- **Technical Guides**: MDN, W3Schools, framework documentation
- **Blog Posts**: Technical articles and tutorials
- **Wiki Pages**: GitHub wikis, Confluence, etc.

## Troubleshooting

### Common Issues

**"WinError 193: %1 is not a valid Win32 application"**
```bash
# Clear ChromeDriver cache
rmdir /s "%USERPROFILE%\.wdm"
pip uninstall webdriver-manager
pip install webdriver-manager
```

**"JavaScript error: enable JavaScript"**
```bash
# Increase wait time
python src/main.py <URL> --wait 15
```

**Page not loading correctly**
```bash
# Use debug mode to see what's happening
python src/main.py <URL> --no-headless
```

### Tips for Better Results

- Use `--wait` for pages with heavy JavaScript loading
- Some sites may require longer wait times (10-15 seconds)
- Use `--no-headless` to debug page loading issues
- Check the output file for quality and adjust wait times accordingly

## Requirements

- **Python**: 3.7 or higher
- **Chrome Browser**: Latest version recommended
- **Internet Connection**: Required for downloading ChromeDriver and accessing pages
- **Operating System**: Windows, macOS, or Linux

## Dependencies

- `selenium`: Web automation and browser control
- `beautifulsoup4`: HTML parsing and manipulation
- `html2text`: HTML to Markdown conversion
- `webdriver-manager`: Automatic ChromeDriver management
- `requests`: HTTP requests (fallback)
- `markdownify`: Additional Markdown conversion support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with various documentation sites
5. Submit a pull request

## License

This project is open source. Feel free to use, modify, and distribute.

## Changelog

### v1.0.0
- Initial release with Selenium support
- Automatic content extraction
- Customizable wait times
- Headless and debug modes
- Clean Markdown output