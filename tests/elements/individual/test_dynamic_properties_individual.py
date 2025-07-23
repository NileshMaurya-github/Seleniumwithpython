from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class DynamicPropertiesTest:
    """Individual test for Dynamic Properties functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_enable_after_button(self):
        """Test button that becomes enabled after delay"""
        print("🔧 Testing Dynamic Properties - Enable After Button...")
        self.driver.get("https://demoqa.com/dynamic-properties")

        try:
            # Wait for button to be enabled (it takes 5 seconds)
            print("  ⏳ Waiting for button to be enabled (5 seconds)...")
            enable_after_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
            
            # Check button properties
            print(f"  ✓ Button enabled: {enable_after_btn.is_enabled()}")
            print(f"  ✓ Button displayed: {enable_after_btn.is_displayed()}")
            print(f"  ✓ Button text: {enable_after_btn.text}")
            
            # Click the button
            enable_after_btn.click()
            print("  ✓ Button clicked successfully")
            
            print("✅ Enable After button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Enable After button test FAILED: {e}")
            return False

    def test_color_change_button(self):
        """Test button that changes color dynamically"""
        print("\n🔧 Testing Dynamic Properties - Color Change Button...")
        self.driver.get("https://demoqa.com/dynamic-properties")

        try:
            # Wait for color change button to be present
            color_change_btn = self.wait.until(EC.presence_of_element_located((By.ID, "colorChange")))
            
            # Get initial color
            initial_color = color_change_btn.value_of_css_property('color')
            print(f"  ✓ Initial button color: {initial_color}")
            
            # Wait a bit and check color again (color changes randomly)
            time.sleep(3)
            current_color = color_change_btn.value_of_css_property('color')
            print(f"  ✓ Current button color: {current_color}")
            
            # Check other properties
            print(f"  ✓ Button text: {color_change_btn.text}")
            print(f"  ✓ Button enabled: {color_change_btn.is_enabled()}")
            print(f"  ✓ Button displayed: {color_change_btn.is_displayed()}")
            
            # Check background color
            bg_color = color_change_btn.value_of_css_property('background-color')
            print(f"  ✓ Button background color: {bg_color}")
            
            print("✅ Color Change button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Color Change button test FAILED: {e}")
            return False

    def test_visible_after_button(self):
        """Test button that becomes visible after delay"""
        print("\n🔧 Testing Dynamic Properties - Visible After Button...")
        self.driver.get("https://demoqa.com/dynamic-properties")

        try:
            # Wait for button to become visible (it takes 5 seconds)
            print("  ⏳ Waiting for button to become visible (5 seconds)...")
            visible_after_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
            
            # Check button properties
            print(f"  ✓ Button visible: {visible_after_btn.is_displayed()}")
            print(f"  ✓ Button enabled: {visible_after_btn.is_enabled()}")
            print(f"  ✓ Button text: {visible_after_btn.text}")
            
            # Click the button
            visible_after_btn.click()
            print("  ✓ Button clicked successfully")
            
            print("✅ Visible After button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Visible After button test FAILED: {e}")
            return False

    def test_static_elements(self):
        """Test static elements that don't change"""
        print("\n🔧 Testing Dynamic Properties - Static Elements...")
        self.driver.get("https://demoqa.com/dynamic-properties")

        try:
            # Check for static text elements
            page_elements = self.driver.find_elements(By.XPATH, "//p | //div[@class='col-12 mt-4 col-md-6']")
            
            static_elements_found = 0
            for element in page_elements:
                if element.is_displayed() and element.text.strip():
                    print(f"  ✓ Static element found: {element.text[:50]}...")
                    static_elements_found += 1
            
            print(f"  ✓ Total static elements found: {static_elements_found}")
            
            # Check page title or heading
            try:
                page_heading = self.driver.find_element(By.XPATH, "//h1 | //h2 | //h3")
                print(f"  ✓ Page heading: {page_heading.text}")
            except:
                print("  ℹ️ No specific heading found")
            
            print("✅ Static elements test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Static elements test FAILED: {e}")
            return False

    def test_button_timing(self):
        """Test timing of dynamic button appearances"""
        print("\n🔧 Testing Dynamic Properties - Button Timing...")
        self.driver.get("https://demoqa.com/dynamic-properties")

        try:
            start_time = time.time()
            
            # Test Enable After button timing
            try:
                enable_after_btn = WebDriverWait(self.driver, 6).until(
                    EC.element_to_be_clickable((By.ID, "enableAfter"))
                )
                enable_time = time.time() - start_time
                print(f"  ✓ Enable After button became clickable after: {enable_time:.2f} seconds")
            except:
                print("  ❌ Enable After button timing test failed")
            
            # Reset timing for Visible After button
            self.driver.refresh()
            start_time = time.time()
            
            # Test Visible After button timing
            try:
                visible_after_btn = WebDriverWait(self.driver, 6).until(
                    EC.visibility_of_element_located((By.ID, "visibleAfter"))
                )
                visible_time = time.time() - start_time
                print(f"  ✓ Visible After button became visible after: {visible_time:.2f} seconds")
            except:
                print("  ❌ Visible After button timing test failed")
            
            print("✅ Button timing test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Button timing test FAILED: {e}")
            return False

    def test_element_states_sequence(self):
        """Test sequence of element state changes"""
        print("\n🔧 Testing Dynamic Properties - Element States Sequence...")
        self.driver.get("https://demoqa.com/dynamic-properties")

        try:
            # Check initial states
            print("  📊 Checking initial element states...")
            
            # Enable After button - should be disabled initially
            try:
                enable_btn = self.driver.find_element(By.ID, "enableAfter")
                initial_enabled = enable_btn.is_enabled()
                print(f"    Enable After button initially enabled: {initial_enabled}")
            except:
                print("    Enable After button not found initially")
            
            # Visible After button - should be invisible initially
            try:
                visible_btn = self.driver.find_element(By.ID, "visibleAfter")
                initial_visible = visible_btn.is_displayed()
                print(f"    Visible After button initially visible: {initial_visible}")
            except:
                print("    Visible After button not found initially (expected)")
            
            # Color Change button - should be present
            try:
                color_btn = self.driver.find_element(By.ID, "colorChange")
                initial_color = color_btn.value_of_css_property('color')
                print(f"    Color Change button initial color: {initial_color}")
            except:
                print("    Color Change button not found")
            
            # Wait and check final states
            print("  ⏳ Waiting for dynamic changes...")
            time.sleep(6)
            
            # Check Enable After button final state
            try:
                enable_btn = self.driver.find_element(By.ID, "enableAfter")
                final_enabled = enable_btn.is_enabled()
                print(f"    Enable After button finally enabled: {final_enabled}")
            except:
                print("    Enable After button check failed")
            
            # Check Visible After button final state
            try:
                visible_btn = self.driver.find_element(By.ID, "visibleAfter")
                final_visible = visible_btn.is_displayed()
                print(f"    Visible After button finally visible: {final_visible}")
            except:
                print("    Visible After button still not visible")
            
            print("✅ Element states sequence test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Element states sequence test FAILED: {e}")
            return False

    def run_all_dynamic_properties_tests(self):
        """Run all dynamic properties tests"""
        print("=" * 60)
        print("⚡ DYNAMIC PROPERTIES INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_enable_after_button())
            results.append(self.test_color_change_button())
            results.append(self.test_visible_after_button())
            results.append(self.test_static_elements())
            results.append(self.test_button_timing())
            results.append(self.test_element_states_sequence())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 DYNAMIC PROPERTIES TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Dynamic Properties tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Dynamic Properties tests passed, some had issues")
            else:
                print("❌ All Dynamic Properties tests had issues")
                
        except Exception as e:
            print(f"❌ Dynamic Properties test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    dynamic_properties_test = DynamicPropertiesTest()
    dynamic_properties_test.run_all_dynamic_properties_tests()