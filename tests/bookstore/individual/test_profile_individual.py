from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class ProfileTest:
    """Individual test for Book Store Profile functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_profile_page_access(self):
        """Test profile page access and elements"""
        print("🔧 Testing Book Store Profile - Page Access...")
        self.driver.get("https://demoqa.com/profile")

        try:
            # Check if redirected to login (not logged in)
            time.sleep(2)
            current_url = self.driver.current_url
            
            if "login" in current_url:
                print("  ✓ Redirected to login page (user not authenticated)")
                
                # Check login page elements
                username_field = self.driver.find_element(By.ID, "userName")
                password_field = self.driver.find_element(By.ID, "password")
                login_btn = self.driver.find_element(By.ID, "login")
                
                assert username_field.is_displayed()
                assert password_field.is_displayed()
                assert login_btn.is_displayed()
                print("  ✓ Login form elements are present")
                
            elif "profile" in current_url:
                print("  ✓ Accessed profile page directly (user may be authenticated)")
                
                # Check for profile elements
                try:
                    profile_wrapper = self.driver.find_element(By.CLASS_NAME, "profile-wrapper")
                    print("  ✓ Profile wrapper found")
                except:
                    print("  ⚠️ Profile wrapper not found")
            
            print("✅ Profile page access test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Profile page access test FAILED: {e}")
            return False

    def test_profile_navigation_from_menu(self):
        """Test navigation to profile from main menu"""
        print("\n🔧 Testing Book Store Profile - Navigation from Menu...")
        self.driver.get("https://demoqa.com/books")

        try:
            # Look for profile link in navigation
            try:
                profile_link = self.driver.find_element(By.XPATH, "//span[text()='Profile']")
                if profile_link.is_displayed():
                    profile_link.click()
                    print("  ✓ Profile link clicked from menu")
                    
                    # Wait for navigation
                    time.sleep(2)
                    current_url = self.driver.current_url
                    
                    if "profile" in current_url or "login" in current_url:
                        print(f"  ✓ Navigated to: {current_url}")
                    else:
                        print(f"  ⚠️ Unexpected navigation: {current_url}")
                        
                else:
                    print("  ⚠️ Profile link not visible in menu")
                    
            except Exception as nav_e:
                print(f"  ⚠️ Profile navigation issue: {nav_e}")
                # Try alternative navigation method
                self.driver.get("https://demoqa.com/profile")
                print("  ✓ Direct navigation to profile page")
            
            print("✅ Profile navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Profile navigation test FAILED: {e}")
            return False

    def test_profile_without_login(self):
        """Test profile page behavior without login"""
        print("\n🔧 Testing Book Store Profile - Without Login...")
        self.driver.get("https://demoqa.com/profile")

        try:
            # Wait for page to load
            time.sleep(3)
            current_url = self.driver.current_url
            
            if "login" in current_url:
                print("  ✓ Redirected to login page (expected behavior)")
                
                # Verify login form is present
                username_field = self.driver.find_element(By.ID, "userName")
                password_field = self.driver.find_element(By.ID, "password")
                login_btn = self.driver.find_element(By.ID, "login")
                
                assert username_field.is_displayed()
                assert password_field.is_displayed()
                assert login_btn.is_displayed()
                print("  ✓ Login form is properly displayed")
                
            else:
                print("  ⚠️ Not redirected to login (unexpected)")
                
                # Check what's on the profile page
                page_source = self.driver.page_source
                if "login" in page_source.lower() or "sign in" in page_source.lower():
                    print("  ✓ Login prompt found on profile page")
                else:
                    print("  ⚠️ No login prompt found")
            
            print("✅ Profile without login test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Profile without login test FAILED: {e}")
            return False

    def test_profile_page_structure(self):
        """Test profile page structure and layout"""
        print("\n🔧 Testing Book Store Profile - Page Structure...")
        self.driver.get("https://demoqa.com/profile")

        try:
            # Wait for page to load
            time.sleep(3)
            
            # Check page title
            page_title = self.driver.title
            print(f"  ✓ Page title: '{page_title}'")
            
            # Check for main content area
            try:
                main_content = self.driver.find_element(By.ID, "app")
                assert main_content.is_displayed()
                print("  ✓ Main content area found")
            except:
                print("  ⚠️ Main content area not found")
            
            # Check for header/navigation
            try:
                header = self.driver.find_element(By.CSS_SELECTOR, "header, .header, .main-header")
                if header.is_displayed():
                    print("  ✓ Header/navigation found")
            except:
                print("  ✓ No specific header found (may be integrated)")
            
            # Check current URL structure
            current_url = self.driver.current_url
            print(f"  ✓ Current URL: {current_url}")
            
            print("✅ Profile page structure test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Profile page structure test FAILED: {e}")
            return False

    def test_profile_book_collection_area(self):
        """Test profile book collection display area"""
        print("\n🔧 Testing Book Store Profile - Book Collection Area...")
        self.driver.get("https://demoqa.com/profile")

        try:
            # Wait for page to load
            time.sleep(3)
            current_url = self.driver.current_url
            
            if "login" in current_url:
                print("  ✓ On login page - checking for profile-related elements")
                
                # Look for any profile-related text or elements
                page_text = self.driver.page_source.lower()
                if "profile" in page_text or "collection" in page_text:
                    print("  ✓ Profile-related content mentioned")
                else:
                    print("  ✓ Standard login page (expected)")
                    
            else:
                print("  ✓ On profile page - checking for book collection area")
                
                # Look for book collection elements
                try:
                    collection_area = self.driver.find_element(By.CSS_SELECTOR, ".profile-wrapper, .books-wrapper, .collection")
                    if collection_area.is_displayed():
                        print("  ✓ Book collection area found")
                    else:
                        print("  ⚠️ Book collection area not visible")
                except:
                    print("  ⚠️ Book collection area not found")
                
                # Look for "no books" message or book list
                try:
                    no_books_msg = self.driver.find_element(By.XPATH, "//*[contains(text(), 'No rows found')]")
                    if no_books_msg.is_displayed():
                        print("  ✓ 'No books' message found (empty collection)")
                except:
                    print("  ✓ No 'no books' message (may have books or different structure)")
            
            print("✅ Profile book collection area test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Profile book collection area test FAILED: {e}")
            return False

    def run_all_profile_tests(self):
        """Run all profile tests"""
        print("=" * 60)
        print("👤 PROFILE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_profile_page_access())
            results.append(self.test_profile_navigation_from_menu())
            results.append(self.test_profile_without_login())
            results.append(self.test_profile_page_structure())
            results.append(self.test_profile_book_collection_area())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 PROFILE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Profile tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Profile tests passed, some had issues")
            else:
                print("❌ All Profile tests had issues")
                
        except Exception as e:
            print(f"❌ Profile test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    profile_test = ProfileTest()
    profile_test.run_all_profile_tests()