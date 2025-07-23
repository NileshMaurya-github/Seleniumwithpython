"""Text Box page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """Text Box page class."""
    
    # Navigation
    TEXT_BOX_MENU = (By.ID, "item-0")
    
    # Form fields
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_TEXTAREA = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_TEXTAREA = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    
    # Output section
    OUTPUT_SECTION = (By.ID, "output")
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")
    
    def navigate_to_text_box(self):
        """Navigate to Text Box section."""
        self.click_element(self.TEXT_BOX_MENU)
    
    def fill_full_name(self, name: str):
        """Fill full name field."""
        self.send_keys(self.FULL_NAME_INPUT, name)
    
    def fill_email(self, email: str):
        """Fill email field."""
        self.send_keys(self.EMAIL_INPUT, email)
    
    def fill_current_address(self, address: str):
        """Fill current address field."""
        self.send_keys(self.CURRENT_ADDRESS_TEXTAREA, address)
    
    def fill_permanent_address(self, address: str):
        """Fill permanent address field."""
        self.send_keys(self.PERMANENT_ADDRESS_TEXTAREA, address)
    
    def click_submit(self):
        """Click submit button."""
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click_element(self.SUBMIT_BUTTON)
    
    def fill_form(self, name: str, email: str, current_address: str, permanent_address: str):
        """Fill complete form."""
        self.fill_full_name(name)
        self.fill_email(email)
        self.fill_current_address(current_address)
        self.fill_permanent_address(permanent_address)
        self.click_submit()
    
    def get_output_name(self) -> str:
        """Get output name text."""
        return self.get_text(self.OUTPUT_NAME)
    
    def get_output_email(self) -> str:
        """Get output email text."""
        return self.get_text(self.OUTPUT_EMAIL)
    
    def get_output_current_address(self) -> str:
        """Get output current address text."""
        return self.get_text(self.OUTPUT_CURRENT_ADDRESS)
    
    def get_output_permanent_address(self) -> str:
        """Get output permanent address text."""
        return self.get_text(self.OUTPUT_PERMANENT_ADDRESS)
    
    def is_output_visible(self) -> bool:
        """Check if output section is visible."""
        return self.is_element_visible(self.OUTPUT_SECTION)