"""WebDriver factory for creating browser instances."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class DriverFactory:
    """Factory class for creating WebDriver instances."""
    
    @staticmethod
    def create_driver():
        """Create Chrome WebDriver instance."""
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver