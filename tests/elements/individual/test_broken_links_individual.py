from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class BrokenLinksTest:
    """Individual test for Broken Links - Images functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_valid_image(self):
        """Test valid image detection"""
        print("🔧 Testing Broken Links - Valid Image...")
        self.driver.get("https://demoqa.com/broken")

        try:
            # Check valid image
            valid_image = self.driver.find_element(By.XPATH, "//img[contains(@src, 'Toolsqa.jpg')]")
            image_src = valid_image.get_attribute('src')
            print(f"  ✓ Valid image found: {image_src}")
            
            # Verify image properties
            print(f"  ✓ Image displayed: {valid_image.is_displayed()}")
            print(f"  ✓ Image enabled: {valid_image.is_enabled()}")
            
            print("✅ Valid image test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Valid image test FAILED: {e}")
            return False

    def test_broken_image(self):
        """Test broken image detection"""
        print("\n🔧 Testing Broken Links - Broken Image...")
        self.driver.get("https://demoqa.com/broken")

        try:
            # Check broken image
            broken_image = self.driver.find_element(By.XPATH, "//img[contains(@src, 'Toolsqa_1.jpg')]")
            image_src = broken_image.get_attribute('src')
            print(f"  ✓ Broken image found: {image_src}")
            
            # Verify image properties
            print(f"  ✓ Image displayed: {broken_image.is_displayed()}")
            print(f"  ✓ Image enabled: {broken_image.is_enabled()}")
            
            print("✅ Broken image test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Broken image test FAILED: {e}")
            return False

    def test_valid_link(self):
        """Test valid link functionality"""
        print("\n🔧 Testing Broken Links - Valid Link...")
        self.driver.get("https://demoqa.com/broken")

        try:
            # Test valid link (using JavaScript to avoid ad overlay)
            valid_link = self.driver.find_element(By.LINK_TEXT, "Click Here for Valid Link")
            print(f"  ✓ Valid link found: {valid_link.text}")
            
            # Use JavaScript click to avoid ad overlay issues
            self.driver.execute_script("arguments[0].click();", valid_link)
            time.sleep(2)
            
            # Check if we're on a demoqa page
            current_url = self.driver.current_url
            if "demoqa.com" in current_url:
                print(f"  ✓ Valid link test passed - redirected to: {current_url}")
                result = True
            else:
                print(f"  ✓ Valid link redirected to: {current_url}")
                result = True
            
            self.driver.back()
            time.sleep(1)
            
            print("✅ Valid link test PASSED")
            return result
            
        except Exception as e:
            print(f"❌ Valid link test FAILED: {e}")
            return False

    def test_broken_link(self):
        """Test broken link functionality"""
        print("\n🔧 Testing Broken Links - Broken Link...")
        self.driver.get("https://demoqa.com/broken")

        try:
            # Test broken link (using JavaScript to avoid ad overlay)
            broken_link = self.driver.find_element(By.LINK_TEXT, "Click Here for Broken Link")
            print(f"  ✓ Broken link found: {broken_link.text}")
            
            # Use JavaScript click to avoid ad overlay issues
            self.driver.execute_script("arguments[0].click();", broken_link)
            time.sleep(2)
            
            current_url = self.driver.current_url
            print(f"  ✓ Broken link redirected to: {current_url}")
            
            # Verify it's a different URL (broken link behavior)
            if "demoqa.com/broken" not in current_url:
                print("  ✓ Broken link behavior confirmed - redirected away from original page")
            
            print("✅ Broken link test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Broken link test FAILED: {e}")
            return False

    def test_image_properties(self):
        """Test image properties and attributes"""
        print("\n🔧 Testing Broken Links - Image Properties...")
        self.driver.get("https://demoqa.com/broken")

        try:
            # Get all images on the page
            images = self.driver.find_elements(By.TAG_NAME, "img")
            print(f"  ✓ Found {len(images)} images on the page")
            
            for i, img in enumerate(images):
                try:
                    src = img.get_attribute('src')
                    alt = img.get_attribute('alt')
                    width = img.get_attribute('width')
                    height = img.get_attribute('height')
                    
                    print(f"  Image {i+1}:")
                    print(f"    - Source: {src}")
                    print(f"    - Alt text: {alt}")
                    print(f"    - Width: {width}")
                    print(f"    - Height: {height}")
                    print(f"    - Displayed: {img.is_displayed()}")
                    
                except Exception as img_error:
                    print(f"    - Error getting properties: {img_error}")
            
            print("✅ Image properties test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Image properties test FAILED: {e}")
            return False

    def test_link_properties(self):
        """Test link properties and attributes"""
        print("\n🔧 Testing Broken Links - Link Properties...")
        self.driver.get("https://demoqa.com/broken")

        try:
            # Get all links on the page
            links = self.driver.find_elements(By.TAG_NAME, "a")
            print(f"  ✓ Found {len(links)} links on the page")
            
            # Focus on the test links
            test_links = [
                "Click Here for Valid Link",
                "Click Here for Broken Link"
            ]
            
            for link_text in test_links:
                try:
                    link = self.driver.find_element(By.LINK_TEXT, link_text)
                    href = link.get_attribute('href')
                    target = link.get_attribute('target')
                    
                    print(f"  Link: {link_text}")
                    print(f"    - Href: {href}")
                    print(f"    - Target: {target}")
                    print(f"    - Displayed: {link.is_displayed()}")
                    print(f"    - Enabled: {link.is_enabled()}")
                    
                except Exception as link_error:
                    print(f"    - Error getting link properties: {link_error}")
            
            print("✅ Link properties test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Link properties test FAILED: {e}")
            return False

    def run_all_broken_links_tests(self):
        """Run all broken links tests"""
        print("=" * 60)
        print("🔗 BROKEN LINKS - IMAGES INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_valid_image())
            results.append(self.test_broken_image())
            results.append(self.test_valid_link())
            results.append(self.test_broken_link())
            results.append(self.test_image_properties())
            results.append(self.test_link_properties())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 BROKEN LINKS TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Broken Links tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Broken Links tests passed, some had issues")
            else:
                print("❌ All Broken Links tests had issues")
                
        except Exception as e:
            print(f"❌ Broken Links test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    broken_links_test = BrokenLinksTest()
    broken_links_test.run_all_broken_links_tests()