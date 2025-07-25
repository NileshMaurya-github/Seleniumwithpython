from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

# Import all individual test classes
from test_text_box_individual import TextBoxTest
from test_checkbox_individual import CheckBoxTest
from test_radio_button_individual import RadioButtonTest
from test_web_tables_individual import WebTablesTest
from test_buttons_individual import ButtonsTest
from test_links_individual import LinksTest
from test_broken_links_individual import BrokenLinksTest
from test_upload_download_individual import UploadDownloadTest
from test_dynamic_properties_individual import DynamicPropertiesTest


class ElementsIndividualTestRunner:
    """Master test runner for all individual Elements tests"""
    
    def __init__(self):
        self.results = {
            'Text Box': False,
            'Checkbox': False,
            'Radio Button': False,
            'Web Tables': False,
            'Buttons': False,
            'Links': False,
            'Broken Links': False,
            'Upload Download': False,
            'Dynamic Properties': False
        }
    
    def run_text_box_tests(self):
        """Run Text Box individual tests"""
        print("🔧 RUNNING TEXT BOX INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            text_box_test = TextBoxTest()
            text_box_test.run_all_text_box_tests()
            self.results['Text Box'] = True
        except Exception as e:
            print(f"❌ Text Box individual tests failed: {e}")
            self.results['Text Box'] = False
    
    def run_checkbox_tests(self):
        """Run Checkbox individual tests"""
        print("\n☑️ RUNNING CHECKBOX INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            checkbox_test = CheckBoxTest()
            checkbox_test.run_all_checkbox_tests()
            self.results['Checkbox'] = True
        except Exception as e:
            print(f"❌ Checkbox individual tests failed: {e}")
            self.results['Checkbox'] = False
    
    def run_radio_button_tests(self):
        """Run Radio Button individual tests"""
        print("\n🔘 RUNNING RADIO BUTTON INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            radio_button_test = RadioButtonTest()
            radio_button_test.run_all_radio_button_tests()
            self.results['Radio Button'] = True
        except Exception as e:
            print(f"❌ Radio Button individual tests failed: {e}")
            self.results['Radio Button'] = False
    
    def run_web_tables_tests(self):
        """Run Web Tables individual tests"""
        print("\n📊 RUNNING WEB TABLES INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            web_tables_test = WebTablesTest()
            web_tables_test.run_all_web_tables_tests()
            self.results['Web Tables'] = True
        except Exception as e:
            print(f"❌ Web Tables individual tests failed: {e}")
            self.results['Web Tables'] = False
    
    def run_buttons_tests(self):
        """Run Buttons individual tests"""
        print("\n🔘 RUNNING BUTTONS INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            buttons_test = ButtonsTest()
            buttons_test.run_all_buttons_tests()
            self.results['Buttons'] = True
        except Exception as e:
            print(f"❌ Buttons individual tests failed: {e}")
            self.results['Buttons'] = False
    
    def run_links_tests(self):
        """Run Links individual tests"""
        print("\n🔗 RUNNING LINKS INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            links_test = LinksTest()
            links_test.run_all_links_tests()
            self.results['Links'] = True
        except Exception as e:
            print(f"❌ Links individual tests failed: {e}")
            self.results['Links'] = False
    
    def run_broken_links_tests(self):
        """Run Broken Links individual tests"""
        print("\n🔗 RUNNING BROKEN LINKS INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            broken_links_test = BrokenLinksTest()
            broken_links_test.run_all_broken_links_tests()
            self.results['Broken Links'] = True
        except Exception as e:
            print(f"❌ Broken Links individual tests failed: {e}")
            self.results['Broken Links'] = False
    
    def run_upload_download_tests(self):
        """Run Upload Download individual tests"""
        print("\n📁 RUNNING UPLOAD DOWNLOAD INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            upload_download_test = UploadDownloadTest()
            upload_download_test.run_all_upload_download_tests()
            self.results['Upload Download'] = True
        except Exception as e:
            print(f"❌ Upload Download individual tests failed: {e}")
            self.results['Upload Download'] = False
    
    def run_dynamic_properties_tests(self):
        """Run Dynamic Properties individual tests"""
        print("\n⚡ RUNNING DYNAMIC PROPERTIES INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            dynamic_properties_test = DynamicPropertiesTest()
            dynamic_properties_test.run_all_dynamic_properties_tests()
            self.results['Dynamic Properties'] = True
        except Exception as e:
            print(f"❌ Dynamic Properties individual tests failed: {e}")
            self.results['Dynamic Properties'] = False
    
    def print_summary(self):
        """Print test execution summary"""
        print("\n" + "=" * 80)
        print("ELEMENTS INDIVIDUAL TESTS EXECUTION SUMMARY")
        print("=" * 80)
        
        passed = sum(1 for result in self.results.values() if result)
        total = len(self.results)
        
        for section, result in self.results.items():
            status = "PASSED" if result else "FAILED"
            print(f"{section:<20}: {status}")
        
        print("-" * 80)
        print(f"TOTAL: {passed}/{total} individual test sections passed")
        
        success_rate = (passed / total) * 100
        print(f"SUCCESS RATE: {success_rate:.1f}%")
        
        if passed == total:
            print("ALL INDIVIDUAL TESTS COMPLETED SUCCESSFULLY!")
        elif passed > total // 2:
            print("MOST INDIVIDUAL TESTS PASSED - Some had issues")
        else:
            print("MANY INDIVIDUAL TESTS HAD ISSUES - Check logs above")
        
        return passed == total
    
    def run_all_individual_tests(self, sections=None):
        """Run all or specific sections of individual tests"""
        start_time = time.time()
        
        print("Starting DemoQA Elements Individual Test Suite")
        print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        # Default to all sections if none specified
        if sections is None:
            sections = ['text_box', 'checkbox', 'radio_button', 'web_tables', 
                       'buttons', 'links', 'broken_links', 'upload_download', 'dynamic_properties']
        
        # Run specified sections
        if 'text_box' in sections:
            self.run_text_box_tests()
        
        if 'checkbox' in sections:
            self.run_checkbox_tests()
        
        if 'radio_button' in sections:
            self.run_radio_button_tests()
        
        if 'web_tables' in sections:
            self.run_web_tables_tests()
        
        if 'buttons' in sections:
            self.run_buttons_tests()
        
        if 'links' in sections:
            self.run_links_tests()
        
        if 'broken_links' in sections:
            self.run_broken_links_tests()
        
        if 'upload_download' in sections:
            self.run_upload_download_tests()
        
        if 'dynamic_properties' in sections:
            self.run_dynamic_properties_tests()
        
        # Print summary
        all_passed = self.print_summary()
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"Total execution time: {duration:.2f} seconds")
        
        return all_passed


def main():
    """Main function to run individual tests based on command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description='DemoQA Elements Individual Test Runner')
    parser.add_argument('--sections', nargs='+', 
                       choices=['text_box', 'checkbox', 'radio_button', 'web_tables', 
                               'buttons', 'links', 'broken_links', 'upload_download', 'dynamic_properties'],
                       help='Specific sections to test (default: all)')
    
    args = parser.parse_args()
    
    runner = ElementsIndividualTestRunner()
    success = runner.run_all_individual_tests(args.sections)
    
    # Exit with appropriate code for CI/CD
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()