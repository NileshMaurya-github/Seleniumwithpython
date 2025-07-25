from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class SelectableTest:
    """Individual test for Selectable functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_list_selectable(self):
        """Test list selectable functionality"""
        print("🔧 Testing Selectable - List...")
        self.driver.get("https://demoqa.com/selectable")

        try:
            # Get list items
            list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            print(f"  ✓ Found {len(list_items)} list items")
            
            if list_items:
                # Click first item to select it
                list_items[0].click()
                print("  ✓ Clicked first item")
                
                # Check if item is selected (has active class)
                time.sleep(0.5)
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                assert len(selected_items) > 0, "At least one item should be selected"
                print(f"  ✓ {len(selected_items)} item(s) selected")
                
                # Select multiple items with Ctrl+Click
                if len(list_items) >= 3:
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.CONTROL).click(list_items[2]).key_up(Keys.CONTROL).perform()
                    print("  ✓ Performed Ctrl+Click for multiple selection")
                    
                    time.sleep(0.5)
                    selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                    print(f"  ✓ {len(selected_items)} item(s) now selected")
                
                # Click on empty area to deselect
                empty_area = self.driver.find_element(By.CSS_SELECTOR, "#demo-tabpane-list")
                empty_area.click()
                print("  ✓ Clicked empty area to deselect")
            
            print("✅ List selectable test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ List selectable test FAILED: {e}")
            return False

    def test_grid_selectable(self):
        """Test grid selectable functionality"""
        print("\n🔧 Testing Selectable - Grid...")
        self.driver.get("https://demoqa.com/selectable")

        try:
            # Click on Grid tab
            grid_tab = self.driver.find_element(By.ID, "demo-tab-grid")
            grid_tab.click()
            print("  ✓ Switched to Grid tab")
            
            time.sleep(1)  # Wait for tab to load
            
            # Get grid items
            grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
            print(f"  ✓ Found {len(grid_items)} grid items")
            
            if grid_items:
                # Select first grid item
                grid_items[0].click()
                print("  ✓ Clicked first grid item")
                
                time.sleep(0.5)
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item.active")
                assert len(selected_items) > 0, "At least one grid item should be selected"
                print(f"  ✓ {len(selected_items)} grid item(s) selected")
                
                # Select multiple grid items
                if len(grid_items) >= 4:
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.CONTROL).click(grid_items[3]).key_up(Keys.CONTROL).perform()
                    print("  ✓ Performed Ctrl+Click on grid item")
                    
                    time.sleep(0.5)
                    selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item.active")
                    print(f"  ✓ {len(selected_items)} grid item(s) now selected")
            
            print("✅ Grid selectable test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Grid selectable test FAILED: {e}")
            return False

    def test_selection_behavior(self):
        """Test selection behavior and visual feedback"""
        print("\n🔧 Testing Selectable - Selection Behavior...")
        self.driver.get("https://demoqa.com/selectable")

        try:
            # Test single selection behavior
            list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            
            if len(list_items) >= 3:
                # Select first item
                list_items[0].click()
                time.sleep(0.3)
                
                # Check background color change (visual feedback)
                selected_item = self.driver.find_element(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                bg_color = selected_item.value_of_css_property("background-color")
                print(f"  ✓ Selected item background color: {bg_color}")
                
                # Select another item (should deselect previous if single selection)
                list_items[1].click()
                time.sleep(0.3)
                
                # Check how many items are selected
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                print(f"  ✓ After single click: {len(selected_items)} item(s) selected")
                
                # Test range selection with Shift+Click
                actions = ActionChains(self.driver)
                actions.key_down(Keys.SHIFT).click(list_items[2]).key_up(Keys.SHIFT).perform()
                print("  ✓ Performed Shift+Click for range selection")
                
                time.sleep(0.5)
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                print(f"  ✓ After range selection: {len(selected_items)} item(s) selected")
            
            print("✅ Selection behavior test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Selection behavior test FAILED: {e}")
            return False

    def test_keyboard_navigation(self):
        """Test keyboard navigation in selectable"""
        print("\n🔧 Testing Selectable - Keyboard Navigation...")
        self.driver.get("https://demoqa.com/selectable")

        try:
            # Focus on first item
            list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            
            if list_items:
                # Click to focus and select first item
                list_items[0].click()
                print("  ✓ Focused on first item")
                
                # Try arrow key navigation
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                print("  ✓ Pressed Arrow Down key")
                
                time.sleep(0.5)
                
                # Check if focus moved (this might not work on all implementations)
                focused_element = self.driver.switch_to.active_element
                print(f"  ✓ Active element tag: {focused_element.tag_name}")
                
                # Test Space key for selection
                actions.send_keys(Keys.SPACE).perform()
                print("  ✓ Pressed Space key")
                
                time.sleep(0.5)
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                print(f"  ✓ Items selected after keyboard interaction: {len(selected_items)}")
            
            print("✅ Keyboard navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Keyboard navigation test FAILED: {e}")
            return False

    def run_all_selectable_tests(self):
        """Run all selectable tests"""
        print("=" * 60)
        print("👆 SELECTABLE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_list_selectable())
            results.append(self.test_grid_selectable())
            results.append(self.test_selection_behavior())
            results.append(self.test_keyboard_navigation())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 SELECTABLE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Selectable tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Selectable tests passed, some had issues")
            else:
                print("❌ All Selectable tests had issues")
                
        except Exception as e:
            print(f"❌ Selectable test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    selectable_test = SelectableTest()
    selectable_test.run_all_selectable_tests()