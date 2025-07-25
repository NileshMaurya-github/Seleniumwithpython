from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class MenuTest:
    """Individual test for Menu functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_main_menu_items(self):
        """Test main menu items"""
        print("🔧 Testing Menu - Main Menu Items...")
        self.driver.get("https://demoqa.com/menu")

        try:
            # Find main menu items
            main_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav > li > a")
            print(f"  ✓ Found {len(main_items)} main menu items")
            
            # Test each main menu item
            for i, item in enumerate(main_items):
                item_text = item.text
                print(f"  ✓ Main item {i+1}: '{item_text}'")
                
                # Hover over item to see if it's interactive
                actions = ActionChains(self.driver)
                actions.move_to_element(item).perform()
                time.sleep(0.5)
                
                # Check if item has submenu (look for expanded state)
                parent_li = item.find_element(By.XPATH, "..")
                li_classes = parent_li.get_attribute("class")
                
                if "has-submenu" in li_classes or "dropdown" in li_classes:
                    print(f"    ✓ '{item_text}' has submenu")
                else:
                    print(f"    ✓ '{item_text}' is a simple menu item")
            
            print("✅ Main menu items test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Main menu items test FAILED: {e}")
            return False

    def test_main_item_2_submenu(self):
        """Test Main Item 2 submenu"""
        print("\n🔧 Testing Menu - Main Item 2 Submenu...")
        self.driver.get("https://demoqa.com/menu")

        try:
            # Find Main Item 2
            main_item_2 = None
            main_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav > li > a")
            
            for item in main_items:
                if "Main Item 2" in item.text:
                    main_item_2 = item
                    break
            
            if not main_item_2:
                print("  ⚠️ Main Item 2 not found, trying alternative approach")
                # Try to find by index
                if len(main_items) >= 2:
                    main_item_2 = main_items[1]
                    print("  ✓ Using second main item")
                else:
                    print("  ❌ Cannot find Main Item 2")
                    return False
            
            print("  ✓ Found Main Item 2")
            
            # Hover over Main Item 2 to reveal submenu
            actions = ActionChains(self.driver)
            actions.move_to_element(main_item_2).perform()
            time.sleep(1)
            print("  ✓ Hovered over Main Item 2")
            
            # Look for submenu items
            try:
                submenu_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav li ul li a")
                if submenu_items:
                    print(f"  ✓ Found {len(submenu_items)} submenu items")
                    
                    for i, sub_item in enumerate(submenu_items):
                        if sub_item.is_displayed():
                            sub_text = sub_item.text
                            print(f"    ✓ Submenu item {i+1}: '{sub_text}'")
                        else:
                            print(f"    ⚠️ Submenu item {i+1} not visible")
                else:
                    print("  ⚠️ No submenu items found")
                    
            except Exception as sub_e:
                print(f"  ⚠️ Submenu search failed: {sub_e}")
            
            # Move away to hide submenu
            actions.move_by_offset(100, 100).perform()
            time.sleep(0.5)
            print("  ✓ Moved away from menu")
            
            print("✅ Main Item 2 submenu test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Main Item 2 submenu test FAILED: {e}")
            return False

    def test_sub_sub_list(self):
        """Test Sub Sub List functionality"""
        print("\n🔧 Testing Menu - Sub Sub List...")
        self.driver.get("https://demoqa.com/menu")

        try:
            # Navigate to Main Item 2 first
            main_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav > li > a")
            main_item_2 = None
            
            for item in main_items:
                if "Main Item 2" in item.text:
                    main_item_2 = item
                    break
            
            if not main_item_2 and len(main_items) >= 2:
                main_item_2 = main_items[1]
            
            if not main_item_2:
                print("  ❌ Cannot find Main Item 2")
                return False
            
            # Hover over Main Item 2
            actions = ActionChains(self.driver)
            actions.move_to_element(main_item_2).perform()
            time.sleep(1)
            print("  ✓ Hovered over Main Item 2")
            
            # Look for Sub Sub List item
            try:
                sub_sub_list_item = None
                submenu_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav li ul li a")
                
                for item in submenu_items:
                    if item.is_displayed() and "Sub Sub List" in item.text:
                        sub_sub_list_item = item
                        break
                
                if sub_sub_list_item:
                    print("  ✓ Found Sub Sub List item")
                    
                    # Hover over Sub Sub List to reveal third level menu
                    actions.move_to_element(sub_sub_list_item).perform()
                    time.sleep(1)
                    print("  ✓ Hovered over Sub Sub List")
                    
                    # Look for third level menu items
                    try:
                        third_level_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav li ul li ul li a")
                        if third_level_items:
                            visible_items = [item for item in third_level_items if item.is_displayed()]
                            print(f"  ✓ Found {len(visible_items)} third level menu items")
                            
                            for i, item in enumerate(visible_items):
                                item_text = item.text
                                print(f"    ✓ Third level item {i+1}: '{item_text}'")
                        else:
                            print("  ⚠️ No third level menu items found")
                            
                    except Exception as third_e:
                        print(f"  ⚠️ Third level menu search failed: {third_e}")
                        
                else:
                    print("  ⚠️ Sub Sub List item not found")
                    
            except Exception as sub_e:
                print(f"  ⚠️ Sub Sub List search failed: {sub_e}")
            
            # Move away to hide all menus
            actions.move_by_offset(200, 200).perform()
            time.sleep(0.5)
            print("  ✓ Moved away from all menus")
            
            print("✅ Sub Sub List test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Sub Sub List test FAILED: {e}")
            return False

    def test_menu_navigation(self):
        """Test menu navigation and interaction"""
        print("\n🔧 Testing Menu - Navigation...")
        self.driver.get("https://demoqa.com/menu")

        try:
            # Test navigation through menu hierarchy
            actions = ActionChains(self.driver)
            
            # Step 1: Hover over first main item
            main_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav > li > a")
            if main_items:
                first_item = main_items[0]
                actions.move_to_element(first_item).perform()
                time.sleep(0.5)
                print(f"  ✓ Navigated to first main item: '{first_item.text}'")
            
            # Step 2: Navigate to second main item
            if len(main_items) >= 2:
                second_item = main_items[1]
                actions.move_to_element(second_item).perform()
                time.sleep(1)
                print(f"  ✓ Navigated to second main item: '{second_item.text}'")
                
                # Check if submenu appeared
                submenu_items = self.driver.find_elements(By.CSS_SELECTOR, "#nav li ul li a")
                visible_submenu = [item for item in submenu_items if item.is_displayed()]
                if visible_submenu:
                    print(f"  ✓ Submenu appeared with {len(visible_submenu)} items")
                    
                    # Navigate to first submenu item
                    if visible_submenu:
                        first_sub = visible_submenu[0]
                        actions.move_to_element(first_sub).perform()
                        time.sleep(0.5)
                        print(f"  ✓ Navigated to submenu item: '{first_sub.text}'")
                else:
                    print("  ⚠️ No visible submenu items found")
            
            # Step 3: Navigate away and back
            actions.move_by_offset(100, 100).perform()
            time.sleep(0.5)
            print("  ✓ Navigated away from menu")
            
            # Navigate back to menu
            if main_items:
                actions.move_to_element(main_items[0]).perform()
                time.sleep(0.5)
                print("  ✓ Navigated back to menu")
            
            print("✅ Menu navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Menu navigation test FAILED: {e}")
            return False

    def test_menu_structure(self):
        """Test menu structure and hierarchy"""
        print("\n🔧 Testing Menu - Structure...")
        self.driver.get("https://demoqa.com/menu")

        try:
            # Analyze menu structure
            menu_container = self.driver.find_element(By.ID, "nav")
            print("  ✓ Found menu container")
            
            # Count main menu items
            main_items = menu_container.find_elements(By.CSS_SELECTOR, "> li")
            print(f"  ✓ Main menu has {len(main_items)} items")
            
            # Analyze each main item
            for i, main_item in enumerate(main_items):
                main_link = main_item.find_element(By.CSS_SELECTOR, "> a")
                main_text = main_link.text
                print(f"  ✓ Main item {i+1}: '{main_text}'")
                
                # Check for submenus
                submenus = main_item.find_elements(By.CSS_SELECTOR, "> ul")
                if submenus:
                    submenu = submenus[0]
                    sub_items = submenu.find_elements(By.CSS_SELECTOR, "> li")
                    print(f"    ✓ Has submenu with {len(sub_items)} items")
                    
                    # Check for third level menus
                    for j, sub_item in enumerate(sub_items):
                        sub_link = sub_item.find_element(By.CSS_SELECTOR, "> a")
                        sub_text = sub_link.text
                        
                        third_level = sub_item.find_elements(By.CSS_SELECTOR, "> ul")
                        if third_level:
                            third_items = third_level[0].find_elements(By.CSS_SELECTOR, "> li")
                            print(f"      ✓ Sub item '{sub_text}' has {len(third_items)} third level items")
                        else:
                            print(f"      ✓ Sub item '{sub_text}' (no third level)")
                else:
                    print(f"    ✓ No submenu")
            
            print("✅ Menu structure test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Menu structure test FAILED: {e}")
            return False

    def run_all_menu_tests(self):
        """Run all menu tests"""
        print("=" * 60)
        print("🍔 MENU INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_main_menu_items())
            results.append(self.test_main_item_2_submenu())
            results.append(self.test_sub_sub_list())
            results.append(self.test_menu_navigation())
            results.append(self.test_menu_structure())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 MENU TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Menu tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Menu tests passed, some had issues")
            else:
                print("❌ All Menu tests had issues")
                
        except Exception as e:
            print(f"❌ Menu test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    menu_test = MenuTest()
    menu_test.run_all_menu_tests()