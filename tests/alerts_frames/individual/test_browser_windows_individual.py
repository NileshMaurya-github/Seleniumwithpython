from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class BrowserWindowsTest:
    """Individual test for Browser Windows functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_new_tab(self):
        """Test new tab functionality"""
        print("🔧 Testing Browser Windows - New Tab...")
        self.driver.get("https://demoqa.com/browser-windows")

        try:
            # Get initial window handle
            original_window = self.driver.current_window_handle
            print(f"  ✓ Original window handle: {original_window}")
            
            # Click new tab button
            new_tab_btn = self.driver.find_element(By.ID, "tabButton")
            new_tab_btn.click()
            print("  ✓ New tab button clicked")
            
            # Wait for new tab to open and switch to it
            self.wait.until(EC.number_of_windows_to_be(2))
            
            # Loop through all window handles and switch to new tab
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            
            print(f"  ✓ Switched to new tab: {self.driver.current_window_handle}")
            
            # Verify new tab content
            page_text = self.wait.until(EC.presence_of_element_located((By.ID, "sampleHeading")))
            assert "This is a sample page" in page_text.text
            print(f"  ✓ New tab content verified: '{page_text.text}'")
            
            # Close new tab and switch back to original window
            self.driver.close()
            self.driver.switch_to.window(original_window)
            print("  ✓ Closed new tab and switched back to original window")
            
            print("✅ New tab test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ New tab test FAILED: {e}")
            return False

    def test_new_window(self):
        """Test new window functionality"""
        print("\n🔧 Testing Browser Windows - New Window...")
        self.driver.get("https://demoqa.com/browser-windows")

        try:
            # Get initial window handle
            original_window = self.driver.current_window_handle
            
            # Click new window button
            new_window_btn = self.driver.find_element(By.ID, "windowButton")
            new_window_btn.click()
            print("  ✓ New window button clicked")
            
            # Wait for new window to open and switch to it
            self.wait.until(EC.number_of_windows_to_be(2))
            
            # Loop through all window handles and switch to new window
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            
            print(f"  ✓ Switched to new window: {self.driver.current_window_handle}")
            
            # Verify new window content
            page_text = self.wait.until(EC.presence_of_element_located((By.ID, "sampleHeading")))
            assert "This is a sample page" in page_text.text
            print(f"  ✓ New window content verified: '{page_text.text}'")
            
            # Close new window and switch back to original window
            self.driver.close()
            self.driver.switch_to.window(original_window)
            print("  ✓ Closed new window and switched back to original window")
            
            print("✅ New window test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ New window test FAILED: {e}")
            return False

    def test_new_window_message(self):
        """Test new window message functionality"""
        print("\n🔧 Testing Browser Windows - New Window Message...")
        self.driver.get("https://demoqa.com/browser-windows")

        try:
            # Get initial window handle
            original_window = self.driver.current_window_handle
            
            # Click new window message button
            new_window_msg_btn = self.driver.find_element(By.ID, "messageWindowButton")
            new_window_msg_btn.click()
            print("  ✓ New window message button clicked")
            
            # Wait for new window to open and switch to it
            self.wait.until(EC.number_of_windows_to_be(2))
            time.sleep(2)  # Give some time for the window to fully load
            
            # Loop through all window handles and switch to new window
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            
            print(f"  ✓ Switched to new window message: {self.driver.current_window_handle}")
            
            # Note: The message window might be empty or have different content
            # Just verify we can switch to it
            print("  ✓ New window message opened successfully")
            
            # Close new window and switch back to original window
            self.driver.close()
            self.driver.switch_to.window(original_window)
            print("  ✓ Closed message window and switched back to original window")
            
            print("✅ New window message test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ New window message test FAILED: {e}")
            # Try to switch back to original window if possible
            try:
                self.driver.switch_to.window(original_window)
            except:
                pass
            return False

    def run_all_browser_windows_tests(self):
        """Run all browser windows tests"""
        print("=" * 60)
        print("🔳 BROWSER WINDOWS INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_new_tab())
            results.append(self.test_new_window())
            results.append(self.test_new_window_message())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 BROWSER WINDOWS TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Browser Windows tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Browser Windows tests passed, some had issues")
            else:
                print("❌ All Browser Windows tests had issues")
                
        except Exception as e:
            print(f"❌ Browser Windows test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    browser_windows_test = BrowserWindowsTest()
    browser_windows_test.run_all_browser_windows_tests()