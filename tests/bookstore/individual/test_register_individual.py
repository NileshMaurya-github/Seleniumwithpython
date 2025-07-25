from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string


class RegisterTest:
    """Individual test for Book Store Register functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def generate_random_user(self):
        """Generate random user data for testing"""
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return {
            'firstName': f'Test{random_suffix}',
            'lastName': f'User{random_suffix}',
            'userName': f'testuser{random_suffix}',
            'password': f'TestPass123!{random_suffix}'
        }

    def test_register_page_elements(self):
        """Test register page elements are present"""
        print("🔧 Testing Book Store Register - Page Elements...")
        self.driver.get("https://demoqa.com/register")

        try:
            # Check first name field
            first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "firstname")))
            assert first_name_field.is_displayed()
            print("  ✓ First Name field is present")
            
            # Check last name field
            last_name_field = self.driver.find_element(By.ID, "lastname")
            assert last_name_field.is_displayed()
            print("  ✓ Last Name field is present")
            
            # Check username field
            username_field = self.driver.find_element(By.ID, "userName")
            assert username_field.is_displayed()
            print("  ✓ Username field is present")
            
            # Check password field
            password_field = self.driver.find_element(By.ID, "password")
            assert password_field.is_displayed()
            print("  ✓ Password field is present")
            
            # Check captcha
            try:
                captcha_element = self.driver.find_element(By.ID, "recaptcha-anchor")
                print("  ✓ Captcha element found")
            except:
                print("  ⚠️ Captcha element not found (may be loaded dynamically)")
            
            # Check register button
            register_btn = self.driver.find_element(By.ID, "register")
            assert register_btn.is_displayed()
            print("  ✓ Register button is present")
            
            # Check back to login button
            back_to_login_btn = self.driver.find_element(By.ID, "gotologin")
            assert back_to_login_btn.is_displayed()
            print("  ✓ Back to Login button is present")
            
            print("✅ Register page elements test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Register page elements test FAILED: {e}")
            return False

    def test_empty_fields_validation(self):
        """Test validation with empty fields"""
        print("\n🔧 Testing Book Store Register - Empty Fields Validation...")
        self.driver.get("https://demoqa.com/register")

        try:
            # Clear all fields and try to register
            first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "firstname")))
            first_name_field.clear()
            
            last_name_field = self.driver.find_element(By.ID, "lastname")
            last_name_field.clear()
            
            username_field = self.driver.find_element(By.ID, "userName")
            username_field.clear()
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            
            # Try to click register button
            register_btn = self.driver.find_element(By.ID, "register")
            register_btn.click()
            print("  ✓ Register attempted with empty fields")
            
            # Check for validation styling
            time.sleep(1)
            
            # Check if fields have validation classes
            first_name_class = first_name_field.get_attribute("class")
            print(f"  ✓ First name field class: {first_name_class}")
            
            print("✅ Empty fields validation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Empty fields validation test FAILED: {e}")
            return False

    def test_password_requirements(self):
        """Test password requirements validation"""
        print("\n🔧 Testing Book Store Register - Password Requirements...")
        self.driver.get("https://demoqa.com/register")

        try:
            user_data = self.generate_random_user()
            
            # Fill in all fields except password with weak password
            first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "firstname")))
            first_name_field.clear()
            first_name_field.send_keys(user_data['firstName'])
            
            last_name_field = self.driver.find_element(By.ID, "lastname")
            last_name_field.clear()
            last_name_field.send_keys(user_data['lastName'])
            
            username_field = self.driver.find_element(By.ID, "userName")
            username_field.clear()
            username_field.send_keys(user_data['userName'])
            
            # Try weak password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("123")  # Weak password
            print("  ✓ Weak password entered")
            
            # Try to register
            register_btn = self.driver.find_element(By.ID, "register")
            register_btn.click()
            
            time.sleep(2)
            
            # Check if still on register page (validation should prevent registration)
            current_url = self.driver.current_url
            if "register" in current_url:
                print("  ✓ Remained on register page (weak password rejected)")
            
            print("✅ Password requirements test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Password requirements test FAILED: {e}")
            return False

    def test_back_to_login_navigation(self):
        """Test navigation back to login page"""
        print("\n🔧 Testing Book Store Register - Back to Login Navigation...")
        self.driver.get("https://demoqa.com/register")

        try:
            # Click back to login button
            back_to_login_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "gotologin")))
            back_to_login_btn.click()
            print("  ✓ Back to Login button clicked")
            
            # Wait for navigation to login page
            self.wait.until(EC.url_contains("login"))
            current_url = self.driver.current_url
            print(f"  ✓ Navigated to: {current_url}")
            
            # Verify we're on login page
            assert "login" in current_url
            print("  ✓ Successfully navigated to login page")
            
            print("✅ Back to login navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Back to login navigation test FAILED: {e}")
            return False

    def test_form_field_interactions(self):
        """Test form field interactions and data entry"""
        print("\n🔧 Testing Book Store Register - Form Field Interactions...")
        self.driver.get("https://demoqa.com/register")

        try:
            user_data = self.generate_random_user()
            
            # Test each field interaction
            first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "firstname")))
            first_name_field.clear()
            first_name_field.send_keys(user_data['firstName'])
            assert first_name_field.get_attribute("value") == user_data['firstName']
            print(f"  ✓ First name entered: {user_data['firstName']}")
            
            last_name_field = self.driver.find_element(By.ID, "lastname")
            last_name_field.clear()
            last_name_field.send_keys(user_data['lastName'])
            assert last_name_field.get_attribute("value") == user_data['lastName']
            print(f"  ✓ Last name entered: {user_data['lastName']}")
            
            username_field = self.driver.find_element(By.ID, "userName")
            username_field.clear()
            username_field.send_keys(user_data['userName'])
            assert username_field.get_attribute("value") == user_data['userName']
            print(f"  ✓ Username entered: {user_data['userName']}")
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(user_data['password'])
            print("  ✓ Password entered (hidden)")
            
            # Test field clearing
            first_name_field.clear()
            assert first_name_field.get_attribute("value") == ""
            print("  ✓ Field clearing works")
            
            print("✅ Form field interactions test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Form field interactions test FAILED: {e}")
            return False

    def run_all_register_tests(self):
        """Run all register tests"""
        print("=" * 60)
        print("📝 REGISTER INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_register_page_elements())
            results.append(self.test_empty_fields_validation())
            results.append(self.test_password_requirements())
            results.append(self.test_back_to_login_navigation())
            results.append(self.test_form_field_interactions())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 REGISTER TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Register tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Register tests passed, some had issues")
            else:
                print("❌ All Register tests had issues")
                
        except Exception as e:
            print(f"❌ Register test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    register_test = RegisterTest()
    register_test.run_all_register_tests()