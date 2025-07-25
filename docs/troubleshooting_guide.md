# DemoQA Selenium Automation - Troubleshooting Guide

## 🚨 Common Issues and Solutions

### 1. WebDriver Issues

#### ChromeDriver Not Found
```
Error: selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH
```

**Solutions:**
```bash
# Option 1: Use webdriver-manager (Recommended)
pip install webdriver-manager

# Update driver_factory.py to use webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Option 2: Manual installation
# Download ChromeDriver from: https://chromedriver.chromium.org/
# Add to PATH or specify path directly
```

#### Chrome Version Mismatch
```
Error: SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version X
```

**Solutions:**
```bash
# Check Chrome version
chrome://version/

# Download matching ChromeDriver version
# Or use webdriver-manager for automatic management
pip install --upgrade webdriver-manager
```

#### Permission Denied (Linux/macOS)
```
Error: Permission denied: 'chromedriver'
```

**Solutions:**
```bash
# Make ChromeDriver executable
chmod +x /path/to/chromedriver

# Or run with sudo (not recommended for regular use)
sudo python test_script.py
```

### 2. Element Location Issues

#### Element Not Found
```
Error: selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element
```

**Solutions:**
```python
# Increase wait time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)  # Increase from 10 to 20 seconds
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))

# Use alternative locators
# Instead of By.ID, try:
By.CSS_SELECTOR
By.XPATH
By.CLASS_NAME
By.TAG_NAME

# Check if element is in iframe
driver.switch_to.frame("frame_name")
element = driver.find_element(By.ID, "element_id")
driver.switch_to.default_content()  # Switch back
```

#### Element Not Clickable
```
Error: selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
```

**Solutions:**
```python
# Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, "element_id")))

# Scroll to element
driver.execute_script("arguments[0].scrollIntoView();", element)

# Use JavaScript click
driver.execute_script("arguments[0].click();", element)

# Handle overlays
try:
    element.click()
except ElementClickInterceptedException:
    # Close overlay or use JavaScript click
    driver.execute_script("arguments[0].click();", element)
```

#### Stale Element Reference
```
Error: selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference
```

**Solutions:**
```python
# Re-find the element
def safe_click(driver, locator):
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            element = driver.find_element(*locator)
            element.click()
            break
        except StaleElementReferenceException:
            if attempt == max_attempts - 1:
                raise
            time.sleep(1)
```

### 3. Timing Issues

#### Page Load Timeout
```
Error: selenium.common.exceptions.TimeoutException: Message: timeout
```

**Solutions:**
```python
# Increase page load timeout
driver.set_page_load_timeout(30)  # 30 seconds

# Use explicit waits instead of implicit waits
wait = WebDriverWait(driver, 30)

# Wait for specific conditions
wait.until(EC.presence_of_element_located((By.ID, "element_id")))
wait.until(EC.url_contains("expected_url_part"))
wait.until(EC.title_contains("expected_title"))
```

#### Element Loading Delays
```python
# Wait for element to be visible
wait.until(EC.visibility_of_element_located((By.ID, "element_id")))

# Wait for element to be present in DOM
wait.until(EC.presence_of_element_located((By.ID, "element_id")))

# Wait for text to be present
wait.until(EC.text_to_be_present_in_element((By.ID, "element_id"), "expected_text"))

# Custom wait condition
def element_has_text(locator, text):
    def _predicate(driver):
        element = driver.find_element(*locator)
        return text in element.text
    return _predicate

wait.until(element_has_text((By.ID, "element_id"), "expected_text"))
```

### 4. Network and Connection Issues

#### Connection Refused
```
Error: urllib3.exceptions.MaxRetryError: HTTPConnectionPool: Max retries exceeded
```

**Solutions:**
```python
# Check internet connection
# Verify DemoQA website is accessible: https://demoqa.com/

# Add retry logic
import time
from selenium.common.exceptions import WebDriverException

def safe_get(driver, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            driver.get(url)
            return
        except WebDriverException as e:
            if attempt == max_retries - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5)
```

#### Slow Network
```python
# Increase timeouts for slow connections
driver.implicitly_wait(20)  # Increase implicit wait
driver.set_page_load_timeout(60)  # Increase page load timeout

# Use explicit waits with longer timeouts
wait = WebDriverWait(driver, 30)
```

### 5. Test-Specific Issues

#### DemoQA Ad Overlays
```python
# Handle ad overlays that block elements
def handle_ads(driver):
    try:
        # Close ad overlay if present
        ad_close = driver.find_element(By.CSS_SELECTOR, ".ad-close, .close-ad, [id*='close']")
        ad_close.click()
    except:
        pass

# Use JavaScript click to bypass overlays
def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# Scroll element into view before clicking
def scroll_and_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)
    element.click()
```

#### Form Validation Issues
```python
# Clear field before entering text
def safe_send_keys(element, text):
    element.clear()
    time.sleep(0.5)
    element.send_keys(text)

# Handle form validation
def fill_form_field(driver, locator, value):
    element = driver.find_element(*locator)
    element.clear()
    element.send_keys(value)
    
    # Trigger validation by clicking elsewhere
    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(0.5)
```

#### File Upload Issues
```python
# Ensure file exists before upload
import os

def safe_file_upload(driver, file_input_locator, file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_input = driver.find_element(*file_input_locator)
    file_input.send_keys(os.path.abspath(file_path))
```

### 6. Allure Reporting Issues

#### Allure Command Not Found
```
Error: 'allure' is not recognized as an internal or external command
```

