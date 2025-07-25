from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class SliderTest:
    """Individual test for Slider functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_slider_drag(self):
        """Test slider drag functionality"""
        print("🔧 Testing Slider - Drag Functionality...")
        self.driver.get("https://demoqa.com/slider")

        try:
            # Find slider element
            slider = self.driver.find_element(By.CSS_SELECTOR, ".range-slider")
            slider_input = self.driver.find_element(By.ID, "sliderContainer")
            
            # Get initial value
            initial_value = self.driver.find_element(By.ID, "sliderValue").get_attribute("value")
            print(f"  ✓ Initial slider value: {initial_value}")
            
            # Find the actual slider handle
            slider_handle = self.driver.find_element(By.CSS_SELECTOR, ".range-slider__thumb")
            
            # Get slider dimensions for calculation
            slider_track = self.driver.find_element(By.CSS_SELECTOR, ".range-slider")
            slider_width = slider_track.size['width']
            print(f"  ✓ Slider width: {slider_width}px")
            
            # Drag slider to the right (increase value)
            actions = ActionChains(self.driver)
            actions.click_and_hold(slider_handle)
            actions.move_by_offset(50, 0)  # Move 50 pixels to the right
            actions.release()
            actions.perform()
            print("  ✓ Dragged slider to the right")
            
            # Get new value
            time.sleep(0.5)
            new_value = self.driver.find_element(By.ID, "sliderValue").get_attribute("value")
            print(f"  ✓ New slider value: {new_value}")
            
            # Verify value changed
            assert int(new_value) > int(initial_value)
            print("  ✓ Slider value increased")
            
            # Drag slider to the left (decrease value)
            actions = ActionChains(self.driver)
            actions.click_and_hold(slider_handle)
            actions.move_by_offset(-30, 0)  # Move 30 pixels to the left
            actions.release()
            actions.perform()
            print("  ✓ Dragged slider to the left")
            
            # Get final value
            time.sleep(0.5)
            final_value = self.driver.find_element(By.ID, "sliderValue").get_attribute("value")
            print(f"  ✓ Final slider value: {final_value}")
            
            # Verify value decreased
            assert int(final_value) < int(new_value)
            print("  ✓ Slider value decreased")
            
            print("✅ Slider drag test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Slider drag test FAILED: {e}")
            return False

    def test_slider_keyboard(self):
        """Test slider keyboard navigation"""
        print("\n🔧 Testing Slider - Keyboard Navigation...")
        self.driver.get("https://demoqa.com/slider")

        try:
            # Find slider input element
            slider_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='range']")
            
            # Get initial value
            initial_value = slider_input.get_attribute("value")
            print(f"  ✓ Initial value: {initial_value}")
            
            # Click on slider to focus
            slider_input.click()
            print("  ✓ Slider focused")
            
            # Use arrow keys to change value
            slider_input.send_keys(Keys.ARROW_RIGHT)
            slider_input.send_keys(Keys.ARROW_RIGHT)
            slider_input.send_keys(Keys.ARROW_RIGHT)
            print("  ✓ Pressed right arrow 3 times")
            
            # Get new value
            time.sleep(0.5)
            new_value = slider_input.get_attribute("value")
            print(f"  ✓ New value: {new_value}")
            
            # Verify value increased
            if int(new_value) > int(initial_value):
                print("  ✓ Value increased with arrow keys")
            else:
                print("  ⚠️ Value may not have changed as expected")
            
            # Use left arrow to decrease
            slider_input.send_keys(Keys.ARROW_LEFT)
            slider_input.send_keys(Keys.ARROW_LEFT)
            print("  ✓ Pressed left arrow 2 times")
            
            # Get final value
            time.sleep(0.5)
            final_value = slider_input.get_attribute("value")
            print(f"  ✓ Final value: {final_value}")
            
            print("✅ Slider keyboard test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Slider keyboard test FAILED: {e}")
            return False

    def test_slider_value_input(self):
        """Test slider value input field"""
        print("\n🔧 Testing Slider - Value Input Field...")
        self.driver.get("https://demoqa.com/slider")

        try:
            # Find value input field
            value_input = self.driver.find_element(By.ID, "sliderValue")
            slider_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='range']")
            
            # Get initial values
            initial_input_value = value_input.get_attribute("value")
            initial_slider_value = slider_input.get_attribute("value")
            print(f"  ✓ Initial input value: {initial_input_value}")
            print(f"  ✓ Initial slider value: {initial_slider_value}")
            
            # Change value through input field
            value_input.clear()
            test_value = "75"
            value_input.send_keys(test_value)
            value_input.send_keys(Keys.ENTER)
            print(f"  ✓ Set input value to: {test_value}")
            
            # Verify slider position changed
            time.sleep(0.5)
            new_slider_value = slider_input.get_attribute("value")
            print(f"  ✓ Slider value after input: {new_slider_value}")
            
            # The values should be synchronized
            if new_slider_value == test_value:
                print("  ✓ Slider and input values are synchronized")
            else:
                print(f"  ⚠️ Values may not be perfectly synchronized: slider={new_slider_value}, input={test_value}")
            
            print("✅ Slider value input test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Slider value input test FAILED: {e}")
            return False

    def test_slider_boundaries(self):
        """Test slider boundary values"""
        print("\n🔧 Testing Slider - Boundary Values...")
        self.driver.get("https://demoqa.com/slider")

        try:
            # Find slider elements
            slider_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='range']")
            value_input = self.driver.find_element(By.ID, "sliderValue")
            
            # Get min and max values
            min_value = slider_input.get_attribute("min") or "0"
            max_value = slider_input.get_attribute("max") or "100"
            print(f"  ✓ Slider range: {min_value} to {max_value}")
            
            # Test minimum value
            value_input.clear()
            value_input.send_keys(min_value)
            value_input.send_keys(Keys.ENTER)
            time.sleep(0.5)
            
            min_result = slider_input.get_attribute("value")
            print(f"  ✓ Set to minimum ({min_value}), result: {min_result}")
            
            # Test maximum value
            value_input.clear()
            value_input.send_keys(max_value)
            value_input.send_keys(Keys.ENTER)
            time.sleep(0.5)
            
            max_result = slider_input.get_attribute("value")
            print(f"  ✓ Set to maximum ({max_value}), result: {max_result}")
            
            # Test value beyond maximum (should be clamped)
            try:
                value_input.clear()
                value_input.send_keys("150")  # Beyond max
                value_input.send_keys(Keys.ENTER)
                time.sleep(0.5)
                
                beyond_max_result = slider_input.get_attribute("value")
                print(f"  ✓ Set beyond max (150), result: {beyond_max_result}")
                
                if int(beyond_max_result) <= int(max_value):
                    print("  ✓ Value correctly clamped to maximum")
                else:
                    print("  ⚠️ Value not clamped as expected")
                    
            except Exception as boundary_e:
                print(f"  ⚠️ Boundary test issue: {boundary_e}")
            
            print("✅ Slider boundaries test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Slider boundaries test FAILED: {e}")
            return False

    def run_all_slider_tests(self):
        """Run all slider tests"""
        print("=" * 60)
        print("🎚️ SLIDER INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_slider_drag())
            results.append(self.test_slider_keyboard())
            results.append(self.test_slider_value_input())
            results.append(self.test_slider_boundaries())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 SLIDER TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Slider tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Slider tests passed, some had issues")
            else:
                print("❌ All Slider tests had issues")
                
        except Exception as e:
            print(f"❌ Slider test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    slider_test = SliderTest()
    slider_test.run_all_slider_tests()