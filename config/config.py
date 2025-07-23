"""Configuration settings for the test framework."""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """Test configuration class."""
    
    # Base URL
    BASE_URL: str = "https://demoqa.com"
    
    # Browser settings
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "false").lower() == "true"
    WINDOW_SIZE: str = os.getenv("WINDOW_SIZE", "1920,1080")
    
    # Timeouts
    IMPLICIT_WAIT: int = 10
    EXPLICIT_WAIT: int = 20
    PAGE_LOAD_TIMEOUT: int = 30
    
    # Directories
    REPORTS_DIR: str = "reports"
    SCREENSHOTS_DIR: str = "reports/screenshots"
    DOWNLOADS_DIR: str = "downloads"
    
    # Test data
    TEST_DATA_DIR: str = "test_data"
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def get_download_dir(cls) -> str:
        """Get absolute path for downloads directory."""
        return os.path.abspath(cls.DOWNLOADS_DIR)
    
    @classmethod
    def get_screenshots_dir(cls) -> str:
        """Get absolute path for screenshots directory."""
        return os.path.abspath(cls.SCREENSHOTS_DIR)


# Create directories if they don't exist
for directory in [Config.REPORTS_DIR, Config.SCREENSHOTS_DIR, Config.DOWNLOADS_DIR]:
    os.makedirs(directory, exist_ok=True)