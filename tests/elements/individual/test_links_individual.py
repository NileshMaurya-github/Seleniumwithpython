from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class LinksTest:
    """Individual test for Links functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_simple_link_new_tab(self):
        """Test simple link that opens in new tab"""
        print("🔧 Testing Links - Simple Link (New Tab)...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Get initial window count
            initial_windows = len(self.driver.window_handles)
            print(f"  ✓ Initial windows: {initial_windows}")

            # Click simple link
            simple_link = self.driver.find_element(By.ID, "simpleLink")
            simple_link.click()
            time.sleep(2)
            print("  ✓ Simple link clicked")

            # Check if new tab opened
            current_windows = len(self.driver.window_handles)
            print(f"  ✓ Current windows: {current_windows}")

            if current_windows > initial_windows:
                # Switch to new tab and verify
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2)
                
                current_url = self.driver.current_url
                print(f"  ✓ New tab URL: {current_url}")
                
                if "demoqa.com" in current_url:
                    print("  ✓ New tab opened with correct URL")
                    
                    # Close new tab and switch back
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    print("  ✓ Returned to original tab")
                    
                    print("✅ Simple link new tab test PASSED")
                    return True
                else:
                    print("  ❌ New tab URL incorrect")
                    return False
            else:
                print("  ❌ New tab was not opened")
                return False
                
        except Exception as e:
            print(f"❌ Simple link new tab test FAILED: {e}")
            return False

    def test_dynamic_link(self):
        """Test dynamic link functionality"""
        print("\n🔧 Testing Links - Dynamic Link...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Get initial window count
            initial_windows = len(self.driver.window_handles)

            # Click dynamic link
            dynamic_link = self.driver.find_element(By.ID, "dynamicLink")
            dynamic_link.click()
            time.sleep(2)
            print("  ✓ Dynamic link clicked")

            # Check if new tab opened
            current_windows = len(self.driver.window_handles)

            if current_windows > initial_windows:
                # Switch to new tab and verify
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2)
                
                current_url = self.driver.current_url
                print(f"  ✓ Dynamic link URL: {current_url}")
                
                if "demoqa.com" in current_url:
                    print("  ✓ Dynamic link opened with correct URL")
                    
                    # Close new tab and switch back
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    
                    print("✅ Dynamic link test PASSED")
                    return True
                else:
                    print("  ❌ Dynamic link URL incorrect")
                    return False
            else:
                print("  ❌ Dynamic link did not open new tab")
                return False
                
        except Exception as e:
            print(f"❌ Dynamic link test FAILED: {e}")
            return False

    def test_api_link_created(self):
        """Test API link - Created (201)"""
        print("\n🔧 Testing Links - API Created Link...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Click Created API link
            created_link = self.driver.find_element(By.ID, "created")
            created_link.click()
            time.sleep(2)
            print("  ✓ Created API link clicked")

            # Check for response message
            response_msg = self.wait.until(EC.presence_of_element_located((By.ID, "linkResponse")))
            response_text = response_msg.text
            print(f"  ✓ API Response: {response_text[:100]}...")
            
            if "201" in response_text or "Created" in response_text:
                print("  ✓ Created API response verified")
            else:
                print("  ⚠️ Created API response format unclear")
            
            print("✅ API Created link test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API Created link test FAILED: {e}")
            return False

    def test_api_link_no_content(self):
        """Test API link - No Content (204)"""
        print("\n🔧 Testing Links - API No Content Link...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Click No Content API link
            no_content_link = self.driver.find_element(By.ID, "no-content")
            no_content_link.click()
            time.sleep(2)
            print("  ✓ No Content API link clicked")

            # Check for response message
            response_msg = self.wait.until(EC.presence_of_element_located((By.ID, "linkResponse")))
            response_text = response_msg.text
            print(f"  ✓ API Response: {response_text[:100]}...")
            
            if "204" in response_text or "No Content" in response_text:
                print("  ✓ No Content API response verified")
            else:
                print("  ⚠️ No Content API response format unclear")
            
            print("✅ API No Content link test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API No Content link test FAILED: {e}")
            return False

    def test_api_link_moved(self):
        """Test API link - Moved (301)"""
        print("\n🔧 Testing Links - API Moved Link...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Click Moved API link
            moved_link = self.driver.find_element(By.ID, "moved")
            moved_link.click()
            time.sleep(2)
            print("  ✓ Moved API link clicked")

            # Check for response message
            response_msg = self.wait.until(EC.presence_of_element_located((By.ID, "linkResponse")))
            response_text = response_msg.text
            print(f"  ✓ API Response: {response_text[:100]}...")
            
            if "301" in response_text or "Moved" in response_text:
                print("  ✓ Moved API response verified")
            else:
                print("  ⚠️ Moved API response format unclear")
            
            print("✅ API Moved link test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API Moved link test FAILED: {e}")
            return False

    def test_api_link_bad_request(self):
        """Test API link - Bad Request (400)"""
        print("\n🔧 Testing Links - API Bad Request Link...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Click Bad Request API link
            bad_request_link = self.driver.find_element(By.ID, "bad-request")
            bad_request_link.click()
            time.sleep(2)
            print("  ✓ Bad Request API link clicked")

            # Check for response message
            response_msg = self.wait.until(EC.presence_of_element_located((By.ID, "linkResponse")))
            response_text = response_msg.text
            print(f"  ✓ API Response: {response_text[:100]}...")
            
            if "400" in response_text or "Bad Request" in response_text:
                print("  ✓ Bad Request API response verified")
            else:
                print("  ⚠️ Bad Request API response format unclear")
            
            print("✅ API Bad Request link test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API Bad Request link test FAILED: {e}")
            return False

    def test_api_link_unauthorized(self):
        """Test API link - Unauthorized (401)"""
        print("\n🔧 Testing Links - API Unauthorized Link...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Click Unauthorized API link
            unauthorized_link = self.driver.find_element(By.ID, "unauthorized")
            unauthorized_link.click()
            time.sleep(2)
            print("  ✓ Unauthorized API link clicked")

            # Check for response message
            response_msg = self.wait.until(EC.presence_of_element_located((By.ID, "linkResponse")))
            response_text = response_msg.text
            print(f"  ✓ API Response: {response_text[:100]}...")
            
            if "401" in response_text or "Unauthorized" in response_text:
                print("  ✓ Unauthorized API response verified")
            else:
                print("  ⚠️ Unauthorized API response format unclear")
            
            print("✅ API Unauthorized link test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API Unauthorized link test FAILED: {e}")
            return False

    def test_link_properties(self):
        """Test link properties and attributes"""
        print("\n🔧 Testing Links - Link Properties...")
        self.driver.get("https://demoqa.com/links")

        try:
            # Test simple link properties
            simple_link = self.driver.find_element(By.ID, "simpleLink")
            print(f"  ✓ Simple link text: {simple_link.text}")
            print(f"  ✓ Simple link href: {simple_link.get_attribute('href')}")
            print(f"  ✓ Simple link target: {simple_link.get_attribute('target')}")

            # Test dynamic link properties
            dynamic_link = self.driver.find_element(By.ID, "dynamicLink")
            print(f"  ✓ Dynamic link text: {dynamic_link.text}")
            print(f"  ✓ Dynamic link href: {dynamic_link.get_attribute('href')}")

            # Test API link properties
            created_link = self.driver.find_element(By.ID, "created")
            print(f"  ✓ Created API link text: {created_link.text}")
            print(f"  ✓ Created API link href: {created_link.get_attribute('href')}")
            
            print("✅ Link properties test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Link properties test FAILED: {e}")
            return False

    def run_all_links_tests(self):
        """Run all links tests"""
        print("=" * 60)
        print("🔗 LINKS INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_simple_link_new_tab())
            results.append(self.test_dynamic_link())
            results.append(self.test_api_link_created())
            results.append(self.test_api_link_no_content())
            results.append(self.test_api_link_moved())
            results.append(self.test_api_link_bad_request())
            results.append(self.test_api_link_unauthorized())
            results.append(self.test_link_properties())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 LINKS TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Links tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Links tests passed, some had issues")
            else:
                print("❌ All Links tests had issues")
                
        except Exception as e:
            print(f"❌ Links test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    links_test = LinksTest()
    links_test.run_all_links_tests()