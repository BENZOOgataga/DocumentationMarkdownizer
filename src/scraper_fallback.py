import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class DocumentationScraper:
    def __init__(self, headless=True):
        self.driver = None
        self.headless = headless
        
    def setup_driver(self):
        """Setup Chrome WebDriver with manual Chrome path"""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        # Common Chrome installation paths on Windows
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
        ]
        
        chrome_path = None
        for path in chrome_paths:
            if os.path.exists(path):
                chrome_path = path
                break
                
        if chrome_path:
            chrome_options.binary_location = chrome_path
            
        try:
            # Try without service first
            self.driver = webdriver.Chrome(options=chrome_options)
        except Exception as e:
            print(f"Error: {str(e)}")
            raise Exception("Please install Chrome browser or add ChromeDriver to PATH")
        
    def scrape_page(self, url, wait_time=5):
        """Scrape a documentation page, waiting for JavaScript to load"""
        if not self.driver:
            self.setup_driver()
            
        try:
            print(f"Loading page: {url}")
            self.driver.get(url)
            time.sleep(wait_time)
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            time.sleep(3)
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            return soup
            
        except Exception as e:
            print(f"Error scraping page: {str(e)}")
            return None
            
    def close(self):
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass