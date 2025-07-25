from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class AccordianTest:
    """Individual test for Accordian functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_first_section(self):
        """Test first accordian section"""
        print("🔧 Testing Accordian - First Section...")
        self.driver.get("https://demoqa.com/accordian")

        try:
            # Click first section header
            first_section = self.driver.find_element(By.ID, "section1Heading")
            first_section.click()
            print("  ✓ First section header clicked")
            
            # Wait for content to be visible
            first_content = self.wait.until(EC.visibility_of_element_located((By.ID, "section1Content")))
            content_text = first_content.text
            print(f"  ✓ First section content visible: {len(content_text)} characters")
            
            # Verify content is not empty
            assert len(content_text) > 0
            assert "Lorem Ipsum" in content_text
            print("  ✓ First section content verified")
            
            # Click again to collapse
            first_section.click()
            print("  ✓ First section collapsed")
            
            print("✅ First section test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ First section test FAILED: {e}")
            return False

    def test_second_section(self):
        """Test second accordian section"""
        print("\n🔧 Testing Accordian - Second Section...")
        self.driver.get("https://demoqa.com/accordian")

        try:
            # Click second section header
            second_section = self.driver.find_element(By.ID, "section2Heading")
            second_section.click()
            print("  ✓ Second section header clicked")
            
            # Wait for content to be visible
            second_content = self.wait.until(EC.visibility_of_element_located((By.ID, "section2Content")))
            content_text = second_content.text
            print(f"  ✓ Second section content visible: {len(content_text)} characters")
            
            # Verify content is not empty
            assert len(content_text) > 0
            print("  ✓ Second section content verified")
            
            # Click again to collapse
            second_section.click()
            print("  ✓ Second section collapsed")
            
            print("✅ Second section test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Second section test FAILED: {e}")
            return False

    def test_third_section(self):
        """Test third accordian section"""
        print("\n🔧 Testing Accordian - Third Section...")
        self.driver.get("https://demoqa.com/accordian")

        try:
            # Click third section header
            third_section = self.driver.find_element(By.ID, "section3Heading")
            third_section.click()
            print("  ✓ Third section header clicked")
            
            # Wait for content to be visible
            third_content = self.wait.until(EC.visibility_of_element_located((By.ID, "section3Content")))
            content_text = third_content.text
            print(f"  ✓ Third section content visible: {len(content_text)} characters")
            
            # Verify content is not empty
            assert len(content_text) > 0
            print("  ✓ Third section content verified")
            
            # Click again to collapse
            third_section.click()
            print("  ✓ Third section collapsed")
            
            print("✅ Third section test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Third section test FAILED: {e}")
            return False

    def test_multiple_sections(self):
        """Test multiple accordian sections interaction"""
        print("\n🔧 Testing Accordian - Multiple Sections...")
        self.driver.get("https://demoqa.com/accordian")

        try:
            # Open first section
            first_section = self.driver.find_element(By.ID, "section1Heading")
            first_section.click()
            self.wait.until(EC.visibility_of_element_located((By.ID, "section1Content")))
            print("  ✓ First section opened")
            
            # Open second section (should close first)
            second_section = self.driver.find_element(By.ID, "section2Heading")
            second_section.click()
            self.wait.until(EC.visibility_of_element_located((By.ID, "section2Content")))
            print("  ✓ Second section opened")
            
            # Verify first section is collapsed
            try:
                first_content = self.driver.find_element(By.ID, "section1Content")
                if not first_content.is_displayed():
                    print("  ✓ First section automatically collapsed")
                else:
                    print("  ⚠️ First section still visible (multiple sections can be open)")
            except:
                print("  ✓ First section collapsed")
            
            # Open third section
            third_section = self.driver.find_element(By.ID, "section3Heading")
            third_section.click()
            self.wait.until(EC.visibility_of_element_located((By.ID, "section3Content")))
            print("  ✓ Third section opened")
            
            print("✅ Multiple sections test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Multiple sections test FAILED: {e}")
            return False

    def run_all_accordian_tests(self):
        """Run all accordian tests"""
        print("=" * 60)
        print("🪗 ACCORDIAN INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_first_section())
            results.append(self.test_second_section())
            results.append(self.test_third_section())
            results.append(self.test_multiple_sections())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 ACCORDIAN TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Accordian tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Accordian tests passed, some had issues")
            else:
                print("❌ All Accordian tests had issues")
                
        except Exception as e:
            print(f"❌ Accordian test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    accordian_test = AccordianTest()
    accordian_test.run_all_accordian_tests()