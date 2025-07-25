import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("DemoQA Automation")
@allure.feature("Widgets")
class TestSimpleWidgets:
    """Simple widgets tests"""
    
    def setup_method(self):
        """Setup for each test"""
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        
        if os.environ.get('HEADLESS', '').lower() == 'true':
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        if not os.environ.get('HEADLESS', '').lower() == 'true':
            self.driver.maximize_window()
    
    def teardown_method(self):
        """Teardown for each test"""
        self.driver.quit()
    
    @allure.story("Accordion")
    @allure.title("Test Accordion Functionality")
    def test_accordion(self):
        """Test accordion functionality"""
        self.driver.get("https://demoqa.com/accordian")
        
        first_section = self.driver.find_element(By.ID, "section1Heading")
        first_section.click()
        
        first_content = self.wait.until(EC.visibility_of_element_located((By.ID, "section1Content")))
        assert len(first_content.text) > 0
    
    @allure.story("Tabs")
    @allure.title("Test Tabs Functionality")
    def test_tabs(self):
        """Test tabs functionality"""
        self.driver.get("https://demoqa.com/tabs")
        
        what_tab = self.driver.find_element(By.ID, "demo-tab-what")
        what_tab.click()
        
        what_content = self.wait.until(EC.visibility_of_element_located((By.ID, "demo-tabpane-what")))
        assert len(what_content.text) > 0
    
    @allure.story("Slider")
    @allure.title("Test Slider Functionality")
    def test_slider(self):
        """Test slider functionality"""
        self.driver.get("https://demoqa.com/slider")
        
        initial_value = self.driver.find_element(By.ID, "sliderValue").get_attribute("value")
        assert initial_value is not None
    
    @allure.story("Progress Bar")
    @allure.title("Test Progress Bar Functionality")
    def test_progress_bar(self):
        """Test progress bar functionality"""
        self.driver.get("https://demoqa.com/progress-bar")
        
        start_button = self.driver.find_element(By.ID, "startStopButton")
        start_button.click()
        
        # Stop it quickly
        stop_button = self.driver.find_element(By.ID, "startStopButton")
        stop_button.click()
    
    @allure.story("Date Picker")
    @allure.title("Test Date Picker Functionality")
    def test_date_picker(self):
        """Test date picker functionality"""
        self.driver.get("https://demoqa.com/date-picker")
        
        date_input = self.driver.find_element(By.ID, "datePickerMonthYearInput")
        initial_date = date_input.get_attribute("value")
        assert initial_date is not None