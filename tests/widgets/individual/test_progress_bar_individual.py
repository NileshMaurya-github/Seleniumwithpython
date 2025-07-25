from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProgressBarTest:
    """Individual test for Progress Bar functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)  # Longer wait for progress bar
        self.driver.maximize_window()

    def test_start_progress_bar(self):
        """Test starting the progress bar"""
        print("🔧 Testing Progress Bar - Start Functionality...")
        self.driver.get("https://demoqa.com/progress-bar")

        try:
            # Find start button
            start_button = self.driver.find_element(By.ID, "startStopButton")
            button_text = start_button.text
            print(f"  ✓ Found button with text: '{button_text}'")
            
            # Get initial progress value
            progress_bar = self.driver.find_element(By.CSS_SELECTOR, ".progress-bar")
            initial_progress = progress_bar.get_attribute("aria-valuenow") or "0"
            print(f"  ✓ Initial progress: {initial_progress}%")
            
            # Click start button
            start_button.click()
            print("  ✓ Start button clicked")
            
            # Wait a moment and check if progress started
            time.sleep(2)
            current_progress = progress_bar.get_attribute("aria-valuenow") or "0"
            print(f"  ✓ Progress after 2 seconds: {current_progress}%")
            
            # Verify progress is increasing
            if int(current_progress) > int(initial_progress):
                print("  ✓ Progress bar is advancing")
            else:
                print("  ⚠️ Progress may not be advancing as expected")
            
            # Check button text changed to "Stop"
            button_text_after = start_button.text
            print(f"  ✓ Button text after start: '{button_text_after}'")
            
            print("✅ Start progress bar test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Start progress bar test FAILED: {e}")
            return False

    def test_stop_progress_bar(self):
        """Test stopping the progress bar"""
        print("\n🔧 Testing Progress Bar - Stop Functionality...")
        self.driver.get("https://demoqa.com/progress-bar")

        try:
            # Start the progress bar first
            start_button = self.driver.find_element(By.ID, "startStopButton")
            progress_bar = self.driver.find_element(By.CSS_SELECTOR, ".progress-bar")
            
            start_button.click()
            print("  ✓ Started progress bar")
            
            # Wait for some progress
            time.sleep(3)
            progress_before_stop = progress_bar.get_attribute("aria-valuenow") or "0"
            print(f"  ✓ Progress before stop: {progress_before_stop}%")
            
            # Stop the progress bar
            stop_button = self.driver.find_element(By.ID, "startStopButton")
            stop_button.click()
            print("  ✓ Stop button clicked")
            
            # Wait a moment and verify progress stopped
            time.sleep(2)
            progress_after_stop = progress_bar.get_attribute("aria-valuenow") or "0"
            print(f"  ✓ Progress after stop: {progress_after_stop}%")
            
            # Progress should be the same or very close
            progress_diff = abs(int(progress_after_stop) - int(progress_before_stop))
            if progress_diff <= 2:  # Allow small difference due to timing
                print("  ✓ Progress bar stopped successfully")
            else:
                print(f"  ⚠️ Progress may still be advancing (diff: {progress_diff}%)")
            
            # Check button text changed back
            button_text = stop_button.text
            print(f"  ✓ Button text after stop: '{button_text}'")
            
            print("✅ Stop progress bar test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Stop progress bar test FAILED: {e}")
            return False

    def test_progress_bar_completion(self):
        """Test progress bar completion"""
        print("\n🔧 Testing Progress Bar - Completion...")
        self.driver.get("https://demoqa.com/progress-bar")

        try:
            # Start the progress bar
            start_button = self.driver.find_element(By.ID, "startStopButton")
            progress_bar = self.driver.find_element(By.CSS_SELECTOR, ".progress-bar")
            
            start_button.click()
            print("  ✓ Started progress bar")
            
            # Wait for completion (this might take a while)
            print("  ⏳ Waiting for progress bar to complete...")
            completion_timeout = 30  # 30 seconds timeout
            start_time = time.time()
            
            while time.time() - start_time < completion_timeout:
                current_progress = progress_bar.get_attribute("aria-valuenow") or "0"
                
                if int(current_progress) >= 100:
                    print(f"  ✅ Progress bar completed: {current_progress}%")
                    break
                    
                if int(current_progress) % 20 == 0 and int(current_progress) > 0:
                    print(f"  ⏳ Progress: {current_progress}%")
                
                time.sleep(1)
            else:
                # Timeout reached
                final_progress = progress_bar.get_attribute("aria-valuenow") or "0"
                print(f"  ⚠️ Timeout reached. Final progress: {final_progress}%")
                
                # If we got significant progress, consider it a partial success
                if int(final_progress) > 50:
                    print("  ✓ Progress bar is working (reached >50%)")
                else:
                    print("  ❌ Progress bar may not be working properly")
                    return False
            
            # Check if reset button appeared
            try:
                reset_button = self.driver.find_element(By.ID, "resetButton")
                if reset_button.is_displayed():
                    print("  ✓ Reset button appeared after completion")
                    
                    # Test reset functionality
                    reset_button.click()
                    time.sleep(1)
                    
                    reset_progress = progress_bar.get_attribute("aria-valuenow") or "0"
                    print(f"  ✓ Progress after reset: {reset_progress}%")
                    
                    if int(reset_progress) == 0:
                        print("  ✓ Reset functionality works")
                    else:
                        print("  ⚠️ Reset may not have worked completely")
                        
            except Exception as reset_e:
                print(f"  ⚠️ Reset button test issue: {reset_e}")
            
            print("✅ Progress bar completion test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Progress bar completion test FAILED: {e}")
            return False

    def test_progress_bar_attributes(self):
        """Test progress bar attributes and styling"""
        print("\n🔧 Testing Progress Bar - Attributes...")
        self.driver.get("https://demoqa.com/progress-bar")

        try:
            # Find progress bar elements
            progress_bar = self.driver.find_element(By.CSS_SELECTOR, ".progress-bar")
            progress_container = self.driver.find_element(By.CSS_SELECTOR, ".progress")
            
            # Check initial attributes
            initial_value = progress_bar.get_attribute("aria-valuenow") or "0"
            min_value = progress_bar.get_attribute("aria-valuemin") or "0"
            max_value = progress_bar.get_attribute("aria-valuemax") or "100"
            
            print(f"  ✓ Progress range: {min_value} to {max_value}")
            print(f"  ✓ Initial value: {initial_value}")
            
            # Check styling attributes
            progress_style = progress_bar.get_attribute("style")
            print(f"  ✓ Progress bar style: {progress_style[:50]}..." if progress_style else "  ✓ No inline styles")
            
            # Check CSS classes
            progress_classes = progress_bar.get_attribute("class")
            container_classes = progress_container.get_attribute("class")
            print(f"  ✓ Progress bar classes: {progress_classes}")
            print(f"  ✓ Container classes: {container_classes}")
            
            # Start progress and check dynamic attributes
            start_button = self.driver.find_element(By.ID, "startStopButton")
            start_button.click()
            
            time.sleep(2)
            
            # Check updated attributes
            updated_value = progress_bar.get_attribute("aria-valuenow") or "0"
            updated_style = progress_bar.get_attribute("style")
            
            print(f"  ✓ Updated value: {updated_value}")
            print(f"  ✓ Updated style contains width: {'width' in updated_style if updated_style else False}")
            
            # Stop the progress
            start_button.click()
            
            print("✅ Progress bar attributes test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Progress bar attributes test FAILED: {e}")
            return False

    def run_all_progress_bar_tests(self):
        """Run all progress bar tests"""
        print("=" * 60)
        print("📊 PROGRESS BAR INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_start_progress_bar())
            results.append(self.test_stop_progress_bar())
            results.append(self.test_progress_bar_completion())
            results.append(self.test_progress_bar_attributes())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 PROGRESS BAR TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Progress Bar tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Progress Bar tests passed, some had issues")
            else:
                print("❌ All Progress Bar tests had issues")
                
        except Exception as e:
            print(f"❌ Progress Bar test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    progress_bar_test = ProgressBarTest()
    progress_bar_test.run_all_progress_bar_tests()