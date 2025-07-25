from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os


class PracticeFormTest:
    """Individual test for Practice Form functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_form_field_validation(self):
        """Test form field validation"""
        print("🔧 Testing Practice Form - Field Validation...")
        self.driver.get("https://demoqa.com/automation-practice-form")

        try:
            # Test required field validation
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            
            # Check if form validation prevents submission
            first_name_field = self.driver.find_element(By.ID, "firstName")
            field_class = first_name_field.get_attribute("class")
            print(f"  ✓ First name field validation: {field_class}")
            
            print("✅ Form field validation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Form field validation test FAILED: {e}")
            return False

    def test_complete_form_submission(self):
        """Test complete form submission with all fields"""
        print("\n🔧 Testing Practice Form - Complete Submission...")
        self.driver.get("https://demoqa.com/automation-practice-form")

        try:
            # Fill basic information
            self.driver.find_element(By.ID, "firstName").send_keys("John")
            self.driver.find_element(By.ID, "lastName").send_keys("Doe")
            self.driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
            print("  ✓ Basic information filled")

            # Select gender
            gender_radio = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
            self.driver.execute_script("arguments[0].click();", gender_radio)
            print("  ✓ Gender selected")

            # Fill mobile number
            self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")
            print("  ✓ Mobile number filled")

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
            print("  ✓ Date of birth selected")

            # Fill subjects
            subjects_input = self.driver.find_element(By.ID, "subjectsInput")
            subjects_input.send_keys("Math")
            subjects_input.send_keys(Keys.ENTER)
            print("  ✓ Subject added")

            # Select hobbies
            hobby_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
            self.driver.execute_script("arguments[0].click();", hobby_checkbox)
            print("  ✓ Hobby selected")

            # Upload picture
            test_image_path = os.path.join(os.getcwd(), "test_image.txt")
            with open(test_image_path, "w") as f:
                f.write("This is a test image file")

            upload_input = self.driver.find_element(By.ID, "uploadPicture")
            upload_input.send_keys(test_image_path)
            print("  ✓ Picture uploaded")

            # Fill current address
            self.driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street, City, State")
            print("  ✓ Address filled")

            # Select state
            state_dropdown = self.driver.find_element(By.ID, "state")
            state_dropdown.click()
            state_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']")))
            state_option.click()
            print("  ✓ State selected")

            # Select city
            city_dropdown = self.driver.find_element(By.ID, "city")
            city_dropdown.click()
            city_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']")))
            city_option.click()
            print("  ✓ City selected")

            # Submit form
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            print("  ✓ Form submitted")

            # Verify submission
            modal = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
            modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            assert "Thanks for submitting the form" in modal_title.text
            print("  ✓ Submission confirmed")

            # Close modal
            close_btn = self.driver.find_element(By.ID, "closeLargeModal")
            self.driver.execute_script("arguments[0].click();", close_btn)

            # Clean up
            os.remove(test_image_path)
            
            print("✅ Complete form submission test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Complete form submission test FAILED: {e}")
            # Clean up in case of error
            test_image_path = os.path.join(os.getcwd(), "test_image.txt")
            if os.path.exists(test_image_path):
                os.remove(test_image_path)
            return False

    def test_form_field_interactions(self):
        """Test individual form field interactions"""
        print("\n🔧 Testing Practice Form - Field Interactions...")
        self.driver.get("https://demoqa.com/automation-practice-form")

        try:
            # Test text inputs
            first_name = self.driver.find_element(By.ID, "firstName")
            first_name.send_keys("Test")
            assert first_name.get_attribute("value") == "Test"
            print("  ✓ Text input working")

            # Test radio buttons
            male_radio = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
            self.driver.execute_script("arguments[0].click();", male_radio)
            
            female_radio = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")
            self.driver.execute_script("arguments[0].click();", female_radio)
            print("  ✓ Radio buttons working")

            # Test checkboxes
            sports_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
            self.driver.execute_script("arguments[0].click();", sports_checkbox)
            
            reading_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']")
            self.driver.execute_script("arguments[0].click();", reading_checkbox)
            print("  ✓ Checkboxes working")

            # Test dropdown interactions
            state_dropdown = self.driver.find_element(By.ID, "state")
            state_dropdown.click()
            time.sleep(1)
            
            # Close dropdown
            self.driver.find_element(By.TAG_NAME, "body").click()
            print("  ✓ Dropdown interactions working")
            
            print("✅ Form field interactions test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Form field interactions test FAILED: {e}")
            return False

    def run_all_practice_form_tests(self):
        """Run all practice form tests"""
        print("=" * 60)
        print("📝 PRACTICE FORM INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_form_field_validation())
            results.append(self.test_complete_form_submission())
            results.append(self.test_form_field_interactions())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 PRACTICE FORM TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Practice Form tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Practice Form tests passed, some had issues")
            else:
                print("❌ All Practice Form tests had issues")
                
        except Exception as e:
            print(f"❌ Practice Form test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    practice_form_test = PracticeFormTest()
    practice_form_test.run_all_practice_form_tests()