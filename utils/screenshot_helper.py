"""Screenshot utility for capturing test evidence."""

import os
from datetime import datetime
from selenium import webdriver
from config.config import Config
import logging

logger = logging.getLogger(__name__)


class ScreenshotHelper:
    """Helper class for capturing screenshots."""
    
    @staticmethod
    def capture_screenshot(driver: webdriver.Remote, name: str) -> str:
        """
        Capture screenshot and save to file.
        
        Args:
            driver: WebDriver instance
            name: Screenshot name
            
        Returns:
            Path to saved screenshot
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(Config.get_screenshots_dir(), filename)
        
        try:
            driver.save_screenshot(filepath)
            logger.info(f"Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
            return None
    
    @staticmethod
    def capture_element_screenshot(driver: webdriver.Remote, element, name: str) -> str:
        """
        Capture screenshot of specific element.
        
        Args:
            driver: WebDriver instance
            element: WebElement to capture
            name: Screenshot name
            
        Returns:
            Path to saved screenshot
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"element_{name}_{timestamp}.png"
        filepath = os.path.join(Config.get_screenshots_dir(), filename)
        
        try:
            element.screenshot(filepath)
            logger.info(f"Element screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Failed to capture element screenshot: {e}")
            return None