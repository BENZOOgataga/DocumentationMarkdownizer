# Markdownizer Documentation

Welcome to the complete documentation for Markdownizer - a powerful Python tool for converting documentation pages to clean Markdown format.

## 📚 Documentation Structure

- **[Getting Started](getting-started.md)** - Installation, setup, and first steps
- **[User Guide](user-guide.md)** - Complete usage guide with examples
- **[API Reference](api-reference.md)** - Detailed API documentation
- **[Configuration](configuration.md)** - Configuration options and customization
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions
- **[Development](development.md)** - Contributing and development guide
- **[Examples](examples/)** - Real-world usage examples
- **[FAQ](faq.md)** - Frequently asked questions

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Single page conversion
python src/main.py https://docs.example.com/api

# Multi-page documentation scraping
python src/main.py https://docs.example.com/guide --multi-page
```

## 📖 What is Markdownizer?

Markdownizer is a robust Python tool that converts documentation pages to clean Markdown format. It handles JavaScript-rendered content using Selenium WebDriver and can scrape entire documentation sites automatically.

### Key Features

- **JavaScript Support**: Handles dynamically loaded content
- **Multi-Page Scraping**: Scrape entire documentation sites
- **Smart Content Extraction**: Automatically identifies main content
- **Clean Output**: Removes navigation, ads, and unwanted elements
- **Production Ready**: Comprehensive error handling and logging

## 🔗 Quick Links

- [Installation Guide](getting-started.md#installation)
- [Multi-Page Scraping Guide](user-guide.md#multi-page-scraping)
- [Configuration Options](configuration.md)
- [Troubleshooting Common Issues](troubleshooting.md)
- [Contributing Guidelines](development.md#contributing)

## 📝 Latest Updates

**v1.2.0** - Multi-Page Documentation Scraping
- Added complete documentation site scraping
- Intelligent link discovery and filtering
- Automatic index file generation
- Rate limiting and respectful scraping

For detailed changelog, see [CHANGELOG.md](../CHANGELOG.md).