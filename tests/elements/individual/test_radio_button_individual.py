from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class RadioButtonTest:
    """Individual test for Radio Button functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_yes_radio_button(self):
        """Test Yes radio button selection"""
        print("🔧 Testing Radio Button - Yes Selection...")
        self.driver.get("https://demoqa.com/radio-button")

        try:
            # Click Yes radio button
            yes_radio = self.driver.find_element(By.XPATH, "//label[@for='yesRadio']")
            yes_radio.click()
            print("  ✓ Yes radio button clicked")

            # Verify selection
            success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
            assert "Yes" in success_text.text
            print(f"  ✓ Verification passed: {success_text.text}")
            
            print("✅ Yes radio button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Yes radio button test FAILED: {e}")
            return False

    def test_impressive_radio_button(self):
        """Test Impressive radio button selection"""
        print("\n🔧 Testing Radio Button - Impressive Selection...")
        self.driver.get("https://demoqa.com/radio-button")

        try:
            # Click Impressive radio button
            impressive_radio = self.driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
            impressive_radio.click()
            print("  ✓ Impressive radio button clicked")

            # Verify selection
            success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
            assert "Impressive" in success_text.text
            print(f"  ✓ Verification passed: {success_text.text}")
            
            print("✅ Impressive radio button test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Impressive radio button test FAILED: {e}")
            return False

    def test_no_radio_button_disabled(self):
        """Test that No radio button is disabled"""
        print("\n🔧 Testing Radio Button - No Button Disabled State...")
        self.driver.get("https://demoqa.com/radio-button")

        try:
            # Check if No radio button is disabled
            no_radio_input = self.driver.find_element(By.ID, "noRadio")
            is_disabled = not no_radio_input.is_enabled()
            
            if is_disabled:
                print("  ✓ No radio button is correctly disabled")
            else:
                print("  ⚠️ No radio button appears to be enabled")
            
            # Try to click the label and verify it doesn't work
            try:
                no_radio_label = self.driver.find_element(By.XPATH, "//label[@for='noRadio']")
                no_radio_label.click()
                time.sleep(1)
                
                # Check if any result appeared (shouldn't happen)
                try:
                    result_element = self.driver.find_element(By.CSS_SELECTOR, ".text-success")
                    result_text = result_element.text
                    if "No" in result_text:
                        print("  ⚠️ No radio button was clickable (unexpected)")
                        return False
                    else:
                        print("  ✓ No radio button click had no effect (expected)")
                except:
                    print("  ✓ No radio button click had no effect (expected)")
                    
            except Exception as e:
                print(f"  ✓ No radio button interaction failed as expected: {e}")
            
            print("✅ No radio button disabled test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ No radio button disabled test FAILED: {e}")
            return False

    def test_radio_button_mutual_exclusion(self):
        """Test that radio buttons are mutually exclusive"""
        print("\n🔧 Testing Radio Button - Mutual Exclusion...")
        self.driver.get("https://demoqa.com/radio-button")

        try:
            # First select Yes
            yes_radio = self.driver.find_element(By.XPATH, "//label[@for='yesRadio']")
            yes_radio.click()
            time.sleep(1)
            
            success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
            first_selection = success_text.text
            print(f"  ✓ First selection: {first_selection}")
            
            # Then select Impressive
            impressive_radio = self.driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
            impressive_radio.click()
            time.sleep(1)
            
            # Verify that the selection changed to Impressive
            success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
            second_selection = success_text.text
            print(f"  ✓ Second selection: {second_selection}")
            
            # Verify mutual exclusion
            if "Impressive" in second_selection and "Yes" not in second_selection:
                print("  ✓ Radio buttons are mutually exclusive")
                print("✅ Radio button mutual exclusion test PASSED")
                return True
            else:
                print("  ❌ Radio buttons may not be mutually exclusive")
                return False
                
        except Exception as e:
            print(f"❌ Radio button mutual exclusion test FAILED: {e}")
            return False

    def test_radio_button_states(self):
        """Test radio button visual states"""
        print("\n🔧 Testing Radio Button - Visual States...")
        self.driver.get("https://demoqa.com/radio-button")

        try:
            # Check initial states
            yes_radio_input = self.driver.find_element(By.ID, "yesRadio")
            impressive_radio_input = self.driver.find_element(By.ID, "impressiveRadio")
            no_radio_input = self.driver.find_element(By.ID, "noRadio")
            
            print(f"  ✓ Yes radio enabled: {yes_radio_input.is_enabled()}")
            print(f"  ✓ Impressive radio enabled: {impressive_radio_input.is_enabled()}")
            print(f"  ✓ No radio enabled: {no_radio_input.is_enabled()}")
            
            # Test selection states
            yes_radio_label = self.driver.find_element(By.XPATH, "//label[@for='yesRadio']")
            yes_radio_label.click()
            time.sleep(1)
            
            # Check if Yes is selected
            is_yes_selected = yes_radio_input.is_selected()
            is_impressive_selected = impressive_radio_input.is_selected()
            
            print(f"  ✓ Yes radio selected: {is_yes_selected}")
            print(f"  ✓ Impressive radio selected: {is_impressive_selected}")
            
            if is_yes_selected and not is_impressive_selected:
                print("✅ Radio button states test PASSED")
                return True
            else:
                print("⚠️ Radio button states may not be working as expected")
                return False
                
        except Exception as e:
            print(f"❌ Radio button states test FAILED: {e}")
            return False

    def run_all_radio_button_tests(self):
        """Run all radio button tests"""
        print("=" * 60)
        print("🔘 RADIO BUTTON INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_yes_radio_button())
            results.append(self.test_impressive_radio_button())
            results.append(self.test_no_radio_button_disabled())
            results.append(self.test_radio_button_mutual_exclusion())
            results.append(self.test_radio_button_states())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 RADIO BUTTON TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Radio Button tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Radio Button tests passed, some had issues")
            else:
                print("❌ All Radio Button tests had issues")
                
        except Exception as e:
            print(f"❌ Radio Button test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    radio_button_test = RadioButtonTest()
    radio_button_test.run_all_radio_button_tests()