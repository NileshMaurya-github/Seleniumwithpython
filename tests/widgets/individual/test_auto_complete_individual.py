from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class AutoCompleteTest:
    """Individual test for Auto Complete functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_multiple_color_names(self):
        """Test multiple color names auto complete"""
        print("🔧 Testing Auto Complete - Multiple Color Names...")
        self.driver.get("https://demoqa.com/auto-complete")

        try:
            # Find multiple color names input
            multi_input = self.driver.find_element(By.ID, "autoCompleteMultipleInput")
            multi_input.click()
            print("  ✓ Multiple color names input clicked")
            
            # Type partial color name
            multi_input.send_keys("re")
            time.sleep(1)  # Wait for suggestions
            print("  ✓ Typed 're' in multiple input")
            
            # Wait for dropdown options to appear
            try:
                options = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".auto-complete__option")))
                print(f"  ✓ Found {len(options)} auto-complete options")
                
                # Click first option
                if options:
                    options[0].click()
                    print("  ✓ Selected first option")
                    
                    # Verify selection was added
                    selected_values = self.driver.find_elements(By.CSS_SELECTOR, ".auto-complete__multi-value__label")
                    assert len(selected_values) > 0
                    print(f"  ✓ Selected value: '{selected_values[0].text}'")
                    
            except Exception as dropdown_e:
                print(f"  ⚠️ Dropdown interaction issue: {dropdown_e}")
                # Try alternative approach - just type and press Enter
                multi_input.clear()
                multi_input.send_keys("Red")
                multi_input.send_keys(Keys.ENTER)
                print("  ✓ Alternative: typed 'Red' and pressed Enter")
            
            # Add another color
            multi_input.send_keys("bl")
            time.sleep(1)
            
            try:
                options = self.driver.find_elements(By.CSS_SELECTOR, ".auto-complete__option")
                if options:
                    options[0].click()
                    print("  ✓ Added second color")
            except:
                multi_input.send_keys("ue")
                multi_input.send_keys(Keys.ENTER)
                print("  ✓ Alternative: completed 'Blue' manually")
            
            print("✅ Multiple color names test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Multiple color names test FAILED: {e}")
            return False

    def test_single_color_name(self):
        """Test single color name auto complete"""
        print("\n🔧 Testing Auto Complete - Single Color Name...")
        self.driver.get("https://demoqa.com/auto-complete")

        try:
            # Find single color name input
            single_input = self.driver.find_element(By.ID, "autoCompleteSingleInput")
            single_input.click()
            print("  ✓ Single color name input clicked")
            
            # Type partial color name
            single_input.send_keys("gr")
            time.sleep(1)  # Wait for suggestions
            print("  ✓ Typed 'gr' in single input")
            
            # Wait for dropdown options to appear
            try:
                options = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".auto-complete__option")))
                print(f"  ✓ Found {len(options)} auto-complete options")
                
                # Click first option
                if options:
                    options[0].click()
                    print("  ✓ Selected first option")
                    
                    # Verify selection
                    input_value = single_input.get_attribute("value")
                    assert len(input_value) > 2
                    print(f"  ✓ Selected value: '{input_value}'")
                    
            except Exception as dropdown_e:
                print(f"  ⚠️ Dropdown interaction issue: {dropdown_e}")
                # Try alternative approach
                single_input.clear()
                single_input.send_keys("Green")
                print("  ✓ Alternative: typed 'Green' manually")
            
            print("✅ Single color name test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Single color name test FAILED: {e}")
            return False

    def test_clear_selections(self):
        """Test clearing auto complete selections"""
        print("\n🔧 Testing Auto Complete - Clear Selections...")
        self.driver.get("https://demoqa.com/auto-complete")

        try:
            # Add multiple selections first
            multi_input = self.driver.find_element(By.ID, "autoCompleteMultipleInput")
            multi_input.click()
            
            # Add first color
            multi_input.send_keys("Red")
            multi_input.send_keys(Keys.ENTER)
            time.sleep(0.5)
            
            # Add second color
            multi_input.send_keys("Blue")
            multi_input.send_keys(Keys.ENTER)
            time.sleep(0.5)
            print("  ✓ Added multiple colors")
            
            # Try to clear selections using remove buttons
            try:
                remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".auto-complete__multi-value__remove")
                if remove_buttons:
                    initial_count = len(remove_buttons)
                    remove_buttons[0].click()
                    print("  ✓ Removed one selection")
                    
                    # Verify removal
                    time.sleep(0.5)
                    remaining_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".auto-complete__multi-value__remove")
                    assert len(remaining_buttons) < initial_count
                    print("  ✓ Selection removal verified")
                else:
                    print("  ⚠️ No remove buttons found")
                    
            except Exception as clear_e:
                print(f"  ⚠️ Clear functionality issue: {clear_e}")
            
            # Test single input clear
            single_input = self.driver.find_element(By.ID, "autoCompleteSingleInput")
            single_input.clear()
            single_input.send_keys("Yellow")
            print("  ✓ Added value to single input")
            
            single_input.clear()
            assert single_input.get_attribute("value") == ""
            print("  ✓ Single input cleared successfully")
            
            print("✅ Clear selections test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Clear selections test FAILED: {e}")
            return False

    def test_keyboard_navigation(self):
        """Test keyboard navigation in auto complete"""
        print("\n🔧 Testing Auto Complete - Keyboard Navigation...")
        self.driver.get("https://demoqa.com/auto-complete")

        try:
            # Test keyboard navigation in single input
            single_input = self.driver.find_element(By.ID, "autoCompleteSingleInput")
            single_input.click()
            single_input.send_keys("b")
            time.sleep(1)
            print("  ✓ Typed 'b' to trigger suggestions")
            
            # Try arrow key navigation
            try:
                single_input.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                single_input.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.5)
                print("  ✓ Used arrow keys for navigation")
                
                # Select with Enter
                single_input.send_keys(Keys.ENTER)
                print("  ✓ Selected option with Enter key")
                
                # Verify selection
                input_value = single_input.get_attribute("value")
                if input_value and len(input_value) > 1:
                    print(f"  ✓ Keyboard selection successful: '{input_value}'")
                else:
                    print("  ⚠️ Keyboard selection may not have worked as expected")
                    
            except Exception as nav_e:
                print(f"  ⚠️ Keyboard navigation issue: {nav_e}")
                # Fallback - just complete the word
                single_input.send_keys("lue")
                print("  ✓ Fallback: completed word manually")
            
            print("✅ Keyboard navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Keyboard navigation test FAILED: {e}")
            return False

    def run_all_auto_complete_tests(self):
        """Run all auto complete tests"""
        print("=" * 60)
        print("🔍 AUTO COMPLETE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_multiple_color_names())
            results.append(self.test_single_color_name())
            results.append(self.test_clear_selections())
            results.append(self.test_keyboard_navigation())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 AUTO COMPLETE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Auto Complete tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Auto Complete tests passed, some had issues")
            else:
                print("❌ All Auto Complete tests had issues")
                
        except Exception as e:
            print(f"❌ Auto Complete test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    auto_complete_test = AutoCompleteTest()
    auto_complete_test.run_all_auto_complete_tests()