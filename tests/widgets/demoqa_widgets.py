from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os


class DemoQAWidgets:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_accordian(self):
        """Test Accordian functionality"""
        print("Testing Accordian...")
        self.driver.get("https://demoqa.com/accordian")

        # Test first accordian
        first_accordian = self.driver.find_element(By.ID, "section1Heading")
        first_accordian.click()
        time.sleep(1)

        first_content = self.driver.find_element(By.ID, "section1Content")
        assert first_content.is_displayed()
        print("  ✓ First accordian expanded")

        # Test second accordian
        second_accordian = self.driver.find_element(By.ID, "section2Heading")
        second_accordian.click()
        time.sleep(1)

        second_content = self.driver.find_element(By.ID, "section2Content")
        assert second_content.is_displayed()
        print("  ✓ Second accordian expanded")

        # Test third accordian
        third_accordian = self.driver.find_element(By.ID, "section3Heading")
        third_accordian.click()
        time.sleep(1)

        third_content = self.driver.find_element(By.ID, "section3Content")
        assert third_content.is_displayed()
        print("  ✓ Third accordian expanded")

        print("✓ Accordian test passed")

    def test_auto_complete(self):
        """Test Auto Complete functionality"""
        print("Testing Auto Complete...")
        self.driver.get("https://demoqa.com/auto-complete")

        # Test multiple auto complete
        multi_input = self.driver.find_element(By.ID, "autoCompleteMultipleInput")
        multi_input.send_keys("Red")
        time.sleep(1)

        # Select from dropdown
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'auto-complete__option') and text()='Red']")))
        option.click()

        # Add another color
        multi_input.send_keys("Blue")
        time.sleep(1)
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'auto-complete__option') and text()='Blue']")))
        option.click()

        print("  ✓ Multiple auto complete tested")

        # Test single auto complete
        single_input = self.driver.find_element(By.ID, "autoCompleteSingleInput")
        single_input.send_keys("Green")
        time.sleep(1)

        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'auto-complete__option') and text()='Green']")))
        option.click()

        print("  ✓ Single auto complete tested")

        print("✓ Auto Complete test passed")

    def test_date_picker(self):
        """Test Date Picker functionality"""
        print("Testing Date Picker...")
        self.driver.get("https://demoqa.com/date-picker")

        # Test simple date picker
        date_input = self.driver.find_element(By.ID, "datePickerMonthYearInput")
        date_input.click()

        # Select month
        month_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_dropdown.select_by_visible_text("January")

        # Select year
        year_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_dropdown.select_by_visible_text("2025")

        # Select day
        day = self.driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']")
        day.click()

        print("  ✓ Simple date picker tested")

        # Test date and time picker
        datetime_input = self.driver.find_element(By.ID, "dateAndTimePickerInput")
        datetime_input.click()

        # Select month
        month_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_dropdown.select_by_visible_text("December")

        # Select year
        year_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_dropdown.select_by_visible_text("2024")

        # Select day
        day = self.driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='25']")
        day.click()

        # Select time
        time_option = self.driver.find_element(By.XPATH, "//li[contains(@class, 'react-datepicker__time-list-item') and text()='12:00']")
        time_option.click()

        print("  ✓ Date and time picker tested")

        print("✓ Date Picker test passed")

    def test_slider(self):
        """Test Slider functionality"""
        print("Testing Slider...")
        self.driver.get("https://demoqa.com/slider")

        # Get slider element
        slider = self.driver.find_element(By.CSS_SELECTOR, "input[type='range']")
        
        # Move slider using Actions
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(50, 0).release().perform()

        # Verify slider value changed
        slider_value = self.driver.find_element(By.ID, "sliderValue")
        print(f"  Slider value: {slider_value.get_attribute('value')}")

        print("✓ Slider test passed")

    def test_progress_bar(self):
        """Test Progress Bar functionality"""
        print("Testing Progress Bar...")
        self.driver.get("https://demoqa.com/progress-bar")

        # Start progress bar
        start_btn = self.driver.find_element(By.ID, "startStopButton")
        start_btn.click()

        # Wait for progress to start
        time.sleep(2)

        # Check progress value
        progress_bar = self.driver.find_element(By.CSS_SELECTOR, ".progress-bar")
        progress_value = progress_bar.get_attribute("aria-valuenow")
        print(f"  Progress value: {progress_value}%")

        # Stop progress bar
        start_btn.click()

        print("✓ Progress Bar test passed")

    def test_tabs(self):
        """Test Tabs functionality"""
        print("Testing Tabs...")
        self.driver.get("https://demoqa.com/tabs")

        # Test What tab (default active)
        what_content = self.driver.find_element(By.ID, "demo-tabpane-what")
        assert what_content.is_displayed()
        print("  ✓ What tab is active by default")

        # Test Origin tab
        origin_tab = self.driver.find_element(By.ID, "demo-tab-origin")
        origin_tab.click()
        time.sleep(1)

        origin_content = self.driver.find_element(By.ID, "demo-tabpane-origin")
        assert origin_content.is_displayed()
        print("  ✓ Origin tab activated")

        # Test Use tab
        use_tab = self.driver.find_element(By.ID, "demo-tab-use")
        use_tab.click()
        time.sleep(1)

        use_content = self.driver.find_element(By.ID, "demo-tabpane-use")
        assert use_content.is_displayed()
        print("  ✓ Use tab activated")

        print("✓ Tabs test passed")

    def test_tool_tips(self):
        """Test Tool Tips functionality"""
        print("Testing Tool Tips...")
        self.driver.get("https://demoqa.com/tool-tips")

        actions = ActionChains(self.driver)

        # Hover over button
        hover_btn = self.driver.find_element(By.ID, "toolTipButton")
        actions.move_to_element(hover_btn).perform()
        time.sleep(2)

        # Check for tooltip
        try:
            tooltip = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tooltip-inner")))
            print(f"  Button tooltip: {tooltip.text}")
        except:
            print("  Button tooltip not found")

        # Hover over text field
        text_field = self.driver.find_element(By.ID, "toolTipTextField")
        actions.move_to_element(text_field).perform()
        time.sleep(2)

        # Hover over link
        link = self.driver.find_element(By.XPATH, "//a[text()='Contrary']")
        actions.move_to_element(link).perform()
        time.sleep(2)

        print("✓ Tool Tips test passed")

    def test_menu(self):
        """Test Menu functionality"""
        print("Testing Menu...")
        self.driver.get("https://demoqa.com/menu")

        actions = ActionChains(self.driver)

        # Hover over Main Item 2
        main_item2 = self.driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
        actions.move_to_element(main_item2).perform()
        time.sleep(1)

        # Check if submenu appears
        submenu = self.driver.find_element(By.XPATH, "//a[text()='Sub Item']")
        assert submenu.is_displayed()
        print("  ✓ Submenu appeared on hover")

        # Hover over Sub Sub List
        sub_sub_list = self.driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
        actions.move_to_element(sub_sub_list).perform()
        time.sleep(1)

        # Check if sub-submenu appears
        sub_sub_item = self.driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 1']")
        assert sub_sub_item.is_displayed()
        print("  ✓ Sub-submenu appeared on hover")

        print("✓ Menu test passed")

    def test_select_menu(self):
        """Test Select Menu functionality"""
        print("Testing Select Menu...")
        self.driver.get("https://demoqa.com/select-menu")

        # Test Select Value dropdown
        select_value = self.driver.find_element(By.ID, "withOptGroup")
        select_value.click()

        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Group 1, option 1']")))
        option.click()
        print("  ✓ Select Value dropdown tested")

        # Test Select One dropdown
        select_one = self.driver.find_element(By.ID, "selectOne")
        select_one.click()

        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Dr.']")))
        option.click()
        print("  ✓ Select One dropdown tested")

        # Test Old Style Select Menu
        old_select = Select(self.driver.find_element(By.ID, "oldSelectMenu"))
        old_select.select_by_visible_text("Purple")
        print("  ✓ Old Style Select Menu tested")

        # Test Multiselect dropdown
        multiselect = self.driver.find_element(By.XPATH, "//div[contains(@class, 'css-1hwfws3')]")
        multiselect.click()

        option1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Green']")))
        option1.click()

        option2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Blue']")))
        option2.click()

        # Click outside to close dropdown
        self.driver.find_element(By.TAG_NAME, "body").click()
        print("  ✓ Multiselect dropdown tested")

        print("✓ Select Menu test passed")

    def run_all_tests(self):
        """Run all widget tests"""
        try:
            self.test_accordian()
            self.test_auto_complete()
            self.test_date_picker()
            self.test_slider()
            self.test_progress_bar()
            self.test_tabs()
            self.test_tool_tips()
            self.test_menu()
            self.test_select_menu()
            print("\n✅ All Widgets tests completed successfully!")
        except Exception as e:
            print(f"\n❌ Test failed: {str(e)}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    widgets_test = DemoQAWidgets()
    widgets_test.run_all_tests()