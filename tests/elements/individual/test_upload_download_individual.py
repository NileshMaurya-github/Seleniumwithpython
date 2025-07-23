from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


class UploadDownloadTest:
    """Individual test for Upload and Download functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_download_functionality(self):
        """Test download functionality"""
        print("🔧 Testing Upload Download - Download...")
        self.driver.get("https://demoqa.com/upload-download")

        try:
            # Test download
            download_btn = self.driver.find_element(By.ID, "downloadButton")
            print(f"  ✓ Download button found: {download_btn.text}")
            print(f"  ✓ Download button enabled: {download_btn.is_enabled()}")
            print(f"  ✓ Download button displayed: {download_btn.is_displayed()}")
            
            # Click download button
            download_btn.click()
            time.sleep(2)
            print("  ✓ Download initiated")
            
            print("✅ Download functionality test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Download functionality test FAILED: {e}")
            return False

    def test_upload_functionality(self):
        """Test upload functionality"""
        print("\n🔧 Testing Upload Download - Upload...")
        self.driver.get("https://demoqa.com/upload-download")

        try:
            # Create a temporary file for upload
            test_file_path = os.path.join(os.getcwd(), "test_upload.txt")
            with open(test_file_path, "w") as f:
                f.write("This is a test file for upload functionality testing")
            print(f"  ✓ Created test file: {test_file_path}")

            # Find upload input
            upload_input = self.driver.find_element(By.ID, "uploadFile")
            print("  ✓ Upload input found")
            
            # Upload the file
            upload_input.send_keys(test_file_path)
            print("  ✓ File uploaded")

            # Verify upload
            uploaded_file_path = self.wait.until(EC.presence_of_element_located((By.ID, "uploadedFilePath")))
            uploaded_text = uploaded_file_path.text
            print(f"  ✓ Upload confirmation: {uploaded_text}")
            
            # Verify the filename appears in the confirmation
            assert "test_upload.txt" in uploaded_text
            print("  ✓ Upload verification successful")

            # Clean up
            os.remove(test_file_path)
            print("  ✓ Test file cleaned up")
            
            print("✅ Upload functionality test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Upload functionality test FAILED: {e}")
            # Clean up in case of error
            test_file_path = os.path.join(os.getcwd(), "test_upload.txt")
            if os.path.exists(test_file_path):
                os.remove(test_file_path)
            return False

    def test_upload_different_file_types(self):
        """Test upload with different file types"""
        print("\n🔧 Testing Upload Download - Different File Types...")
        self.driver.get("https://demoqa.com/upload-download")

        results = []
        file_types = [
            ("test_text.txt", "This is a text file for testing"),
            ("test_data.csv", "Name,Age,City\nJohn,25,NYC\nJane,30,LA"),
            ("test_config.json", '{"name": "test", "version": "1.0"}')
        ]

        for filename, content in file_types:
            try:
                # Create test file
                test_file_path = os.path.join(os.getcwd(), filename)
                with open(test_file_path, "w") as f:
                    f.write(content)
                print(f"  ✓ Created {filename}")

                # Upload the file
                upload_input = self.driver.find_element(By.ID, "uploadFile")
                upload_input.clear()
                upload_input.send_keys(test_file_path)

                # Verify upload
                uploaded_file_path = self.wait.until(EC.presence_of_element_located((By.ID, "uploadedFilePath")))
                uploaded_text = uploaded_file_path.text
                
                if filename in uploaded_text:
                    print(f"  ✓ {filename} uploaded successfully")
                    results.append(True)
                else:
                    print(f"  ❌ {filename} upload failed")
                    results.append(False)

                # Clean up
                os.remove(test_file_path)
                time.sleep(1)
                
            except Exception as e:
                print(f"  ❌ Error with {filename}: {e}")
                results.append(False)
                # Clean up in case of error
                test_file_path = os.path.join(os.getcwd(), filename)
                if os.path.exists(test_file_path):
                    os.remove(test_file_path)

        success_rate = sum(results) / len(results) * 100
        print(f"  📊 File type upload success rate: {success_rate:.1f}%")
        
        if success_rate >= 50:
            print("✅ Different file types test PASSED")
            return True
        else:
            print("❌ Different file types test FAILED")
            return False

    def test_upload_input_properties(self):
        """Test upload input properties"""
        print("\n🔧 Testing Upload Download - Input Properties...")
        self.driver.get("https://demoqa.com/upload-download")

        try:
            # Find upload input
            upload_input = self.driver.find_element(By.ID, "uploadFile")
            
            # Check properties
            input_type = upload_input.get_attribute("type")
            input_accept = upload_input.get_attribute("accept")
            input_multiple = upload_input.get_attribute("multiple")
            
            print(f"  ✓ Input type: {input_type}")
            print(f"  ✓ Input accept: {input_accept}")
            print(f"  ✓ Input multiple: {input_multiple}")
            print(f"  ✓ Input enabled: {upload_input.is_enabled()}")
            print(f"  ✓ Input displayed: {upload_input.is_displayed()}")
            
            # Verify it's a file input
            assert input_type == "file", f"Expected file input, got {input_type}"
            
            print("✅ Upload input properties test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Upload input properties test FAILED: {e}")
            return False

    def test_download_button_properties(self):
        """Test download button properties"""
        print("\n🔧 Testing Upload Download - Download Button Properties...")
        self.driver.get("https://demoqa.com/upload-download")

        try:
            # Find download button
            download_btn = self.driver.find_element(By.ID, "downloadButton")
            
            # Check properties
            button_text = download_btn.text
            button_type = download_btn.get_attribute("type")
            button_class = download_btn.get_attribute("class")
            button_href = download_btn.get_attribute("href")
            
            print(f"  ✓ Button text: {button_text}")
            print(f"  ✓ Button type: {button_type}")
            print(f"  ✓ Button class: {button_class}")
            print(f"  ✓ Button href: {button_href}")
            print(f"  ✓ Button enabled: {download_btn.is_enabled()}")
            print(f"  ✓ Button displayed: {download_btn.is_displayed()}")
            
            print("✅ Download button properties test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Download button properties test FAILED: {e}")
            return False

    def test_page_elements_presence(self):
        """Test presence of all page elements"""
        print("\n🔧 Testing Upload Download - Page Elements...")
        self.driver.get("https://demoqa.com/upload-download")

        try:
            elements_to_check = [
                (By.ID, "downloadButton", "Download button"),
                (By.ID, "uploadFile", "Upload input"),
                (By.XPATH, "//label[@for='uploadFile']", "Upload label")
            ]
            
            all_present = True
            for locator_type, locator_value, element_name in elements_to_check:
                try:
                    element = self.driver.find_element(locator_type, locator_value)
                    print(f"  ✓ {element_name} found and displayed: {element.is_displayed()}")
                except:
                    print(f"  ❌ {element_name} not found")
                    all_present = False
            
            if all_present:
                print("✅ Page elements presence test PASSED")
                return True
            else:
                print("❌ Page elements presence test FAILED")
                return False
            
        except Exception as e:
            print(f"❌ Page elements presence test FAILED: {e}")
            return False

    def run_all_upload_download_tests(self):
        """Run all upload download tests"""
        print("=" * 60)
        print("📁 UPLOAD DOWNLOAD INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_download_functionality())
            results.append(self.test_upload_functionality())
            results.append(self.test_upload_different_file_types())
            results.append(self.test_upload_input_properties())
            results.append(self.test_download_button_properties())
            results.append(self.test_page_elements_presence())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 UPLOAD DOWNLOAD TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Upload Download tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Upload Download tests passed, some had issues")
            else:
                print("❌ All Upload Download tests had issues")
                
        except Exception as e:
            print(f"❌ Upload Download test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    upload_download_test = UploadDownloadTest()
    upload_download_test.run_all_upload_download_tests()