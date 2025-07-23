from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class DemoQAInteractions:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_sortable(self):
        """Test Sortable functionality"""
        print("Testing Sortable...")
        self.driver.get("https://demoqa.com/sortable")

        actions = ActionChains(self.driver)

        # Test List tab (default)
        list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
        
        # Get initial order
        initial_order = [item.text for item in list_items]
        print(f"  Initial order: {initial_order}")

        # Drag first item to third position
        source = list_items[0]
        target = list_items[2]
        actions.drag_and_drop(source, target).perform()
        time.sleep(1)

        # Verify order changed
        updated_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
        updated_order = [item.text for item in updated_items]
        print(f"  Updated order: {updated_order}")

        assert initial_order != updated_order
        print("  ✓ List sortable tested")

        # Test Grid tab
        grid_tab = self.driver.find_element(By.ID, "demo-tab-grid")
        grid_tab.click()
        time.sleep(1)

        grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
        
        # Drag first grid item to last position
        if len(grid_items) >= 2:
            source = grid_items[0]
            target = grid_items[-1]
            actions.drag_and_drop(source, target).perform()
            time.sleep(1)
            print("  ✓ Grid sortable tested")

        print("✓ Sortable test passed")

    def test_selectable(self):
        """Test Selectable functionality"""
        print("Testing Selectable...")
        self.driver.get("https://demoqa.com/selectable")

        # Test List tab (default)
        list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
        
        # Select first item
        list_items[0].click()
        time.sleep(0.5)
        
        # Verify item is selected
        assert "active" in list_items[0].get_attribute("class")
        print("  ✓ First list item selected")

        # Select multiple items with Ctrl
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(list_items[2]).key_up(Keys.CONTROL).perform()
        time.sleep(0.5)

        # Verify multiple selection
        selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
        assert len(selected_items) >= 2
        print(f"  ✓ Multiple items selected: {len(selected_items)}")

        # Test Grid tab
        grid_tab = self.driver.find_element(By.ID, "demo-tab-grid")
        grid_tab.click()
        time.sleep(1)

        grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
        
        # Select grid items
        grid_items[0].click()
        time.sleep(0.5)
        
        actions.key_down(Keys.CONTROL).click(grid_items[1]).key_up(Keys.CONTROL).perform()
        time.sleep(0.5)

        selected_grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item.active")
        print(f"  ✓ Grid items selected: {len(selected_grid_items)}")

        print("✓ Selectable test passed")

    def test_resizable(self):
        """Test Resizable functionality"""
        print("Testing Resizable...")
        self.driver.get("https://demoqa.com/resizable")

        actions = ActionChains(self.driver)

        # Test resizable box with restriction
        resizable_box = self.driver.find_element(By.ID, "resizableBoxWithRestriction")
        resize_handle = self.driver.find_element(By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")

        # Get initial size
        initial_size = resizable_box.size
        print(f"  Initial restricted box size: {initial_size}")

        # Resize the box
        actions.click_and_hold(resize_handle).move_by_offset(50, 30).release().perform()
        time.sleep(1)

        # Get new size
        new_size = resizable_box.size
        print(f"  New restricted box size: {new_size}")

        assert new_size != initial_size
        print("  ✓ Restricted resizable box tested")

        # Test resizable box without restriction
        resizable_box2 = self.driver.find_element(By.ID, "resizable")
        resize_handle2 = self.driver.find_element(By.CSS_SELECTOR, "#resizable .react-resizable-handle")

        # Get initial size
        initial_size2 = resizable_box2.size
        print(f"  Initial unrestricted box size: {initial_size2}")

        # Resize the box
        actions.click_and_hold(resize_handle2).move_by_offset(100, 50).release().perform()
        time.sleep(1)

        # Get new size
        new_size2 = resizable_box2.size
        print(f"  New unrestricted box size: {new_size2}")

        assert new_size2 != initial_size2
        print("  ✓ Unrestricted resizable box tested")

        print("✓ Resizable test passed")

    def test_droppable(self):
        """Test Droppable functionality"""
        print("Testing Droppable...")
        self.driver.get("https://demoqa.com/droppable")

        actions = ActionChains(self.driver)

        # Test Simple tab (default)
        draggable = self.driver.find_element(By.ID, "draggable")
        droppable = self.driver.find_element(By.ID, "droppable")

        # Get initial droppable text
        initial_text = droppable.text
        print(f"  Initial droppable text: {initial_text}")

        # Perform drag and drop
        actions.drag_and_drop(draggable, droppable).perform()
        time.sleep(1)

        # Verify drop was successful
        dropped_text = droppable.text
        print(f"  After drop text: {dropped_text}")
        assert "Dropped!" in dropped_text
        print("  ✓ Simple drag and drop tested")

        # Test Accept tab
        accept_tab = self.driver.find_element(By.ID, "droppableExample-tab-accept")
        accept_tab.click()
        time.sleep(1)

        acceptable = self.driver.find_element(By.ID, "acceptable")
        not_acceptable = self.driver.find_element(By.ID, "notAcceptable")
        drop_box = self.driver.find_element(By.CSS_SELECTOR, "#acceptDropContainer #droppable")

        # Try dropping acceptable item
        actions.drag_and_drop(acceptable, drop_box).perform()
        time.sleep(1)

        drop_text = drop_box.text
        print(f"  Acceptable drop result: {drop_text}")

        # Try dropping not acceptable item
        actions.drag_and_drop(not_acceptable, drop_box).perform()
        time.sleep(1)

        print("  ✓ Accept tab tested")

        # Test Prevent Propagation tab
        prevent_tab = self.driver.find_element(By.ID, "droppableExample-tab-preventPropogation")
        prevent_tab.click()
        time.sleep(1)

        drag_me = self.driver.find_element(By.ID, "dragBox")
        outer_drop = self.driver.find_element(By.ID, "notGreedyDropBox")

        actions.drag_and_drop(drag_me, outer_drop).perform()
        time.sleep(1)
        print("  ✓ Prevent Propagation tab tested")

        # Test Revert Draggable tab
        revert_tab = self.driver.find_element(By.ID, "droppableExample-tab-revertable")
        revert_tab.click()
        time.sleep(1)

        will_revert = self.driver.find_element(By.ID, "revertable")
        not_revert = self.driver.find_element(By.ID, "notRevertable")
        revert_drop = self.driver.find_element(By.CSS_SELECTOR, "#revertableDropContainer #droppable")

        # Test revertable drag
        actions.drag_and_drop(will_revert, revert_drop).perform()
        time.sleep(2)  # Wait for revert animation

        print("  ✓ Revert Draggable tab tested")

        print("✓ Droppable test passed")

    def test_dragabble(self):
        """Test Dragabble functionality"""
        print("Testing Dragabble...")
        self.driver.get("https://demoqa.com/dragabble")

        actions = ActionChains(self.driver)

        # Test Simple tab (default)
        simple_drag = self.driver.find_element(By.ID, "dragBox")
        
        # Get initial position
        initial_location = simple_drag.location
        print(f"  Initial position: {initial_location}")

        # Drag the element
        actions.click_and_hold(simple_drag).move_by_offset(100, 50).release().perform()
        time.sleep(1)

        # Get new position
        new_location = simple_drag.location
        print(f"  New position: {new_location}")

        assert new_location != initial_location
        print("  ✓ Simple drag tested")

        # Test Axis Restricted tab
        axis_tab = self.driver.find_element(By.ID, "draggableExample-tab-axisRestriction")
        axis_tab.click()
        time.sleep(1)

        # Test X-axis restricted drag
        x_restricted = self.driver.find_element(By.ID, "restrictedX")
        initial_x_pos = x_restricted.location
        
        actions.click_and_hold(x_restricted).move_by_offset(100, 0).release().perform()
        time.sleep(1)
        
        new_x_pos = x_restricted.location
        print(f"  X-restricted drag: {initial_x_pos} -> {new_x_pos}")

        # Test Y-axis restricted drag
        y_restricted = self.driver.find_element(By.ID, "restrictedY")
        initial_y_pos = y_restricted.location
        
        actions.click_and_hold(y_restricted).move_by_offset(0, 50).release().perform()
        time.sleep(1)
        
        new_y_pos = y_restricted.location
        print(f"  Y-restricted drag: {initial_y_pos} -> {new_y_pos}")

        print("  ✓ Axis restricted drag tested")

        # Test Container Restricted tab
        container_tab = self.driver.find_element(By.ID, "draggableExample-tab-containerRestriction")
        container_tab.click()
        time.sleep(1)

        # Test container restricted drag
        container_restricted = self.driver.find_element(By.CSS_SELECTOR, "#containmentWrapper .draggable")
        
        actions.click_and_hold(container_restricted).move_by_offset(50, 30).release().perform()
        time.sleep(1)
        
        print("  ✓ Container restricted drag tested")

        print("✓ Dragabble test passed")

    def run_all_tests(self):
        """Run all interaction tests"""
        try:
            self.test_sortable()
            self.test_selectable()
            self.test_resizable()
            self.test_droppable()
            self.test_dragabble()
            print("\n✅ All Interactions tests completed successfully!")
        except Exception as e:
            print(f"\n❌ Test failed: {str(e)}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    interactions_test = DemoQAInteractions()
    interactions_test.run_all_tests()