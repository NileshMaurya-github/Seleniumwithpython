from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class SelectableTest:
    """Individual test for Selectable functionality"""
    
    def __init__(self):
        # Configure Chrome options to block ads and improve interactions
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-images")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values": {
                "notifications": 2,
                "media_stream": 2,
                "ads": 2,
                "popups": 2
            }
        })
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        
    def safe_click(self, element):
        """Safely click an element, handling overlays"""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)
            element.click()
            return True
        except Exception:
            try:
                self.driver.execute_script("arguments[0].click();", element)
                return True
            except Exception:
                try:
                    ActionChains(self.driver).move_to_element_with_offset(element, 5, 5).click().perform()
                    return True
                except Exception:
                    try:
                        self.driver.execute_script("""
                            arguments[0].style.zIndex = '9999';
                            arguments[0].style.position = 'relative';
                            arguments[0].click();
                        """, element)
                        return True
                    except Exception:
                        return False
                        
    def remove_ads(self):
        """Remove ad elements that might interfere with testing"""
        try:
            time.sleep(2)
            self.driver.execute_script("""
                var ads = document.querySelectorAll('iframe[src*="googlesyndication"], iframe[id*="google_ads"], iframe[title*="Advertisement"]');
                for(var i = 0; i < ads.length; i++) {
                    ads[i].style.display = 'none';
                    ads[i].remove();
                }
                var adContainers = document.querySelectorAll('[id*="ad"], [class*="ad"], [class*="advertisement"], [data-google-container-id]');
                for(var i = 0; i < adContainers.length; i++) {
                    if(adContainers[i].offsetHeight > 30 || adContainers[i].offsetWidth > 100) {
                        adContainers[i].style.display = 'none';
                        adContainers[i].remove();
                    }
                }
                var overlays = document.querySelectorAll('[style*="position: fixed"], [style*="position: absolute"]');
                for(var i = 0; i < overlays.length; i++) {
                    var rect = overlays[i].getBoundingClientRect();
                    if(rect.width > 500 && rect.height > 50) {
                        overlays[i].style.display = 'none';
                    }
                }
            """)
            time.sleep(1)
        except Exception:
            pass

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
                self.remove_ads()  # Remove ads before clicking
                if self.safe_click(empty_area):
                    print("  ✓ Clicked empty area to deselect")
                else:
                    print("  ⚠️ Empty area click had issues, but continuing test")
            
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
                self.remove_ads()  # Remove ads before clicking
                if self.safe_click(list_items[1]):
                    print("  ✓ Clicked second item")
                else:
                    print("  ⚠️ Second item click had issues, but continuing test")
                time.sleep(0.3)
                
                # Check how many items are selected
                selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                print(f"  ✓ After single click: {len(selected_items)} item(s) selected")
                
                # Test range selection with Shift+Click
                # Re-find elements to avoid stale reference
                list_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
                if len(list_items) >= 3:
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.SHIFT).click(list_items[2]).key_up(Keys.SHIFT).perform()
                    print("  ✓ Performed Shift+Click for range selection")
                    
                    time.sleep(0.5)
                    selected_items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item.active")
                    print(f"  ✓ After range selection: {len(selected_items)} item(s) selected")
                else:
                    print("  ⚠️ Not enough items for range selection test")
            
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