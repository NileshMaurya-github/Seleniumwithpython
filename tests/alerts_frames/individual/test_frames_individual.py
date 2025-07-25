from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FramesTest:
    """Individual test for Frames functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_frame1(self):
        """Test frame1 functionality"""
        print("🔧 Testing Frames - Frame 1...")
        self.driver.get("https://demoqa.com/frames")

        try:
            # Switch to frame1
            frame1 = self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
            print("  ✓ Switched to frame1")
            
            # Find and verify content in frame1
            frame_content = self.driver.find_element(By.ID, "sampleHeading")
            frame_text = frame_content.text
            print(f"  ✓ Frame1 content: '{frame_text}'")
            
            # Verify frame content
            assert "This is a sample page" in frame_text
            
            # Get frame size info
            frame_size = self.driver.get_window_size()
            print(f"  ✓ Frame1 dimensions: {frame_size}")
            
            # Switch back to default content
            self.driver.switch_to.default_content()
            print("  ✓ Switched back to default content")
            
            print("✅ Frame1 test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Frame1 test FAILED: {e}")
            # Try to switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def test_frame2(self):
        """Test frame2 functionality"""
        print("\n🔧 Testing Frames - Frame 2...")
        self.driver.get("https://demoqa.com/frames")

        try:
            # Switch to frame2
            frame2 = self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))
            print("  ✓ Switched to frame2")
            
            # Find and verify content in frame2
            frame_content = self.driver.find_element(By.ID, "sampleHeading")
            frame_text = frame_content.text
            print(f"  ✓ Frame2 content: '{frame_text}'")
            
            # Verify frame content
            assert "This is a sample page" in frame_text
            
            # Get frame size info
            frame_size = self.driver.get_window_size()
            print(f"  ✓ Frame2 dimensions: {frame_size}")
            
            # Switch back to default content
            self.driver.switch_to.default_content()
            print("  ✓ Switched back to default content")
            
            print("✅ Frame2 test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Frame2 test FAILED: {e}")
            # Try to switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def test_frame_switching(self):
        """Test switching between frames"""
        print("\n🔧 Testing Frames - Frame Switching...")
        self.driver.get("https://demoqa.com/frames")

        try:
            # Switch to frame1
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
            frame1_content = self.driver.find_element(By.ID, "sampleHeading").text
            print(f"  ✓ Frame1 content: '{frame1_content}'")
            
            # Switch back to default content
            self.driver.switch_to.default_content()
            print("  ✓ Switched back to default content")
            
            # Switch to frame2
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))
            frame2_content = self.driver.find_element(By.ID, "sampleHeading").text
            print(f"  ✓ Frame2 content: '{frame2_content}'")
            
            # Verify both frames have the same content
            assert frame1_content == frame2_content
            print("  ✓ Both frames contain the same content")
            
            # Switch back to default content
            self.driver.switch_to.default_content()
            print("  ✓ Final switch back to default content")
            
            print("✅ Frame switching test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Frame switching test FAILED: {e}")
            # Try to switch back to default content
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def test_frame_properties(self):
        """Test frame properties and attributes"""
        print("\n🔧 Testing Frames - Frame Properties...")
        self.driver.get("https://demoqa.com/frames")

        try:
            # Get frame1 element and check its properties
            frame1_element = self.driver.find_element(By.ID, "frame1")
            frame1_width = frame1_element.get_attribute("width")
            frame1_height = frame1_element.get_attribute("height")
            print(f"  ✓ Frame1 dimensions: {frame1_width}x{frame1_height}")
            
            # Get frame2 element and check its properties
            frame2_element = self.driver.find_element(By.ID, "frame2")
            frame2_width = frame2_element.get_attribute("width")
            frame2_height = frame2_element.get_attribute("height")
            print(f"  ✓ Frame2 dimensions: {frame2_width}x{frame2_height}")
            
            # Verify frames have different sizes
            if frame1_width and frame2_width:
                print(f"  ✓ Frame1 width: {frame1_width}, Frame2 width: {frame2_width}")
            
            if frame1_height and frame2_height:
                print(f"  ✓ Frame1 height: {frame1_height}, Frame2 height: {frame2_height}")
            
            print("✅ Frame properties test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Frame properties test FAILED: {e}")
            return False

    def run_all_frames_tests(self):
        """Run all frames tests"""
        print("=" * 60)
        print("🖼️ FRAMES INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_frame1())
            results.append(self.test_frame2())
            results.append(self.test_frame_switching())
            results.append(self.test_frame_properties())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 FRAMES TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Frames tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Frames tests passed, some had issues")
            else:
                print("❌ All Frames tests had issues")
                
        except Exception as e:
            print(f"❌ Frames test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    frames_test = FramesTest()
    frames_test.run_all_frames_tests()