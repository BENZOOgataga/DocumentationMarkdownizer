# User Guide

Complete guide to using Markdownizer for converting documentation pages and scraping entire documentation sites.

## 📖 Table of Contents

- [Basic Usage](#basic-usage)
- [Single Page Conversion](#single-page-conversion)
- [Multi-Page Scraping](#multi-page-scraping)
- [Command Line Options](#command-line-options)
- [Output Management](#output-management)
- [Advanced Techniques](#advanced-techniques)

## 🎯 Basic Usage

### Command Structure

```bash
python src/main.py <URL> [OPTIONS]
```

### Simple Examples

```bash
# Convert single page to output.md
python src/main.py https://docs.example.com/api

# Convert with custom filename
python src/main.py https://docs.example.com/api -o api-docs.md

# Scrape multiple pages
python src/main.py https://docs.example.com/guide --multi-page
```

## 📄 Single Page Conversion

### Basic Single Page Conversion

```bash
# Default output (output.md)
python src/main.py https://docs.python.org/3/tutorial/introduction.html

# Custom filename
python src/main.py https://docs.python.org/3/tutorial/introduction.html -o python-intro.md

# Custom output directory
python src/main.py https://docs.python.org/3/tutorial/introduction.html --output-path="./python-docs"
```

### Single Page Options

```bash
# Wait longer for slow pages
python src/main.py https://slow-site.com/docs --wait 15

# Set maximum timeout
python src/main.py https://slow-site.com/docs --timeout 60

# Debug mode (visible browser)
python src/main.py https://docs.example.com/api --no-headless --verbose

# Force overwrite existing file
python src/main.py https://docs.example.com/api -o existing-file.md --force
```

## 🌐 Multi-Page Scraping

Multi-page scraping automatically discovers and converts entire documentation sites.

### Basic Multi-Page Usage

```bash
# Scrape up to 50 pages (default)
python src/main.py https://docs.example.com/guide --multi-page

# Limit to specific number of pages
python src/main.py https://docs.example.com/guide --multi-page --max-pages 20

# Custom output directory
python src/main.py https://docs.example.com/guide --multi-page --output-path="./complete-docs"
```

### Multi-Page with Rate Limiting

```bash
# Respectful scraping with 2-second delays
python src/main.py https://docs.example.com/guide --multi-page --rate-limit 2.0

# Very respectful scraping (5-second delays)
python src/main.py https://docs.example.com/guide --multi-page --rate-limit 5.0 --max-pages 10
```

### Real-World Multi-Page Examples

```bash
# Scrape React documentation
python src/main.py https://react.dev/learn --multi-page --max-pages 30 --output-path="./react-docs"

# Scrape Vue.js guide
python src/main.py https://vuejs.org/guide/ --multi-page --max-pages 25 --rate-limit 2.0

# Scrape Python tutorial
python src/main.py https://docs.python.org/3/tutorial/ --multi-page --max-pages 15

# Scrape API documentation
python src/main.py https://api.example.com/docs --multi-page --max-pages 50 --output-path="./api-docs"
```

### How Multi-Page Scraping Works

1. **Starting Point**: Begins with the provided URL
2. **Link Discovery**: Finds documentation links in:
   - Navigation menus
   - Sidebars
   - Table of contents
   - Content areas
3. **Intelligent Filtering**: Only follows links that match documentation patterns:
   - `/docs/`, `/guide/`, `/tutorial/`, `/reference/`
   - `/api/`, `/manual/`, `/help/`, `/documentation/`
4. **Content Extraction**: Converts each page to clean Markdown
5. **File Organization**: Creates meaningful filenames from page titles
6. **Index Generation**: Creates `index.md` with links to all pages

## ⚙️ Command Line Options

### Core Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output` | `-o` | Output filename (single page only) | `output.md` |
| `--output-path` | | Output directory | Current directory |
| `--verbose` | `-v` | Enable detailed logging | Disabled |
| `--force` | `-f` | Overwrite without prompting | Disabled |

### Multi-Page Options

| Option | Description | Default |
|--------|-------------|---------|
| `--multi-page` | Enable multi-page scraping | Disabled |
| `--max-pages` | Maximum pages to scrape | 50 |
| `--rate-limit` | Delay between requests (seconds) | 1.0 |
| `--same-domain-only` | Only scrape same domain | Enabled |

### Browser Options

| Option | Description | Default |
|--------|-------------|---------|
| `--wait` | Page load wait time (seconds) | 5 |
| `--timeout` | Maximum page load timeout | 30 |
| `--no-headless` | Show browser (debugging) | Headless |

## 📁 Output Management

### File Naming

**Single Page Mode:**
- Default: `output.md`
- Custom: `-o filename.md`
- Auto-numbered: `output_1.md`, `output_2.md` if file exists

**Multi-Page Mode:**
- Directory name: Generated from domain or custom `--output-path`
- File names: Generated from page titles
- Index file: Always `index.md`

### Output Structure Examples

**Single Page:**
```
./
├── output.md              # Default
├── api-reference.md       # Custom name
└── output_1.md           # Auto-numbered
```

**Multi-Page:**
```
./docs-example-com_docs/   # Auto-generated directory
├── index.md              # Generated index
├── getting-started.md    # From page title
├── api-reference.md      # From page title
├── user-guide.md         # From page title
└── troubleshooting.md    # From page title
```

### Handling Existing Files

```bash
# Prompt before overwriting (default)
python src/main.py https://docs.example.com/api -o existing.md

# Force overwrite without prompting
python src/main.py https://docs.example.com/api -o existing.md --force

# Auto-number if file exists (single page)
python src/main.py https://docs.example.com/api
# Creates: output.md, output_1.md, output_2.md, etc.
```

## 🔧 Advanced Techniques

### Debugging and Troubleshooting

```bash
# Maximum verbosity with visible browser
python src/main.py https://problematic-site.com --no-headless --verbose --wait 15

# Debug multi-page discovery
python src/main.py https://docs.example.com --multi-page --verbose --max-pages 5

# Test with minimal pages first
python src/main.py https://docs.example.com --multi-page --max-pages 3 --rate-limit 3.0
```

### Site-Specific Optimizations

**For slow sites:**
```bash
python src/main.py https://slow-docs.com --wait 20 --timeout 120 --rate-limit 5.0
```

**For JavaScript-heavy sites:**
```bash
python src/main.py https://spa-docs.com --wait 10 --no-headless --verbose
```

**For large documentation sites:**
```bash
python src/main.py https://huge-docs.com --multi-page --max-pages 100 --rate-limit 2.0 --output-path="./massive-docs"
```

### Batch Processing

**Process multiple sites:**
```bash
#!/bin/bash
SITES=(
    "https://docs.react.dev/learn"
    "https://vuejs.org/guide/"
    "https://docs.python.org/3/tutorial/"
)

for site in "${SITES[@]}"; do
    echo "Processing: $site"
    python src/main.py "$site" --multi-page --max-pages 30 --force
    sleep 5  # Brief pause between sites
done
```

**Create organized documentation:**
```bash
# Organize by framework
python src/main.py https://react.dev/learn --multi-page --output-path="./docs/react"
python src/main.py https://vuejs.org/guide/ --multi-page --output-path="./docs/vue"
python src/main.py https://angular.io/guide/setup-local --multi-page --output-path="./docs/angular"
```

### Performance Optimization

**Faster scraping (less respectful):**
```bash
python src/main.py https://docs.example.com --multi-page --rate-limit 0.5 --max-pages 20
```

**More respectful scraping:**
```bash
python src/main.py https://docs.example.com --multi-page --rate-limit 3.0 --max-pages 50
```

**Memory-efficient for large sites:**
```bash
python src/main.py https://huge-docs.com --multi-page --max-pages 25
# Process in smaller chunks
```

## 📊 Understanding Output Quality

### Good Output Indicators

- Clean, readable Markdown formatting
- Proper heading hierarchy
- Preserved code blocks and syntax highlighting
- Working internal links (in multi-page mode)
- Meaningful filenames

### Common Issues and Solutions

**Poor content extraction:**
```bash
# Use debug mode to see what's captured
python src/main.py https://problematic-site.com --no-headless --verbose
```

**Missing JavaScript content:**
```bash
# Increase wait time
python src/main.py https://js-heavy-site.com --wait 15 --timeout 60
```

**Too many unwanted pages in multi-page mode:**
```bash
# Reduce max-pages and check patterns
python src/main.py https://docs.example.com --multi-page --max-pages 10 --verbose
```

## 🎯 Best Practices

### For Single Page Conversion

1. **Test first**: Use `--verbose` to understand the process
2. **Adjust timing**: Use `--wait` for slow-loading content
3. **Choose good filenames**: Use `-o` with descriptive names
4. **Organize output**: Use `--output-path` for organization

### For Multi-Page Scraping

1. **Start small**: Begin with `--max-pages 5-10` to test
2. **Be respectful**: Use appropriate `--rate-limit` values (1-3 seconds)
3. **Monitor progress**: Use `--verbose` for the first run
4. **Organize output**: Always use `--output-path` for multi-page
5. **Check patterns**: Verify it's scraping the right pages

### General Best Practices

1. **Respect robots.txt**: Check site's robots.txt before large scraping
2. **Use rate limiting**: Always include `--rate-limit` for multi-page
3. **Test incrementally**: Start small and scale up
4. **Monitor resources**: Watch CPU/memory usage for large sites
5. **Backup originals**: Keep original URLs documented
6. **Review output**: Always check output quality

## 🔗 Next Steps

- **[Configuration Guide](configuration.md)** - Customize Markdownizer behavior
- **[Examples](examples/)** - See real-world usage examples
- **[Troubleshooting](troubleshooting.md)** - Solve common issues
- **[API Reference](api-reference.md)** - Technical documentation