**Solutions:**
```bash
# Windows - Install using Scoop
scoop install allure

# macOS - Install using Homebrew
brew install allure

# Linux - Manual installation
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
tar -zxvf allure-2.24.0.tgz
sudo mv allure-2.24.0 /opt/allure
echo 'export PATH="/opt/allure/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify installation
allure --version
```

#### Allure Results Not Generated
```python
# Ensure pytest-allure is installed
pip install allure-pytest

# Run tests with allure directory
pytest tests/ --alluredir=reports/allure-results

# Check if results directory exists
import os
if not os.path.exists("reports/allure-results"):
    os.makedirs("reports/allure-results")
```

#### Report Generation Fails
```bash
# Clear previous results
rm -rf reports/allure-results/*
rm -rf reports/allure-report/*

# Generate fresh results
pytest tests/ --alluredir=reports/allure-results --clean-alluredir

# Generate report
allure generate reports/allure-results --output reports/allure-report --clean
```

### 7. Python Environment Issues

#### Module Not Found
```
Error: ModuleNotFoundError: No module named 'selenium'
```

**Solutions:**
```bash
# Check Python version
python --version

# Install requirements
pip install -r requirements.txt

# Use virtual environment (recommended)
python -m venv selenium_env
# Windows
selenium_env\Scripts\activate
# macOS/Linux
source selenium_env/bin/activate

pip install -r requirements.txt
```

#### Version Conflicts
```bash
# Check installed packages
pip list

# Upgrade specific packages
pip install --upgrade selenium
pip install --upgrade pytest

# Create fresh environment
pip freeze > old_requirements.txt
pip uninstall -r old_requirements.txt -y
pip install -r requirements.txt
```

### 8. System-Specific Issues

#### Windows Issues
```bash
# Path separator issues
# Use os.path.join() or pathlib
import os
file_path = os.path.join("reports", "test_results.txt")

# Permission issues
# Run Command Prompt as Administrator

# Antivirus blocking
# Add project folder to antivirus exclusions
```

#### macOS Issues
```bash
# ChromeDriver security warning
# Go to System Preferences > Security & Privacy > General
# Click "Allow Anyway" for ChromeDriver

# Permission issues
chmod +x chromedriver
xattr -d com.apple.quarantine chromedriver
```

#### Linux Issues
```bash
# Missing dependencies
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver

# Display issues (headless)
export DISPLAY=:99
Xvfb :99 -screen 0 1024x768x24 &

# Or use headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
```

### 9. Performance Issues

#### Slow Test Execution
```python
# Use headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

# Disable images and CSS
prefs = {
    "profile.managed_default_content_settings.images": 2,
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# Optimize waits
# Use explicit waits instead of time.sleep()
# Reduce wait times where appropriate
```

#### Memory Issues
```python
# Properly close drivers
def cleanup_driver(driver):
    try:
        driver.quit()
    except:
        pass

# Use context managers
from contextlib import contextmanager

@contextmanager
def get_driver():
    driver = webdriver.Chrome()
    try:
        yield driver
    finally:
        driver.quit()

# Usage
with get_driver() as driver:
    driver.get("https://demoqa.com/")
    # Test code here
```

### 10. Debugging Tips

#### Enable Logging
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add debug information
logger.info(f"Navigating to: {url}")
logger.info(f"Current URL: {driver.current_url}")
logger.info(f"Page title: {driver.title}")
```

#### Take Screenshots on Failure
```python
def take_screenshot_on_failure(driver, test_name):
    try:
        screenshot_path = f"reports/screenshots/{test_name}_failure.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")

# Usage in test
try:
    # Test code
    pass
except Exception as e:
    take_screenshot_on_failure(driver, "test_name")
    raise
```

#### Browser Developer Tools
```python
# Enable Chrome DevTools
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--auto-open-devtools-for-tabs")

# Get browser logs
logs = driver.get_log('browser')
for log in logs:
    print(f"Browser log: {log}")

# Execute JavaScript for debugging
result = driver.execute_script("return document.readyState;")
print(f"Document ready state: {result}")
```

## 🔍 Diagnostic Commands

### System Check
```bash
# Check Python version
python --version

# Check pip packages
pip list | grep selenium
pip list | grep pytest
pip list | grep allure

# Check Chrome version
google-chrome --version  # Linux
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version  # macOS

# Check ChromeDriver version
chromedriver --version
```

### Network Check
```bash
# Test DemoQA connectivity
ping demoqa.com
curl -I https://demoqa.com/

# Check DNS resolution
nslookup demoqa.com
```

### File System Check
```bash
# Check file permissions
ls -la chromedriver

# Check disk space
df -h

# Check directory structure
tree Selenium/  # If tree is installed
```

## 📞 Getting Help

### Before Seeking Help
1. ✅ Check this troubleshooting guide
2. ✅ Verify all prerequisites are met
3. ✅ Try running a simple test first
4. ✅ Check console output for specific errors
5. ✅ Take screenshots of error messages

### Information to Provide
- Operating system and version
- Python version
- Chrome and ChromeDriver versions
- Complete error message
- Steps to reproduce the issue
- Screenshots if applicable

### Resources
- **Selenium Documentation**: https://selenium-python.readthedocs.io/
- **DemoQA Website**: https://demoqa.com/
- **Chrome DevTools**: F12 in Chrome browser
- **Stack Overflow**: Search for specific error messages

---

**Last Updated**: December 2024  
**Version**: 1.0  
**Maintainer**: DemoQA Automation Team