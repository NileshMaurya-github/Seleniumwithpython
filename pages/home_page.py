"""Home page object for DemoQA main page."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """Home page class with locators and methods."""
    
    # Main category cards
    ELEMENTS_CARD = (By.XPATH, "//div[@class='card mt-4 top-card'][1]")
    FORMS_CARD = (By.XPATH, "//div[@class='card mt-4 top-card'][2]")
    ALERTS_FRAMES_CARD = (By.XPATH, "//div[@class='card mt-4 top-card'][3]")
    WIDGETS_CARD = (By.XPATH, "//div[@class='card mt-4 top-card'][4]")
    INTERACTIONS_CARD = (By.XPATH, "//div[@class='card mt-4 top-card'][5]")
    BOOKSTORE_CARD = (By.XPATH, "//div[@class='card mt-4 top-card'][6]")
    
    # Card titles
    ELEMENTS_TITLE = (By.XPATH, "//h5[text()='Elements']")
    FORMS_TITLE = (By.XPATH, "//h5[text()='Forms']")
    ALERTS_FRAMES_TITLE = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
    WIDGETS_TITLE = (By.XPATH, "//h5[text()='Widgets']")
    INTERACTIONS_TITLE = (By.XPATH, "//h5[text()='Interactions']")
    BOOKSTORE_TITLE = (By.XPATH, "//h5[text()='Book Store Application']")
    
    def click_elements_card(self):
        """Click on Elements card."""
        self.scroll_to_element(self.ELEMENTS_CARD)
        self.click_element(self.ELEMENTS_CARD)
    
    def click_forms_card(self):
        """Click on Forms card."""
        self.scroll_to_element(self.FORMS_CARD)
        self.click_element(self.FORMS_CARD)
    
    def click_alerts_frames_card(self):
        """Click on Alerts, Frame & Windows card."""
        self.scroll_to_element(self.ALERTS_FRAMES_CARD)
        self.click_element(self.ALERTS_FRAMES_CARD)
    
    def click_widgets_card(self):
        """Click on Widgets card."""
        self.scroll_to_element(self.WIDGETS_CARD)
        self.click_element(self.WIDGETS_CARD)
    
    def click_interactions_card(self):
        """Click on Interactions card."""
        self.scroll_to_element(self.INTERACTIONS_CARD)
        self.click_element(self.INTERACTIONS_CARD)
    
    def click_bookstore_card(self):
        """Click on Book Store Application card."""
        self.scroll_to_element(self.BOOKSTORE_CARD)
        self.click_element(self.BOOKSTORE_CARD)
    
    def is_elements_card_visible(self) -> bool:
        """Check if Elements card is visible."""
        return self.is_element_visible(self.ELEMENTS_CARD)
    
    def is_forms_card_visible(self) -> bool:
        """Check if Forms card is visible."""
        return self.is_element_visible(self.FORMS_CARD)
    
    def is_alerts_frames_card_visible(self) -> bool:
        """Check if Alerts, Frame & Windows card is visible."""
        return self.is_element_visible(self.ALERTS_FRAMES_CARD)
    
    def is_widgets_card_visible(self) -> bool:
        """Check if Widgets card is visible."""
        return self.is_element_visible(self.WIDGETS_CARD)
    
    def is_interactions_card_visible(self) -> bool:
        """Check if Interactions card is visible."""
        return self.is_element_visible(self.INTERACTIONS_CARD)
    
    def is_bookstore_card_visible(self) -> bool:
        """Check if Book Store Application card is visible."""
        return self.is_element_visible(self.BOOKSTORE_CARD)