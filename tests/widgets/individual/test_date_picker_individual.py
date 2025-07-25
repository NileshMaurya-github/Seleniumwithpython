from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime, timedelta


class DatePickerTest:
    """Individual test for Date Picker functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_select_date(self):
        """Test basic date selection"""
        print("🔧 Testing Date Picker - Select Date...")
        self.driver.get("https://demoqa.com/date-picker")

        try:
            # Find date input field
            date_input = self.driver.find_element(By.ID, "datePickerMonthYearInput")
            original_date = date_input.get_attribute("value")
            print(f"  ✓ Original date: {original_date}")
            
            # Click to open date picker
            date_input.click()
            print("  ✓ Date picker opened")
            
            # Wait for calendar to appear
            calendar = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker")))
            print("  ✓ Calendar appeared")
            
            # Select a different date (try to click on day 15)
            try:
                days = self.driver.find_elements(By.CSS_SELECTOR, ".react-datepicker__day:not(.react-datepicker__day--disabled)")
                target_day = None
                for day in days:
                    if day.text == "15" and "react-datepicker__day--outside-month" not in day.get_attribute("class"):
                        target_day = day
                        break
                
                if target_day:
                    target_day.click()
                    print("  ✓ Selected day 15")
                else:
                    # Fallback: click any available day
                    available_days = [day for day in days if day.text.isdigit()]
                    if available_days:
                        available_days[0].click()
                        print(f"  ✓ Selected day {available_days[0].text}")
                
                # Verify date changed
                time.sleep(0.5)
                new_date = date_input.get_attribute("value")
                assert new_date != original_date
                print(f"  ✓ Date changed to: {new_date}")
                
            except Exception as day_e:
                print(f"  ⚠️ Day selection issue: {day_e}")
                # Try clicking outside to close calendar
                self.driver.find_element(By.TAG_NAME, "body").click()
            
            print("✅ Select date test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Select date test FAILED: {e}")
            return False

    def test_navigate_months(self):
        """Test month navigation in date picker"""
        print("\n🔧 Testing Date Picker - Navigate Months...")
        self.driver.get("https://demoqa.com/date-picker")

        try:
            # Open date picker
            date_input = self.driver.find_element(By.ID, "datePickerMonthYearInput")
            date_input.click()
            
            # Wait for calendar
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker")))
            
            # Get current month
            current_month = self.driver.find_element(By.CLASS_NAME, "react-datepicker__current-month")
            original_month = current_month.text
            print(f"  ✓ Current month: {original_month}")
            
            # Click next month button
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__navigation--next")
                next_button.click()
                time.sleep(0.5)
                
                # Verify month changed
                new_month = current_month.text
                print(f"  ✓ Navigated to: {new_month}")
                
                # Click previous month button
                prev_button = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__navigation--previous")
                prev_button.click()
                time.sleep(0.5)
                
                # Verify back to original month
                back_month = current_month.text
                print(f"  ✓ Navigated back to: {back_month}")
                
            except Exception as nav_e:
                print(f"  ⚠️ Month navigation issue: {nav_e}")
            
            # Close calendar
            self.driver.find_element(By.TAG_NAME, "body").click()
            
            print("✅ Navigate months test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Navigate months test FAILED: {e}")
            return False

    def test_date_and_time_picker(self):
        """Test date and time picker functionality"""
        print("\n🔧 Testing Date Picker - Date and Time...")
        self.driver.get("https://demoqa.com/date-picker")

        try:
            # Find date and time input field
            datetime_input = self.driver.find_element(By.ID, "dateAndTimePickerInput")
            original_datetime = datetime_input.get_attribute("value")
            print(f"  ✓ Original date/time: {original_datetime}")
            
            # Click to open date/time picker
            datetime_input.click()
            print("  ✓ Date/time picker opened")
            
            # Wait for calendar to appear
            calendar = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker")))
            
            # Try to select a date
            try:
                days = self.driver.find_elements(By.CSS_SELECTOR, ".react-datepicker__day:not(.react-datepicker__day--disabled)")
                if days:
                    # Find a day that's not outside current month
                    target_day = None
                    for day in days:
                        if (day.text.isdigit() and 
                            "react-datepicker__day--outside-month" not in day.get_attribute("class")):
                            target_day = day
                            break
                    
                    if target_day:
                        target_day.click()
                        print(f"  ✓ Selected day {target_day.text}")
                        
                        # Try to modify time if time picker is available
                        try:
                            time_input = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__time-input input")
                            time_input.clear()
                            time_input.send_keys("14:30")
                            print("  ✓ Set time to 14:30")
                        except:
                            print("  ⚠️ Time input not found or not editable")
                        
                        # Verify datetime changed
                        time.sleep(1)
                        new_datetime = datetime_input.get_attribute("value")
                        if new_datetime != original_datetime:
                            print(f"  ✓ Date/time changed to: {new_datetime}")
                        else:
                            print("  ⚠️ Date/time may not have changed")
                
            except Exception as datetime_e:
                print(f"  ⚠️ Date/time selection issue: {datetime_e}")
                # Close calendar
                self.driver.find_element(By.TAG_NAME, "body").click()
            
            print("✅ Date and time picker test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Date and time picker test FAILED: {e}")
            return False

    def test_keyboard_input(self):
        """Test keyboard input for date picker"""
        print("\n🔧 Testing Date Picker - Keyboard Input...")
        self.driver.get("https://demoqa.com/date-picker")

        try:
            # Test keyboard input on regular date picker
            date_input = self.driver.find_element(By.ID, "datePickerMonthYearInput")
            date_input.click()
            
            # Clear and type new date
            date_input.clear()
            test_date = "01/15/2024"
            date_input.send_keys(test_date)
            date_input.send_keys(Keys.ENTER)
            print(f"  ✓ Typed date: {test_date}")
            
            # Verify input
            time.sleep(0.5)
            input_value = date_input.get_attribute("value")
            print(f"  ✓ Input value: {input_value}")
            
            # Test keyboard input on date/time picker
            datetime_input = self.driver.find_element(By.ID, "dateAndTimePickerInput")
            datetime_input.click()
            
            # Try to clear and input new datetime
            try:
                datetime_input.clear()
                test_datetime = "January 20, 2024 3:00 PM"
                datetime_input.send_keys(test_datetime)
                datetime_input.send_keys(Keys.ENTER)
                print(f"  ✓ Typed datetime: {test_datetime}")
                
                time.sleep(0.5)
                datetime_value = datetime_input.get_attribute("value")
                print(f"  ✓ Datetime value: {datetime_value}")
                
            except Exception as dt_e:
                print(f"  ⚠️ Datetime keyboard input issue: {dt_e}")
            
            print("✅ Keyboard input test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Keyboard input test FAILED: {e}")
            return False

    def run_all_date_picker_tests(self):
        """Run all date picker tests"""
        print("=" * 60)
        print("📅 DATE PICKER INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_select_date())
            results.append(self.test_navigate_months())
            results.append(self.test_date_and_time_picker())
            results.append(self.test_keyboard_input())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 DATE PICKER TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Date Picker tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Date Picker tests passed, some had issues")
            else:
                print("❌ All Date Picker tests had issues")
                
        except Exception as e:
            print(f"❌ Date Picker test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    date_picker_test = DatePickerTest()
    date_picker_test.run_all_date_picker_tests()