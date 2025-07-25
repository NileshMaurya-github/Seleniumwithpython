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
from test_practice_form_individual import PracticeFormTest


class FormsIndividualTestRunner:
    """Master test runner for all individual Forms tests"""
    
    def __init__(self):
        self.results = {
            'Practice Form': False
        }
    
    def run_practice_form_tests(self):
        """Run Practice Form individual tests"""
        print("📝 RUNNING PRACTICE FORM INDIVIDUAL TESTS")
        print("=" * 60)
        try:
            practice_form_test = PracticeFormTest()
            practice_form_test.run_all_practice_form_tests()
            self.results['Practice Form'] = True
        except Exception as e:
            print(f"❌ Practice Form individual tests failed: {e}")
            self.results['Practice Form'] = False
    
    def print_summary(self):
        """Print test execution summary"""
        print("\n" + "=" * 80)
        print("📊 FORMS INDIVIDUAL TESTS EXECUTION SUMMARY")
        print("=" * 80)
        
        passed = sum(1 for result in self.results.values() if result)
        total = len(self.results)
        
        for section, result in self.results.items():
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"{section:<20}: {status}")
        
        print("-" * 80)
        print(f"TOTAL: {passed}/{total} individual test sections passed")
        
        success_rate = (passed / total) * 100
        print(f"SUCCESS RATE: {success_rate:.1f}%")
        
        if passed == total:
            print("🎉 ALL INDIVIDUAL TESTS COMPLETED SUCCESSFULLY!")
        elif passed > total // 2:
            print("⚠️  MOST INDIVIDUAL TESTS PASSED - Some had issues")
        else:
            print("❌ MANY INDIVIDUAL TESTS HAD ISSUES - Check logs above")
        
        return passed == total
    
    def run_all_individual_tests(self, sections=None):
        """Run all or specific sections of individual tests"""
        start_time = time.time()
        
        print("🚀 Starting DemoQA Forms Individual Test Suite")
        print(f"⏰ Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        # Default to all sections if none specified
        if sections is None:
            sections = ['practice_form']
        
        # Run specified sections
        if 'practice_form' in sections:
            self.run_practice_form_tests()
        
        # Print summary
        all_passed = self.print_summary()
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"⏱️  Total execution time: {duration:.2f} seconds")
        
        return all_passed


def main():
    """Main function to run individual tests based on command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description='DemoQA Forms Individual Test Runner')
    parser.add_argument('--sections', nargs='+', 
                       choices=['practice_form'],
                       help='Specific sections to test (default: all)')
    
    args = parser.parse_args()
    
    runner = FormsIndividualTestRunner()
    success = runner.run_all_individual_tests(args.sections)
    
    # Exit with appropriate code for CI/CD
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()