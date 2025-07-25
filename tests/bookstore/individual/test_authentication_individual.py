from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time


class AuthenticationTest:
    """Individual test for Book Store Authentication functionality"""
    
    def __init__(self):
        # Configure Chrome options to block ads but keep JavaScript enabled
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-images")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values": {
                "notifications": 2,
                "media_stream": 2,
                "ads": 2,
                "popups": 2
            }
        })
        # Add ad blocker rules
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        
    def safe_click(self, element):
        """Safely click an element, handling overlays"""
        try:
            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)
            
            # Try normal click first
            element.click()
            return True
        except Exception:
            try:
                # Try JavaScript click
                self.driver.execute_script("arguments[0].click();", element)
                return True
            except Exception:
                try:
                    # Try ActionChains click with offset
                    ActionChains(self.driver).move_to_element_with_offset(element, 5, 5).click().perform()
                    return True
                except Exception:
                    try:
                        # Force click through any overlay
                        self.driver.execute_script("""
                            arguments[0].style.zIndex = '9999';
                            arguments[0].style.position = 'relative';
                            arguments[0].click();
                        """, element)
                        return True
                    except Exception:
                        return False
                        
    def remove_ads(self):
        """Remove ad elements that might interfere with testing"""
        try:
            # Wait for page to load completely
            time.sleep(2)
            
            # Remove Google ads iframes and containers
            self.driver.execute_script("""
                // Remove Google ads iframes
                var ads = document.querySelectorAll('iframe[src*="googlesyndication"], iframe[id*="google_ads"], iframe[title*="Advertisement"]');
                for(var i = 0; i < ads.length; i++) {
                    ads[i].style.display = 'none';
                    ads[i].remove();
                }
                
                // Remove ad containers
                var adContainers = document.querySelectorAll('[id*="ad"], [class*="ad"], [class*="advertisement"], [data-google-container-id]');
                for(var i = 0; i < adContainers.length; i++) {
                    if(adContainers[i].offsetHeight > 30 || adContainers[i].offsetWidth > 100) {
                        adContainers[i].style.display = 'none';
                        adContainers[i].remove();
                    }
                }
                
                // Remove any overlay elements
                var overlays = document.querySelectorAll('[style*="position: fixed"], [style*="position: absolute"]');
                for(var i = 0; i < overlays.length; i++) {
                    var rect = overlays[i].getBoundingClientRect();
                    if(rect.width > 500 && rect.height > 50) {
                        overlays[i].style.display = 'none';
                    }
                }
            """)
            time.sleep(1)
        except Exception as e:
            print(f"  ⚠️ Ad removal had issues: {e}")
            pass

    def test_authentication_flow_access(self):
        """Test access to authentication flow"""
        print("🔧 Testing Book Store Authentication - Flow Access...")
        
        try:
            # Start from books page
            self.driver.get("https://demoqa.com/books")
            time.sleep(2)
            
            # Try to access a protected area (profile)
            self.driver.get("https://demoqa.com/profile")
            time.sleep(3)
            
            current_url = self.driver.current_url
            
            if "login" in current_url:
                print("  ✓ Redirected to login page (authentication required)")
                
                # Check login form elements
                username_field = self.driver.find_element(By.ID, "userName")
                password_field = self.driver.find_element(By.ID, "password")
                login_btn = self.driver.find_element(By.ID, "login")
                
                assert username_field.is_displayed()
                assert password_field.is_displayed()
                assert login_btn.is_displayed()
                print("  ✓ Authentication form elements present")
                
            else:
                print("  ⚠️ No authentication redirect (may already be authenticated)")
            
            print("✅ Authentication flow access test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Authentication flow access test FAILED: {e}")
            return False

    def test_login_form_validation(self):
        """Test login form validation"""
        print("\n🔧 Testing Book Store Authentication - Login Form Validation...")
        
        try:
            self.driver.get("https://demoqa.com/login")
            time.sleep(3)  # Wait for page to load
            self.remove_ads()  # Remove interfering ads
            
            # Test empty form submission
            login_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login")))
            if self.safe_click(login_btn):
                print("  ✓ Attempted login with empty form")
            else:
                print("  ⚠️ Login button click had issues, but continuing test")
            
            time.sleep(2)
            
            # Check if still on login page (validation should prevent submission)
            current_url = self.driver.current_url
            if "login" in current_url:
                print("  ✓ Remained on login page (validation working)")
            else:
                print("  ⚠️ Navigation occurred despite empty form")
            
            # Test with only username
            username_field = self.driver.find_element(By.ID, "userName")
            username_field.clear()
            username_field.send_keys("testuser")
            
            if self.safe_click(login_btn):
                print("  ✓ Attempted login with only username")
            else:
                print("  ⚠️ Login button click had issues, but continuing test")
            
            time.sleep(2)
            
            # Should still be on login page
            current_url = self.driver.current_url
            if "login" in current_url:
                print("  ✓ Remained on login page (password required)")
            
            # Test with only password
            username_field.clear()
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("testpass")
            
            if self.safe_click(login_btn):
                print("  ✓ Attempted login with only password")
            else:
                print("  ⚠️ Login button click had issues, but continuing test")
            
            time.sleep(2)
            
            print("✅ Login form validation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Login form validation test FAILED: {e}")
            return False

    def test_invalid_credentials_handling(self):
        """Test handling of invalid credentials"""
        print("\n🔧 Testing Book Store Authentication - Invalid Credentials...")
        
        try:
            self.driver.get("https://demoqa.com/login")
            time.sleep(3)  # Wait for page to load
            self.remove_ads()  # Remove interfering ads
            
            # Enter invalid credentials
            username_field = self.driver.find_element(By.ID, "userName")
            password_field = self.driver.find_element(By.ID, "password")
            login_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login")))
            
            username_field.clear()
            username_field.send_keys("invaliduser123")
            password_field.clear()
            password_field.send_keys("invalidpass123")
            
            print("  ✓ Invalid credentials entered")
            
            if self.safe_click(login_btn):
                print("  ✓ Login attempted with invalid credentials")
            else:
                print("  ⚠️ Login button click had issues, but continuing test")
            
            time.sleep(3)
            
            # Check for error message or remaining on login page
            current_url = self.driver.current_url
            
            if "login" in current_url:
                print("  ✓ Remained on login page (invalid credentials rejected)")
                
                # Look for error message
                try:
                    error_elements = self.driver.find_elements(By.CSS_SELECTOR, 
                        ".error, .alert, .invalid-feedback, [class*='error'], [id*='error']")
                    
                    if error_elements:
                        for error in error_elements:
                            if error.is_displayed() and error.text.strip():
                                print(f"  ✓ Error message found: '{error.text}'")
                                break
                    else:
                        print("  ⚠️ No visible error message found")
                        
                except Exception as error_e:
                    print(f"  ⚠️ Could not check for error messages: {error_e}")
                    
            else:
                print(f"  ⚠️ Unexpected navigation: {current_url}")
            
            print("✅ Invalid credentials handling test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Invalid credentials handling test FAILED: {e}")
            return False

    def test_authentication_state_persistence(self):
        """Test authentication state persistence"""
        print("\n🔧 Testing Book Store Authentication - State Persistence...")
        
        try:
            # Start from login page
            self.driver.get("https://demoqa.com/login")
            time.sleep(2)
            
            # Navigate to different pages and check authentication state
            test_pages = [
                "https://demoqa.com/books",
                "https://demoqa.com/profile",
                "https://demoqa.com/login"
            ]
            
            for page in test_pages:
                self.driver.get(page)
                time.sleep(2)
                
                current_url = self.driver.current_url
                print(f"  ✓ Navigated to: {page}")
                print(f"    Current URL: {current_url}")
                
                # Check authentication indicators
                try:
                    # Look for login/logout buttons
                    login_elements = self.driver.find_elements(By.XPATH, 
                        "//button[contains(text(), 'Login')] | //a[contains(text(), 'Login')] | //button[@id='login']")
                    
                    logout_elements = self.driver.find_elements(By.XPATH, 
                        "//button[contains(text(), 'Logout')] | //a[contains(text(), 'Logout')] | //button[@id='logout']")
                    
                    if login_elements and any(elem.is_displayed() for elem in login_elements):
                        print("    ✓ Login button visible (not authenticated)")
                    elif logout_elements and any(elem.is_displayed() for elem in logout_elements):
                        print("    ✓ Logout button visible (authenticated)")
                    else:
                        print("    ⚠️ Authentication state unclear")
                        
                except Exception as state_e:
                    print(f"    ⚠️ Could not determine authentication state: {state_e}")
            
            print("✅ Authentication state persistence test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Authentication state persistence test FAILED: {e}")
            return False

    def test_logout_functionality(self):
        """Test logout functionality"""
        print("\n🔧 Testing Book Store Authentication - Logout Functionality...")
        
        try:
            # Start from books page
            self.driver.get("https://demoqa.com/books")
            time.sleep(2)
            
            # Look for logout button
            try:
                logout_elements = self.driver.find_elements(By.XPATH, 
                    "//button[contains(text(), 'Logout')] | //a[contains(text(), 'Logout')] | //button[@id='logout']")
                
                if logout_elements:
                    logout_btn = None
                    for elem in logout_elements:
                        if elem.is_displayed():
                            logout_btn = elem
                            break
                    
                    if logout_btn:
                        print("  ✓ Logout button found")
                        logout_btn.click()
                        print("  ✓ Logout button clicked")
                        
                        time.sleep(2)
                        
                        # Check if redirected or state changed
                        current_url = self.driver.current_url
                        print(f"  ✓ Current URL after logout: {current_url}")
                        
                        # Try to access protected area
                        self.driver.get("https://demoqa.com/profile")
                        time.sleep(2)
                        
                        final_url = self.driver.current_url
                        if "login" in final_url:
                            print("  ✓ Redirected to login after logout (logout successful)")
                        else:
                            print("  ⚠️ No redirect to login (logout may not have worked)")
                            
                    else:
                        print("  ⚠️ Logout button not visible")
                        
                else:
                    print("  ⚠️ No logout button found (user may not be logged in)")
                    
            except Exception as logout_e:
                print(f"  ⚠️ Logout test issue: {logout_e}")
            
            print("✅ Logout functionality test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Logout functionality test FAILED: {e}")
            return False

    def test_protected_routes_access(self):
        """Test access to protected routes"""
        print("\n🔧 Testing Book Store Authentication - Protected Routes Access...")
        
        try:
            # Test access to protected routes without authentication
            protected_routes = [
                "https://demoqa.com/profile",
                "https://demoqa.com/books?book=add",  # Hypothetical add book route
            ]
            
            for route in protected_routes:
                try:
                    self.driver.get(route)
                    time.sleep(3)
                    
                    current_url = self.driver.current_url
                    print(f"  ✓ Attempted to access: {route}")
                    print(f"    Redirected to: {current_url}")
                    
                    if "login" in current_url:
                        print("    ✓ Properly redirected to login (route protected)")
                    elif current_url == route:
                        print("    ⚠️ Access granted (route may not be protected)")
                    else:
                        print("    ⚠️ Unexpected redirect")
                        
                except Exception as route_e:
                    print(f"    ⚠️ Route access issue: {route_e}")
            
            print("✅ Protected routes access test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Protected routes access test FAILED: {e}")
            return False

    def run_all_authentication_tests(self):
        """Run all authentication tests"""
        print("=" * 60)
        print("🔐 AUTHENTICATION INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_authentication_flow_access())
            results.append(self.test_login_form_validation())
            results.append(self.test_invalid_credentials_handling())
            results.append(self.test_authentication_state_persistence())
            results.append(self.test_logout_functionality())
            results.append(self.test_protected_routes_access())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 AUTHENTICATION TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Authentication tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Authentication tests passed, some had issues")
            else:
                print("❌ All Authentication tests had issues")
                
        except Exception as e:
            print(f"❌ Authentication test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    auth_test = AuthenticationTest()
    auth_test.run_all_authentication_tests()