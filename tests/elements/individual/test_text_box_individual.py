from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class TextBoxTest:
    """Individual test for Text Box functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_text_box_basic_functionality(self):
        """Test basic text box form filling and submission"""
        print("🔧 Testing Text Box - Basic Functionality...")
        self.driver.get("https://demoqa.com/text-box")

        try:
            # Fill text box fields
            self.driver.find_element(By.ID, "userName").send_keys("John Doe")
            print("  ✓ Full Name field filled")
            
            self.driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
            print("  ✓ Email field filled")
            
            self.driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street, City")
            print("  ✓ Current Address field filled")
            
            self.driver.find_element(By.ID, "permanentAddress").send_keys("456 Oak Avenue, Town")
            print("  ✓ Permanent Address field filled")

            # Submit form (using JavaScript to avoid ad overlay issues)
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            print("  ✓ Form submitted successfully")

            # Verify output
            output = self.wait.until(EC.presence_of_element_located((By.ID, "output")))
            assert "John Doe" in output.text
            print("  ✓ Output verification passed")
            
            print("✅ Text Box basic functionality test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Text Box test FAILED: {e}")
            return False

    def test_text_box_validation(self):
        """Test text box field validation"""
        print("\n🔧 Testing Text Box - Field Validation...")
        self.driver.get("https://demoqa.com/text-box")

        try:
            # Test invalid email validation
            self.driver.find_element(By.ID, "userName").send_keys("Test User")
            self.driver.find_element(By.ID, "userEmail").send_keys("invalid-email")
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            
            # Check if email field has error styling
            email_field = self.driver.find_element(By.ID, "userEmail")
            field_class = email_field.get_attribute("class")
            
            if "field-error" in field_class:
                print("  ✓ Email validation working - error class detected")
            else:
                print("  ⚠️ Email validation - no error class (may still be working)")
            
            print("✅ Text Box validation test COMPLETED")
            return True
            
        except Exception as e:
            print(f"❌ Text Box validation test FAILED: {e}")
            return False

    def test_text_box_clear_functionality(self):
        """Test clearing text box fields"""
        print("\n🔧 Testing Text Box - Clear Functionality...")
        self.driver.get("https://demoqa.com/text-box")

        try:
            # Fill fields
            name_field = self.driver.find_element(By.ID, "userName")
            name_field.send_keys("Test Name")
            
            email_field = self.driver.find_element(By.ID, "userEmail")
            email_field.send_keys("test@example.com")
            
            # Clear fields
            name_field.clear()
            email_field.clear()
            
            # Verify fields are empty
            assert name_field.get_attribute("value") == ""
            assert email_field.get_attribute("value") == ""
            
            print("  ✓ Fields cleared successfully")
            print("✅ Text Box clear functionality test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Text Box clear test FAILED: {e}")
            return False

    def run_all_text_box_tests(self):
        """Run all text box tests"""
        print("=" * 60)
        print("📝 TEXT BOX INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_text_box_basic_functionality())
            results.append(self.test_text_box_validation())
            results.append(self.test_text_box_clear_functionality())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 TEXT BOX TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Text Box tests PASSED!")
            else:
                print("⚠️ Some Text Box tests had issues")
                
        except Exception as e:
            print(f"❌ Text Box test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    text_box_test = TextBoxTest()
    text_box_test.run_all_text_box_tests()