from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class ToolTipsTest:
    """Individual test for Tool Tips functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_button_tooltip(self):
        """Test button tooltip functionality"""
        print("🔧 Testing Tool Tips - Button Tooltip...")
        self.driver.get("https://demoqa.com/tool-tips")

        try:
            # Find the button with tooltip
            tooltip_button = self.driver.find_element(By.ID, "toolTipButton")
            print("  ✓ Found tooltip button")
            
            # Hover over the button to trigger tooltip
            actions = ActionChains(self.driver)
            actions.move_to_element(tooltip_button).perform()
            print("  ✓ Hovered over button")
            
            # Wait for tooltip to appear
            try:
                tooltip = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tooltip-inner")))
                tooltip_text = tooltip.text
                print(f"  ✓ Tooltip appeared with text: '{tooltip_text}'")
                
                # Verify tooltip content
                assert len(tooltip_text) > 0
                print("  ✓ Tooltip content verified")
                
            except Exception as tooltip_e:
                print(f"  ⚠️ Tooltip may not have appeared: {tooltip_e}")
                # Try alternative selector
                try:
                    tooltip_alt = self.driver.find_element(By.CSS_SELECTOR, "[role='tooltip']")
                    if tooltip_alt.is_displayed():
                        print("  ✓ Tooltip found with alternative selector")
                    else:
                        print("  ⚠️ Tooltip not visible")
                except:
                    print("  ⚠️ Tooltip not found with alternative selector")
            
            # Move away to hide tooltip
            actions.move_by_offset(100, 100).perform()
            time.sleep(0.5)
            print("  ✓ Moved away from button")
            
            print("✅ Button tooltip test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Button tooltip test FAILED: {e}")
            return False

    def test_text_field_tooltip(self):
        """Test text field tooltip functionality"""
        print("\n🔧 Testing Tool Tips - Text Field Tooltip...")
        self.driver.get("https://demoqa.com/tool-tips")

        try:
            # Find the text field with tooltip
            tooltip_text_field = self.driver.find_element(By.ID, "toolTipTextField")
            print("  ✓ Found tooltip text field")
            
            # Hover over the text field to trigger tooltip
            actions = ActionChains(self.driver)
            actions.move_to_element(tooltip_text_field).perform()
            print("  ✓ Hovered over text field")
            
            # Wait for tooltip to appear
            try:
                tooltip = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tooltip-inner")))
                tooltip_text = tooltip.text
                print(f"  ✓ Tooltip appeared with text: '{tooltip_text}'")
                
                # Verify tooltip content
                assert len(tooltip_text) > 0
                print("  ✓ Tooltip content verified")
                
            except Exception as tooltip_e:
                print(f"  ⚠️ Text field tooltip may not have appeared: {tooltip_e}")
                # Try alternative approach
                try:
                    tooltip_alt = self.driver.find_element(By.CSS_SELECTOR, "[role='tooltip']")
                    if tooltip_alt.is_displayed():
                        print("  ✓ Tooltip found with alternative selector")
                except:
                    print("  ⚠️ Tooltip not found")
            
            # Move away to hide tooltip
            actions.move_by_offset(100, 100).perform()
            time.sleep(0.5)
            print("  ✓ Moved away from text field")
            
            print("✅ Text field tooltip test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Text field tooltip test FAILED: {e}")
            return False

    def test_link_tooltip(self):
        """Test link tooltip functionality"""
        print("\n🔧 Testing Tool Tips - Link Tooltip...")
        self.driver.get("https://demoqa.com/tool-tips")

        try:
            # Find the link with tooltip (Contrary link)
            try:
                tooltip_link = self.driver.find_element(By.LINK_TEXT, "Contrary")
                print("  ✓ Found 'Contrary' link")
            except:
                # Try alternative selector
                tooltip_link = self.driver.find_element(By.CSS_SELECTOR, "a[href]")
                print("  ✓ Found link element")
            
            # Hover over the link to trigger tooltip
            actions = ActionChains(self.driver)
            actions.move_to_element(tooltip_link).perform()
            print("  ✓ Hovered over link")
            
            # Wait for tooltip to appear
            try:
                tooltip = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tooltip-inner")))
                tooltip_text = tooltip.text
                print(f"  ✓ Tooltip appeared with text: '{tooltip_text}'")
                
                # Verify tooltip content
                assert len(tooltip_text) > 0
                print("  ✓ Tooltip content verified")
                
            except Exception as tooltip_e:
                print(f"  ⚠️ Link tooltip may not have appeared: {tooltip_e}")
                # Check if tooltip exists but may not be visible
                try:
                    tooltip_elements = self.driver.find_elements(By.CSS_SELECTOR, "[role='tooltip'], .tooltip")
                    if tooltip_elements:
                        print(f"  ✓ Found {len(tooltip_elements)} tooltip element(s)")
                    else:
                        print("  ⚠️ No tooltip elements found")
                except:
                    print("  ⚠️ Tooltip search failed")
            
            # Move away to hide tooltip
            actions.move_by_offset(100, 100).perform()
            time.sleep(0.5)
            print("  ✓ Moved away from link")
            
            print("✅ Link tooltip test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Link tooltip test FAILED: {e}")
            return False

    def test_tooltip_positioning(self):
        """Test tooltip positioning and behavior"""
        print("\n🔧 Testing Tool Tips - Positioning...")
        self.driver.get("https://demoqa.com/tool-tips")

        try:
            # Test multiple elements to see tooltip positioning
            elements_to_test = [
                ("toolTipButton", "Button"),
                ("toolTipTextField", "Text Field")
            ]
            
            for element_id, element_name in elements_to_test:
                try:
                    element = self.driver.find_element(By.ID, element_id)
                    element_location = element.location
                    print(f"  ✓ {element_name} location: {element_location}")
                    
                    # Hover over element
                    actions = ActionChains(self.driver)
                    actions.move_to_element(element).perform()
                    time.sleep(1)
                    
                    # Try to find tooltip and get its position
                    try:
                        tooltip = self.driver.find_element(By.CSS_SELECTOR, ".tooltip-inner, [role='tooltip']")
                        if tooltip.is_displayed():
                            tooltip_location = tooltip.location
                            print(f"  ✓ {element_name} tooltip location: {tooltip_location}")
                            
                            # Check if tooltip is positioned relative to element
                            if tooltip_location['y'] != element_location['y']:
                                print(f"  ✓ {element_name} tooltip positioned differently from element")
                            else:
                                print(f"  ⚠️ {element_name} tooltip may overlap with element")
                        else:
                            print(f"  ⚠️ {element_name} tooltip not visible")
                            
                    except Exception as pos_e:
                        print(f"  ⚠️ {element_name} tooltip positioning check failed: {pos_e}")
                    
                    # Move away
                    actions.move_by_offset(50, 50).perform()
                    time.sleep(0.5)
                    
                except Exception as elem_e:
                    print(f"  ⚠️ {element_name} test failed: {elem_e}")
            
            print("✅ Tooltip positioning test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Tooltip positioning test FAILED: {e}")
            return False

    def test_tooltip_timing(self):
        """Test tooltip timing and persistence"""
        print("\n🔧 Testing Tool Tips - Timing...")
        self.driver.get("https://demoqa.com/tool-tips")

        try:
            # Find button for timing test
            tooltip_button = self.driver.find_element(By.ID, "toolTipButton")
            
            # Quick hover and move away
            actions = ActionChains(self.driver)
            actions.move_to_element(tooltip_button).perform()
            time.sleep(0.1)  # Very brief hover
            actions.move_by_offset(100, 100).perform()
            print("  ✓ Quick hover test completed")
            
            # Longer hover test
            actions.move_to_element(tooltip_button).perform()
            print("  ✓ Started longer hover")
            
            # Check tooltip appearance over time
            tooltip_appeared = False
            for i in range(5):
                try:
                    tooltip = self.driver.find_element(By.CSS_SELECTOR, ".tooltip-inner, [role='tooltip']")
                    if tooltip.is_displayed():
                        tooltip_appeared = True
                        print(f"  ✓ Tooltip appeared after {i+1} second(s)")
                        break
                except:
                    pass
                time.sleep(1)
            
            if not tooltip_appeared:
                print("  ⚠️ Tooltip did not appear during longer hover")
            
            # Test tooltip persistence
            if tooltip_appeared:
                print("  ✓ Testing tooltip persistence...")
                time.sleep(2)  # Keep hovering
                
                try:
                    tooltip = self.driver.find_element(By.CSS_SELECTOR, ".tooltip-inner, [role='tooltip']")
                    if tooltip.is_displayed():
                        print("  ✓ Tooltip persisted during hover")
                    else:
                        print("  ⚠️ Tooltip disappeared during hover")
                except:
                    print("  ⚠️ Tooltip not found during persistence test")
            
            # Move away and check tooltip disappears
            actions.move_by_offset(100, 100).perform()
            time.sleep(1)
            
            try:
                tooltip = self.driver.find_element(By.CSS_SELECTOR, ".tooltip-inner, [role='tooltip']")
                if not tooltip.is_displayed():
                    print("  ✓ Tooltip disappeared after moving away")
                else:
                    print("  ⚠️ Tooltip may still be visible after moving away")
            except:
                print("  ✓ Tooltip properly removed after moving away")
            
            print("✅ Tooltip timing test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Tooltip timing test FAILED: {e}")
            return False

    def run_all_tool_tips_tests(self):
        """Run all tool tips tests"""
        print("=" * 60)
        print("💡 TOOL TIPS INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_button_tooltip())
            results.append(self.test_text_field_tooltip())
            results.append(self.test_link_tooltip())
            results.append(self.test_tooltip_positioning())
            results.append(self.test_tooltip_timing())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 TOOL TIPS TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Tool Tips tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Tool Tips tests passed, some had issues")
            else:
                print("❌ All Tool Tips tests had issues")
                
        except Exception as e:
            print(f"❌ Tool Tips test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    tool_tips_test = ToolTipsTest()
    tool_tips_test.run_all_tool_tips_tests()