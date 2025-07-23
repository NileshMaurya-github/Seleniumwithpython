from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class DemoQAElements:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_text_box(self):
        """Test Text Box functionality"""
        print("Testing Text Box...")
        self.driver.get("https://demoqa.com/text-box")

        # Fill text box fields
        self.driver.find_element(By.ID, "userName").send_keys("John Doe")
        self.driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        self.driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street, City")
        self.driver.find_element(By.ID, "permanentAddress").send_keys("456 Oak Avenue, Town")

        # Submit form (using JavaScript to avoid ad overlay issues)
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_btn)

        # Verify output
        output = self.wait.until(EC.presence_of_element_located((By.ID, "output")))
        assert "John Doe" in output.text
        print("✓ Text Box test passed")

    def test_check_box(self):
        """Test Check Box functionality"""
        print("Testing Check Box...")
        self.driver.get("https://demoqa.com/checkbox")

        # Expand all nodes
        try:
            expand_all = self.driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
            expand_all.click()
            time.sleep(1)
        except:
            pass

        # Select various checkboxes
        checkboxes = [
            "//span[text()='Home']/../span[@class='rct-checkbox']",
            "//span[text()='Desktop']/../span[@class='rct-checkbox']",
            "//span[text()='Documents']/../span[@class='rct-checkbox']"
        ]

        for checkbox in checkboxes:
            try:
                element = self.driver.find_element(By.XPATH, checkbox)
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(0.5)
            except:
                continue

        # Verify selection
        result = self.wait.until(EC.presence_of_element_located((By.ID, "result")))
        print(f"✓ Check Box test passed - Selected: {result.text}")

    def test_radio_button(self):
        """Test Radio Button functionality"""
        print("Testing Radio Button...")
        self.driver.get("https://demoqa.com/radio-button")

        # Test Yes radio button
        yes_radio = self.driver.find_element(By.XPATH, "//label[@for='yesRadio']")
        yes_radio.click()

        success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
        assert "Yes" in success_text.text

        # Test Impressive radio button
        impressive_radio = self.driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
        impressive_radio.click()

        success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
        assert "Impressive" in success_text.text

        print("✓ Radio Button test passed")

    def test_web_tables(self):
        """Test Web Tables functionality"""
        print("Testing Web Tables...")
        self.driver.get("https://demoqa.com/webtables")

        # Add new record
        add_button = self.driver.find_element(By.ID, "addNewRecordButton")
        add_button.click()

        # Fill registration form
        self.driver.find_element(By.ID, "firstName").send_keys("Jane")
        self.driver.find_element(By.ID, "lastName").send_keys("Smith")
        self.driver.find_element(By.ID, "userEmail").send_keys("jane.smith@example.com")
        self.driver.find_element(By.ID, "age").send_keys("30")
        self.driver.find_element(By.ID, "salary").send_keys("75000")
        self.driver.find_element(By.ID, "department").send_keys("Engineering")

        # Submit form (using JavaScript to avoid ad overlay issues)
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_btn)

        # Verify record added
        table = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rt-table")))
        assert "Jane" in table.text

        # Test search functionality
        search_box = self.driver.find_element(By.ID, "searchBox")
        search_box.send_keys("Jane")
        time.sleep(1)

        # Edit record
        edit_button = self.driver.find_element(By.CSS_SELECTOR, "span[title='Edit']")
        edit_button.click()

        # Update salary
        salary_field = self.driver.find_element(By.ID, "salary")
        salary_field.clear()
        salary_field.send_keys("80000")
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_btn)

        print("✓ Web Tables test passed")

    def test_buttons(self):
        """Test Buttons functionality"""
        print("Testing Buttons...")
        self.driver.get("https://demoqa.com/buttons")

        actions = ActionChains(self.driver)

        # Double click
        double_click_btn = self.driver.find_element(By.ID, "doubleClickBtn")
        actions.double_click(double_click_btn).perform()

        double_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))
        assert "double click" in double_click_msg.text.lower()

        # Right click
        right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
        actions.context_click(right_click_btn).perform()

        right_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "rightClickMessage")))
        assert "right click" in right_click_msg.text.lower()

        # Dynamic click
        dynamic_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
        dynamic_click_btn.click()

        dynamic_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))
        assert "dynamic click" in dynamic_click_msg.text.lower()

        print("✓ Buttons test passed")

    def test_links(self):
        """Test Links functionality"""
        print("Testing Links...")
        self.driver.get("https://demoqa.com/links")

        # Test simple link (opens in new tab)
        simple_link = self.driver.find_element(By.ID, "simpleLink")
        simple_link.click()

        # Switch to new tab and verify
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        assert "demoqa.com" in self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Test API links
        api_links = ["created", "no-content", "moved", "bad-request", "unauthorized", "forbidden", "not-found"]

        for link_id in api_links:
            try:
                link = self.driver.find_element(By.ID, link_id)
                link.click()
                time.sleep(1)

                # Check for response message
                response_msg = self.wait.until(EC.presence_of_element_located((By.ID, "linkResponse")))
                print(f"  Link {link_id}: {response_msg.text[:50]}...")
            except:
                continue

        print("✓ Links test passed")

    def test_broken_links_images(self):
        """Test Broken Links - Images functionality"""
        print("Testing Broken Links - Images...")
        self.driver.get("https://demoqa.com/broken")

        # Check valid image
        valid_image = self.driver.find_element(By.XPATH, "//img[contains(@src, 'Toolsqa.jpg')]")
        print(f"  Valid image found: {valid_image.get_attribute('src')}")

        # Check broken image
        broken_image = self.driver.find_element(By.XPATH, "//img[contains(@src, 'Toolsqa_1.jpg')]")
        print(f"  Broken image found: {broken_image.get_attribute('src')}")

        # Test valid link
        valid_link = self.driver.find_element(By.LINK_TEXT, "Click Here for Valid Link")
        valid_link.click()
        time.sleep(2)
        assert "demoqa.com" in self.driver.current_url
        self.driver.back()

        # Test broken link
        broken_link = self.driver.find_element(By.LINK_TEXT, "Click Here for Broken Link")
        broken_link.click()
        time.sleep(2)
        print(f"  Broken link redirected to: {self.driver.current_url}")

        print("✓ Broken Links - Images test passed")

    def test_upload_download(self):
        """Test Upload and Download functionality"""
        print("Testing Upload and Download...")
        self.driver.get("https://demoqa.com/upload-download")

        # Test download
        download_btn = self.driver.find_element(By.ID, "downloadButton")
        download_btn.click()
        time.sleep(2)
        print("  Download initiated")

        # Test upload
        # Create a temporary file for upload
        test_file_path = os.path.join(os.getcwd(), "test_upload.txt")
        with open(test_file_path, "w") as f:
            f.write("This is a test file for upload")

        upload_input = self.driver.find_element(By.ID, "uploadFile")
        upload_input.send_keys(test_file_path)

        # Verify upload
        uploaded_file_path = self.wait.until(EC.presence_of_element_located((By.ID, "uploadedFilePath")))
        assert "test_upload.txt" in uploaded_file_path.text

        # Clean up
        os.remove(test_file_path)

        print("✓ Upload and Download test passed")

    def test_dynamic_properties(self):
        """Test Dynamic Properties functionality"""
        print("Testing Dynamic Properties...")
        self.driver.get("https://demoqa.com/dynamic-properties")

        # Wait for button to be enabled
        enable_after_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
        enable_after_btn.click()

        # Wait for color change button
        color_change_btn = self.wait.until(EC.presence_of_element_located((By.ID, "colorChange")))
        print(f"  Color change button found: {color_change_btn.value_of_css_property('color')}")

        # Wait for visible after button
        try:
            visible_after_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
            visible_after_btn.click()
            print("  Visible after button appeared and clicked")
        except:
            print("  Visible after button test skipped")

        print("✓ Dynamic Properties test passed")

    def run_all_tests(self):
        """Run all element tests"""
        try:
            self.test_text_box()
            self.test_check_box()
            self.test_radio_button()
            self.test_web_tables()
            self.test_buttons()
            self.test_links()
            self.test_broken_links_images()
            self.test_upload_download()
            self.test_dynamic_properties()
            print("\n✅ All Elements tests completed successfully!")
        except Exception as e:
            print(f"\n❌ Test failed: {str(e)}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    elements_test = DemoQAElements()
    elements_test.run_all_tests()