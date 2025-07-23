from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class ButtonsTest:
    """Individual test for Buttons functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_double_click_button(self):
        """Test double click button functionality"""
        print("🔧 Testing Buttons - Double Click...")
        self.driver.get("https://demoqa.com/buttons")

        try:
            actions = ActionChains(self.driver)

            # Double click button
            double_click_btn = self.driver.find_element(By.ID, "doubleClickBtn")
            actions.double_click(double_click_btn).perform()
            print("  ✓ Double click performed")

            # Verify double click message
            double_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))
            assert "double click" in double_click_msg.text.lower()
            print(f"  ✓ Double click message verified: {double_click_msg.text}")
            
            print("✅ Double click button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Double click button test FAILED: {e}")
            return False

    def test_right_click_button(self):
        """Test right click button functionality"""
        print("\n🔧 Testing Buttons - Right Click...")
        self.driver.get("https://demoqa.com/buttons")

        try:
            actions = ActionChains(self.driver)

            # Right click button
            right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
            actions.context_click(right_click_btn).perform()
            print("  ✓ Right click performed")

            # Verify right click message
            right_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "rightClickMessage")))
            assert "right click" in right_click_msg.text.lower()
            print(f"  ✓ Right click message verified: {right_click_msg.text}")
            
            print("✅ Right click button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Right click button test FAILED: {e}")
            return False

    def test_dynamic_click_button(self):
        """Test dynamic click button functionality"""
        print("\n🔧 Testing Buttons - Dynamic Click...")
        self.driver.get("https://demoqa.com/buttons")

        try:
            # Find and click the dynamic button
            dynamic_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
            dynamic_click_btn.click()
            print("  ✓ Dynamic click performed")

            # Verify dynamic click message
            dynamic_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))
            assert "dynamic click" in dynamic_click_msg.text.lower()
            print(f"  ✓ Dynamic click message verified: {dynamic_click_msg.text}")
            
            print("✅ Dynamic click button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Dynamic click button test FAILED: {e}")
            return False

    def test_button_states(self):
        """Test button states and properties"""
        print("\n🔧 Testing Buttons - Button States...")
        self.driver.get("https://demoqa.com/buttons")

        try:
            # Check double click button properties
            double_click_btn = self.driver.find_element(By.ID, "doubleClickBtn")
            print(f"  ✓ Double click button enabled: {double_click_btn.is_enabled()}")
            print(f"  ✓ Double click button displayed: {double_click_btn.is_displayed()}")
            print(f"  ✓ Double click button text: {double_click_btn.text}")

            # Check right click button properties
            right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
            print(f"  ✓ Right click button enabled: {right_click_btn.is_enabled()}")
            print(f"  ✓ Right click button displayed: {right_click_btn.is_displayed()}")
            print(f"  ✓ Right click button text: {right_click_btn.text}")

            # Check dynamic click button properties
            dynamic_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
            print(f"  ✓ Dynamic click button enabled: {dynamic_click_btn.is_enabled()}")
            print(f"  ✓ Dynamic click button displayed: {dynamic_click_btn.is_displayed()}")
            print(f"  ✓ Dynamic click button text: {dynamic_click_btn.text}")
            
            print("✅ Button states test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Button states test FAILED: {e}")
            return False

    def test_button_hover_effects(self):
        """Test button hover effects"""
        print("\n🔧 Testing Buttons - Hover Effects...")
        self.driver.get("https://demoqa.com/buttons")

        try:
            actions = ActionChains(self.driver)

            # Test hover on double click button
            double_click_btn = self.driver.find_element(By.ID, "doubleClickBtn")
            actions.move_to_element(double_click_btn).perform()
            time.sleep(1)
            print("  ✓ Hovered over double click button")

            # Test hover on right click button
            right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
            actions.move_to_element(right_click_btn).perform()
            time.sleep(1)
            print("  ✓ Hovered over right click button")

            # Test hover on dynamic click button
            dynamic_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
            actions.move_to_element(dynamic_click_btn).perform()
            time.sleep(1)
            print("  ✓ Hovered over dynamic click button")
            
            print("✅ Button hover effects test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Button hover effects test FAILED: {e}")
            return False

    def test_all_buttons_sequence(self):
        """Test all buttons in sequence"""
        print("\n🔧 Testing Buttons - All Buttons Sequence...")
        self.driver.get("https://demoqa.com/buttons")

        try:
            actions = ActionChains(self.driver)

            # Perform all button actions in sequence
            # 1. Double click
            double_click_btn = self.driver.find_element(By.ID, "doubleClickBtn")
            actions.double_click(double_click_btn).perform()
            time.sleep(1)
            
            double_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))
            print(f"  ✓ Double click: {double_click_msg.text}")

            # 2. Right click
            right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
            actions.context_click(right_click_btn).perform()
            time.sleep(1)
            
            right_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "rightClickMessage")))
            print(f"  ✓ Right click: {right_click_msg.text}")

            # 3. Dynamic click
            dynamic_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
            dynamic_click_btn.click()
            time.sleep(1)
            
            dynamic_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))
            print(f"  ✓ Dynamic click: {dynamic_click_msg.text}")

            # Verify all messages are present
            all_messages_present = (
                "double click" in double_click_msg.text.lower() and
                "right click" in right_click_msg.text.lower() and
                "dynamic click" in dynamic_click_msg.text.lower()
            )

            if all_messages_present:
                print("  ✓ All button interactions successful")
                print("✅ All buttons sequence test PASSED")
                return True
            else:
                print("  ❌ Some button interactions failed")
                return False
            
        except Exception as e:
            print(f"❌ All buttons sequence test FAILED: {e}")
            return False

    def run_all_buttons_tests(self):
        """Run all buttons tests"""
        print("=" * 60)
        print("🔘 BUTTONS INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_double_click_button())
            results.append(self.test_right_click_button())
            results.append(self.test_dynamic_click_button())
            results.append(self.test_button_states())
            results.append(self.test_button_hover_effects())
            results.append(self.test_all_buttons_sequence())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 BUTTONS TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Buttons tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Buttons tests passed, some had issues")
            else:
                print("❌ All Buttons tests had issues")
                
        except Exception as e:
            print(f"❌ Buttons test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    buttons_test = ButtonsTest()
    buttons_test.run_all_buttons_tests()