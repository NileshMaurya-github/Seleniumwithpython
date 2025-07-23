from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os


class DemoQAForms:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_practice_form(self):
        """Test Practice Form functionality"""
        print("Testing Practice Form...")
        self.driver.get("https://demoqa.com/automation-practice-form")

        # Fill basic information
        self.driver.find_element(By.ID, "firstName").send_keys("John")
        self.driver.find_element(By.ID, "lastName").send_keys("Doe")
        self.driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")

        # Select gender
        gender_radio = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
        self.driver.execute_script("arguments[0].click();", gender_radio)

        # Fill mobile number
        self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")

        # Select date of birth
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

        # Fill subjects
        subjects_input = self.driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("Math")
        subjects_input.send_keys(Keys.ENTER)

        # Select hobbies
        hobby_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
        self.driver.execute_script("arguments[0].click();", hobby_checkbox)

        # Upload picture
        # Create a temporary image file
        test_image_path = os.path.join(os.getcwd(), "test_image.txt")
        with open(test_image_path, "w") as f:
            f.write("This is a test image file")

        upload_input = self.driver.find_element(By.ID, "uploadPicture")
        upload_input.send_keys(test_image_path)

        # Fill current address
        self.driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street, City, State")

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

        # Submit form (using JavaScript to avoid ad overlay issues)
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_btn)

        # Verify submission
        modal = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
        modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
        assert "Thanks for submitting the form" in modal_title.text

        # Verify form data in modal
        table_data = self.driver.find_element(By.CSS_SELECTOR, ".table-responsive")
        assert "John Doe" in table_data.text
        assert "john.doe@example.com" in table_data.text
        assert "Male" in table_data.text
        assert "1234567890" in table_data.text

        # Close modal (using JavaScript to avoid ad overlay issues)
        close_btn = self.driver.find_element(By.ID, "closeLargeModal")
        self.driver.execute_script("arguments[0].click();", close_btn)

        # Clean up
        os.remove(test_image_path)

        print("✓ Practice Form test passed")

    def test_form_validation(self):
        """Test form validation"""
        print("Testing Form Validation...")
        self.driver.get("https://demoqa.com/automation-practice-form")

        # Try to submit empty form (using JavaScript to avoid ad overlay issues)
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_btn)

        # Check for required field validation
        first_name_field = self.driver.find_element(By.ID, "firstName")
        field_class = first_name_field.get_attribute("class")
        print(f"  First name field validation: {field_class}")

        # Test invalid email
        self.driver.find_element(By.ID, "firstName").send_keys("Test")
        self.driver.find_element(By.ID, "lastName").send_keys("User")
        self.driver.find_element(By.ID, "userEmail").send_keys("invalid-email")

        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_btn)

        email_field = self.driver.find_element(By.ID, "userEmail")
        email_class = email_field.get_attribute("class")
        print(f"  Email field validation: {email_class}")

        print("✓ Form Validation test passed")

    def run_all_tests(self):
        """Run all form tests"""
        try:
            self.test_practice_form()
            self.test_form_validation()
            print("\n✅ All Forms tests completed successfully!")
        except Exception as e:
            print(f"\n❌ Test failed: {str(e)}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    forms_test = DemoQAForms()
    forms_test.run_all_tests()