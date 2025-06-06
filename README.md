# Documentation to Markdown Converter

A Python tool that converts documentation pages to Markdown format, handling JavaScript-rendered content.

## Features

- Converts any documentation page to clean Markdown
- Handles JavaScript-rendered content using Selenium
- Extracts main content automatically
- Removes navigation, ads, and other unwanted elements
- Supports headless browser operation
- Customizable wait times for slow-loading pages

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. The tool will automatically download ChromeDriver when first run.

## Usage

### Basic usage:
```bash
python src/main.py https://example.com/docs/page
```

### With custom output file:
```bash
python src/main.py https://example.com/docs/page -o my_docs.md
```

### With custom wait time (for slow pages):
```bash
python src/main.py https://example.com/docs/page --wait 10
```

### Run with visible browser (for debugging):
```bash
python src/main.py https://example.com/docs/page --no-headless
```

## Examples

```bash
# Convert a React documentation page
python src/main.py https://reactjs.org/docs/getting-started.html

# Convert Vue.js docs with longer wait time
python src/main.py https://vuejs.org/guide/ --wait 8 -o vue-guide.md
```

## Requirements

- Python 3.7+
- Chrome browser installed
- Internet connection