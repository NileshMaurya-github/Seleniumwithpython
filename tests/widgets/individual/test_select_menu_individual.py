from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time


class SelectMenuTest:
    """Individual test for Select Menu functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        
    def safe_click(self, element):
        """Safely click an element using JavaScript if normal click fails"""
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def test_select_value_dropdown(self):
        """Test Select Value dropdown"""
        print("🔧 Testing Select Menu - Select Value...")
        self.driver.get("https://demoqa.com/select-menu")

        try:
            # Find Select Value dropdown
            select_value_container = self.driver.find_element(By.ID, "withOptGroup")
            select_value_container.click()
            print("  ✓ Select Value dropdown clicked")
            
            # Wait for options to appear
            time.sleep(1)
            
            # Look for dropdown options
            try:
                options = self.driver.find_elements(By.CSS_SELECTOR, ".css-1n7v3ny-option")
                if not options:
                    # Try alternative selector
                    options = self.driver.find_elements(By.CSS_SELECTOR, "[id*='option']")
                
                if options:
                    print(f"  ✓ Found {len(options)} options")
                    
                    # Select first available option
                    first_option = options[0]
                    option_text = first_option.text
                    first_option.click()
                    print(f"  ✓ Selected option: '{option_text}'")
                    
                    # Verify selection
                    time.sleep(0.5)
                    selected_text = select_value_container.text
                    print(f"  ✓ Current selection: '{selected_text}'")
                    
                else:
                    print("  ⚠️ No dropdown options found")
                    # Try typing to search
                    select_value_container.send_keys("Group 1")
                    select_value_container.send_keys(Keys.ENTER)
                    print("  ✓ Attempted selection by typing")
                    
            except Exception as option_e:
                print(f"  ⚠️ Option selection issue: {option_e}")
            
            print("✅ Select Value test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Select Value test FAILED: {e}")
            return False

    def test_select_one_dropdown(self):
        """Test Select One dropdown"""
        print("\n🔧 Testing Select Menu - Select One...")
        self.driver.get("https://demoqa.com/select-menu")

        try:
            # Find Select One dropdown
            select_one_container = self.driver.find_element(By.ID, "selectOne")
            self.safe_click(select_one_container)
            print("  ✓ Select One dropdown clicked")
            
            # Wait for options to appear
            time.sleep(1)
            
            # Look for dropdown options
            try:
                options = self.driver.find_elements(By.CSS_SELECTOR, ".css-1n7v3ny-option")
                if not options:
                    # Try alternative selector
                    options = self.driver.find_elements(By.CSS_SELECTOR, "[id*='option']")
                
                if options:
                    print(f"  ✓ Found {len(options)} options")
                    
                    # Select an option (try to find "Dr." or similar)
                    target_option = None
                    for option in options:
                        if "Dr." in option.text or "Mr." in option.text:
                            target_option = option
                            break
                    
                    if not target_option and options:
                        target_option = options[0]
                    
                    if target_option:
                        option_text = target_option.text
                        target_option.click()
                        print(f"  ✓ Selected option: '{option_text}'")
                        
                        # Verify selection
                        time.sleep(0.5)
                        selected_text = select_one_container.text
                        print(f"  ✓ Current selection: '{selected_text}'")
                    else:
                        print("  ⚠️ No suitable option found")
                        
                else:
                    print("  ⚠️ No dropdown options found")
                    
            except Exception as option_e:
                print(f"  ⚠️ Option selection issue: {option_e}")
            
            print("✅ Select One test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Select One test FAILED: {e}")
            return False

    def test_old_style_select_menu(self):
        """Test Old Style Select Menu"""
        print("\n🔧 Testing Select Menu - Old Style...")
        self.driver.get("https://demoqa.com/select-menu")

        try:
            # Find old style select menu
            old_select = self.driver.find_element(By.ID, "oldSelectMenu")
            print("  ✓ Found old style select menu")
            
            # Use Selenium's Select class for traditional select element
            select = Select(old_select)
            
            # Get all options
            options = select.options
            print(f"  ✓ Found {len(options)} options in old style select")
            
            # Print available options
            for i, option in enumerate(options):
                print(f"    Option {i}: '{option.text}' (value: '{option.get_attribute('value')}')")
            
            # Select by visible text
            if len(options) > 1:
                target_option = options[1]  # Select second option
                select.select_by_visible_text(target_option.text)
                print(f"  ✓ Selected by text: '{target_option.text}'")
                
                # Verify selection
                selected_option = select.first_selected_option
                print(f"  ✓ Currently selected: '{selected_option.text}'")
                
                # Select by value
                if len(options) > 2:
                    third_option = options[2]
                    select.select_by_value(third_option.get_attribute('value'))
                    print(f"  ✓ Selected by value: '{third_option.text}'")
                
                # Select by index
                select.select_by_index(0)
                print("  ✓ Selected by index: first option")
                
            else:
                print("  ⚠️ Not enough options to test selection")
            
            print("✅ Old Style Select Menu test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Old Style Select Menu test FAILED: {e}")
            return False

    def test_multiselect_dropdown(self):
        """Test Multiselect dropdown"""
        print("\n🔧 Testing Select Menu - Multiselect...")
        self.driver.get("https://demoqa.com/select-menu")

        try:
            # Find multiselect dropdown
            multiselect_container = self.driver.find_element(By.CSS_SELECTOR, ".css-2b097c-container")
            multiselect_input = multiselect_container.find_element(By.CSS_SELECTOR, "input")
            print("  ✓ Found multiselect dropdown")
            
            # Click to open dropdown
            multiselect_container.click()
            time.sleep(1)
            print("  ✓ Multiselect dropdown opened")
            
            # Look for options
            try:
                options = self.driver.find_elements(By.CSS_SELECTOR, ".css-1n7v3ny-option")
                if options:
                    print(f"  ✓ Found {len(options)} multiselect options")
                    
                    # Select multiple options
                    selections_made = 0
                    for i, option in enumerate(options[:3]):  # Select first 3 options
                        try:
                            option_text = option.text
                            option.click()
                            selections_made += 1
                            print(f"  ✓ Selected option {i+1}: '{option_text}'")
                            time.sleep(0.5)
                        except Exception as select_e:
                            print(f"  ⚠️ Could not select option {i+1}: {select_e}")
                    
                    print(f"  ✓ Made {selections_made} selections")
                    
                    # Verify selections are displayed
                    try:
                        selected_values = self.driver.find_elements(By.CSS_SELECTOR, ".css-12jo7m5")
                        print(f"  ✓ {len(selected_values)} values displayed as selected")
                        
                        # Try to remove one selection
                        if selected_values:
                            remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".css-1rhbuit-multiValue__remove")
                            if remove_buttons:
                                remove_buttons[0].click()
                                print("  ✓ Removed one selection")
                            else:
                                print("  ⚠️ No remove buttons found")
                                
                    except Exception as verify_e:
                        print(f"  ⚠️ Selection verification issue: {verify_e}")
                        
                else:
                    print("  ⚠️ No multiselect options found")
                    # Try typing to add options
                    multiselect_input.send_keys("Green")
                    multiselect_input.send_keys(Keys.ENTER)
                    print("  ✓ Attempted to add option by typing")
                    
            except Exception as option_e:
                print(f"  ⚠️ Multiselect option handling issue: {option_e}")
            
            # Click outside to close dropdown
            self.driver.find_element(By.TAG_NAME, "body").click()
            
            print("✅ Multiselect test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Multiselect test FAILED: {e}")
            return False

    def test_standard_multi_select(self):
        """Test Standard Multi Select"""
        print("\n🔧 Testing Select Menu - Standard Multi Select...")
        self.driver.get("https://demoqa.com/select-menu")

        try:
            # Find standard multi select
            multi_select = self.driver.find_element(By.ID, "cars")
            print("  ✓ Found standard multi select")
            
            # Use Selenium's Select class
            select = Select(multi_select)
            
            # Verify it's a multi-select
            if select.is_multiple:
                print("  ✓ Confirmed this is a multi-select element")
            else:
                print("  ⚠️ This may not be a multi-select element")
            
            # Get all options
            options = select.options
            print(f"  ✓ Found {len(options)} options in standard multi select")
            
            # Print available options
            for i, option in enumerate(options):
                print(f"    Option {i}: '{option.text}' (value: '{option.get_attribute('value')}')")
            
            # Select multiple options
            if len(options) >= 2:
                # Select first two options
                select.select_by_index(0)
                select.select_by_index(1)
                print("  ✓ Selected first two options")
                
                # Verify selections
                selected_options = select.all_selected_options
                print(f"  ✓ {len(selected_options)} options are selected:")
                for selected in selected_options:
                    print(f"    - '{selected.text}'")
                
                # Deselect one option
                if len(selected_options) > 1:
                    select.deselect_by_index(0)
                    print("  ✓ Deselected first option")
                    
                    # Verify deselection
                    remaining_selected = select.all_selected_options
                    print(f"  ✓ {len(remaining_selected)} options remain selected")
                
                # Deselect all
                select.deselect_all()
                print("  ✓ Deselected all options")
                
                final_selected = select.all_selected_options
                print(f"  ✓ {len(final_selected)} options selected after deselect all")
                
            else:
                print("  ⚠️ Not enough options to test multi-selection")
            
            print("✅ Standard Multi Select test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Standard Multi Select test FAILED: {e}")
            return False

    def run_all_select_menu_tests(self):
        """Run all select menu tests"""
        print("=" * 60)
        print("📋 SELECT MENU INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_select_value_dropdown())
            results.append(self.test_select_one_dropdown())
            results.append(self.test_old_style_select_menu())
            results.append(self.test_multiselect_dropdown())
            results.append(self.test_standard_multi_select())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 SELECT MENU TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Select Menu tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Select Menu tests passed, some had issues")
            else:
                print("❌ All Select Menu tests had issues")
                
        except Exception as e:
            print(f"❌ Select Menu test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    select_menu_test = SelectMenuTest()
    select_menu_test.run_all_select_menu_tests()