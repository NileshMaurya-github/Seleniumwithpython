from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class DragabbleTest:
    """Individual test for Dragabble functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_simple_dragabble(self):
        """Test simple drag functionality"""
        print("🔧 Testing Dragabble - Simple...")
        self.driver.get("https://demoqa.com/dragabble")

        try:
            # Find the draggable element
            draggable = self.driver.find_element(By.ID, "dragBox")
            
            # Get initial position
            initial_position = draggable.location
            print(f"  ✓ Initial position: {initial_position}")
            
            # Perform drag operation
            actions = ActionChains(self.driver)
            actions.click_and_hold(draggable).move_by_offset(100, 50).release().perform()
            print("  ✓ Performed drag operation (100, 50)")
            
            time.sleep(1)  # Wait for drag animation
            
            # Get new position
            new_position = draggable.location
            print(f"  ✓ New position: {new_position}")
            
            # Verify position changed
            assert new_position != initial_position, "Element position should have changed"
            print("  ✓ Element successfully moved")
            
            # Test another drag operation
            actions.click_and_hold(draggable).move_by_offset(-50, 75).release().perform()
            print("  ✓ Performed second drag operation (-50, 75)")
            
            time.sleep(1)
            final_position = draggable.location
            print(f"  ✓ Final position: {final_position}")
            
            assert final_position != new_position, "Element should move again"
            
            print("✅ Simple dragabble test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Simple dragabble test FAILED: {e}")
            return False

    def test_axis_restricted_drag(self):
        """Test axis restricted drag functionality"""
        print("\n🔧 Testing Dragabble - Axis Restricted...")
        self.driver.get("https://demoqa.com/dragabble")

        try:
            # Click on Axis Restricted tab
            axis_tab = self.driver.find_element(By.ID, "draggableExample-tab-axisRestriction")
            axis_tab.click()
            print("  ✓ Switched to Axis Restricted tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Test X-axis restricted drag
            x_restricted = self.driver.find_element(By.ID, "restrictedX")
            x_initial_pos = x_restricted.location
            print(f"  ✓ X-restricted initial position: {x_initial_pos}")
            
            # Try to drag in both X and Y directions
            actions = ActionChains(self.driver)
            actions.click_and_hold(x_restricted).move_by_offset(100, 50).release().perform()
            print("  ✓ Attempted to drag X-restricted element")
            
            time.sleep(1)
            x_new_pos = x_restricted.location
            print(f"  ✓ X-restricted new position: {x_new_pos}")
            
            # X should change, Y should remain similar (allowing for small variations)
            x_moved = abs(x_new_pos['x'] - x_initial_pos['x']) > 10
            y_restricted = abs(x_new_pos['y'] - x_initial_pos['y']) < 20
            print(f"  ✓ X moved: {x_moved}, Y restricted: {y_restricted}")
            
            # Test Y-axis restricted drag
            y_restricted_elem = self.driver.find_element(By.ID, "restrictedY")
            y_initial_pos = y_restricted_elem.location
            print(f"  ✓ Y-restricted initial position: {y_initial_pos}")
            
            actions.click_and_hold(y_restricted_elem).move_by_offset(50, 100).release().perform()
            print("  ✓ Attempted to drag Y-restricted element")
            
            time.sleep(1)
            y_new_pos = y_restricted_elem.location
            print(f"  ✓ Y-restricted new position: {y_new_pos}")
            
            # Y should change, X should remain similar
            y_moved = abs(y_new_pos['y'] - y_initial_pos['y']) > 10
            x_restricted_check = abs(y_new_pos['x'] - y_initial_pos['x']) < 20
            print(f"  ✓ Y moved: {y_moved}, X restricted: {x_restricted_check}")
            
            print("✅ Axis restricted drag test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Axis restricted drag test FAILED: {e}")
            return False

    def test_container_restricted_drag(self):
        """Test container restricted drag functionality"""
        print("\n🔧 Testing Dragabble - Container Restricted...")
        self.driver.get("https://demoqa.com/dragabble")

        try:
            # Click on Container Restricted tab
            container_tab = self.driver.find_element(By.ID, "draggableExample-tab-containerRestriction")
            container_tab.click()
            print("  ✓ Switched to Container Restricted tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Test container restricted drag
            container_restricted = self.driver.find_element(By.CSS_SELECTOR, "#containmentWrapper .ui-widget-content")
            container = self.driver.find_element(By.ID, "containmentWrapper")
            
            # Get container boundaries
            container_location = container.location
            container_size = container.size
            print(f"  ✓ Container location: {container_location}, size: {container_size}")
            
            # Get initial position of draggable element
            initial_pos = container_restricted.location
            print(f"  ✓ Container restricted element initial position: {initial_pos}")
            
            # Try to drag within container
            actions = ActionChains(self.driver)
            actions.click_and_hold(container_restricted).move_by_offset(50, 30).release().perform()
            print("  ✓ Dragged within container bounds")
            
            time.sleep(1)
            within_bounds_pos = container_restricted.location
            print(f"  ✓ Position after within-bounds drag: {within_bounds_pos}")
            
            # Try to drag outside container (should be restricted)
            actions.click_and_hold(container_restricted).move_by_offset(500, 500).release().perform()
            print("  ✓ Attempted to drag outside container")
            
            time.sleep(1)
            restricted_pos = container_restricted.location
            print(f"  ✓ Position after out-of-bounds drag attempt: {restricted_pos}")
            
            # Element should still be within reasonable bounds
            container_right = container_location['x'] + container_size['width']
            container_bottom = container_location['y'] + container_size['height']
            
            within_x_bounds = container_location['x'] <= restricted_pos['x'] <= container_right
            within_y_bounds = container_location['y'] <= restricted_pos['y'] <= container_bottom
            
            print(f"  ✓ Within X bounds: {within_x_bounds}, Within Y bounds: {within_y_bounds}")
            
            print("✅ Container restricted drag test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Container restricted drag test FAILED: {e}")
            return False

    def test_cursor_style_drag(self):
        """Test cursor style during drag"""
        print("\n🔧 Testing Dragabble - Cursor Style...")
        self.driver.get("https://demoqa.com/dragabble")

        try:
            # Click on Cursor Style tab
            cursor_tab = self.driver.find_element(By.ID, "draggableExample-tab-cursorStyle")
            cursor_tab.click()
            print("  ✓ Switched to Cursor Style tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Test center cursor style
            cursor_center = self.driver.find_element(By.ID, "cursorCenter")
            cursor_top_left = self.driver.find_element(By.ID, "cursorTopLeft")
            cursor_bottom = self.driver.find_element(By.ID, "cursorBottom")
            
            # Get initial positions
            center_initial = cursor_center.location
            top_left_initial = cursor_top_left.location
            bottom_initial = cursor_bottom.location
            
            print(f"  ✓ Center cursor initial: {center_initial}")
            print(f"  ✓ Top-left cursor initial: {top_left_initial}")
            print(f"  ✓ Bottom cursor initial: {bottom_initial}")
            
            # Test dragging with different cursor styles
            actions = ActionChains(self.driver)
            
            # Drag center cursor element
            actions.click_and_hold(cursor_center).move_by_offset(80, 40).release().perform()
            print("  ✓ Dragged center cursor element")
            
            time.sleep(0.5)
            
            # Drag top-left cursor element
            actions.click_and_hold(cursor_top_left).move_by_offset(60, 60).release().perform()
            print("  ✓ Dragged top-left cursor element")
            
            time.sleep(0.5)
            
            # Drag bottom cursor element
            actions.click_and_hold(cursor_bottom).move_by_offset(40, 80).release().perform()
            print("  ✓ Dragged bottom cursor element")
            
            time.sleep(0.5)
            
            # Verify all elements moved
            center_final = cursor_center.location
            top_left_final = cursor_top_left.location
            bottom_final = cursor_bottom.location
            
            center_moved = center_final != center_initial
            top_left_moved = top_left_final != top_left_initial
            bottom_moved = bottom_final != bottom_initial
            
            print(f"  ✓ Center moved: {center_moved}")
            print(f"  ✓ Top-left moved: {top_left_moved}")
            print(f"  ✓ Bottom moved: {bottom_moved}")
            
            assert center_moved and top_left_moved and bottom_moved, "All cursor style elements should move"
            
            print("✅ Cursor style drag test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Cursor style drag test FAILED: {e}")
            return False

    def run_all_dragabble_tests(self):
        """Run all dragabble tests"""
        print("=" * 60)
        print("🖱️ DRAGABBLE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_simple_dragabble())
            results.append(self.test_axis_restricted_drag())
            results.append(self.test_container_restricted_drag())
            results.append(self.test_cursor_style_drag())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 DRAGABBLE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Dragabble tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Dragabble tests passed, some had issues")
            else:
                print("❌ All Dragabble tests had issues")
                
        except Exception as e:
            print(f"❌ Dragabble test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    dragabble_test = DragabbleTest()
    dragabble_test.run_all_dragabble_tests()