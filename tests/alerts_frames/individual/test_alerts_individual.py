from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time


class AlertsTest:
    """Individual test for Alerts functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_simple_alert(self):
        """Test simple alert functionality"""
        print("🔧 Testing Alerts - Simple Alert...")
        self.driver.get("https://demoqa.com/alerts")

        try:
            # Click simple alert button
            alert_btn = self.driver.find_element(By.ID, "alertButton")
            alert_btn.click()
            print("  ✓ Simple alert button clicked")
            
            # Wait for alert and switch to it
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"  ✓ Alert text: '{alert_text}'")
            
            # Verify alert text
            assert "You clicked a button" in alert_text
            
            # Accept the alert
            alert.accept()
            print("  ✓ Alert accepted")
            
            print("✅ Simple alert test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Simple alert test FAILED: {e}")
            return False

    def test_timer_alert(self):
        """Test timer alert functionality"""
        print("\n🔧 Testing Alerts - Timer Alert...")
        self.driver.get("https://demoqa.com/alerts")

        try:
            # Click timer alert button
            timer_alert_btn = self.driver.find_element(By.ID, "timerAlertButton")
            timer_alert_btn.click()
            print("  ✓ Timer alert button clicked")
            
            # Wait for alert to appear (it appears after 5 seconds)
            print("  ⏳ Waiting for timer alert to appear...")
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"  ✓ Timer alert text: '{alert_text}'")
            
            # Verify alert text
            assert "This alert appeared after 5 seconds" in alert_text
            
            # Accept the alert
            alert.accept()
            print("  ✓ Timer alert accepted")
            
            print("✅ Timer alert test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Timer alert test FAILED: {e}")
            return False

    def test_confirm_alert_accept(self):
        """Test confirm alert with accept"""
        print("\n🔧 Testing Alerts - Confirm Alert (Accept)...")
        self.driver.get("https://demoqa.com/alerts")

        try:
            # Click confirm alert button
            confirm_btn = self.driver.find_element(By.ID, "confirmButton")
            confirm_btn.click()
            print("  ✓ Confirm alert button clicked")
            
            # Wait for alert and switch to it
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"  ✓ Confirm alert text: '{alert_text}'")
            
            # Verify alert text
            assert "Do you confirm action?" in alert_text
            
            # Accept the alert
            alert.accept()
            print("  ✓ Confirm alert accepted")
            
            # Verify result message
            result = self.driver.find_element(By.ID, "confirmResult")
            assert "You selected Ok" in result.text
            print(f"  ✓ Result verified: '{result.text}'")
            
            print("✅ Confirm alert (accept) test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Confirm alert (accept) test FAILED: {e}")
            return False

    def test_confirm_alert_dismiss(self):
        """Test confirm alert with dismiss"""
        print("\n🔧 Testing Alerts - Confirm Alert (Dismiss)...")
        self.driver.get("https://demoqa.com/alerts")

        try:
            # Click confirm alert button
            confirm_btn = self.driver.find_element(By.ID, "confirmButton")
            confirm_btn.click()
            print("  ✓ Confirm alert button clicked")
            
            # Wait for alert and switch to it
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"  ✓ Confirm alert text: '{alert_text}'")
            
            # Verify alert text
            assert "Do you confirm action?" in alert_text
            
            # Dismiss the alert
            alert.dismiss()
            print("  ✓ Confirm alert dismissed")
            
            # Verify result message
            result = self.driver.find_element(By.ID, "confirmResult")
            assert "You selected Cancel" in result.text
            print(f"  ✓ Result verified: '{result.text}'")
            
            print("✅ Confirm alert (dismiss) test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Confirm alert (dismiss) test FAILED: {e}")
            return False

    def test_prompt_alert(self):
        """Test prompt alert functionality"""
        print("\n🔧 Testing Alerts - Prompt Alert...")
        self.driver.get("https://demoqa.com/alerts")

        try:
            # Click prompt alert button
            prompt_btn = self.driver.find_element(By.ID, "promtButton")
            prompt_btn.click()
            print("  ✓ Prompt alert button clicked")
            
            # Wait for alert and switch to it
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"  ✓ Prompt alert text: '{alert_text}'")
            
            # Verify alert text
            assert "Please enter your name" in alert_text
            
            # Send text to prompt
            test_name = "Test User"
            alert.send_keys(test_name)
            print(f"  ✓ Text entered in prompt: '{test_name}'")
            
            # Accept the alert
            alert.accept()
            print("  ✓ Prompt alert accepted")
            
            # Verify result message
            result = self.driver.find_element(By.ID, "promptResult")
            assert test_name in result.text
            print(f"  ✓ Result verified: '{result.text}'")
            
            print("✅ Prompt alert test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Prompt alert test FAILED: {e}")
            return False

    def run_all_alerts_tests(self):
        """Run all alerts tests"""
        print("=" * 60)
        print("🚨 ALERTS INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_simple_alert())
            results.append(self.test_timer_alert())
            results.append(self.test_confirm_alert_accept())
            results.append(self.test_confirm_alert_dismiss())
            results.append(self.test_prompt_alert())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 ALERTS TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All Alerts tests PASSED!")
            elif passed > 0:
                print("⚠️ Some Alerts tests passed, some had issues")
            else:
                print("❌ All Alerts tests had issues")
                
        except Exception as e:
            print(f"❌ Alerts test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    alerts_test = AlertsTest()
    alerts_test.run_all_alerts_tests()