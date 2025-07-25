from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class SortableTest:
    """Individual test for Sortable functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_list_sortable(self):
        """Test list sortable functionality"""
        print("🔧 Testing Sortable - List...")
        self.driver.get("https://demoqa.com/sortable")

        try:
            # Get initial list order
            list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            initial_order = [item.text for item in list_items]
            print(f"  ✓ Initial list order: {initial_order}")
            
            # Drag first item to third position
            if len(list_items) >= 3:
                source = list_items[0]
                target = list_items[2]
                
                actions = ActionChains(self.driver)
                actions.drag_and_drop(source, target).perform()
                print("  ✓ Performed drag and drop operation")
                
                time.sleep(1)  # Wait for animation
                
                # Get new order
                updated_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
                new_order = [item.text for item in updated_items]
                print(f"  ✓ New list order: {new_order}")
                
                # Verify order changed
                assert initial_order != new_order, "List order should have changed"
                print("  ✓ List order successfully changed")
            else:
                print("  ⚠️ Not enough list items for drag and drop test")
            
            print("✅ List sortable test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ List sortable test FAILED: {e}")
            return False

    def test_grid_sortable(self):
        """Test grid sortable functionality"""
        print("\n🔧 Testing Sortable - Grid...")
        self.driver.get("https://demoqa.com/sortable")

        try:
            # Click on Grid tab
            grid_tab = self.driver.find_element(By.ID, "demo-tab-grid")
            grid_tab.click()
            print("  ✓ Switched to Grid tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Get initial grid order
            grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
            initial_order = [item.text for item in grid_items]
            print(f"  ✓ Initial grid order: {initial_order}")
            
            # Drag first item to last position
            if len(grid_items) >= 2:
                source = grid_items[0]
                target = grid_items[-1]
                
                actions = ActionChains(self.driver)
                actions.drag_and_drop(source, target).perform()
                print("  ✓ Performed drag and drop operation")
                
                time.sleep(1)  # Wait for animation
                
                # Get new order
                updated_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
                new_order = [item.text for item in updated_items]
                print(f"  ✓ New grid order: {new_order}")
                
                # Verify order changed
                assert initial_order != new_order, "Grid order should have changed"
                print("  ✓ Grid order successfully changed")
            else:
                print("  ⚠️ Not enough grid items for drag and drop test")
            
            print("✅ Grid sortable test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Grid sortable test FAILED: {e}")
            return False

    def test_sortable_interaction(self):
        """Test sortable interaction behavior"""
        print("\n🔧 Testing Sortable - Interaction Behavior...")
        self.driver.get("https://demoqa.com/sortable")

        try:
            # Test hover behavior on list items
            list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            
            if list_items:
                # Hover over first item
                actions = ActionChains(self.driver)
                actions.move_to_element(list_items[0]).perform()
                print("  ✓ Hovered over list item")
                
                # Check if cursor changes (visual feedback)
                cursor_style = list_items[0].value_of_css_property("cursor")
                print(f"  ✓ Cursor style: {cursor_style}")
                
                # Test multiple drag operations
                if len(list_items) >= 4:
                    # Move item from position 0 to position 2
                    actions.drag_and_drop(list_items[0], list_items[2]).perform()
                    time.sleep(0.5)
                    
                    # Get updated items and move another
                    updated_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
                    if len(updated_items) >= 3:
                        actions.drag_and_drop(updated_items[1], updated_items[0]).perform()
                        print("  ✓ Performed multiple drag operations")
                
            print("✅ Sortable interaction test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Sortable interaction test FAILED: {e}")
            return False

    def run_all_sortable_tests(self):
        """Run all sortable tests"""
        print("=" * 60)
        print("🔄 SORTABLE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_list_sortable())
            results.append(self.test_grid_sortable())
            results.append(self.test_sortable_interaction())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 SORTABLE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Sortable tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Sortable tests passed, some had issues")
            else:
                print("❌ All Sortable tests had issues")
                
        except Exception as e:
            print(f"❌ Sortable test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    sortable_test = SortableTest()
    sortable_test.run_all_sortable_tests()