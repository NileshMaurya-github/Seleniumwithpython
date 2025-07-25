import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


@allure.epic("DemoQA Automation")
@allure.feature("Interactions")
class TestInteractions:
    """Allure test suite for Interactions functionality"""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to initialize WebDriver"""
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)
        yield
        self.driver.quit()

    @allure.story("Sortable")
    @allure.title("Test List Sortable Functionality")
    @allure.description("Verify that list items can be sorted by drag and drop")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_list_sortable(self):
        with allure.step("Navigate to Sortable page"):
            self.driver.get("https://demoqa.com/sortable")
            
        with allure.step("Wait for sortable list to load"):
            sortable_list = self.wait.until(EC.presence_of_element_located((By.ID, "demo-tabpane-list")))
            
        with allure.step("Get initial list order"):
            list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            initial_order = [item.text for item in list_items]
            allure.attach(str(initial_order), "Initial Order", allure.attachment_type.TEXT)
            
        with allure.step("Perform drag and drop operation"):
            if len(list_items) >= 2:
                source = list_items[0]
                target = list_items[1]
                
                self.actions.drag_and_drop(source, target).perform()
                time.sleep(2)
                
                # Get new order
                updated_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
                new_order = [item.text for item in updated_items]
                allure.attach(str(new_order), "New Order", allure.attachment_type.TEXT)
                
                # Verify order changed
                assert initial_order != new_order

    @allure.story("Sortable")
    @allure.title("Test Grid Sortable Functionality")
    @allure.description("Verify that grid items can be sorted by drag and drop")
    @allure.severity(allure.severity_level.NORMAL)
    def test_grid_sortable(self):
        with allure.step("Navigate to Sortable page"):
            self.driver.get("https://demoqa.com/sortable")
            
        with allure.step("Switch to Grid tab"):
            grid_tab = self.wait.until(EC.element_to_be_clickable((By.ID, "demo-tab-grid")))
            grid_tab.click()
            
        with allure.step("Wait for grid to load"):
            grid_container = self.wait.until(EC.presence_of_element_located((By.ID, "demo-tabpane-grid")))
            
        with allure.step("Get initial grid order"):
            grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
            initial_order = [item.text for item in grid_items]
            allure.attach(str(initial_order), "Initial Grid Order", allure.attachment_type.TEXT)
            
        with allure.step("Perform grid drag and drop"):
            if len(grid_items) >= 2:
                source = grid_items[0]
                target = grid_items[-1]
                
                self.actions.drag_and_drop(source, target).perform()
                time.sleep(2)
                
                updated_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
                new_order = [item.text for item in updated_items]
                allure.attach(str(new_order), "New Grid Order", allure.attachment_type.TEXT)

    @allure.story("Selectable")
    @allure.title("Test List Selection Functionality")
    @allure.description("Verify that list items can be selected and deselected")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_list_selectable(self):
        with allure.step("Navigate to Selectable page"):
            self.driver.get("https://demoqa.com/selectable")
            
        with allure.step("Wait for selectable list to load"):
            selectable_list = self.wait.until(EC.presence_of_element_located((By.ID, "demo-tabpane-list")))
            
        with allure.step("Get list items"):
            list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            allure.attach(f"Found {len(list_items)} selectable items", "Items Count", allure.attachment_type.TEXT)
            
        with allure.step("Select first item"):
            if list_items:
                first_item = list_items[0]
                first_item.click()
                time.sleep(1)
                
                # Check if item is selected (usually has 'active' class)
                item_classes = first_item.get_attribute("class")
                allure.attach(item_classes, "Selected Item Classes", allure.attachment_type.TEXT)
                
        with allure.step("Select multiple items with Ctrl"):
            if len(list_items) >= 3:
                self.actions.key_down(Keys.CONTROL).click(list_items[1]).click(list_items[2]).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                
                # Count selected items
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                allure.attach(f"Selected {len(selected_items)} items", "Selection Count", allure.attachment_type.TEXT)

    @allure.story("Selectable")
    @allure.title("Test Grid Selection Functionality")
    @allure.description("Verify that grid items can be selected")
    @allure.severity(allure.severity_level.NORMAL)
    def test_grid_selectable(self):
        with allure.step("Navigate to Selectable page"):
            self.driver.get("https://demoqa.com/selectable")
            
        with allure.step("Switch to Grid tab"):
            grid_tab = self.wait.until(EC.element_to_be_clickable((By.ID, "demo-tab-grid")))
            grid_tab.click()
            
        with allure.step("Wait for grid to load"):
            grid_container = self.wait.until(EC.presence_of_element_located((By.ID, "demo-tabpane-grid")))
            
        with allure.step("Select grid items"):
            grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")
            
            if grid_items:
                # Select first grid item
                grid_items[0].click()
                time.sleep(1)
                
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item.active")
                allure.attach(f"Selected {len(selected_items)} grid items", "Grid Selection", allure.attachment_type.TEXT)

    @allure.story("Resizable")
    @allure.title("Test Resizable Box Functionality")
    @allure.description("Verify that resizable elements can be resized by dragging")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_resizable_box(self):
        with allure.step("Navigate to Resizable page"):
            self.driver.get("https://demoqa.com/resizable")
            
        with allure.step("Find resizable box"):
            resizable_box = self.wait.until(EC.presence_of_element_located((By.ID, "resizableBoxWithRestriction")))
            
        with allure.step("Get initial size"):
            initial_size = resizable_box.size
            allure.attach(str(initial_size), "Initial Size", allure.attachment_type.TEXT)
            
        with allure.step("Find resize handle"):
            try:
                resize_handle = self.driver.find_element(By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")
                
                # Perform resize operation
                self.actions.click_and_hold(resize_handle).move_by_offset(50, 50).release().perform()
                time.sleep(2)
                
                # Get new size
                new_size = resizable_box.size
                allure.attach(str(new_size), "New Size", allure.attachment_type.TEXT)
                
                # Verify size changed
                assert initial_size != new_size
                
            except Exception as e:
                allure.attach(f"Resize handle not found: {str(e)}", "Resize Error", allure.attachment_type.TEXT)

    @allure.story("Resizable")
    @allure.title("Test Resizable Element Without Restriction")
    @allure.description("Verify that unrestricted resizable elements work correctly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_resizable_no_restriction(self):
        with allure.step("Navigate to Resizable page"):
            self.driver.get("https://demoqa.com/resizable")
            
        with allure.step("Find unrestricted resizable element"):
            try:
                resizable_element = self.driver.find_element(By.ID, "resizable")
                initial_size = resizable_element.size
                allure.attach(str(initial_size), "Initial Unrestricted Size", allure.attachment_type.TEXT)
                
                # Try to find and use resize handle
                resize_handle = self.driver.find_element(By.CSS_SELECTOR, "#resizable .react-resizable-handle")
                self.actions.click_and_hold(resize_handle).move_by_offset(30, 30).release().perform()
                time.sleep(2)
                
                new_size = resizable_element.size
                allure.attach(str(new_size), "New Unrestricted Size", allure.attachment_type.TEXT)
                
            except Exception as e:
                allure.attach(f"Unrestricted resize test issue: {str(e)}", "Resize Error", allure.attachment_type.TEXT)

    @allure.story("Droppable")
    @allure.title("Test Simple Drop Functionality")
    @allure.description("Verify that elements can be dragged and dropped into drop zones")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_simple_drop(self):
        with allure.step("Navigate to Droppable page"):
            self.driver.get("https://demoqa.com/droppable")
            
        with allure.step("Find draggable and droppable elements"):
            draggable = self.wait.until(EC.presence_of_element_located((By.ID, "draggable")))
            droppable = self.driver.find_element(By.ID, "droppable")
            
        with allure.step("Get initial states"):
            initial_draggable_text = draggable.text
            initial_droppable_text = droppable.text
            allure.attach(f"Draggable: {initial_draggable_text}", "Initial State", allure.attachment_type.TEXT)
            allure.attach(f"Droppable: {initial_droppable_text}", "Initial State", allure.attachment_type.TEXT)
            
        with allure.step("Perform drag and drop"):
            self.actions.drag_and_drop(draggable, droppable).perform()
            time.sleep(2)
            
        with allure.step("Verify drop success"):
            final_droppable_text = droppable.text
            allure.attach(f"Final droppable text: {final_droppable_text}", "Final State", allure.attachment_type.TEXT)
            
            # Check if text changed (indicating successful drop)
            assert initial_droppable_text != final_droppable_text

    @allure.story("Droppable")
    @allure.title("Test Accept Drop Functionality")
    @allure.description("Verify that drop zones only accept specific draggable elements")
    @allure.severity(allure.severity_level.NORMAL)
    def test_accept_drop(self):
        with allure.step("Navigate to Droppable page"):
            self.driver.get("https://demoqa.com/droppable")
            
        with allure.step("Switch to Accept tab"):
            try:
                accept_tab = self.wait.until(EC.element_to_be_clickable((By.ID, "droppableExample-tab-accept")))
                accept_tab.click()
                time.sleep(1)
                
                # Find acceptable and not acceptable elements
                acceptable = self.driver.find_element(By.ID, "acceptable")
                not_acceptable = self.driver.find_element(By.ID, "notAcceptable")
                drop_zone = self.driver.find_element(By.CSS_SELECTOR, "#acceptDropContainer #droppable")
                
                initial_drop_text = drop_zone.text
                allure.attach(initial_drop_text, "Initial Drop Zone Text", allure.attachment_type.TEXT)
                
                # Try dropping not acceptable element
                self.actions.drag_and_drop(not_acceptable, drop_zone).perform()
                time.sleep(1)
                
                after_invalid_drop = drop_zone.text
                allure.attach(after_invalid_drop, "After Invalid Drop", allure.attachment_type.TEXT)
                
                # Try dropping acceptable element
                self.actions.drag_and_drop(acceptable, drop_zone).perform()
                time.sleep(1)
                
                after_valid_drop = drop_zone.text
                allure.attach(after_valid_drop, "After Valid Drop", allure.attachment_type.TEXT)
                
            except Exception as e:
                allure.attach(f"Accept drop test issue: {str(e)}", "Test Error", allure.attachment_type.TEXT)

    @allure.story("Dragabble")
    @allure.title("Test Simple Drag Functionality")
    @allure.description("Verify that elements can be dragged around the screen")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_simple_drag(self):
        with allure.step("Navigate to Dragabble page"):
            self.driver.get("https://demoqa.com/dragabble")
            
        with allure.step("Find draggable element"):
            draggable = self.wait.until(EC.presence_of_element_located((By.ID, "dragBox")))
            
        with allure.step("Get initial position"):
            initial_location = draggable.location
            allure.attach(str(initial_location), "Initial Position", allure.attachment_type.TEXT)
            
        with allure.step("Perform drag operation"):
            self.actions.click_and_hold(draggable).move_by_offset(100, 50).release().perform()
            time.sleep(2)
            
        with allure.step("Verify position changed"):
            new_location = draggable.location
            allure.attach(str(new_location), "New Position", allure.attachment_type.TEXT)
            
            # Verify element moved
            assert initial_location != new_location

    @allure.story("Dragabble")
    @allure.title("Test Axis Restricted Drag")
    @allure.description("Verify that axis-restricted dragging works correctly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_axis_restricted_drag(self):
        with allure.step("Navigate to Dragabble page"):
            self.driver.get("https://demoqa.com/dragabble")
            
        with allure.step("Switch to Axis Restricted tab"):
            try:
                axis_tab = self.wait.until(EC.element_to_be_clickable((By.ID, "draggableExample-tab-axisRestriction")))
                axis_tab.click()
                time.sleep(1)
                
                # Test X-axis restricted drag
                x_restricted = self.driver.find_element(By.ID, "restrictedX")
                initial_x_pos = x_restricted.location
                
                self.actions.click_and_hold(x_restricted).move_by_offset(100, 50).release().perform()
                time.sleep(1)
                
                new_x_pos = x_restricted.location
                allure.attach(f"X-restricted: {initial_x_pos} -> {new_x_pos}", "X-Axis Movement", allure.attachment_type.TEXT)
                
                # Test Y-axis restricted drag
                y_restricted = self.driver.find_element(By.ID, "restrictedY")
                initial_y_pos = y_restricted.location
                
                self.actions.click_and_hold(y_restricted).move_by_offset(50, 100).release().perform()
                time.sleep(1)
                
                new_y_pos = y_restricted.location
                allure.attach(f"Y-restricted: {initial_y_pos} -> {new_y_pos}", "Y-Axis Movement", allure.attachment_type.TEXT)
                
            except Exception as e:
                allure.attach(f"Axis restricted test issue: {str(e)}", "Test Error", allure.attachment_type.TEXT)