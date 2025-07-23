"""Pytest configuration and fixtures."""

import pytest
import logging
from utils.driver_factory import DriverFactory
from utils.screenshot_helper import ScreenshotHelper
from config.config import Config

# Configure logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


@pytest.fixture(scope="function")
def driver():
    """WebDriver fixture."""
    driver_instance = DriverFactory.create_driver()
    driver_instance.get(Config.BASE_URL)
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="function")
def screenshot_on_failure(request, driver):
    """Capture screenshot on test failure."""
    yield
    if request.node.rep_call.failed:
        ScreenshotHelper.capture_screenshot(
            driver, 
            f"failed_{request.node.name}"
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot fixture."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)