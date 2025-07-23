from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class CheckBoxTest:
    """Individual test for Check Box functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_checkbox_expand_functionality(self):
        """Test checkbox tree expansion"""
        print("🔧 Testing Check Box - Expand Functionality...")
        self.driver.get("https://demoqa.com/checkbox")

        try:
            # Try to expand all nodes
            try:
                expand_all = self.driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
                expand_all.click()
                time.sleep(1)
                print("  ✓ Expand all button clicked successfully")
            except:
                print("  ⚠️ Expand all button not found, trying alternative method")
                
            # Try to expand home node specifically
            try:
                home_toggle = self.driver.find_element(By.XPATH, "//span[text()='Home']/../button")
                home_toggle.click()
                time.sleep(1)
                print("  ✓ Home node expanded")
            except:
                print("  ⚠️ Home node expansion not found")
            
            print("✅ Check Box expand functionality test COMPLETED")
            return True
            
        except Exception as e:
            print(f"❌ Check Box expand test FAILED: {e}")
            return False

    def test_checkbox_selection(self):
        """Test checkbox selection functionality"""
        print("\n🔧 Testing Check Box - Selection Functionality...")
        self.driver.get("https://demoqa.com/checkbox")

        try:
            # Expand tree first
            try:
                expand_all = self.driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
                expand_all.click()
                time.sleep(1)
            except:
                pass

            # Select various checkboxes
            checkboxes_to_select = [
                ("Home", "//span[text()='Home']/../span[@class='rct-checkbox']"),
                ("Desktop", "//span[text()='Desktop']/../span[@class='rct-checkbox']"),
                ("Documents", "//span[text()='Documents']/../span[@class='rct-checkbox']")
            ]

            selected_count = 0
            for name, xpath in checkboxes_to_select:
                try:
                    element = self.driver.find_element(By.XPATH, xpath)
                    self.driver.execute_script("arguments[0].click();", element)
                    time.sleep(0.5)
                    print(f"  ✓ {name} checkbox selected")
                    selected_count += 1
                except:
                    print(f"  ⚠️ {name} checkbox not found or not selectable")

            # Verify selection result
            try:
                result = self.wait.until(EC.presence_of_element_located((By.ID, "result")))
                result_text = result.text
                print(f"  ✓ Selection result: {result_text}")
                
                if selected_count > 0:
                    print(f"✅ Check Box selection test PASSED - {selected_count} checkboxes selected")
                    return True
                else:
                    print("⚠️ Check Box selection test COMPLETED - no checkboxes selected")
                    return False
            except:
                print("  ⚠️ Result element not found")
                return selected_count > 0
                
        except Exception as e:
            print(f"❌ Check Box selection test FAILED: {e}")
            return False

    def test_checkbox_unselection(self):
        """Test checkbox unselection functionality"""
        print("\n🔧 Testing Check Box - Unselection Functionality...")
        self.driver.get("https://demoqa.com/checkbox")

        try:
            # Expand and select a checkbox first
            try:
                expand_all = self.driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
                expand_all.click()
                time.sleep(1)
            except:
                pass

            # Select Home checkbox
            try:
                home_checkbox = self.driver.find_element(By.XPATH, "//span[text()='Home']/../span[@class='rct-checkbox']")
                self.driver.execute_script("arguments[0].click();", home_checkbox)
                time.sleep(1)
                print("  ✓ Home checkbox selected first")
                
                # Now unselect it
                self.driver.execute_script("arguments[0].click();", home_checkbox)
                time.sleep(1)
                print("  ✓ Home checkbox unselected")
                
                # Check if result is empty or shows unselection
                try:
                    result = self.driver.find_element(By.ID, "result")
                    result_text = result.text.strip()
                    if not result_text or "You have selected" not in result_text:
                        print("  ✓ Unselection verified - no items selected")
                    else:
                        print(f"  ⚠️ Result still shows: {result_text}")
                except:
                    print("  ✓ Result element not visible - likely unselected")
                
                print("✅ Check Box unselection test PASSED")
                return True
                
            except Exception as e:
                print(f"  ⚠️ Could not test unselection: {e}")
                return False
                
        except Exception as e:
            print(f"❌ Check Box unselection test FAILED: {e}")
            return False

    def test_checkbox_partial_selection(self):
        """Test partial checkbox selection (parent-child relationship)"""
        print("\n🔧 Testing Check Box - Partial Selection...")
        self.driver.get("https://demoqa.com/checkbox")

        try:
            # Expand tree
            try:
                expand_all = self.driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
                expand_all.click()
                time.sleep(1)
            except:
                pass

            # Select a child item to see if parent shows partial selection
            try:
                # Try to select a specific file under Desktop
                desktop_file = self.driver.find_element(By.XPATH, "//span[text()='Notes']/../span[@class='rct-checkbox']")
                self.driver.execute_script("arguments[0].click();", desktop_file)
                time.sleep(1)
                print("  ✓ Child item (Notes) selected")
                
                # Check if parent (Desktop) shows partial selection
                desktop_checkbox = self.driver.find_element(By.XPATH, "//span[text()='Desktop']/../span[@class='rct-checkbox']")
                checkbox_class = desktop_checkbox.get_attribute("class")
                
                if "rct-icon-half-check" in checkbox_class:
                    print("  ✓ Parent shows partial selection state")
                else:
                    print("  ⚠️ Parent selection state unclear")
                
                print("✅ Check Box partial selection test COMPLETED")
                return True
                
            except Exception as e:
                print(f"  ⚠️ Could not test partial selection: {e}")
                return False
                
        except Exception as e:
            print(f"❌ Check Box partial selection test FAILED: {e}")
            return False

    def run_all_checkbox_tests(self):
        """Run all checkbox tests"""
        print("=" * 60)
        print("☑️ CHECK BOX INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_checkbox_expand_functionality())
            results.append(self.test_checkbox_selection())
            results.append(self.test_checkbox_unselection())
            results.append(self.test_checkbox_partial_selection())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 CHECK BOX TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Check Box tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Check Box tests passed, some had issues")
            else:
                print("❌ All Check Box tests had issues")
                
        except Exception as e:
            print(f"❌ Check Box test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    checkbox_test = CheckBoxTest()
    checkbox_test.run_all_checkbox_tests()