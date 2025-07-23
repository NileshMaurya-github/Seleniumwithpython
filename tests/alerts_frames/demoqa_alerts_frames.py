from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class DemoQAAlertsFrames:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_browser_windows(self):
        """Test Browser Windows functionality"""
        print("Testing Browser Windows...")
        self.driver.get("https://demoqa.com/browser-windows")

        # Test new tab
        new_tab_btn = self.driver.find_element(By.ID, "tabButton")
        new_tab_btn.click()

        # Switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

        # Verify new tab content
        page_text = self.driver.find_element(By.ID, "sampleHeading")
        assert "This is a sample page" in page_text.text
        print("  ✓ New tab opened successfully")

        # Close new tab and switch back
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Test new window
        new_window_btn = self.driver.find_element(By.ID, "windowButton")
        new_window_btn.click()

        # Switch to new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

        # Verify new window content
        page_text = self.driver.find_element(By.ID, "sampleHeading")
        assert "This is a sample page" in page_text.text
        print("  ✓ New window opened successfully")

        # Close new window and switch back
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        print("✓ Browser Windows test passed")

    def test_alerts(self):
        """Test Alerts functionality"""
        print("Testing Alerts...")
        self.driver.get("https://demoqa.com/alerts")

        # Test simple alert
        alert_btn = self.driver.find_element(By.ID, "alertButton")
        alert_btn.click()

        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert "You clicked a button" in alert_text
        alert.accept()
        print("  ✓ Simple alert handled")

        # Test timer alert
        timer_alert_btn = self.driver.find_element(By.ID, "timerAlertButton")
        timer_alert_btn.click()

        # Wait for timer alert (appears after 5 seconds)
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert "This alert appeared after 5 seconds" in alert_text
        alert.accept()
        print("  ✓ Timer alert handled")

        # Test confirm alert - Accept
        confirm_btn = self.driver.find_element(By.ID, "confirmButton")
        confirm_btn.click()

        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

        confirm_result = self.driver.find_element(By.ID, "confirmResult")
        assert "You selected Ok" in confirm_result.text
        print("  ✓ Confirm alert (Accept) handled")

        # Test confirm alert - Dismiss
        confirm_btn.click()
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()

        confirm_result = self.driver.find_element(By.ID, "confirmResult")
        assert "You selected Cancel" in confirm_result.text
        print("  ✓ Confirm alert (Dismiss) handled")

        # Test prompt alert
        prompt_btn = self.driver.find_element(By.ID, "promtButton")
        prompt_btn.click()

        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys("Test User")
        alert.accept()

        prompt_result = self.driver.find_element(By.ID, "promptResult")
        assert "You entered Test User" in prompt_result.text
        print("  ✓ Prompt alert handled")

        print("✓ Alerts test passed")

    def test_frames(self):
        """Test Frames functionality"""
        print("Testing Frames...")
        self.driver.get("https://demoqa.com/frames")

        # Test frame 1
        frame1 = self.driver.find_element(By.ID, "frame1")
        self.driver.switch_to.frame(frame1)

        frame_text = self.driver.find_element(By.ID, "sampleHeading")
        assert "This is a sample page" in frame_text.text
        print("  ✓ Frame 1 content verified")

        # Switch back to main content
        self.driver.switch_to.default_content()

        # Test frame 2
        frame2 = self.driver.find_element(By.ID, "frame2")
        self.driver.switch_to.frame(frame2)

        frame_text = self.driver.find_element(By.ID, "sampleHeading")
        assert "This is a sample page" in frame_text.text
        print("  ✓ Frame 2 content verified")

        # Switch back to main content
        self.driver.switch_to.default_content()

        print("✓ Frames test passed")

    def test_nested_frames(self):
        """Test Nested Frames functionality"""
        print("Testing Nested Frames...")
        self.driver.get("https://demoqa.com/nestedframes")

        # Switch to parent frame
        parent_frame = self.driver.find_element(By.ID, "frame1")
        self.driver.switch_to.frame(parent_frame)

        parent_text = self.driver.find_element(By.TAG_NAME, "body")
        print(f"  Parent frame text: {parent_text.text}")

        # Switch to child frame
        child_frame = self.driver.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(child_frame)

        child_text = self.driver.find_element(By.TAG_NAME, "body")
        print(f"  Child frame text: {child_text.text}")

        # Switch back to main content
        self.driver.switch_to.default_content()

        print("✓ Nested Frames test passed")

    def test_modal_dialogs(self):
        """Test Modal Dialogs functionality"""
        print("Testing Modal Dialogs...")
        self.driver.get("https://demoqa.com/modal-dialogs")

        # Test small modal
        small_modal_btn = self.driver.find_element(By.ID, "showSmallModal")
        small_modal_btn.click()

        # Verify modal is displayed
        modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-sm")
        assert "Small Modal" in modal_title.text
        print("  ✓ Small modal opened")

        # Close modal
        close_btn = self.driver.find_element(By.ID, "closeSmallModal")
        close_btn.click()

        # Wait for modal to disappear
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
        print("  ✓ Small modal closed")

        # Test large modal
        large_modal_btn = self.driver.find_element(By.ID, "showLargeModal")
        large_modal_btn.click()

        # Verify modal is displayed
        modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
        assert "Large Modal" in modal_title.text
        print("  ✓ Large modal opened")

        # Close modal using X button
        close_x_btn = self.driver.find_element(By.CSS_SELECTOR, ".close")
        close_x_btn.click()

        # Wait for modal to disappear
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
        print("  ✓ Large modal closed")

        print("✓ Modal Dialogs test passed")

    def run_all_tests(self):
        """Run all alerts, frames and windows tests"""
        try:
            self.test_browser_windows()
            self.test_alerts()
            self.test_frames()
            self.test_nested_frames()
            self.test_modal_dialogs()
            print("\n✅ All Alerts, Frame & Windows tests completed successfully!")
        except Exception as e:
            print(f"\n❌ Test failed: {str(e)}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    alerts_frames_test = DemoQAAlertsFrames()
    alerts_frames_test.run_all_tests()