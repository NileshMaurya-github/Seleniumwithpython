#!/usr/bin/env python3
"""
Simple Test Runner for DemoQA Selenium Automation Project
=========================================================

This script runs all available tests in the project with basic reporting.

Usage:
    python run_all_tests_simple.py [category]

Categories:
    elements, forms, interactions, widgets, alerts, bookstore, all (default)
"""

import os
import sys
import subprocess
import time
from datetime import datetime


def get_python_executable():
    """Get the correct Python executable path"""
    if sys.platform == "win32":
        return f'"{os.environ.get("LOCALAPPDATA")}\\Programs\\Python\\Python312\\python.exe"'
    else:
        return "python3"


def run_test_category(category, python_exe):
    """Run tests for a specific category"""
    test_scripts = {
        'elements': 'tests/elements/individual/run_all_individual_tests.py',
        'forms': 'tests/forms/individual/run_all_individual_tests.py',
        'interactions': 'tests/interactions/individual/run_all_individual_tests.py',
        'widgets': 'tests/widgets/individual/run_all_individual_tests.py',
        'alerts': 'tests/alerts_frames/individual/run_all_individual_tests.py',
        'bookstore': 'tests/bookstore/individual/run_all_individual_tests.py'
    }
    
    if category not in test_scripts:
        print(f"❌ Unknown category: {category}")
        return False
    
    script_path = test_scripts[category]
    
    if not os.path.exists(script_path):
        print(f"❌ Test script not found: {script_path}")
        return False
    
    print(f"\n{'='*80}")
    print(f"🚀 RUNNING {category.upper()} TESTS")
    print(f"{'='*80}")
    print(f"Script: {script_path}")
    
    start_time = time.time()
    
    try:
        # Run the test script
        result = subprocess.run(
            f"{python_exe} {script_path}",
            shell=True,
            cwd=os.path.dirname(os.path.abspath(__file__)),
            timeout=600  # 10 minutes timeout
        )
        
        duration = time.time() - start_time
        success = result.returncode == 0
        
        print(f"\n{'='*80}")
        print(f"📊 {category.upper()} TESTS COMPLETED")
        print(f"{'='*80}")
        print(f"⏱️ Duration: {duration:.2f} seconds")
        print(f"📈 Result: {'✅ SUCCESS' if success else '❌ FAILURE'}")
        print(f"🔢 Exit Code: {result.returncode}")
        
        return success
        
    except subprocess.TimeoutExpired:
        print(f"❌ {category} tests timed out after 10 minutes")
        return False
    except Exception as e:
        print(f"❌ Error running {category} tests: {e}")
        return False


def main():
    """Main function"""
    print("🧪 DemoQA Selenium Test Suite - Simple Runner")
    print(f"⏰ Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get category from command line argument
    category = sys.argv[1] if len(sys.argv) > 1 else 'all'
    
    python_exe = get_python_executable()
    
    categories_to_run = []
    if category == 'all':
        categories_to_run = ['elements', 'forms', 'interactions', 'widgets', 'alerts', 'bookstore']
    else:
        categories_to_run = [category]
    
    print(f"📋 Categories to run: {', '.join(categories_to_run)}")
    
    overall_start = time.time()
    results = []
    
    for cat in categories_to_run:
        success = run_test_category(cat, python_exe)
        results.append((cat, success))
    
    total_duration = time.time() - overall_start
    
    print(f"\n{'='*80}")
    print("🏁 ALL TESTS COMPLETED")
    print(f"{'='*80}")
    print(f"⏰ End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️ Total duration: {total_duration:.2f} seconds")
    
    print(f"\n📊 RESULTS SUMMARY:")
    print(f"{'='*80}")
    
    passed_count = 0
    for cat, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"  {cat.upper():15} - {status}")
        if success:
            passed_count += 1
    
    success_rate = (passed_count / len(results)) * 100 if results else 0
    
    print(f"\n📈 Overall Success Rate: {success_rate:.1f}% ({passed_count}/{len(results)})")
    
    overall_success = passed_count == len(results)
    print(f"🎯 Final Result: {'✅ ALL TESTS PASSED' if overall_success else '❌ SOME TESTS FAILED'}")
    
    return 0 if overall_success else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)