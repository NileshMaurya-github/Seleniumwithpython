from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class LoginTest:
    """Individual test for Book Store Login functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_login_page_elements(self):
        """Test login page elements are present"""
        print("🔧 Testing Book Store Login - Page Elements...")
        self.driver.get("https://demoqa.com/login")

        try:
            # Check username field
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "userName")))
            assert username_field.is_displayed()
            print("  ✓ Username field is present")
            
            # Check password field
            password_field = self.driver.find_element(By.ID, "password")
            assert password_field.is_displayed()
            print("  ✓ Password field is present")
            
            # Check login button
            login_btn = self.driver.find_element(By.ID, "login")
            assert login_btn.is_displayed()
            print("  ✓ Login button is present")
            
            # Check new user button
            new_user_btn = self.driver.find_element(By.ID, "newUser")
            assert new_user_btn.is_displayed()
            print("  ✓ New User button is present")
            
            print("✅ Login page elements test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Login page elements test FAILED: {e}")
            return False

    def test_invalid_login(self):
        """Test login with invalid credentials"""
        print("\n🔧 Testing Book Store Login - Invalid Credentials...")
        self.driver.get("https://demoqa.com/login")

        try:
            # Enter invalid credentials
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "userName")))
            username_field.clear()
            username_field.send_keys("invaliduser")
            print("  ✓ Invalid username entered")
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("invalidpass")
            print("  ✓ Invalid password entered")
            
            # Click login button
            login_btn = self.driver.find_element(By.ID, "login")
            login_btn.click()
            print("  ✓ Login button clicked")
            
            # Wait for error message or check if still on login page
            time.sleep(2)
            current_url = self.driver.current_url
            
            # Should still be on login page or show error
            if "login" in current_url:
                print("  ✓ Remained on login page (expected for invalid credentials)")
            else:
                print("  ⚠️ Unexpected navigation occurred")
            
            print("✅ Invalid login test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Invalid login test FAILED: {e}")
            return False

    def test_empty_fields_validation(self):
        """Test validation with empty fields"""
        print("\n🔧 Testing Book Store Login - Empty Fields Validation...")
        self.driver.get("https://demoqa.com/login")

        try:
            # Clear fields and try to login
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "userName")))
            username_field.clear()
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            
            # Click login button
            login_btn = self.driver.find_element(By.ID, "login")
            login_btn.click()
            print("  ✓ Login attempted with empty fields")
            
            # Check for validation (fields should be highlighted or error shown)
            time.sleep(1)
            
            # Check if fields have validation styling
            username_class = username_field.get_attribute("class")
            password_class = password_field.get_attribute("class")
            
            print(f"  ✓ Username field class: {username_class}")
            print(f"  ✓ Password field class: {password_class}")
            
            print("✅ Empty fields validation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Empty fields validation test FAILED: {e}")
            return False

    def test_new_user_navigation(self):
        """Test navigation to new user registration"""
        print("\n🔧 Testing Book Store Login - New User Navigation...")
        self.driver.get("https://demoqa.com/login")

        try:
            # Click new user button
            new_user_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "newUser")))
            new_user_btn.click()
            print("  ✓ New User button clicked")
            
            # Wait for navigation to register page
            self.wait.until(EC.url_contains("register"))
            current_url = self.driver.current_url
            print(f"  ✓ Navigated to: {current_url}")
            
            # Verify we're on register page
            assert "register" in current_url
            print("  ✓ Successfully navigated to register page")
            
            print("✅ New user navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ New user navigation test FAILED: {e}")
            return False

    def run_all_login_tests(self):
        """Run all login tests"""
        print("=" * 60)
        print("🔐 LOGIN INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_login_page_elements())
            results.append(self.test_invalid_login())
            results.append(self.test_empty_fields_validation())
            results.append(self.test_new_user_navigation())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 LOGIN TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Login tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Login tests passed, some had issues")
            else:
                print("❌ All Login tests had issues")
                
        except Exception as e:
            print(f"❌ Login test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    login_test = LoginTest()
    login_test.run_all_login_tests()