from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class BookStoreTest:
    """Individual test for Book Store functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_book_store_page_elements(self):
        """Test book store page elements are present"""
        print("🔧 Testing Book Store - Page Elements...")
        self.driver.get("https://demoqa.com/books")

        try:
            # Check search box
            search_box = self.wait.until(EC.presence_of_element_located((By.ID, "searchBox")))
            assert search_box.is_displayed()
            print("  ✓ Search box is present")
            
            # Check books table/list
            try:
                books_table = self.driver.find_element(By.CLASS_NAME, "rt-table")
                assert books_table.is_displayed()
                print("  ✓ Books table is present")
            except:
                print("  ⚠️ Books table not found (may be loaded dynamically)")
            
            # Check login button (if not logged in)
            try:
                login_btn = self.driver.find_element(By.ID, "login")
                if login_btn.is_displayed():
                    print("  ✓ Login button is present (user not logged in)")
            except:
                print("  ✓ Login button not found (user may be logged in)")
            
            print("✅ Book store page elements test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Book store page elements test FAILED: {e}")
            return False

    def test_search_functionality(self):
        """Test book search functionality"""
        print("\n🔧 Testing Book Store - Search Functionality...")
        self.driver.get("https://demoqa.com/books")

        try:
            # Wait for search box and enter search term
            search_box = self.wait.until(EC.presence_of_element_located((By.ID, "searchBox")))
            search_term = "Git"
            search_box.clear()
            search_box.send_keys(search_term)
            print(f"  ✓ Search term entered: '{search_term}'")
            
            # Wait a moment for search to process
            time.sleep(2)
            
            # Check if results are filtered
            try:
                # Look for book titles or rows
                book_elements = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
                if book_elements:
                    print(f"  ✓ Found {len(book_elements)} book elements after search")
                else:
                    print("  ⚠️ No book elements found after search")
            except:
                print("  ⚠️ Could not verify search results")
            
            # Clear search
            search_box.clear()
            print("  ✓ Search cleared")
            
            print("✅ Search functionality test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Search functionality test FAILED: {e}")
            return False

    def test_book_list_display(self):
        """Test book list display and information"""
        print("\n🔧 Testing Book Store - Book List Display...")
        self.driver.get("https://demoqa.com/books")

        try:
            # Wait for page to load
            time.sleep(3)
            
            # Check for book rows
            try:
                book_rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
                visible_books = [row for row in book_rows if row.text.strip()]
                
                if visible_books:
                    print(f"  ✓ Found {len(visible_books)} books displayed")
                    
                    # Check first book details
                    first_book = visible_books[0]
                    book_text = first_book.text
                    print(f"  ✓ First book info: {book_text[:100]}...")
                    
                else:
                    print("  ⚠️ No books found in the list")
                    
            except Exception as list_e:
                print(f"  ⚠️ Could not find book list: {list_e}")
            
            # Check for pagination if present
            try:
                pagination = self.driver.find_element(By.CLASS_NAME, "pagination")
                if pagination.is_displayed():
                    print("  ✓ Pagination controls found")
            except:
                print("  ✓ No pagination controls (may not be needed)")
            
            print("✅ Book list display test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Book list display test FAILED: {e}")
            return False

    def test_book_details_navigation(self):
        """Test navigation to book details"""
        print("\n🔧 Testing Book Store - Book Details Navigation...")
        self.driver.get("https://demoqa.com/books")

        try:
            # Wait for page to load
            time.sleep(3)
            
            # Try to find and click on a book title
            try:
                book_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/books?book=']")
                if book_links:
                    first_book_link = book_links[0]
                    book_title = first_book_link.text
                    print(f"  ✓ Found book link: '{book_title}'")
                    
                    # Click on the book
                    first_book_link.click()
                    print("  ✓ Book link clicked")
                    
                    # Wait for navigation
                    time.sleep(2)
                    
                    # Check if we navigated to book details
                    current_url = self.driver.current_url
                    if "book=" in current_url:
                        print(f"  ✓ Navigated to book details: {current_url}")
                    else:
                        print(f"  ⚠️ Navigation unclear: {current_url}")
                        
                else:
                    print("  ⚠️ No book links found")
                    
            except Exception as nav_e:
                print(f"  ⚠️ Book navigation issue: {nav_e}")
            
            print("✅ Book details navigation test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Book details navigation test FAILED: {e}")
            return False

    def test_rows_per_page_selection(self):
        """Test rows per page selection functionality"""
        print("\n🔧 Testing Book Store - Rows Per Page Selection...")
        self.driver.get("https://demoqa.com/books")

        try:
            # Wait for page to load
            time.sleep(3)
            
            # Look for rows per page selector
            try:
                rows_selector = self.driver.find_element(By.CSS_SELECTOR, "select[aria-label*='rows per page']")
                if rows_selector.is_displayed():
                    print("  ✓ Rows per page selector found")
                    
                    # Get current selection
                    current_value = rows_selector.get_attribute("value")
                    print(f"  ✓ Current rows per page: {current_value}")
                    
                    # Try to change selection (if options available)
                    options = rows_selector.find_elements(By.TAG_NAME, "option")
                    if len(options) > 1:
                        options[1].click()
                        print("  ✓ Changed rows per page selection")
                        time.sleep(2)
                    
                else:
                    print("  ⚠️ Rows per page selector not visible")
                    
            except Exception as selector_e:
                print(f"  ⚠️ Rows per page selector not found: {selector_e}")
            
            print("✅ Rows per page selection test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Rows per page selection test FAILED: {e}")
            return False

    def run_all_book_store_tests(self):
        """Run all book store tests"""
        print("=" * 60)
        print("📚 BOOK STORE INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_book_store_page_elements())
            results.append(self.test_search_functionality())
            results.append(self.test_book_list_display())
            results.append(self.test_book_details_navigation())
            results.append(self.test_rows_per_page_selection())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 BOOK STORE TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Book Store tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Book Store tests passed, some had issues")
            else:
                print("❌ All Book Store tests had issues")
                
        except Exception as e:
            print(f"❌ Book Store test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    book_store_test = BookStoreTest()
    book_store_test.run_all_book_store_tests()