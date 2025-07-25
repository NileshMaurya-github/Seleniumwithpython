from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class ResizableTest:
    """Individual test for Resizable functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_resizable_box(self):
        """Test resizable box functionality"""
        print("🔧 Testing Resizable - Resizable Box...")
        self.driver.get("https://demoqa.com/resizable")

        try:
            # Find the resizable box
            resizable_box = self.driver.find_element(By.ID, "resizableBoxWithRestriction")
            initial_size = resizable_box.size
            print(f"  ✓ Initial box size: {initial_size}")
            
            # Find the resize handle (usually bottom-right corner)
            resize_handle = self.driver.find_element(By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")
            print("  ✓ Found resize handle")
            
            # Perform resize operation
            actions = ActionChains(self.driver)
            actions.click_and_hold(resize_handle).move_by_offset(50, 30).release().perform()
            print("  ✓ Performed resize operation")
            
            time.sleep(1)  # Wait for resize animation
            
            # Check new size
            new_size = resizable_box.size
            print(f"  ✓ New box size: {new_size}")
            
            # Verify size changed
            assert new_size != initial_size, "Box size should have changed"
            print("  ✓ Box successfully resized")
            
            # Test resize constraints (if any)
            # Try to resize beyond maximum
            actions.click_and_hold(resize_handle).move_by_offset(200, 200).release().perform()
            time.sleep(1)
            
            constrained_size = resizable_box.size
            print(f"  ✓ Size after large resize attempt: {constrained_size}")
            
            print("✅ Resizable box test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Resizable box test FAILED: {e}")
            return False

    def test_resizable_element(self):
        """Test general resizable element functionality"""
        print("\n🔧 Testing Resizable - General Element...")
        self.driver.get("https://demoqa.com/resizable")

        try:
            # Find the general resizable element
            resizable_element = self.driver.find_element(By.ID, "resizable")
            initial_size = resizable_element.size
            print(f"  ✓ Initial element size: {initial_size}")
            
            # Find the resize handle for general element
            resize_handle = self.driver.find_element(By.CSS_SELECTOR, "#resizable .react-resizable-handle")
            print("  ✓ Found resize handle for general element")
            
            # Perform resize operation
            actions = ActionChains(self.driver)
            actions.click_and_hold(resize_handle).move_by_offset(80, 60).release().perform()
            print("  ✓ Performed resize operation")
            
            time.sleep(1)  # Wait for resize animation
            
            # Check new size
            new_size = resizable_element.size
            print(f"  ✓ New element size: {new_size}")
            
            # Verify size changed
            assert new_size != initial_size, "Element size should have changed"
            print("  ✓ Element successfully resized")
            
            # Test shrinking
            actions.click_and_hold(resize_handle).move_by_offset(-40, -30).release().perform()
            time.sleep(1)
            
            shrunk_size = resizable_element.size
            print(f"  ✓ Size after shrinking: {shrunk_size}")
            
            print("✅ Resizable element test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Resizable element test FAILED: {e}")
            return False

    def test_resize_handles(self):
        """Test different resize handles and directions"""
        print("\n🔧 Testing Resizable - Resize Handles...")
        self.driver.get("https://demoqa.com/resizable")

        try:
            # Test resizable box handles
            resizable_box = self.driver.find_element(By.ID, "resizableBoxWithRestriction")
            initial_size = resizable_box.size
            
            # Find all resize handles
            handles = self.driver.find_elements(By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")
            print(f"  ✓ Found {len(handles)} resize handle(s)")
            
            if handles:
                # Test the main handle (usually the last one - bottom-right)
                main_handle = handles[-1]
                
                # Get handle position and properties
                handle_location = main_handle.location
                handle_size = main_handle.size
                print(f"  ✓ Handle location: {handle_location}, size: {handle_size}")
                
                # Test hover effect on handle
                actions = ActionChains(self.driver)
                actions.move_to_element(main_handle).perform()
                print("  ✓ Hovered over resize handle")
                
                # Check cursor change
                cursor_style = main_handle.value_of_css_property("cursor")
                print(f"  ✓ Handle cursor style: {cursor_style}")
                
                # Perform precise resize
                actions.click_and_hold(main_handle).move_by_offset(25, 25).release().perform()
                time.sleep(0.5)
                
                final_size = resizable_box.size
                print(f"  ✓ Final size after handle test: {final_size}")
                
                # Verify resize worked
                size_changed = (final_size['width'] != initial_size['width'] or 
                              final_size['height'] != initial_size['height'])
                assert size_changed, "Size should have changed"
            
            print("✅ Resize handles test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Resize handles test FAILED: {e}")
            return False

    def test_resize_constraints(self):
        """Test resize constraints and limits"""
        print("\n🔧 Testing Resizable - Constraints...")
        self.driver.get("https://demoqa.com/resizable")

        try:
            # Test constrained resizable box
            resizable_box = self.driver.find_element(By.ID, "resizableBoxWithRestriction")
            resize_handle = self.driver.find_element(By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")
            
            initial_size = resizable_box.size
            print(f"  ✓ Initial constrained box size: {initial_size}")
            
            # Try to resize very small (test minimum constraints)
            actions = ActionChains(self.driver)
            actions.click_and_hold(resize_handle).move_by_offset(-100, -100).release().perform()
            time.sleep(1)
            
            min_size = resizable_box.size
            print(f"  ✓ Size after minimum resize attempt: {min_size}")
            
            # Try to resize very large (test maximum constraints)
            actions.click_and_hold(resize_handle).move_by_offset(300, 300).release().perform()
            time.sleep(1)
            
            max_size = resizable_box.size
            print(f"  ✓ Size after maximum resize attempt: {max_size}")
            
            # Verify constraints are working
            # The box should not become too small or too large
            print(f"  ✓ Width range: {min_size['width']} - {max_size['width']}")
            print(f"  ✓ Height range: {min_size['height']} - {max_size['height']}")
            
            # Test that constraints are reasonable
            assert min_size['width'] > 0 and min_size['height'] > 0, "Minimum size should be positive"
            assert max_size['width'] < 1000 and max_size['height'] < 1000, "Maximum size should be reasonable"
            
            print("✅ Resize constraints test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Resize constraints test FAILED: {e}")
            return False

    def run_all_resizable_tests(self):
        """Run all resizable tests"""
        print("=" * 60)
        print("📏 RESIZABLE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_resizable_box())
            results.append(self.test_resizable_element())
            results.append(self.test_resize_handles())
            results.append(self.test_resize_constraints())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 RESIZABLE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Resizable tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Resizable tests passed, some had issues")
            else:
                print("❌ All Resizable tests had issues")
                
        except Exception as e:
            print(f"❌ Resizable test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    resizable_test = ResizableTest()
    resizable_test.run_all_resizable_tests()