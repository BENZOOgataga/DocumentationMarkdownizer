import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import sys

class DocumentationScraper:
    def __init__(self, headless=True):
        self.driver = None
        self.headless = headless
        
    def setup_driver(self):
        """Setup Chrome WebDriver with appropriate options"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--disable-extensions')
        
        try:
            # Try to get ChromeDriver path
            print("Downloading/updating ChromeDriver...")
            driver_path = ChromeDriverManager().install()
            print(f"ChromeDriver path: {driver_path}")
            
            # Verify the driver exists and is executable
            if not os.path.exists(driver_path):
                raise Exception(f"ChromeDriver not found at {driver_path}")
                
            service = Service(driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
        except Exception as e:
            print(f"Error setting up ChromeDriver: {str(e)}")
            print("Trying alternative Chrome setup...")
            
            # Try without specifying service (use system PATH)
            try:
                self.driver = webdriver.Chrome(options=chrome_options)
            except Exception as e2:
                print(f"Alternative setup also failed: {str(e2)}")
                print("\nPlease ensure:")
                print("1. Chrome browser is installed")
                print("2. ChromeDriver is in your PATH, or")
                print("3. Run: pip install --upgrade webdriver-manager")
                raise Exception("Unable to initialize Chrome WebDriver")
        
    def scrape_page(self, url, wait_time=5):
        """Scrape a documentation page, waiting for JavaScript to load"""
        if not self.driver:
            self.setup_driver()
            
        try:
            print(f"Loading page: {url}")
            self.driver.get(url)
            
            # Wait for page to load
            time.sleep(wait_time)
            
            # Wait for main content to be present
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Additional wait for JavaScript content to load
            print("Waiting for JavaScript content...")
            time.sleep(3)
            
            # Check if we still have the JavaScript error message
            page_text = self.driver.find_element(By.TAG_NAME, "body").text
            if "enable JavaScript" in page_text and len(page_text) < 200:
                print("Page still showing JavaScript error, waiting longer...")
                time.sleep(wait_time * 2)
            
            # Get page source after JavaScript execution
            page_source = self.driver.page_source
            
            # Parse with BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')
            
            return soup
            
        except Exception as e:
            print(f"Error scraping page: {str(e)}")
            return None
            
    def close(self):
        """Close the WebDriver"""
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()