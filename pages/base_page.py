"""Base page class with common page functionality."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class with common functionality."""
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator: tuple) -> webdriver.Remote:
        """Find element with explicit wait."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator: tuple) -> list:
        """Find multiple elements."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            logger.error(f"Elements not found: {locator}")
            return []
    
    def click_element(self, locator: tuple) -> None:
        """Click element with explicit wait."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info(f"Clicked element: {locator}")
    
    def send_keys(self, locator: tuple, text: str) -> None:
        """Send keys to element."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Sent keys '{text}' to element: {locator}")
    
    def get_text(self, locator: tuple) -> str:
        """Get text from element."""
        element = self.find_element(locator)
        text = element.text
        logger.info(f"Got text '{text}' from element: {locator}")
        return text
    
    def get_attribute(self, locator: tuple, attribute: str) -> str:
        """Get attribute value from element."""
        element = self.find_element(locator)
        value = element.get_attribute(attribute)
        logger.info(f"Got attribute '{attribute}' = '{value}' from element: {locator}")
        return value
    
    def is_element_visible(self, locator: tuple) -> bool:
        """Check if element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator: tuple) -> bool:
        """Check if element is present in DOM."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def wait_for_element_to_disappear(self, locator: tuple) -> bool:
        """Wait for element to disappear."""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator: tuple) -> None:
        """Scroll to element."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Scrolled to element: {locator}")
    
    def hover_over_element(self, locator: tuple) -> None:
        """Hover over element."""
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()
        logger.info(f"Hovered over element: {locator}")
    
    def select_dropdown_by_text(self, locator: tuple, text: str) -> None:
        """Select dropdown option by visible text."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
        logger.info(f"Selected '{text}' from dropdown: {locator}")
    
    def select_dropdown_by_value(self, locator: tuple, value: str) -> None:
        """Select dropdown option by value."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
        logger.info(f"Selected value '{value}' from dropdown: {locator}")
    
    def drag_and_drop(self, source_locator: tuple, target_locator: tuple) -> None:
        """Drag and drop element."""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()
        logger.info(f"Dragged from {source_locator} to {target_locator}")
    
    def switch_to_frame(self, frame_locator: tuple) -> None:
        """Switch to iframe."""
        frame = self.find_element(frame_locator)
        self.driver.switch_to.frame(frame)
        logger.info(f"Switched to frame: {frame_locator}")
    
    def switch_to_default_content(self) -> None:
        """Switch back to default content."""
        self.driver.switch_to.default_content()
        logger.info("Switched to default content")
    
    def get_current_url(self) -> str:
        """Get current page URL."""
        return self.driver.current_url
    
    def get_page_title(self) -> str:
        """Get page title."""
        return self.driver.title