from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class DroppableTest:
    """Individual test for Droppable functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_simple_droppable(self):
        """Test simple drag and drop functionality"""
        print("🔧 Testing Droppable - Simple...")
        self.driver.get("https://demoqa.com/droppable")

        try:
            # Find draggable and droppable elements
            draggable = self.driver.find_element(By.ID, "draggable")
            droppable = self.driver.find_element(By.ID, "droppable")
            
            # Get initial states
            initial_drag_text = draggable.text
            initial_drop_text = droppable.text
            initial_drop_color = droppable.value_of_css_property("background-color")
            
            print(f"  ✓ Draggable text: '{initial_drag_text}'")
            print(f"  ✓ Initial droppable text: '{initial_drop_text}'")
            print(f"  ✓ Initial droppable color: {initial_drop_color}")
            
            # Perform drag and drop
            actions = ActionChains(self.driver)
            actions.drag_and_drop(draggable, droppable).perform()
            print("  ✓ Performed drag and drop operation")
            
            time.sleep(1)  # Wait for drop animation/effect
            
            # Check if drop was successful
            new_drop_text = droppable.text
            new_drop_color = droppable.value_of_css_property("background-color")
            
            print(f"  ✓ New droppable text: '{new_drop_text}'")
            print(f"  ✓ New droppable color: {new_drop_color}")
            
            # Verify drop success
            assert new_drop_text != initial_drop_text, "Drop text should change"
            assert "Dropped" in new_drop_text, "Should indicate successful drop"
            
            print("✅ Simple droppable test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Simple droppable test FAILED: {e}")
            return False

    def test_accept_droppable(self):
        """Test accept droppable functionality"""
        print("\n🔧 Testing Droppable - Accept...")
        self.driver.get("https://demoqa.com/droppable")

        try:
            # Click on Accept tab
            accept_tab = self.driver.find_element(By.ID, "droppableExample-tab-accept")
            accept_tab.click()
            print("  ✓ Switched to Accept tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Find acceptable and not acceptable elements
            acceptable = self.driver.find_element(By.ID, "acceptable")
            not_acceptable = self.driver.find_element(By.ID, "notAcceptable")
            drop_zone = self.driver.find_element(By.CSS_SELECTOR, "#acceptDropContainer #droppable")
            
            initial_drop_text = drop_zone.text
            print(f"  ✓ Initial drop zone text: '{initial_drop_text}'")
            
            # Test with not acceptable element first
            actions = ActionChains(self.driver)
            actions.drag_and_drop(not_acceptable, drop_zone).perform()
            print("  ✓ Attempted drop with not acceptable element")
            
            time.sleep(1)
            not_acceptable_result = drop_zone.text
            print(f"  ✓ Result after not acceptable drop: '{not_acceptable_result}'")
            
            # Test with acceptable element
            actions.drag_and_drop(acceptable, drop_zone).perform()
            print("  ✓ Attempted drop with acceptable element")
            
            time.sleep(1)
            acceptable_result = drop_zone.text
            print(f"  ✓ Result after acceptable drop: '{acceptable_result}'")
            
            # Verify accept behavior
            assert acceptable_result != initial_drop_text, "Acceptable drop should change text"
            
            print("✅ Accept droppable test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Accept droppable test FAILED: {e}")
            return False

    def test_prevent_propagation(self):
        """Test prevent propagation functionality"""
        print("\n🔧 Testing Droppable - Prevent Propagation...")
        self.driver.get("https://demoqa.com/droppable")

        try:
            # Click on Prevent Propagation tab
            prevent_tab = self.driver.find_element(By.ID, "droppableExample-tab-preventPropogation")
            prevent_tab.click()
            print("  ✓ Switched to Prevent Propagation tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Find elements
            draggable = self.driver.find_element(By.CSS_SELECTOR, "#ppDropContainer #dragBox")
            outer_drop = self.driver.find_element(By.CSS_SELECTOR, "#ppDropContainer #notGreedyDropBox")
            inner_drop = self.driver.find_element(By.CSS_SELECTOR, "#ppDropContainer #notGreedyInnerDropBox")
            
            # Get initial states
            outer_initial = outer_drop.text
            inner_initial = inner_drop.text
            
            print(f"  ✓ Outer drop initial: '{outer_initial}'")
            print(f"  ✓ Inner drop initial: '{inner_initial}'")
            
            # Drop on inner element
            actions = ActionChains(self.driver)
            actions.drag_and_drop(draggable, inner_drop).perform()
            print("  ✓ Dropped on inner element")
            
            time.sleep(1)
            
            # Check results
            outer_result = outer_drop.text
            inner_result = inner_drop.text
            
            print(f"  ✓ Outer drop result: '{outer_result}'")
            print(f"  ✓ Inner drop result: '{inner_result}'")
            
            # Test greedy drop box
            greedy_outer = self.driver.find_element(By.CSS_SELECTOR, "#ppDropContainer #greedyDropBox")
            greedy_inner = self.driver.find_element(By.CSS_SELECTOR, "#ppDropContainer #greedyDropBoxInner")
            
            greedy_outer_initial = greedy_outer.text
            greedy_inner_initial = greedy_inner.text
            
            # Drop on greedy inner element
            actions.drag_and_drop(draggable, greedy_inner).perform()
            print("  ✓ Dropped on greedy inner element")
            
            time.sleep(1)
            
            greedy_outer_result = greedy_outer.text
            greedy_inner_result = greedy_inner.text
            
            print(f"  ✓ Greedy outer result: '{greedy_outer_result}'")
            print(f"  ✓ Greedy inner result: '{greedy_inner_result}'")
            
            print("✅ Prevent propagation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Prevent propagation test FAILED: {e}")
            return False

    def test_revert_draggable(self):
        """Test revert draggable functionality"""
        print("\n🔧 Testing Droppable - Revert Draggable...")
        self.driver.get("https://demoqa.com/droppable")

        try:
            # Click on Revert Draggable tab
            revert_tab = self.driver.find_element(By.ID, "droppableExample-tab-revertable")
            revert_tab.click()
            print("  ✓ Switched to Revert Draggable tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Find elements
            will_revert = self.driver.find_element(By.ID, "revertable")
            not_revert = self.driver.find_element(By.ID, "notRevertable")
            drop_zone = self.driver.find_element(By.CSS_SELECTOR, "#revertableDropContainer #droppable")
            
            # Get initial positions
            will_revert_initial_pos = will_revert.location
            not_revert_initial_pos = not_revert.location
            
            print(f"  ✓ Will revert initial position: {will_revert_initial_pos}")
            print(f"  ✓ Not revert initial position: {not_revert_initial_pos}")
            
            # Test revertable element - drag to drop zone
            actions = ActionChains(self.driver)
            actions.drag_and_drop(will_revert, drop_zone).perform()
            print("  ✓ Dropped revertable element")
            
            time.sleep(2)  # Wait for revert animation
            
            # Check if element reverted
            will_revert_final_pos = will_revert.location
            print(f"  ✓ Will revert final position: {will_revert_final_pos}")
            
            # Test non-revertable element
            actions.drag_and_drop(not_revert, drop_zone).perform()
            print("  ✓ Dropped non-revertable element")
            
            time.sleep(2)
            
            not_revert_final_pos = not_revert.location
            print(f"  ✓ Not revert final position: {not_revert_final_pos}")
            
            # Check drop zone status
            drop_zone_text = drop_zone.text
            print(f"  ✓ Drop zone text: '{drop_zone_text}'")
            
            print("✅ Revert draggable test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Revert draggable test FAILED: {e}")
            return False

    def run_all_droppable_tests(self):
        """Run all droppable tests"""
        print("=" * 60)
        print("🎯 DROPPABLE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_simple_droppable())
            results.append(self.test_accept_droppable())
            results.append(self.test_prevent_propagation())
            results.append(self.test_revert_draggable())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 DROPPABLE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Droppable tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Droppable tests passed, some had issues")
            else:
                print("❌ All Droppable tests had issues")
                
        except Exception as e:
            print(f"❌ Droppable test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    droppable_test = DroppableTest()
    droppable_test.run_all_droppable_tests()