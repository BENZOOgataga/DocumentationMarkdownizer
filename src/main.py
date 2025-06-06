import argparse
import os
import sys
import logging
from pathlib import Path
from scraper import DocumentationScraper
from converter import DocumentationConverter
from utils import sanitize_filename, get_safe_output_path, setup_logging

def main():
    parser = argparse.ArgumentParser(
        description='Convert documentation page to Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/main.py https://docs.example.com/api
  python src/main.py https://docs.example.com/api -o custom-name.md
  python src/main.py https://docs.example.com/api --output-path="./docs"
  python src/main.py https://docs.example.com/api --wait 10 --no-headless
        """
    )
    
    parser.add_argument('url', help='URL of the documentation page to convert')
    parser.add_argument('-o', '--output', 
                       help='Output filename (default: auto-generated from page title)')
    parser.add_argument('--output-path', 
                       help='Output directory path (default: current directory)')
    parser.add_argument('--wait', type=int, default=5,
                       help='Wait time for page to load in seconds (default: 5)')
    parser.add_argument('--no-headless', action='store_true',
                       help='Run browser in non-headless mode for debugging')
    parser.add_argument('--timeout', type=int, default=30,
                       help='Maximum time to wait for page load in seconds (default: 30)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--force', '-f', action='store_true',
                       help='Overwrite existing output file without prompting')
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    logger = logging.getLogger(__name__)
    
    try:
        # Validate URL
        if not args.url.startswith(('http://', 'https://')):
            logger.error("❌ Invalid URL. Please provide a URL starting with http:// or https://")
            sys.exit(1)
        
        logger.info(f"🚀 Starting conversion of: {args.url}")
        
        # Initialize scraper and converter
        scraper = DocumentationScraper(headless=not args.no_headless)
        converter = DocumentationConverter()
        
        # Scrape the page
        logger.info("🔍 Scraping page content...")
        soup = scraper.scrape_page(args.url, wait_time=args.wait, timeout=args.timeout)
        
        if not soup:
            logger.error("❌ Failed to scrape the page content.")
            sys.exit(1)
        
        # Convert to markdown
        logger.info("🔄 Converting HTML to Markdown...")
        markdown_content = converter.convert_to_markdown(soup)
        
        if not markdown_content or "Error:" in markdown_content:
            logger.error(f"❌ Conversion failed: {markdown_content}")
            sys.exit(1)
        
        # Determine output file path
        output_path = determine_output_path(
            args.output, 
            args.output_path, 
            soup, 
            args.force,
            logger
        )
        
        if not output_path:
            logger.error("❌ Could not determine output path.")
            sys.exit(1)
        
        # Write to file
        write_output_file(output_path, markdown_content, logger)
        
        logger.info(f"✅ Conversion completed successfully!")
        logger.info(f"📄 Output saved to: {output_path}")
        logger.info(f"📊 File size: {os.path.getsize(output_path)} bytes")
        
    except KeyboardInterrupt:
        logger.info("\n⚠️  Conversion interrupted by user.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        if args.verbose:
            logger.exception("Full error traceback:")
        sys.exit(1)
    finally:
        try:
            scraper.close()
        except:
            pass

def determine_output_path(output_arg, output_path_arg, soup, force, logger):
    """Determine the final output file path"""
    
    # Set base directory
    if output_path_arg:
        base_dir = Path(output_path_arg)
        base_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"📁 Using output directory: {base_dir}")
    else:
        base_dir = Path.cwd()
    
    # Determine filename
    if output_arg:
        filename = output_arg
        if not filename.endswith('.md'):
            filename += '.md'
    else:
        # Generate filename from page title
        page_title = get_page_title_from_soup(soup)
        filename = sanitize_filename(page_title) + '.md'
        logger.info(f"📝 Generated filename from page title: {filename}")
    
    # Get safe output path (handles existing files)
    output_path = get_safe_output_path(base_dir / filename, force)
    
    if output_path != base_dir / filename:
        logger.info(f"📄 File already exists, using: {output_path.name}")
    
    # Confirm overwrite if file exists and force is not set
    if output_path.exists() and not force:
        response = input(f"⚠️  File '{output_path}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            logger.info("❌ Operation cancelled by user.")
            return None
    
    return output_path

def get_page_title_from_soup(soup):
    """Extract page title from BeautifulSoup object"""
    # Try multiple selectors for title
    title_selectors = ['title', 'h1', '[data-title]', '.title', '.page-title']
    
    for selector in title_selectors:
        element = soup.select_one(selector)
        if element:
            title = element.get_text().strip()
            if title:
                return title[:50]  # Limit length
    
    return "documentation"

def write_output_file(output_path, content, logger):
    """Write content to output file with error handling"""
    try:
        # Ensure directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write file with UTF-8 encoding
        with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        
        logger.debug(f"✅ Successfully wrote {len(content)} characters to {output_path}")
        
    except PermissionError:
        logger.error(f"❌ Permission denied: Cannot write to {output_path}")
        raise
    except OSError as e:
        logger.error(f"❌ OS Error while writing file: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Unexpected error while writing file: {e}")
        raise

if __name__ == "__main__":
    main()