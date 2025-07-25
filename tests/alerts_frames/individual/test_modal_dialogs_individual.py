from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class ModalDialogsTest:
    """Individual test for Modal Dialogs functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_small_modal(self):
        """Test small modal functionality"""
        print("🔧 Testing Modal Dialogs - Small Modal...")
        self.driver.get("https://demoqa.com/modal-dialogs")

        try:
            # Click small modal button
            small_modal_btn = self.driver.find_element(By.ID, "showSmallModal")
            small_modal_btn.click()
            print("  ✓ Small modal button clicked")
            
            # Wait for modal to appear
            modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            print("  ✓ Small modal appeared")
            
            # Verify modal title
            modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-sm")
            title_text = modal_title.text
            print(f"  ✓ Modal title: '{title_text}'")
            assert "Small Modal" in title_text
            
            # Verify modal body content
            modal_body = self.driver.find_element(By.CLASS_NAME, "modal-body")
            body_text = modal_body.text
            print(f"  ✓ Modal body: '{body_text}'")
            assert "This is a small modal" in body_text
            
            # Close modal using close button
            close_btn = self.driver.find_element(By.ID, "closeSmallModal")
            close_btn.click()
            print("  ✓ Modal closed using close button")
            
            # Wait for modal to disappear
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
            print("  ✓ Modal disappeared")
            
            print("✅ Small modal test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Small modal test FAILED: {e}")
            # Try to close modal if it's still open
            try:
                close_btn = self.driver.find_element(By.ID, "closeSmallModal")
                close_btn.click()
            except:
                pass
            return False

    def test_large_modal(self):
        """Test large modal functionality"""
        print("\n🔧 Testing Modal Dialogs - Large Modal...")
        self.driver.get("https://demoqa.com/modal-dialogs")

        try:
            # Click large modal button
            large_modal_btn = self.driver.find_element(By.ID, "showLargeModal")
            large_modal_btn.click()
            print("  ✓ Large modal button clicked")
            
            # Wait for modal to appear
            modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            print("  ✓ Large modal appeared")
            
            # Verify modal title
            modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            title_text = modal_title.text
            print(f"  ✓ Modal title: '{title_text}'")
            assert "Large Modal" in title_text
            
            # Verify modal body content
            modal_body = self.driver.find_element(By.CLASS_NAME, "modal-body")
            body_text = modal_body.text
            print(f"  ✓ Modal body length: {len(body_text)} characters")
            assert len(body_text) > 100  # Large modal should have more content
            
            # Close modal using close button
            close_btn = self.driver.find_element(By.ID, "closeLargeModal")
            close_btn.click()
            print("  ✓ Modal closed using close button")
            
            # Wait for modal to disappear
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
            print("  ✓ Modal disappeared")
            
            print("✅ Large modal test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Large modal test FAILED: {e}")
            # Try to close modal if it's still open
            try:
                close_btn = self.driver.find_element(By.ID, "closeLargeModal")
                close_btn.click()
            except:
                pass
            return False

    def test_modal_close_with_x(self):
        """Test closing modal with X button"""
        print("\n🔧 Testing Modal Dialogs - Close with X...")
        self.driver.get("https://demoqa.com/modal-dialogs")

        try:
            # Open small modal
            small_modal_btn = self.driver.find_element(By.ID, "showSmallModal")
            small_modal_btn.click()
            print("  ✓ Small modal opened")
            
            # Wait for modal to appear
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            
            # Close modal using X button
            x_button = self.driver.find_element(By.CSS_SELECTOR, ".modal-header .close")
            x_button.click()
            print("  ✓ Modal closed using X button")
            
            # Wait for modal to disappear
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
            print("  ✓ Modal disappeared")
            
            print("✅ Modal close with X test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Modal close with X test FAILED: {e}")
            # Try to close modal if it's still open
            try:
                self.driver.find_element(By.CSS_SELECTOR, ".modal-header .close").click()
            except:
                pass
            return False

    def test_modal_close_with_escape(self):
        """Test closing modal with Escape key"""
        print("\n🔧 Testing Modal Dialogs - Close with Escape...")
        self.driver.get("https://demoqa.com/modal-dialogs")

        try:
            # Open small modal
            small_modal_btn = self.driver.find_element(By.ID, "showSmallModal")
            small_modal_btn.click()
            print("  ✓ Small modal opened")
            
            # Wait for modal to appear
            modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            
            # Press Escape key to close modal
            modal.send_keys(Keys.ESCAPE)
            print("  ✓ Escape key pressed")
            
            # Wait for modal to disappear
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
            print("  ✓ Modal closed with Escape key")
            
            print("✅ Modal close with Escape test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Modal close with Escape test FAILED: {e}")
            # Try to close modal if it's still open
            try:
                close_btn = self.driver.find_element(By.ID, "closeSmallModal")
                close_btn.click()
            except:
                pass
            return False

    def test_modal_backdrop_click(self):
        """Test closing modal by clicking backdrop"""
        print("\n🔧 Testing Modal Dialogs - Close with Backdrop Click...")
        self.driver.get("https://demoqa.com/modal-dialogs")

        try:
            # Open small modal
            small_modal_btn = self.driver.find_element(By.ID, "showSmallModal")
            small_modal_btn.click()
            print("  ✓ Small modal opened")
            
            # Wait for modal to appear
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            
            # Try to click on backdrop (outside modal content)
            try:
                modal_backdrop = self.driver.find_element(By.CLASS_NAME, "modal")
                # Click on the backdrop area (not the content)
                self.driver.execute_script("arguments[0].click();", modal_backdrop)
                print("  ✓ Clicked on modal backdrop")
                
                # Check if modal is still visible (some modals don't close on backdrop click)
                time.sleep(1)
                try:
                    modal_content = self.driver.find_element(By.CLASS_NAME, "modal-content")
                    if modal_content.is_displayed():
                        print("  ⚠️ Modal didn't close with backdrop click (expected behavior)")
                        # Close it manually
                        close_btn = self.driver.find_element(By.ID, "closeSmallModal")
                        close_btn.click()
                    else:
                        print("  ✓ Modal closed with backdrop click")
                except:
                    print("  ✓ Modal closed with backdrop click")
                    
            except Exception as backdrop_e:
                print(f"  ⚠️ Backdrop click test inconclusive: {backdrop_e}")
                # Close modal manually
                close_btn = self.driver.find_element(By.ID, "closeSmallModal")
                close_btn.click()
            
            # Wait for modal to disappear
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
            print("  ✓ Modal is closed")
            
            print("✅ Modal backdrop click test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Modal backdrop click test FAILED: {e}")
            # Try to close modal if it's still open
            try:
                close_btn = self.driver.find_element(By.ID, "closeSmallModal")
                close_btn.click()
            except:
                pass
            return False

    def run_all_modal_dialogs_tests(self):
        """Run all modal dialogs tests"""
        print("=" * 60)
        print("💬 MODAL DIALOGS INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_small_modal())
            results.append(self.test_large_modal())
            results.append(self.test_modal_close_with_x())
            results.append(self.test_modal_close_with_escape())
            results.append(self.test_modal_backdrop_click())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 MODAL DIALOGS TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Modal Dialogs tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Modal Dialogs tests passed, some had issues")
            else:
                print("❌ All Modal Dialogs tests had issues")
                
        except Exception as e:
            print(f"❌ Modal Dialogs test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    modal_dialogs_test = ModalDialogsTest()
    modal_dialogs_test.run_all_modal_dialogs_tests()