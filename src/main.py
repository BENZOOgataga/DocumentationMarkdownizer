import argparse
import os
from scraper import DocumentationScraper
from converter import DocumentationConverter

def main():
    parser = argparse.ArgumentParser(description='Convert documentation page to Markdown')
    parser.add_argument('url', help='URL of the documentation page to convert')
    parser.add_argument('-o', '--output', help='Output file path (default: output.md)', default='output.md')
    parser.add_argument('--wait', type=int, help='Wait time for page to load (seconds)', default=5)
    parser.add_argument('--no-headless', action='store_true', help='Run browser in non-headless mode')
    
    args = parser.parse_args()
    
    print(f"Converting documentation from: {args.url}")
    
    # Initialize scraper and converter
    scraper = DocumentationScraper(headless=not args.no_headless)
    converter = DocumentationConverter()
    
    try:
        # Scrape the page
        print("Scraping page content...")
        soup = scraper.scrape_page(args.url, wait_time=args.wait)
        
        if soup:
            # Convert to markdown
            print("Converting to Markdown...")
            markdown_content = converter.convert_to_markdown(soup)
            
            # Ensure output directory exists
            output_dir = os.path.dirname(args.output)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Write to file
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            print(f"✅ Conversion completed! Output saved to: {args.output}")
        else:
            print("❌ Failed to scrape the page content.")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        
    finally:
        scraper.close()

if __name__ == "__main__":
    main()