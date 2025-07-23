"""Home page tests."""

import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Home Page")
class TestHomePage:
    """Test cases for home page functionality."""
    
    @allure.story("Navigation Cards")
    @allure.title("Verify all main category cards are visible")
    @pytest.mark.smoke
    def test_all_cards_visible(self, driver):
        """Test that all main category cards are visible on home page."""
        home_page = HomePage(driver)
        
        with allure.step("Verify Elements card is visible"):
            assert home_page.is_elements_card_visible(), "Elements card should be visible"
        
        with allure.step("Verify Forms card is visible"):
            assert home_page.is_forms_card_visible(), "Forms card should be visible"
        
        with allure.step("Verify Alerts, Frame & Windows card is visible"):
            assert home_page.is_alerts_frames_card_visible(), "Alerts, Frame & Windows card should be visible"
        
        with allure.step("Verify Widgets card is visible"):
            assert home_page.is_widgets_card_visible(), "Widgets card should be visible"
        
        with allure.step("Verify Interactions card is visible"):
            assert home_page.is_interactions_card_visible(), "Interactions card should be visible"
        
        with allure.step("Verify Book Store Application card is visible"):
            assert home_page.is_bookstore_card_visible(), "Book Store Application card should be visible"
    
    @allure.story("Navigation")
    @allure.title("Navigate to Elements section")
    @pytest.mark.elements
    def test_navigate_to_elements(self, driver):
        """Test navigation to Elements section."""
        home_page = HomePage(driver)
        
        with allure.step("Click on Elements card"):
            home_page.click_elements_card()
        
        with allure.step("Verify navigation to Elements page"):
            assert "/elements" in driver.current_url, "Should navigate to Elements page"
    
    @allure.story("Navigation")
    @allure.title("Navigate to Forms section")
    @pytest.mark.forms
    def test_navigate_to_forms(self, driver):
        """Test navigation to Forms section."""
        home_page = HomePage(driver)
        
        with allure.step("Click on Forms card"):
            home_page.click_forms_card()
        
        with allure.step("Verify navigation to Forms page"):
            assert "/forms" in driver.current_url, "Should navigate to Forms page"