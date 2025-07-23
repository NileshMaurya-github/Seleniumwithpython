"""Text Box tests."""

import pytest
import allure
from pages.home_page import HomePage
from pages.elements.text_box_page import TextBoxPage


@allure.feature("Elements")
@allure.sub_feature("Text Box")
class TestTextBox:
    """Test cases for Text Box functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup for Text Box tests."""
        self.home_page = HomePage(driver)
        self.text_box_page = TextBoxPage(driver)
        
        # Navigate to Text Box page
        self.home_page.click_elements_card()
        self.text_box_page.navigate_to_text_box()
    
    @allure.story("Form Submission")
    @allure.title("Submit form with valid data")
    @pytest.mark.smoke
    @pytest.mark.elements
    def test_submit_valid_form(self, driver):
        """Test submitting form with valid data."""
        test_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "current_address": "123 Main St, City, State",
            "permanent_address": "456 Oak Ave, Town, State"
        }
        
        with allure.step("Fill and submit form"):
            self.text_box_page.fill_form(
                test_data["name"],
                test_data["email"],
                test_data["current_address"],
                test_data["permanent_address"]
            )
        
        with allure.step("Verify output is displayed"):
            assert self.text_box_page.is_output_visible(), "Output section should be visible"
        
        with allure.step("Verify output contains correct name"):
            output_name = self.text_box_page.get_output_name()
            assert test_data["name"] in output_name, f"Output should contain name: {test_data['name']}"
        
        with allure.step("Verify output contains correct email"):
            output_email = self.text_box_page.get_output_email()
            assert test_data["email"] in output_email, f"Output should contain email: {test_data['email']}"
    
    @allure.story("Form Validation")
    @allure.title("Submit form with invalid email")
    @pytest.mark.regression
    @pytest.mark.elements
    def test_submit_invalid_email(self, driver):
        """Test submitting form with invalid email."""
        with allure.step("Fill form with invalid email"):
            self.text_box_page.fill_full_name("Test User")
            self.text_box_page.fill_email("invalid-email")
            self.text_box_page.fill_current_address("Test Address")
            self.text_box_page.click_submit()
        
        with allure.step("Verify email field has error styling"):
            email_field = self.text_box_page.find_element(self.text_box_page.EMAIL_INPUT)
            field_class = email_field.get_attribute("class")
            assert "field-error" in field_class, "Email field should have error styling"
    
    @allure.story("Form Fields")
    @allure.title("Verify all form fields are present")
    @pytest.mark.smoke
    @pytest.mark.elements
    def test_form_fields_present(self, driver):
        """Test that all form fields are present and accessible."""
        with allure.step("Verify Full Name field is present"):
            assert self.text_box_page.is_element_present(self.text_box_page.FULL_NAME_INPUT), "Full Name field should be present"
        
        with allure.step("Verify Email field is present"):
            assert self.text_box_page.is_element_present(self.text_box_page.EMAIL_INPUT), "Email field should be present"
        
        with allure.step("Verify Current Address field is present"):
            assert self.text_box_page.is_element_present(self.text_box_page.CURRENT_ADDRESS_TEXTAREA), "Current Address field should be present"
        
        with allure.step("Verify Permanent Address field is present"):
            assert self.text_box_page.is_element_present(self.text_box_page.PERMANENT_ADDRESS_TEXTAREA), "Permanent Address field should be present"
        
        with allure.step("Verify Submit button is present"):
            assert self.text_box_page.is_element_present(self.text_box_page.SUBMIT_BUTTON), "Submit button should be present"