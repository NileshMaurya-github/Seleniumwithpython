"""Base test class with common setup and teardown."""

import pytest
import logging
from selenium import webdriver
from utils.driver_factory import DriverFactory
from utils.screenshot_helper import ScreenshotHelper
from config.config import Config

logger = logging.getLogger(__name__)


class BaseTest:
    """Base test class with common functionality."""
    
    driver: webdriver.Remote = None
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request):
        """Setup and teardown for each test."""
        # Setup
        logger.info(f"Starting test: {request.node.name}")
        self.driver = DriverFactory.create_driver()
        self.driver.get(Config.BASE_URL)
        
        yield
        
        # Teardown
        if request.node.rep_call.failed:
            ScreenshotHelper.capture_screenshot(
                self.driver, 
                f"failed_{request.node.name}"
            )
        
        logger.info(f"Finished test: {request.node.name}")
        if self.driver:
            self.driver.quit()
    
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        """Hook to capture test results."""
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)