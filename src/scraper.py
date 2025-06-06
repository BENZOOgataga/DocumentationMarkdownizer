import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class DocumentationScraper:
    def __init__(self, headless=True):
        self.driver = None
        self.headless = headless
        self.logger = logging.getLogger(__name__)
        
    def setup_driver(self):
        """Setup Chrome WebDriver with appropriate options"""
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless')
        
        # Chrome options for better stability
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-plugins')
        chrome_options.add_argument('--disable-images')  # Faster loading
        chrome_options.add_argument('--disable-javascript-harmony-shipping')
        chrome_options.add_argument('--disable-background-timer-throttling')
        chrome_options.add_argument('--disable-renderer-backgrounding')
        chrome_options.add_argument('--disable-backgrounding-occluded-windows')
        
        # User agent to avoid bot detection
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        try:
            self.logger.debug("Setting up ChromeDriver...")
            driver_path = ChromeDriverManager().install()
            self.logger.debug(f"ChromeDriver path: {driver_path}")
            
            if not os.path.exists(driver_path):
                raise Exception(f"ChromeDriver not found at {driver_path}")
                
            service = Service(driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Set timeouts
            self.driver.implicitly_wait(10)
            self.driver.set_page_load_timeout(60)
            
            self.logger.debug("✅ ChromeDriver setup successful")
            
        except Exception as e:
            self.logger.error(f"❌ Error setting up ChromeDriver: {str(e)}")
            self.logger.info("🔄 Trying alternative Chrome setup...")
            
            try:
                self.driver = webdriver.Chrome(options=chrome_options)
                self.driver.implicitly_wait(10)
                self.driver.set_page_load_timeout(60)
                self.logger.debug("✅ Alternative Chrome setup successful")
            except Exception as e2:
                self.logger.error(f"❌ Alternative setup failed: {str(e2)}")
                raise Exception(
                    "Unable to initialize Chrome WebDriver. Please ensure:\n"
                    "1. Chrome browser is installed\n"
                    "2. Run: pip install --upgrade webdriver-manager\n"
                    "3. Check your internet connection"
                )
        
    def scrape_page(self, url, wait_time=5, timeout=30):
        """Scrape a documentation page, waiting for JavaScript to load"""
        if not self.driver:
            self.setup_driver()
            
        try:
            self.logger.debug(f"🌐 Loading page: {url}")
            self.driver.get(url)
            
            # Wait for initial page load
            self.logger.debug(f"⏳ Waiting {wait_time}s for page to load...")
            time.sleep(wait_time)
            
            # Wait for body element
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Check for common loading indicators and wait for them to disappear
            loading_selectors = [
                '[class*="loading"]',
                '[class*="spinner"]',
                '[id*="loading"]',
                '.loader'
            ]
            
            for selector in loading_selectors:
                try:
                    WebDriverWait(self.driver, 5).until_not(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    self.logger.debug(f"⏳ Waited for loading element to disappear: {selector}")
                except TimeoutException:
                    continue
            
            # Additional wait for JavaScript content
            self.logger.debug("⏳ Waiting for JavaScript content to render...")
            time.sleep(3)
            
            # Check if page still shows JavaScript error
            body_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
            if "enable javascript" in body_text and len(body_text) < 500:
                self.logger.warning("⚠️  Page showing JavaScript error, waiting longer...")
                time.sleep(wait_time * 2)
            
            # Scroll to trigger lazy loading
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 0);")
            
            # Get page source
            page_source = self.driver.page_source
            
            if len(page_source) < 1000:
                self.logger.warning("⚠️  Page content seems unusually short")
            
            # Parse with BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')
            
            self.logger.debug(f"✅ Successfully scraped page ({len(page_source)} characters)")
            return soup
            
        except TimeoutException:
            self.logger.error(f"❌ Timeout: Page took longer than {timeout}s to load")
            return None
        except WebDriverException as e:
            self.logger.error(f"❌ WebDriver error: {str(e)}")
            return None
        except Exception as e:
            self.logger.error(f"❌ Error scraping page: {str(e)}")
            return None
            
    def close(self):
        """Close the WebDriver safely"""
        if self.driver:
            try:
                self.driver.quit()
                self.logger.debug("🔒 WebDriver closed successfully")
            except Exception as e:
                self.logger.debug(f"⚠️  Error closing WebDriver: {e}")
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()