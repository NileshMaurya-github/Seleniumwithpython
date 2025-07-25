import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time


@allure.epic("DemoQA Automation")
@allure.feature("Alerts, Frames & Windows")
class TestAlertsFramesWindows:
    """Allure test suite for Alerts, Frames & Windows functionality"""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to initialize WebDriver"""
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.story("Browser Windows")
    @allure.title("Test New Tab Functionality")
    @allure.description("Verify that new tab opens correctly and contains expected content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_new_tab(self):
        with allure.step("Navigate to Browser Windows page"):
            self.driver.get("https://demoqa.com/browser-windows")
            
        with allure.step("Get original window handle"):
            original_window = self.driver.current_window_handle
            allure.attach(original_window, "Original Window Handle", allure.attachment_type.TEXT)
            
        with allure.step("Click new tab button"):
            new_tab_btn = self.driver.find_element(By.ID, "tabButton")
            new_tab_btn.click()
            
        with allure.step("Wait for new tab and switch to it"):
            self.wait.until(EC.number_of_windows_to_be(2))
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
                    
        with allure.step("Verify new tab content"):
            page_text = self.wait.until(EC.presence_of_element_located((By.ID, "sampleHeading")))
            assert "This is a sample page" in page_text.text
            allure.attach(page_text.text, "New Tab Content", allure.attachment_type.TEXT)
            
        with allure.step("Close new tab and return to original window"):
            self.driver.close()
            self.driver.switch_to.window(original_window)

    @allure.story("Browser Windows")
    @allure.title("Test New Window Functionality")
    @allure.description("Verify that new window opens correctly and contains expected content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_new_window(self):
        with allure.step("Navigate to Browser Windows page"):
            self.driver.get("https://demoqa.com/browser-windows")
            
        with allure.step("Get original window handle"):
            original_window = self.driver.current_window_handle
            
        with allure.step("Click new window button"):
            new_window_btn = self.driver.find_element(By.ID, "windowButton")
            new_window_btn.click()
            
        with allure.step("Wait for new window and switch to it"):
            self.wait.until(EC.number_of_windows_to_be(2))
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
                    
        with allure.step("Verify new window content"):
            page_text = self.wait.until(EC.presence_of_element_located((By.ID, "sampleHeading")))
            assert "This is a sample page" in page_text.text
            allure.attach(page_text.text, "New Window Content", allure.attachment_type.TEXT)
            
        with allure.step("Close new window and return to original window"):
            self.driver.close()
            self.driver.switch_to.window(original_window)

    @allure.story("Alerts")
    @allure.title("Test Simple Alert")
    @allure.description("Verify simple alert functionality and text content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_simple_alert(self):
        with allure.step("Navigate to Alerts page"):
            self.driver.get("https://demoqa.com/alerts")
            
        with allure.step("Click simple alert button"):
            alert_btn = self.driver.find_element(By.ID, "alertButton")
            alert_btn.click()
            
        with allure.step("Handle alert and verify text"):
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            allure.attach(alert_text, "Alert Text", allure.attachment_type.TEXT)
            assert "You clicked a button" in alert_text
            alert.accept()

    @allure.story("Alerts")
    @allure.title("Test Timer Alert")
    @allure.description("Verify timer alert appears after delay and contains expected text")
    @allure.severity(allure.severity_level.NORMAL)
    def test_timer_alert(self):
        with allure.step("Navigate to Alerts page"):
            self.driver.get("https://demoqa.com/alerts")
            
        with allure.step("Click timer alert button"):
            timer_alert_btn = self.driver.find_element(By.ID, "timerAlertButton")
            timer_alert_btn.click()
            
        with allure.step("Wait for timer alert and verify text"):
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            allure.attach(alert_text, "Timer Alert Text", allure.attachment_type.TEXT)
            assert "This alert appeared after 5 seconds" in alert_text
            alert.accept()

    @allure.story("Alerts")
    @allure.title("Test Confirm Alert - Accept")
    @allure.description("Verify confirm alert accept functionality and result message")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_confirm_alert_accept(self):
        with allure.step("Navigate to Alerts page"):
            self.driver.get("https://demoqa.com/alerts")
            
        with allure.step("Click confirm alert button"):
            confirm_btn = self.driver.find_element(By.ID, "confirmButton")
            confirm_btn.click()
            
        with allure.step("Accept confirm alert"):
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            allure.attach(alert_text, "Confirm Alert Text", allure.attachment_type.TEXT)
            assert "Do you confirm action?" in alert_text
            alert.accept()
            
        with allure.step("Verify result message"):
            result = self.driver.find_element(By.ID, "confirmResult")
            assert "You selected Ok" in result.text
            allure.attach(result.text, "Confirm Result", allure.attachment_type.TEXT)

    @allure.story("Alerts")
    @allure.title("Test Prompt Alert")
    @allure.description("Verify prompt alert functionality with text input")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_prompt_alert(self):
        with allure.step("Navigate to Alerts page"):
            self.driver.get("https://demoqa.com/alerts")
            
        with allure.step("Click prompt alert button"):
            prompt_btn = self.driver.find_element(By.ID, "promtButton")
            prompt_btn.click()
            
        with allure.step("Handle prompt alert and enter text"):
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            allure.attach(alert_text, "Prompt Alert Text", allure.attachment_type.TEXT)
            assert "Please enter your name" in alert_text
            
            test_name = "Test User"
            alert.send_keys(test_name)
            alert.accept()
            
        with allure.step("Verify prompt result"):
            result = self.driver.find_element(By.ID, "promptResult")
            assert test_name in result.text
            allure.attach(result.text, "Prompt Result", allure.attachment_type.TEXT)

    @allure.story("Frames")
    @allure.title("Test Frame 1")
    @allure.description("Verify frame 1 content and switching functionality")
    @allure.severity(allure.severity_level.NORMAL)
    def test_frame1(self):
        with allure.step("Navigate to Frames page"):
            self.driver.get("https://demoqa.com/frames")
            
        with allure.step("Switch to frame 1"):
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
            
        with allure.step("Verify frame 1 content"):
            frame_content = self.driver.find_element(By.ID, "sampleHeading")
            frame_text = frame_content.text
            allure.attach(frame_text, "Frame 1 Content", allure.attachment_type.TEXT)
            assert "This is a sample page" in frame_text
            
        with allure.step("Switch back to default content"):
            self.driver.switch_to.default_content()

    @allure.story("Frames")
    @allure.title("Test Frame 2")
    @allure.description("Verify frame 2 content and switching functionality")
    @allure.severity(allure.severity_level.NORMAL)
    def test_frame2(self):
        with allure.step("Navigate to Frames page"):
            self.driver.get("https://demoqa.com/frames")
            
        with allure.step("Switch to frame 2"):
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))
            
        with allure.step("Verify frame 2 content"):
            frame_content = self.driver.find_element(By.ID, "sampleHeading")
            frame_text = frame_content.text
            allure.attach(frame_text, "Frame 2 Content", allure.attachment_type.TEXT)
            assert "This is a sample page" in frame_text
            
        with allure.step("Switch back to default content"):
            self.driver.switch_to.default_content()

    @allure.story("Nested Frames")
    @allure.title("Test Parent Frame")
    @allure.description("Verify parent frame accessibility and content")
    @allure.severity(allure.severity_level.NORMAL)
    def test_parent_frame(self):
        with allure.step("Navigate to Nested Frames page"):
            self.driver.get("https://demoqa.com/nestedframes")
            
        with allure.step("Switch to parent frame"):
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
            
        with allure.step("Verify parent frame is accessible"):
            frame_body = self.driver.find_element(By.TAG_NAME, "body")
            frame_text = frame_body.text
            allure.attach(frame_text, "Parent Frame Content", allure.attachment_type.TEXT)
            
        with allure.step("Switch back to default content"):
            self.driver.switch_to.default_content()

    @allure.story("Modal Dialogs")
    @allure.title("Test Small Modal")
    @allure.description("Verify small modal functionality and content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_small_modal(self):
        with allure.step("Navigate to Modal Dialogs page"):
            self.driver.get("https://demoqa.com/modal-dialogs")
            
        with allure.step("Click small modal button"):
            small_modal_btn = self.driver.find_element(By.ID, "showSmallModal")
            small_modal_btn.click()
            
        with allure.step("Verify modal appears and check content"):
            modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            
            modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-sm")
            title_text = modal_title.text
            allure.attach(title_text, "Modal Title", allure.attachment_type.TEXT)
            assert "Small Modal" in title_text
            
            modal_body = self.driver.find_element(By.CLASS_NAME, "modal-body")
            body_text = modal_body.text
            allure.attach(body_text, "Modal Body", allure.attachment_type.TEXT)
            assert "This is a small modal" in body_text
            
        with allure.step("Close modal"):
            close_btn = self.driver.find_element(By.ID, "closeSmallModal")
            close_btn.click()
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))

    @allure.story("Modal Dialogs")
    @allure.title("Test Large Modal")
    @allure.description("Verify large modal functionality and content")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_large_modal(self):
        with allure.step("Navigate to Modal Dialogs page"):
            self.driver.get("https://demoqa.com/modal-dialogs")
            
        with allure.step("Click large modal button"):
            large_modal_btn = self.driver.find_element(By.ID, "showLargeModal")
            large_modal_btn.click()
            
        with allure.step("Verify modal appears and check content"):
            modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            
            modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            title_text = modal_title.text
            allure.attach(title_text, "Modal Title", allure.attachment_type.TEXT)
            assert "Large Modal" in title_text
            
            modal_body = self.driver.find_element(By.CLASS_NAME, "modal-body")
            body_text = modal_body.text
            allure.attach(f"Body length: {len(body_text)} characters", "Modal Body Info", allure.attachment_type.TEXT)
            assert len(body_text) > 100  # Large modal should have more content
            
        with allure.step("Close modal"):
            close_btn = self.driver.find_element(By.ID, "closeLargeModal")
            close_btn.click()
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))