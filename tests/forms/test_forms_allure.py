"""
DemoQA Forms Tests with Allure Reporting
========================================
"""

import pytest
import allure
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@allure.epic("DemoQA Automation")
@allure.feature("Forms Section")
class TestFormsAllure:
    """Forms section tests with Allure reporting"""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        with allure.step("Initialize WebDriver"):
            self.driver = webdriver.Chrome()
            self.wait = WebDriverWait(self.driver, 10)
            self.driver.maximize_window()
        
        yield
        
        with allure.step("Close WebDriver"):
            self.driver.quit()
    
    @allure.story("Form Validation")
    @allure.title("Practice Form - Complete Form Submission")
    @allure.description("Test complete practice form submission with all fields")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_practice_form_complete(self):
        """Test complete practice form submission with Allure reporting"""
        
        with allure.step("Navigate to Practice Form page"):
            self.driver.get("https://demoqa.com/automation-practice-form")
            allure.attach(self.driver.current_url, "Page URL", allure.attachment_type.TEXT)
        
        with allure.step("Fill basic information"):
            test_data = {
                "firstName": "John",
                "lastName": "Doe",
                "email": "john.doe@example.com",
                "mobile": "1234567890"
            }
            
            self.driver.find_element(By.ID, "firstName").send_keys(test_data["firstName"])
            self.driver.find_element(By.ID, "lastName").send_keys(test_data["lastName"])
            self.driver.find_element(By.ID, "userEmail").send_keys(test_data["email"])
            self.driver.find_element(By.ID, "userNumber").send_keys(test_data["mobile"])
            
            allure.attach(str(test_data), "Basic Information", allure.attachment_type.JSON)
        
        with allure.step("Select gender"):
            gender_radio = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
            self.driver.execute_script("arguments[0].click();", gender_radio)
            allure.attach("Male selected", "Gender Selection", allure.attachment_type.TEXT)
        
        with allure.step("Select date of birth"):
            date_input = self.driver.find_element(By.ID, "dateOfBirthInput")
            date_input.click()
            
            # Select month
            month_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
            month_dropdown.select_by_visible_text("January")
            
            # Select year
            year_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
            year_dropdown.select_by_visible_text("1990")
            
            # Select day
            day = self.driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']")
            day.click()
            
            allure.attach("January 15, 1990", "Date of Birth", allure.attachment_type.TEXT)
        
        with allure.step("Add subject"):
            subjects_input = self.driver.find_element(By.ID, "subjectsInput")
            subjects_input.send_keys("Math")
            subjects_input.send_keys(Keys.ENTER)
            allure.attach("Math", "Subject Added", allure.attachment_type.TEXT)
        
        with allure.step("Select hobbies"):
            hobby_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
            self.driver.execute_script("arguments[0].click();", hobby_checkbox)
            allure.attach("Sports selected", "Hobby Selection", allure.attachment_type.TEXT)
        
        with allure.step("Upload picture"):
            test_image_path = os.path.join(os.getcwd(), "test_image.txt")
            with open(test_image_path, "w") as f:
                f.write("This is a test image file")
            
            upload_input = self.driver.find_element(By.ID, "uploadPicture")
            upload_input.send_keys(test_image_path)
            allure.attach("test_image.txt", "Uploaded File", allure.attachment_type.TEXT)
        
        with allure.step("Fill address"):
            address = "123 Main Street, City, State"
            self.driver.find_element(By.ID, "currentAddress").send_keys(address)
            allure.attach(address, "Current Address", allure.attachment_type.TEXT)
        
        with allure.step("Select state and city"):
            # Select state
            state_dropdown = self.driver.find_element(By.ID, "state")
            state_dropdown.click()
            state_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']")))
            state_option.click()
            
            # Select city
            city_dropdown = self.driver.find_element(By.ID, "city")
            city_dropdown.click()
            city_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']")))
            city_option.click()
            
            allure.attach("NCR - Delhi", "State and City", allure.attachment_type.TEXT)
        
        with allure.step("Submit form"):
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
        
        with allure.step("Verify form submission"):
            modal = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
            modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            assert "Thanks for submitting the form" in modal_title.text
            
            # Get form data from modal
            table_data = self.driver.find_element(By.CSS_SELECTOR, ".table-responsive")
            allure.attach(table_data.text, "Submitted Form Data", allure.attachment_type.TEXT)
            
            # Close modal
            close_btn = self.driver.find_element(By.ID, "closeLargeModal")
            self.driver.execute_script("arguments[0].click();", close_btn)
            
            # Clean up
            os.remove(test_image_path)
    
    @allure.story("Form Validation")
    @allure.title("Practice Form - Field Validation")
    @allure.description("Test form field validation and error handling")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_practice_form_validation(self):
        """Test practice form validation with Allure reporting"""
        
        with allure.step("Navigate to Practice Form page"):
            self.driver.get("https://demoqa.com/automation-practice-form")
        
        with allure.step("Test empty form submission"):
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            
            # Check for required field validation
            first_name_field = self.driver.find_element(By.ID, "firstName")
            field_class = first_name_field.get_attribute("class")
            allure.attach(field_class, "First Name Field Class", allure.attachment_type.TEXT)
        
        with allure.step("Test invalid email validation"):
            self.driver.find_element(By.ID, "firstName").send_keys("Test")
            self.driver.find_element(By.ID, "lastName").send_keys("User")
            self.driver.find_element(By.ID, "userEmail").send_keys("invalid-email")
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            
            email_field = self.driver.find_element(By.ID, "userEmail")
            email_class = email_field.get_attribute("class")
            allure.attach(email_class, "Email Field Validation", allure.attachment_type.TEXT)
    
    @pytest.fixture(autouse=True)
    def attach_screenshot_on_failure(self, request):
        """Attach screenshot on test failure"""
        yield
        if request.node.rep_call.failed:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )
    
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        """Hook to capture test results"""
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)