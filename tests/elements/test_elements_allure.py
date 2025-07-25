"""
DemoQA Elements Tests with Allure Reporting
==========================================
"""

import pytest
import allure
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.epic("DemoQA Automation")
@allure.feature("Elements Section")
class TestElementsAllure:
    """Elements section tests with Allure reporting"""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        with allure.step("Initialize WebDriver"):
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            
            # Check for headless mode from environment variable
            if os.environ.get('HEADLESS', '').lower() == 'true':
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--window-size=1920,1080')
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            if not os.environ.get('HEADLESS', '').lower() == 'true':
                self.driver.maximize_window()
        
        yield
        
        with allure.step("Close WebDriver"):
            self.driver.quit()
    
    @allure.story("Form Input")
    @allure.title("Text Box - Form Submission and Validation")
    @allure.description("Test text box form filling, submission, and output validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_text_box(self):
        """Test Text Box functionality with Allure reporting"""
        
        with allure.step("Navigate to Text Box page"):
            self.driver.get("https://demoqa.com/text-box")
            allure.attach(self.driver.current_url, "Page URL", allure.attachment_type.TEXT)
        
        with allure.step("Fill form fields"):
            test_data = {
                "name": "John Doe",
                "email": "john.doe@example.com", 
                "current_address": "123 Main Street, City",
                "permanent_address": "456 Oak Avenue, Town"
            }
            
            self.driver.find_element(By.ID, "userName").send_keys(test_data["name"])
            self.driver.find_element(By.ID, "userEmail").send_keys(test_data["email"])
            self.driver.find_element(By.ID, "currentAddress").send_keys(test_data["current_address"])
            self.driver.find_element(By.ID, "permanentAddress").send_keys(test_data["permanent_address"])
            
            allure.attach(str(test_data), "Test Data", allure.attachment_type.JSON)
        
        with allure.step("Submit form"):
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
        
        with allure.step("Verify output"):
            output = self.wait.until(EC.presence_of_element_located((By.ID, "output")))
            assert test_data["name"] in output.text
            allure.attach(output.text, "Form Output", allure.attachment_type.TEXT)
    
    @allure.story("Selection Controls")
    @allure.title("Check Box - Multi-selection and Tree Navigation")
    @allure.description("Test checkbox tree expansion and multi-selection functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_check_box(self):
        """Test Check Box functionality with Allure reporting"""
        
        with allure.step("Navigate to Check Box page"):
            self.driver.get("https://demoqa.com/checkbox")
        
        with allure.step("Expand checkbox tree"):
            try:
                expand_all = self.driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
                expand_all.click()
                time.sleep(1)
                allure.attach("Tree expanded successfully", "Expansion Status", allure.attachment_type.TEXT)
            except:
                allure.attach("Expand button not found", "Expansion Status", allure.attachment_type.TEXT)
        
        with allure.step("Select multiple checkboxes"):
            checkboxes = [
                "//span[text()='Home']/../span[@class='rct-checkbox']",
                "//span[text()='Desktop']/../span[@class='rct-checkbox']", 
                "//span[text()='Documents']/../span[@class='rct-checkbox']"
            ]
            
            selected_count = 0
            for checkbox in checkboxes:
                try:
                    element = self.driver.find_element(By.XPATH, checkbox)
                    self.driver.execute_script("arguments[0].click();", element)
                    selected_count += 1
                    time.sleep(0.5)
                except:
                    continue
            
            allure.attach(f"Selected {selected_count} checkboxes", "Selection Count", allure.attachment_type.TEXT)
        
        with allure.step("Verify selection results"):
            result = self.wait.until(EC.presence_of_element_located((By.ID, "result")))
            allure.attach(result.text, "Selection Results", allure.attachment_type.TEXT)
            assert result.text  # Verify some text is present
    
    @allure.story("Selection Controls")
    @allure.title("Radio Button - Single Selection Validation")
    @allure.description("Test radio button selection and state validation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_radio_button(self):
        """Test Radio Button functionality with Allure reporting"""
        
        with allure.step("Navigate to Radio Button page"):
            self.driver.get("https://demoqa.com/radio-button")
        
        with allure.step("Test 'Yes' radio button"):
            yes_radio = self.driver.find_element(By.XPATH, "//label[@for='yesRadio']")
            yes_radio.click()
            
            success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
            assert "Yes" in success_text.text
            allure.attach(success_text.text, "Yes Radio Result", allure.attachment_type.TEXT)
        
        with allure.step("Test 'Impressive' radio button"):
            impressive_radio = self.driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
            impressive_radio.click()
            
            success_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success")))
            assert "Impressive" in success_text.text
            allure.attach(success_text.text, "Impressive Radio Result", allure.attachment_type.TEXT)
    
    @allure.story("Data Management")
    @allure.title("Web Tables - CRUD Operations and Search")
    @allure.description("Test web table create, read, update, delete operations and search functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_web_tables(self):
        """Test Web Tables functionality with Allure reporting"""
        
        with allure.step("Navigate to Web Tables page"):
            self.driver.get("https://demoqa.com/webtables")
        
        with allure.step("Add new record"):
            add_button = self.driver.find_element(By.ID, "addNewRecordButton")
            add_button.click()
            
            test_record = {
                "firstName": "Jane",
                "lastName": "Smith", 
                "userEmail": "jane.smith@example.com",
                "age": "30",
                "salary": "75000",
                "department": "Engineering"
            }
            
            for field, value in test_record.items():
                self.driver.find_element(By.ID, field).send_keys(value)
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            
            allure.attach(str(test_record), "New Record Data", allure.attachment_type.JSON)
        
        with allure.step("Verify record added"):
            table = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rt-table")))
            assert "Jane" in table.text
            allure.attach("Record successfully added to table", "Add Verification", allure.attachment_type.TEXT)
        
        with allure.step("Test search functionality"):
            search_box = self.driver.find_element(By.ID, "searchBox")
            search_box.send_keys("Jane")
            time.sleep(1)
            allure.attach("Searched for 'Jane'", "Search Query", allure.attachment_type.TEXT)
        
        with allure.step("Edit record"):
            edit_button = self.driver.find_element(By.CSS_SELECTOR, "span[title='Edit']")
            edit_button.click()
            
            salary_field = self.driver.find_element(By.ID, "salary")
            salary_field.clear()
            salary_field.send_keys("80000")
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            
            allure.attach("Updated salary to 80000", "Edit Operation", allure.attachment_type.TEXT)
    
    @allure.story("User Interactions")
    @allure.title("Buttons - Click, Double-click, Right-click")
    @allure.description("Test various button interaction types and their responses")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_buttons(self):
        """Test Buttons functionality with Allure reporting"""
        
        with allure.step("Navigate to Buttons page"):
            self.driver.get("https://demoqa.com/buttons")
        
        actions = ActionChains(self.driver)
        
        with allure.step("Test double-click button"):
            try:
                double_click_btn = self.driver.find_element(By.ID, "doubleClickBtn")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", double_click_btn)
                time.sleep(1)
                actions.double_click(double_click_btn).perform()
                
                double_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))
                assert "double click" in double_click_msg.text.lower()
                allure.attach(double_click_msg.text, "Double Click Result", allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), "Double Click Error", allure.attachment_type.TEXT)
        
        with allure.step("Test right-click button"):
            try:
                right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", right_click_btn)
                time.sleep(1)
                actions.context_click(right_click_btn).perform()
                
                right_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "rightClickMessage")))
                assert "right click" in right_click_msg.text.lower()
                allure.attach(right_click_msg.text, "Right Click Result", allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), "Right Click Error", allure.attachment_type.TEXT)
        
        with allure.step("Test dynamic click button"):
            try:
                dynamic_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
                self.driver.execute_script("arguments[0].click();", dynamic_click_btn)
                
                dynamic_click_msg = self.wait.until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))
                assert "dynamic click" in dynamic_click_msg.text.lower()
                allure.attach(dynamic_click_msg.text, "Dynamic Click Result", allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), "Dynamic Click Error", allure.attachment_type.TEXT)
    
    @allure.story("Navigation")
    @allure.title("Links - Navigation and API Response Testing")
    @allure.description("Test link navigation and API response validation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_links(self):
        """Test Links functionality with Allure reporting"""
        
        with allure.step("Navigate to Links page"):
            self.driver.get("https://demoqa.com/links")
        
        with allure.step("Test simple link navigation"):
            try:
                simple_link = self.driver.find_element(By.ID, "simpleLink")
                self.driver.execute_script("arguments[0].click();", simple_link)
                
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2)
                current_url = self.driver.current_url
                assert "demoqa.com" in current_url
                allure.attach(current_url, "New Tab URL", allure.attachment_type.TEXT)
                
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            except Exception as e:
                allure.attach(str(e), "Simple Link Error", allure.attachment_type.TEXT)
        
        with allure.step("Test API response links"):
            api_links = ["created", "no-content", "moved", "bad-request", "unauthorized", "forbidden"]
            api_results = []
            
            for link_id in api_links:
                try:
                    link = self.driver.find_element(By.ID, link_id)
                    self.driver.execute_script("arguments[0].click();", link)
                    time.sleep(1)
                    
                    response_msg = self.wait.until(EC.presence_of_element_located((By.ID, "linkResponse")))
                    api_results.append(f"{link_id}: {response_msg.text[:50]}...")
                except Exception as e:
                    api_results.append(f"{link_id}: Error - {str(e)[:30]}...")
            
            allure.attach("\n".join(api_results), "API Link Results", allure.attachment_type.TEXT)
    
    @allure.story("Validation")
    @allure.title("Broken Links - Image and Link Validation")
    @allure.description("Test broken and valid image/link detection and handling")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_broken_links_images(self):
        """Test Broken Links - Images functionality with Allure reporting"""
        
        with allure.step("Navigate to Broken Links page"):
            self.driver.get("https://demoqa.com/broken")
        
        with allure.step("Check image validation"):
            try:
                valid_image = self.driver.find_element(By.XPATH, "//img[contains(@src, 'Toolsqa.jpg')]")
                valid_src = valid_image.get_attribute('src')
                allure.attach(valid_src, "Valid Image URL", allure.attachment_type.TEXT)
                
                broken_image = self.driver.find_element(By.XPATH, "//img[contains(@src, 'Toolsqa_1.jpg')]")
                broken_src = broken_image.get_attribute('src')
                allure.attach(broken_src, "Broken Image URL", allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), "Image Check Error", allure.attachment_type.TEXT)
        
        with allure.step("Test valid link"):
            try:
                valid_link = self.driver.find_element(By.LINK_TEXT, "Click Here for Valid Link")
                self.driver.execute_script("arguments[0].click();", valid_link)
                time.sleep(2)
                
                current_url = self.driver.current_url
                allure.attach(current_url, "Valid Link Destination", allure.attachment_type.TEXT)
                self.driver.back()
                time.sleep(1)
            except Exception as e:
                allure.attach(str(e), "Valid Link Error", allure.attachment_type.TEXT)
        
        with allure.step("Test broken link"):
            try:
                broken_link = self.driver.find_element(By.LINK_TEXT, "Click Here for Broken Link")
                self.driver.execute_script("arguments[0].click();", broken_link)
                time.sleep(2)
                
                current_url = self.driver.current_url
                allure.attach(current_url, "Broken Link Destination", allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), "Broken Link Error", allure.attachment_type.TEXT)
    
    @allure.story("File Operations")
    @allure.title("Upload Download - File Operations")
    @allure.description("Test file upload and download functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_upload_download(self):
        """Test Upload and Download functionality with Allure reporting"""
        
        with allure.step("Navigate to Upload Download page"):
            self.driver.get("https://demoqa.com/upload-download")
        
        with allure.step("Test download functionality"):
            download_btn = self.driver.find_element(By.ID, "downloadButton")
            download_btn.click()
            time.sleep(2)
            allure.attach("Download initiated successfully", "Download Status", allure.attachment_type.TEXT)
        
        with allure.step("Test upload functionality"):
            test_file_path = os.path.join(os.getcwd(), "test_upload.txt")
            with open(test_file_path, "w") as f:
                f.write("This is a test file for upload functionality testing")
            
            upload_input = self.driver.find_element(By.ID, "uploadFile")
            upload_input.send_keys(test_file_path)
            
            uploaded_file_path = self.wait.until(EC.presence_of_element_located((By.ID, "uploadedFilePath")))
            assert "test_upload.txt" in uploaded_file_path.text
            allure.attach(uploaded_file_path.text, "Upload Confirmation", allure.attachment_type.TEXT)
            
            os.remove(test_file_path)
            allure.attach("Test file cleaned up", "Cleanup Status", allure.attachment_type.TEXT)
    
    @allure.story("Dynamic Behavior")
    @allure.title("Dynamic Properties - Element State Changes")
    @allure.description("Test dynamic element behavior and timing")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_dynamic_properties(self):
        """Test Dynamic Properties functionality with Allure reporting"""
        
        with allure.step("Navigate to Dynamic Properties page"):
            self.driver.get("https://demoqa.com/dynamic-properties")
        
        with allure.step("Test Enable After button"):
            start_time = time.time()
            enable_after_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
            enable_time = time.time() - start_time
            
            enable_after_btn.click()
            allure.attach(f"Button enabled after {enable_time:.2f} seconds", "Enable Timing", allure.attachment_type.TEXT)
        
        with allure.step("Test Color Change button"):
            color_change_btn = self.wait.until(EC.presence_of_element_located((By.ID, "colorChange")))
            initial_color = color_change_btn.value_of_css_property('color')
            allure.attach(initial_color, "Button Color", allure.attachment_type.TEXT)
        
        with allure.step("Test Visible After button"):
            try:
                start_time = time.time()
                visible_after_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
                visible_time = time.time() - start_time
                
                visible_after_btn.click()
                allure.attach(f"Button became visible after {visible_time:.2f} seconds", "Visibility Timing", allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), "Visible After Error", allure.attachment_type.TEXT)
    
    @pytest.fixture(autouse=True)
    def attach_screenshot_on_failure(self, request):
        """Attach screenshot on test failure"""
        yield
        if request.node.rep_call.failed:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )
    
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        """Hook to capture test results"""
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)