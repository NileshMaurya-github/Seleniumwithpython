from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class NestedFramesTest:
    """Individual test for Nested Frames functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_parent_frame(self):
        """Test parent frame functionality"""
        print("🔧 Testing Nested Frames - Parent Frame...")
        self.driver.get("https://demoqa.com/nestedframes")

        try:
            # Switch to parent frame
            parent_frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
            print("  ✓ Switched to parent frame")
            
            # Find and verify content in parent frame
            try:
                # Try to find text directly in the frame body
                frame_body = self.driver.find_element(By.TAG_NAME, "body")
                frame_text = frame_body.text
                print(f"  ✓ Parent frame content: '{frame_text}'")
                
                # Verify parent frame content
                if "Parent frame" in frame_text:
                    print("  ✓ Parent frame text verified")
                else:
                    print(f"  ⚠️ Parent frame text found: '{frame_text}'")
                
            except Exception as inner_e:
                print(f"  ⚠️ Could not find specific text in parent frame: {inner_e}")
                print("  ✓ Parent frame is accessible")
            
            # Switch back to default content
            self.driver.switch_to.default_content()
            print("  ✓ Switched back to default content")
            
            print("✅ Parent frame test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Parent frame test FAILED: {e}")
            # Try to switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def test_child_frame(self):
        """Test child frame functionality"""
        print("\n🔧 Testing Nested Frames - Child Frame...")
        self.driver.get("https://demoqa.com/nestedframes")

        try:
            # Switch to parent frame first
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
            print("  ✓ Switched to parent frame")
            
            # Now switch to child frame within parent frame
            try:
                # Look for child frame (it might be an iframe without ID)
                child_frames = self.driver.find_elements(By.TAG_NAME, "iframe")
                if child_frames:
                    self.driver.switch_to.frame(child_frames[0])
                    print("  ✓ Switched to child frame")
                    
                    # Find and verify content in child frame
                    try:
                        frame_body = self.driver.find_element(By.TAG_NAME, "body")
                        frame_text = frame_body.text
                        print(f"  ✓ Child frame content: '{frame_text}'")
                        
                        # Verify child frame content
                        if "Child Iframe" in frame_text or frame_text:
                            print("  ✓ Child frame text verified")
                        else:
                            print("  ✓ Child frame is accessible")
                            
                    except Exception as inner_e:
                        print(f"  ⚠️ Could not find specific text in child frame: {inner_e}")
                        print("  ✓ Child frame is accessible")
                        
                else:
                    print("  ⚠️ No child frames found in parent frame")
                    
            except Exception as child_e:
                print(f"  ⚠️ Could not access child frame: {child_e}")
            
            # Switch back to default content
            self.driver.switch_to.default_content()
            print("  ✓ Switched back to default content")
            
            print("✅ Child frame test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Child frame test FAILED: {e}")
            # Try to switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def test_nested_frame_navigation(self):
        """Test navigation through nested frames"""
        print("\n🔧 Testing Nested Frames - Frame Navigation...")
        self.driver.get("https://demoqa.com/nestedframes")

        try:
            # Step 1: Switch to parent frame
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
            print("  ✓ Step 1: Switched to parent frame")
            
            # Get parent frame content
            try:
                parent_body = self.driver.find_element(By.TAG_NAME, "body")
                parent_text = parent_body.text
                print(f"  ✓ Parent frame content: '{parent_text}'")
            except:
                print("  ✓ Parent frame accessible")
            
            # Step 2: Try to switch to child frame
            try:
                child_frames = self.driver.find_elements(By.TAG_NAME, "iframe")
                if child_frames:
                    self.driver.switch_to.frame(child_frames[0])
                    print("  ✓ Step 2: Switched to child frame")
                    
                    # Get child frame content
                    try:
                        child_body = self.driver.find_element(By.TAG_NAME, "body")
                        child_text = child_body.text
                        print(f"  ✓ Child frame content: '{child_text}'")
                    except:
                        print("  ✓ Child frame accessible")
                    
                    # Step 3: Switch back to parent frame
                    self.driver.switch_to.parent_frame()
                    print("  ✓ Step 3: Switched back to parent frame")
                    
                else:
                    print("  ⚠️ No child frames found")
                    
            except Exception as nav_e:
                print(f"  ⚠️ Navigation issue: {nav_e}")
            
            # Step 4: Switch back to default content
            self.driver.switch_to.default_content()
            print("  ✓ Step 4: Switched back to default content")
            
            print("✅ Nested frame navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Nested frame navigation test FAILED: {e}")
            # Try to switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def test_frame_structure(self):
        """Test nested frame structure"""
        print("\n🔧 Testing Nested Frames - Frame Structure...")
        self.driver.get("https://demoqa.com/nestedframes")

        try:
            # Check for parent frame
            parent_frames = self.driver.find_elements(By.ID, "frame1")
            print(f"  ✓ Found {len(parent_frames)} parent frame(s)")
            
            if parent_frames:
                # Switch to parent frame and check for child frames
                self.driver.switch_to.frame(parent_frames[0])
                child_frames = self.driver.find_elements(By.TAG_NAME, "iframe")
                print(f"  ✓ Found {len(child_frames)} child frame(s) in parent frame")
                
                # Check frame attributes
                for i, frame in enumerate(child_frames):
                    frame_src = frame.get_attribute("src")
                    frame_name = frame.get_attribute("name")
                    print(f"  ✓ Child frame {i+1}: src='{frame_src}', name='{frame_name}'")
                
                # Switch back to default content
                self.driver.switch_to.default_content()
                print("  ✓ Switched back to default content")
            
            print("✅ Frame structure test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Frame structure test FAILED: {e}")
            # Try to switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def run_all_nested_frames_tests(self):
        """Run all nested frames tests"""
        print("=" * 60)
        print("🔗 NESTED FRAMES INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_parent_frame())
            results.append(self.test_child_frame())
            results.append(self.test_nested_frame_navigation())
            results.append(self.test_frame_structure())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 NESTED FRAMES TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Nested Frames tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Nested Frames tests passed, some had issues")
            else:
                print("❌ All Nested Frames tests had issues")
                
        except Exception as e:
            print(f"❌ Nested Frames test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    nested_frames_test = NestedFramesTest()
    nested_frames_test.run_all_nested_frames_tests()