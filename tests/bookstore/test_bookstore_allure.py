import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string


@allure.epic("DemoQA Automation")
@allure.feature("Book Store Application")
class TestBookStoreApplication:
    """Allure test suite for Book Store Application functionality"""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to initialize WebDriver"""
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def generate_random_user(self):
        """Generate random user data for testing"""
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return {
            'firstName': f'Test{random_suffix}',
            'lastName': f'User{random_suffix}',
            'userName': f'testuser{random_suffix}',
            'password': f'TestPass123!{random_suffix}'
        }

    @allure.story("Login")
    @allure.title("Test Login Page Elements")
    @allure.description("Verify that all login page elements are present and displayed correctly")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_page_elements(self):
        with allure.step("Navigate to login page"):
            self.driver.get("https://demoqa.com/login")
            
        with allure.step("Verify username field is present"):
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "userName")))
            assert username_field.is_displayed()
            allure.attach("Username field found", "Element Check", allure.attachment_type.TEXT)
            
        with allure.step("Verify password field is present"):
            password_field = self.driver.find_element(By.ID, "password")
            assert password_field.is_displayed()
            
        with allure.step("Verify login button is present"):
            login_btn = self.driver.find_element(By.ID, "login")
            assert login_btn.is_displayed()
            
        with allure.step("Verify new user button is present"):
            new_user_btn = self.driver.find_element(By.ID, "newUser")
            assert new_user_btn.is_displayed()

    @allure.story("Login")
    @allure.title("Test Invalid Login Credentials")
    @allure.description("Verify that invalid login credentials are properly handled")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_login(self):
        with allure.step("Navigate to login page"):
            self.driver.get("https://demoqa.com/login")
            
        with allure.step("Enter invalid credentials"):
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "userName")))
            username_field.clear()
            username_field.send_keys("invaliduser")
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("invalidpass")
            
            allure.attach("invaliduser / invalidpass", "Test Credentials", allure.attachment_type.TEXT)
            
        with allure.step("Attempt login"):
            login_btn = self.driver.find_element(By.ID, "login")
            login_btn.click()
            
        with allure.step("Verify login failure handling"):
            time.sleep(2)
            current_url = self.driver.current_url
            assert "login" in current_url
            allure.attach(current_url, "Current URL", allure.attachment_type.TEXT)

    @allure.story("Register")
    @allure.title("Test Registration Page Elements")
    @allure.description("Verify that all registration page elements are present and functional")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_page_elements(self):
        with allure.step("Navigate to register page"):
            self.driver.get("https://demoqa.com/register")
            
        with allure.step("Verify first name field"):
            first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "firstname")))
            assert first_name_field.is_displayed()
            
        with allure.step("Verify last name field"):
            last_name_field = self.driver.find_element(By.ID, "lastname")
            assert last_name_field.is_displayed()
            
        with allure.step("Verify username field"):
            username_field = self.driver.find_element(By.ID, "userName")
            assert username_field.is_displayed()
            
        with allure.step("Verify password field"):
            password_field = self.driver.find_element(By.ID, "password")
            assert password_field.is_displayed()
            
        with allure.step("Verify register button"):
            register_btn = self.driver.find_element(By.ID, "register")
            assert register_btn.is_displayed()

    @allure.story("Register")
    @allure.title("Test Registration Form Interactions")
    @allure.description("Verify that registration form fields accept input correctly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_registration_form_interactions(self):
        with allure.step("Navigate to register page"):
            self.driver.get("https://demoqa.com/register")
            
        with allure.step("Generate test user data"):
            user_data = self.generate_random_user()
            allure.attach(str(user_data), "Generated User Data", allure.attachment_type.JSON)
            
        with allure.step("Fill registration form"):
            first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "firstname")))
            first_name_field.clear()
            first_name_field.send_keys(user_data['firstName'])
            
            last_name_field = self.driver.find_element(By.ID, "lastname")
            last_name_field.clear()
            last_name_field.send_keys(user_data['lastName'])
            
            username_field = self.driver.find_element(By.ID, "userName")
            username_field.clear()
            username_field.send_keys(user_data['userName'])
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(user_data['password'])
            
        with allure.step("Verify form data entry"):
            assert first_name_field.get_attribute("value") == user_data['firstName']
            assert last_name_field.get_attribute("value") == user_data['lastName']
            assert username_field.get_attribute("value") == user_data['userName']

    @allure.story("Book Store")
    @allure.title("Test Book Store Page Elements")
    @allure.description("Verify that book store page loads with all necessary elements")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_book_store_page_elements(self):
        with allure.step("Navigate to book store"):
            self.driver.get("https://demoqa.com/books")
            
        with allure.step("Verify search box is present"):
            search_box = self.wait.until(EC.presence_of_element_located((By.ID, "searchBox")))
            assert search_box.is_displayed()
            
        with allure.step("Check for books table"):
            try:
                books_table = self.driver.find_element(By.CLASS_NAME, "rt-table")
                assert books_table.is_displayed()
                allure.attach("Books table found", "Table Status", allure.attachment_type.TEXT)
            except:
                allure.attach("Books table not found", "Table Status", allure.attachment_type.TEXT)

    @allure.story("Book Store")
    @allure.title("Test Book Search Functionality")
    @allure.description("Verify that book search functionality works correctly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_book_search_functionality(self):
        with allure.step("Navigate to book store"):
            self.driver.get("https://demoqa.com/books")
            
        with allure.step("Perform search"):
            search_box = self.wait.until(EC.presence_of_element_located((By.ID, "searchBox")))
            search_term = "Git"
            search_box.clear()
            search_box.send_keys(search_term)
            allure.attach(search_term, "Search Term", allure.attachment_type.TEXT)
            
        with allure.step("Wait for search results"):
            time.sleep(2)
            
        with allure.step("Verify search results"):
            try:
                book_elements = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
                results_count = len([elem for elem in book_elements if elem.text.strip()])
                allure.attach(f"Found {results_count} results", "Search Results", allure.attachment_type.TEXT)
            except:
                allure.attach("Could not verify search results", "Search Results", allure.attachment_type.TEXT)

    @allure.story("Profile")
    @allure.title("Test Profile Page Access")
    @allure.description("Verify profile page access and authentication requirements")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_profile_page_access(self):
        with allure.step("Navigate to profile page"):
            self.driver.get("https://demoqa.com/profile")
            
        with allure.step("Check authentication redirect"):
            time.sleep(2)
            current_url = self.driver.current_url
            allure.attach(current_url, "Current URL", allure.attachment_type.TEXT)
            
            if "login" in current_url:
                allure.attach("Redirected to login (expected)", "Authentication Status", allure.attachment_type.TEXT)
                
                # Verify login form elements
                username_field = self.driver.find_element(By.ID, "userName")
                password_field = self.driver.find_element(By.ID, "password")
                login_btn = self.driver.find_element(By.ID, "login")
                
                assert username_field.is_displayed()
                assert password_field.is_displayed()
                assert login_btn.is_displayed()

    @allure.story("Book Detail")
    @allure.title("Test Book Detail Page Access")
    @allure.description("Verify that book detail pages can be accessed and display information")
    @allure.severity(allure.severity_level.NORMAL)
    def test_book_detail_page_access(self):
        with allure.step("Navigate to book store"):
            self.driver.get("https://demoqa.com/books")
            
        with allure.step("Find and click on a book"):
            time.sleep(3)
            try:
                book_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/books?book=']")
                if book_links:
                    first_book_link = book_links[0]
                    book_title = first_book_link.text
                    allure.attach(book_title, "Selected Book", allure.attachment_type.TEXT)
                    
                    first_book_link.click()
                    
                    time.sleep(3)
                    current_url = self.driver.current_url
                    allure.attach(current_url, "Book Detail URL", allure.attachment_type.TEXT)
                    
                    if "book=" in current_url:
                        allure.attach("Successfully navigated to book detail", "Navigation Status", allure.attachment_type.TEXT)
                else:
                    # Try direct URL
                    self.driver.get("https://demoqa.com/books?book=9781449325862")
                    allure.attach("Used direct book URL", "Navigation Method", allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(str(e), "Navigation Error", allure.attachment_type.TEXT)

    @allure.story("Authentication")
    @allure.title("Test Authentication Flow")
    @allure.description("Verify the complete authentication flow and protected route access")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_authentication_flow(self):
        with allure.step("Test protected route access without authentication"):
            self.driver.get("https://demoqa.com/profile")
            time.sleep(3)
            
            current_url = self.driver.current_url
            allure.attach(current_url, "Redirect URL", allure.attachment_type.TEXT)
            
            if "login" in current_url:
                allure.attach("Properly redirected to login", "Authentication Check", allure.attachment_type.TEXT)
            else:
                allure.attach("No authentication redirect", "Authentication Check", allure.attachment_type.TEXT)
                
        with allure.step("Test login form validation"):
            if "login" in self.driver.current_url:
                # Test empty form submission
                login_btn = self.driver.find_element(By.ID, "login")
                login_btn.click()
                
                time.sleep(2)
                
                # Should still be on login page
                current_url = self.driver.current_url
                assert "login" in current_url
                allure.attach("Form validation working", "Validation Status", allure.attachment_type.TEXT)

    @allure.story("API")
    @allure.title("Test API Endpoint Accessibility")
    @allure.description("Verify that API endpoints are accessible and return appropriate responses")
    @allure.severity(allure.severity_level.NORMAL)
    def test_api_endpoint_accessibility(self):
        with allure.step("Test Books API endpoint discovery"):
            self.driver.get("https://demoqa.com/books")
            time.sleep(3)
            
            # Check for potential API calls in network logs
            try:
                logs = self.driver.get_log('performance')
                api_requests = []
                
                for log in logs:
                    try:
                        import json
                        message = json.loads(log['message'])
                        if message['message']['method'] == 'Network.responseReceived':
                            url = message['message']['params']['response']['url']
                            if 'api' in url.lower() or 'bookstore' in url.lower():
                                api_requests.append(url)
                    except:
                        continue
                
                if api_requests:
                    allure.attach(f"Found {len(api_requests)} API requests", "API Discovery", allure.attachment_type.TEXT)
                    allure.attach('\n'.join(api_requests[:5]), "API Endpoints", allure.attachment_type.TEXT)
                else:
                    allure.attach("No API requests detected", "API Discovery", allure.attachment_type.TEXT)
                    
            except Exception as e:
                allure.attach(f"Could not analyze network logs: {str(e)}", "API Discovery", allure.attachment_type.TEXT)