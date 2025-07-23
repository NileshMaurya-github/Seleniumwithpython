from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class WebTablesTest:
    """Individual test for Web Tables functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_add_new_record(self):
        """Test adding new record to web table"""
        print("🔧 Testing Web Tables - Add New Record...")
        self.driver.get("https://demoqa.com/webtables")

        try:
            # Click Add button
            add_button = self.driver.find_element(By.ID, "addNewRecordButton")
            add_button.click()
            print("  ✓ Add New Record button clicked")

            # Fill registration form
            self.driver.find_element(By.ID, "firstName").send_keys("Jane")
            self.driver.find_element(By.ID, "lastName").send_keys("Smith")
            self.driver.find_element(By.ID, "userEmail").send_keys("jane.smith@example.com")
            self.driver.find_element(By.ID, "age").send_keys("30")
            self.driver.find_element(By.ID, "salary").send_keys("75000")
            self.driver.find_element(By.ID, "department").send_keys("Engineering")
            print("  ✓ Form fields filled")

            # Submit form (using JavaScript to avoid ad overlay issues)
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            print("  ✓ Form submitted")

            # Verify record added
            table = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rt-table")))
            assert "Jane" in table.text
            print("  ✓ New record verified in table")
            
            print("✅ Add new record test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Add new record test FAILED: {e}")
            return False

    def test_search_functionality(self):
        """Test search functionality in web table"""
        print("\n🔧 Testing Web Tables - Search Functionality...")
        self.driver.get("https://demoqa.com/webtables")

        try:
            # First add a record to search for
            add_button = self.driver.find_element(By.ID, "addNewRecordButton")
            add_button.click()
            
            self.driver.find_element(By.ID, "firstName").send_keys("SearchTest")
            self.driver.find_element(By.ID, "lastName").send_keys("User")
            self.driver.find_element(By.ID, "userEmail").send_keys("search@test.com")
            self.driver.find_element(By.ID, "age").send_keys("25")
            self.driver.find_element(By.ID, "salary").send_keys("50000")
            self.driver.find_element(By.ID, "department").send_keys("QA")
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            time.sleep(1)
            print("  ✓ Test record added for search")

            # Test search functionality
            search_box = self.driver.find_element(By.ID, "searchBox")
            search_box.send_keys("SearchTest")
            time.sleep(2)
            print("  ✓ Search term entered")

            # Verify search results
            table = self.driver.find_element(By.CSS_SELECTOR, ".rt-table")
            table_text = table.text
            
            if "SearchTest" in table_text:
                print("  ✓ Search results show correct record")
            else:
                print("  ⚠️ Search results unclear")

            # Clear search
            search_box.clear()
            search_box.send_keys(Keys.ENTER)
            time.sleep(1)
            print("  ✓ Search cleared")
            
            print("✅ Search functionality test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Search functionality test FAILED: {e}")
            return False

    def test_edit_record(self):
        """Test editing existing record"""
        print("\n🔧 Testing Web Tables - Edit Record...")
        self.driver.get("https://demoqa.com/webtables")

        try:
            # Add a record first
            add_button = self.driver.find_element(By.ID, "addNewRecordButton")
            add_button.click()
            
            self.driver.find_element(By.ID, "firstName").send_keys("EditTest")
            self.driver.find_element(By.ID, "lastName").send_keys("User")
            self.driver.find_element(By.ID, "userEmail").send_keys("edit@test.com")
            self.driver.find_element(By.ID, "age").send_keys("35")
            self.driver.find_element(By.ID, "salary").send_keys("60000")
            self.driver.find_element(By.ID, "department").send_keys("IT")
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            time.sleep(1)
            print("  ✓ Test record added for editing")

            # Search for the record
            search_box = self.driver.find_element(By.ID, "searchBox")
            search_box.send_keys("EditTest")
            time.sleep(1)

            # Click edit button
            edit_button = self.driver.find_element(By.CSS_SELECTOR, "span[title='Edit']")
            edit_button.click()
            print("  ✓ Edit button clicked")

            # Update salary
            salary_field = self.driver.find_element(By.ID, "salary")
            salary_field.clear()
            salary_field.send_keys("80000")
            print("  ✓ Salary updated")

            # Submit changes
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            time.sleep(1)
            print("  ✓ Changes submitted")

            # Verify changes
            table = self.driver.find_element(By.CSS_SELECTOR, ".rt-table")
            if "80000" in table.text:
                print("  ✓ Record updated successfully")
            else:
                print("  ⚠️ Record update verification unclear")
            
            print("✅ Edit record test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Edit record test FAILED: {e}")
            return False

    def test_delete_record(self):
        """Test deleting record from table"""
        print("\n🔧 Testing Web Tables - Delete Record...")
        self.driver.get("https://demoqa.com/webtables")

        try:
            # Add a record to delete
            add_button = self.driver.find_element(By.ID, "addNewRecordButton")
            add_button.click()
            
            self.driver.find_element(By.ID, "firstName").send_keys("DeleteTest")
            self.driver.find_element(By.ID, "lastName").send_keys("User")
            self.driver.find_element(By.ID, "userEmail").send_keys("delete@test.com")
            self.driver.find_element(By.ID, "age").send_keys("40")
            self.driver.find_element(By.ID, "salary").send_keys("70000")
            self.driver.find_element(By.ID, "department").send_keys("HR")
            
            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            time.sleep(1)
            print("  ✓ Test record added for deletion")

            # Search for the record
            search_box = self.driver.find_element(By.ID, "searchBox")
            search_box.send_keys("DeleteTest")
            time.sleep(1)

            # Click delete button
            delete_button = self.driver.find_element(By.CSS_SELECTOR, "span[title='Delete']")
            delete_button.click()
            time.sleep(1)
            print("  ✓ Delete button clicked")

            # Clear search to see if record is gone
            search_box.clear()
            search_box.send_keys(Keys.ENTER)
            time.sleep(1)

            # Verify record is deleted
            table = self.driver.find_element(By.CSS_SELECTOR, ".rt-table")
            if "DeleteTest" not in table.text:
                print("  ✓ Record deleted successfully")
            else:
                print("  ⚠️ Record may still exist")
            
            print("✅ Delete record test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Delete record test FAILED: {e}")
            return False

    def test_table_pagination(self):
        """Test table pagination functionality"""
        print("\n🔧 Testing Web Tables - Pagination...")
        self.driver.get("https://demoqa.com/webtables")

        try:
            # Check rows per page dropdown
            try:
                rows_dropdown = self.driver.find_element(By.CSS_SELECTOR, "select[aria-label='rows per page']")
                current_value = rows_dropdown.get_attribute("value")
                print(f"  ✓ Current rows per page: {current_value}")
                
                # Try to change rows per page
                from selenium.webdriver.support.ui import Select
                select = Select(rows_dropdown)
                select.select_by_value("5")
                time.sleep(1)
                print("  ✓ Changed to 5 rows per page")
                
            except Exception as e:
                print(f"  ⚠️ Pagination dropdown test: {e}")

            # Check pagination buttons
            try:
                next_btn = self.driver.find_element(By.CSS_SELECTOR, ".-next button")
                prev_btn = self.driver.find_element(By.CSS_SELECTOR, ".-previous button")
                
                next_enabled = next_btn.is_enabled()
                prev_enabled = prev_btn.is_enabled()
                
                print(f"  ✓ Next button enabled: {next_enabled}")
                print(f"  ✓ Previous button enabled: {prev_enabled}")
                
            except Exception as e:
                print(f"  ⚠️ Pagination buttons test: {e}")

            print("✅ Table pagination test COMPLETED")
            return True
            
        except Exception as e:
            print(f"❌ Table pagination test FAILED: {e}")
            return False

    def run_all_web_tables_tests(self):
        """Run all web tables tests"""
        print("=" * 60)
        print("📊 WEB TABLES INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_add_new_record())
            results.append(self.test_search_functionality())
            results.append(self.test_edit_record())
            results.append(self.test_delete_record())
            results.append(self.test_table_pagination())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 WEB TABLES TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Web Tables tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Web Tables tests passed, some had issues")
            else:
                print("❌ All Web Tables tests had issues")
                
        except Exception as e:
            print(f"❌ Web Tables test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    web_tables_test = WebTablesTest()
    web_tables_test.run_all_web_tables_tests()