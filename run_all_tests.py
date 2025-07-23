from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

# Add the tests directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tests'))

from tests.elements.demoqa_elements import DemoQAElements
from tests.forms.demoqa_forms import DemoQAForms
from tests.alerts_frames.demoqa_alerts_frames import DemoQAAlertsFrames
from tests.widgets.demoqa_widgets import DemoQAWidgets
from tests.interactions.demoqa_interactions import DemoQAInteractions
from tests.bookstore.demoqa_bookstore import DemoQABookStore


class DemoQATestRunner:
    """Main test runner for all DemoQA sections"""
    
    def __init__(self):
        self.results = {
            'Elements': False,
            'Forms': False,
            'Alerts_Frames': False,
            'Widgets': False,
            'Interactions': False,
            'BookStore': False
        }
    
    def run_elements_tests(self):
        """Run Elements section tests"""
        print("=" * 60)
        print("🔧 RUNNING ELEMENTS TESTS")
        print("=" * 60)
        try:
            elements_test = DemoQAElements()
            elements_test.run_all_tests()
            self.results['Elements'] = True
        except Exception as e:
            print(f"❌ Elements tests failed: {e}")
            self.results['Elements'] = False
    
    def run_forms_tests(self):
        """Run Forms section tests"""
        print("\n" + "=" * 60)
        print("📝 RUNNING FORMS TESTS")
        print("=" * 60)
        try:
            forms_test = DemoQAForms()
            forms_test.run_all_tests()
            self.results['Forms'] = True
        except Exception as e:
            print(f"❌ Forms tests failed: {e}")
            self.results['Forms'] = False
    
    def run_alerts_frames_tests(self):
        """Run Alerts, Frame & Windows section tests"""
        print("\n" + "=" * 60)
        print("🚨 RUNNING ALERTS, FRAME & WINDOWS TESTS")
        print("=" * 60)
        try:
            alerts_frames_test = DemoQAAlertsFrames()
            alerts_frames_test.run_all_tests()
            self.results['Alerts_Frames'] = True
        except Exception as e:
            print(f"❌ Alerts, Frame & Windows tests failed: {e}")
            self.results['Alerts_Frames'] = False
    
    def run_widgets_tests(self):
        """Run Widgets section tests"""
        print("\n" + "=" * 60)
        print("🎛️ RUNNING WIDGETS TESTS")
        print("=" * 60)
        try:
            widgets_test = DemoQAWidgets()
            widgets_test.run_all_tests()
            self.results['Widgets'] = True
        except Exception as e:
            print(f"❌ Widgets tests failed: {e}")
            self.results['Widgets'] = False
    
    def run_interactions_tests(self):
        """Run Interactions section tests"""
        print("\n" + "=" * 60)
        print("🤝 RUNNING INTERACTIONS TESTS")
        print("=" * 60)
        try:
            interactions_test = DemoQAInteractions()
            interactions_test.run_all_tests()
            self.results['Interactions'] = True
        except Exception as e:
            print(f"❌ Interactions tests failed: {e}")
            self.results['Interactions'] = False
    
    def run_bookstore_tests(self):
        """Run Book Store Application section tests"""
        print("\n" + "=" * 60)
        print("📚 RUNNING BOOK STORE APPLICATION TESTS")
        print("=" * 60)
        try:
            bookstore_test = DemoQABookStore()
            bookstore_test.run_all_tests()
            self.results['BookStore'] = True
        except Exception as e:
            print(f"❌ Book Store Application tests failed: {e}")
            self.results['BookStore'] = False
    
    def print_summary(self):
        """Print test execution summary"""
        print("\n" + "=" * 60)
        print("📊 TEST EXECUTION SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.results.values() if result)
        total = len(self.results)
        
        for section, result in self.results.items():
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"{section:<20}: {status}")
        
        print("-" * 60)
        print(f"TOTAL: {passed}/{total} sections passed")
        
        if passed == total:
            print("🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
        else:
            print("⚠️  Some tests failed. Check logs above for details.")
        
        return passed == total
    
    def run_all_tests(self, sections=None):
        """Run all or specific sections of tests"""
        start_time = time.time()
        
        print("🚀 Starting DemoQA Selenium Test Suite")
        print(f"⏰ Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Default to all sections if none specified
        if sections is None:
            sections = ['elements', 'forms', 'alerts_frames', 'widgets', 'interactions', 'bookstore']
        
        # Run specified sections
        if 'elements' in sections:
            self.run_elements_tests()
        
        if 'forms' in sections:
            self.run_forms_tests()
        
        if 'alerts_frames' in sections:
            self.run_alerts_frames_tests()
        
        if 'widgets' in sections:
            self.run_widgets_tests()
        
        if 'interactions' in sections:
            self.run_interactions_tests()
        
        if 'bookstore' in sections:
            self.run_bookstore_tests()
        
        # Print summary
        all_passed = self.print_summary()
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"⏱️  Total execution time: {duration:.2f} seconds")
        
        return all_passed


def main():
    """Main function to run tests based on command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description='DemoQA Selenium Test Runner')
    parser.add_argument('--sections', nargs='+', 
                       choices=['elements', 'forms', 'alerts_frames', 'widgets', 'interactions', 'bookstore'],
                       help='Specific sections to test (default: all)')
    
    args = parser.parse_args()
    
    runner = DemoQATestRunner()
    success = runner.run_all_tests(args.sections)
    
    # Exit with appropriate code for CI/CD
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()