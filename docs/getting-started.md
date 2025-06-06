# Getting Started with Markdownizer

This guide will help you install and set up Markdownizer for converting documentation pages to Markdown.

## 📋 Prerequisites

### System Requirements

- **Python 3.7+** (Python 3.8+ recommended)
- **Google Chrome browser** (latest version)
- **Operating System**: Windows, macOS, or Linux
- **Internet connection** (for ChromeDriver auto-download)

### Verify Python Installation

```bash
python --version
# Should output: Python 3.7.x or higher
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Markdownizer.git
cd Markdownizer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
python src/main.py --help
```

You should see the help output with all available options.

## 🎯 Your First Conversion

### Single Page Conversion

```bash
# Convert a simple documentation page
python src/main.py https://docs.python.org/3/tutorial/introduction.html
```

This will create an `output.md` file in your current directory.

### Multi-Page Scraping

```bash
# Scrape a complete documentation section
python src/main.py https://docs.python.org/3/tutorial/ --multi-page --max-pages 10
```

This will create a directory with multiple Markdown files and an index.

## 🔧 Chrome Setup

Markdownizer automatically downloads and manages ChromeDriver, but you need Chrome browser installed.

### Install Chrome Browser

- **Windows**: Download from [google.com/chrome](https://www.google.com/chrome/)
- **macOS**: `brew install --cask google-chrome`
- **Ubuntu/Debian**: 
  ```bash
  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  sudo apt-get update
  sudo apt-get install google-chrome-stable
  ```

### Verify Chrome Installation

```bash
# Windows
chrome --version

# macOS/Linux
google-chrome --version
```

## 🛠️ Troubleshooting Installation

### Common Issues

**1. Python not found**
```bash
# Try python3 instead
python3 src/main.py --help
```

**2. pip not found**
```bash
# Try pip3 or install pip
python -m pip install -r requirements.txt
```

**3. ChromeDriver issues**
```bash
# Clear ChromeDriver cache
rmdir /s "%USERPROFILE%\.wdm"  # Windows
rm -rf ~/.wdm                   # macOS/Linux

# Reinstall webdriver-manager
pip uninstall webdriver-manager
pip install webdriver-manager
```

**4. Permission errors**
```bash
# Use virtual environment (recommended)
python -m venv markdownizer-env
source markdownizer-env/bin/activate  # macOS/Linux
markdownizer-env\Scripts\activate     # Windows

pip install -r requirements.txt
```

### Virtual Environment Setup (Recommended)

```bash
# Create virtual environment
python -m venv markdownizer-env

# Activate virtual environment
# Windows:
markdownizer-env\Scripts\activate
# macOS/Linux:
source markdownizer-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# When done, deactivate
deactivate
```

## 🎮 Quick Test

Run this command to test your installation:

```bash
python src/main.py https://httpbin.org/html --verbose
```

If successful, you should see:
- ChromeDriver setup messages
- Page scraping progress
- Conversion completion
- Output file creation

## 📝 Configuration

### Basic Configuration

Create a simple test to verify everything works:

```bash
# Test single page conversion
python src/main.py https://example.com -o test-output.md --verbose

# Test multi-page (limited)
python src/main.py https://example.com --multi-page --max-pages 1 --verbose
```

### Environment Variables

You can set these environment variables for customization:

```bash
# Windows
set MARKDOWNIZER_WAIT_TIME=10
set MARKDOWNIZER_OUTPUT_DIR=./docs

# macOS/Linux
export MARKDOWNIZER_WAIT_TIME=10
export MARKDOWNIZER_OUTPUT_DIR=./docs
```

## 🔗 Next Steps

Now that you have Markdownizer installed:

1. **Read the [User Guide](user-guide.md)** for detailed usage instructions
2. **Check [Examples](examples/)** for real-world usage scenarios
3. **Review [Configuration](configuration.md)** for customization options
4. **See [Troubleshooting](troubleshooting.md)** if you encounter issues

## 💡 Tips for New Users

- Start with single-page conversions to familiarize yourself
- Use `--verbose` flag to understand what's happening
- Test with simple sites before trying complex documentation
- Use `--no-headless` to see the browser in action (debugging)
- Always check the output quality and adjust settings as needed

## 📞 Getting Help

If you encounter issues:

1. Check the [Troubleshooting Guide](troubleshooting.md)
2. Review [FAQ](faq.md) for common questions
3. Search existing [GitHub Issues](https://github.com/YOUR_USERNAME/Markdownizer/issues)
4. Create a new issue with detailed information

### Issue Reporting Template

When reporting issues, include:

```
**Environment:**
- OS: [Windows/macOS/Linux version]
- Python version: [output of python --version]
- Chrome version: [output of chrome --version]

**Command used:**
```bash
python src/main.py [your command]
```

**Error message:**
[paste full error message]

**Expected behavior:**
[what you expected to happen]
```