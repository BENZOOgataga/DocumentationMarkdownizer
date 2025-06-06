# config.py

# Configuration settings for the doc-to-markdown-converter project

DEFAULT_OUTPUT_FORMAT = 'markdown'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
TIMEOUT = 10  # seconds for HTTP requests
MAX_RETRIES = 3  # number of retries for failed requests
OUTPUT_DIRECTORY = 'output'  # directory to save converted Markdown files