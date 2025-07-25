#!/usr/bin/env python3
"""
Master Test Runner for DemoQA Selenium Automation Project
=========================================================

This script runs all available tests in the project including:
- Elements Tests (Individual & Allure)
- Forms Tests (Individual & Allure)  
- Alerts & Frames Tests (Individual & Allure)
- Widgets Tests (Individual & Allure)
- Interactions Tests (Individual & Allure)
- Bookstore Tests (Individual & Allure)

Usage:
    python run_all_project_tests.py [options]

Options:
    --browser chrome|firefox|edge    Browser to use (default: chrome)
    --headless                       Run in headless mode
    --individual-only               Run only individual tests
    --allure-only                   Run only allure tests
    --section SECTION               Run specific section (elements, forms, alerts_frames, widgets, interactions, bookstore)
    --verbose                       Verbose output
    --generate-report              Generate final HTML report
"""

import os
import sys
import subprocess
import time
import argparse
from datetime import datetime
import json

class MasterTestRunner:
    def __init__(self):
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        self.python_exe = self._get_python_executable()
        self.results = {
            'start_time': None,
            'end_time': None,
            'total_duration': 0,
            'sections': {},
            'summary': {
                'total_tests': 0,
                'passed_tests': 0,
                'failed_tests': 0,
                'success_rate': 0.0
            }
        }
        
    def _get_python_executable(self):
        """Get the correct Python executable path"""
        if sys.platform == "win32":
            return f'"{os.environ.get("LOCALAPPDATA")}\\Programs\\Python\\Python312\\python.exe"'
        else:
            return "python3"
    
    def _run_command(self, command, cwd=None):
        """Execute a command and return results"""
        try:
            if cwd is None:
                cwd = self.project_root
                
            print(f"🔄 Executing: {command}")
            print(f"📁 Working directory: {cwd}")
            
            result = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout per test suite
            )
            
            return {
                'success': result.returncode == 0,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'stdout': '',
                'stderr': 'Test execution timed out after 5 minutes',
                'returncode': -1
            }
        except Exception as e:
            return {
                'success': False,
                'stdout': '',
                'stderr': str(e),
                'returncode': -1
            }
    
    def _parse_test_output(self, output):
        """Parse test output to extract test counts"""
        lines = output.split('\n')
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        
        for line in lines:
            if 'Total Tests Run:' in line:
                try:
                    total_tests = int(line.split('Total Tests Run:')[1].strip())
                except:
                    pass
            elif 'Tests Passed:' in line:
                try:
                    passed_tests = int(line.split('Tests Passed:')[1].strip())
                except:
                    pass
            elif 'Tests Failed:' in line:
                try:
                    failed_tests = int(line.split('Tests Failed:')[1].strip())
                except:
                    pass
            elif 'TEST SUMMARY:' in line and '/' in line:
                try:
                    # Parse format like "TEST SUMMARY: 5/5 tests passed"
                    summary_part = line.split('TEST SUMMARY:')[1].strip()
                    if '/' in summary_part:
                        parts = summary_part.split('/')
                        passed_tests = int(parts[0].strip())
                        total_part = parts[1].split()[0]
                        total_tests = int(total_part)
                        failed_tests = total_tests - passed_tests
                except:
                    pass
        
        return {
            'total': total_tests,
            'passed': passed_tests,
            'failed': failed_tests,
            'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0
        }
    
    def run_individual_tests(self, section):
        """Run individual tests for a section"""
        test_path = f"tests/{section}/individual/run_all_individual_tests.py"
        
        if not os.path.exists(os.path.join(self.project_root, test_path)):
            return {
                'success': False,
                'message': f"Individual tests not found for {section}",
                'stats': {'total': 0, 'passed': 0, 'failed': 0, 'success_rate': 0}
            }
        
        command = f"{self.python_exe} {test_path}"
        result = self._run_command(command)
        
        stats = self._parse_test_output(result['stdout'])
        
        return {
            'success': result['success'],
            'message': result['stdout'] if result['success'] else result['stderr'],
            'stats': stats
        }
    
    def run_allure_tests(self, section):
        """Run allure tests for a section"""
        test_path = f"tests/{section}/test_{section}_allure.py"
        
        if not os.path.exists(os.path.join(self.project_root, test_path)):
            return {
                'success': False,
                'message': f"Allure tests not found for {section}",
                'stats': {'total': 0, 'passed': 0, 'failed': 0, 'success_rate': 0}
            }
        
        command = f"{self.python_exe} {test_path}"
        result = self._run_command(command)
        
        stats = self._parse_test_output(result['stdout'])
        
        return {
            'success': result['success'],
            'message': result['stdout'] if result['success'] else result['stderr'],
            'stats': stats
        }
    
    def run_section_tests(self, section, individual_only=False, allure_only=False):
        """Run all tests for a specific section"""
        print(f"\n{'='*80}")
        print(f"🧪 RUNNING {section.upper().replace('_', ' & ')} TESTS")
        print(f"{'='*80}")
        
        section_results = {
            'individual': None,
            'allure': None,
            'total_stats': {'total': 0, 'passed': 0, 'failed': 0, 'success_rate': 0}
        }
        
        # Run individual tests
        if not allure_only:
            print(f"\n🔍 Running {section} Individual Tests...")
            individual_result = self.run_individual_tests(section)
            section_results['individual'] = individual_result
            
            if individual_result['success']:
                print(f"✅ {section} Individual Tests: PASSED")
                print(f"📊 Stats: {individual_result['stats']['passed']}/{individual_result['stats']['total']} tests passed")
            else:
                print(f"❌ {section} Individual Tests: FAILED")
                print(f"📊 Stats: {individual_result['stats']['passed']}/{individual_result['stats']['total']} tests passed")
        
        # Run allure tests
        if not individual_only:
            print(f"\n🎯 Running {section} Allure Tests...")
            allure_result = self.run_allure_tests(section)
            section_results['allure'] = allure_result
            
            if allure_result['success']:
                print(f"✅ {section} Allure Tests: PASSED")
                print(f"📊 Stats: {allure_result['stats']['passed']}/{allure_result['stats']['total']} tests passed")
            else:
                print(f"❌ {section} Allure Tests: FAILED")
                print(f"📊 Stats: {allure_result['stats']['passed']}/{allure_result['stats']['total']} tests passed")
        
        # Calculate combined stats
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        
        if section_results['individual']:
            total_tests += section_results['individual']['stats']['total']
            passed_tests += section_results['individual']['stats']['passed']
            failed_tests += section_results['individual']['stats']['failed']
        
        if section_results['allure']:
            total_tests += section_results['allure']['stats']['total']
            passed_tests += section_results['allure']['stats']['passed']
            failed_tests += section_results['allure']['stats']['failed']
        
        section_results['total_stats'] = {
            'total': total_tests,
            'passed': passed_tests,
            'failed': failed_tests,
            'success_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0
        }
        
        print(f"\n📈 {section.upper()} SECTION SUMMARY:")
        print(f"   Total Tests: {total_tests}")
        print(f"   Passed: {passed_tests}")
        print(f"   Failed: {failed_tests}")
        print(f"   Success Rate: {section_results['total_stats']['success_rate']:.1f}%")
        
        return section_results
    
    def run_all_tests(self, individual_only=False, allure_only=False, specific_section=None):
        """Run all tests in the project"""
        self.results['start_time'] = datetime.now()
        
        print("🚀 DEMOQA SELENIUM AUTOMATION PROJECT - MASTER TEST RUNNER")
        print("=" * 80)
        print(f"⏰ Started at: {self.results['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🐍 Python executable: {self.python_exe}")
        print(f"📁 Project root: {self.project_root}")
        
        # Define test sections
        sections = ['elements', 'forms', 'alerts_frames', 'widgets', 'interactions', 'bookstore']
        
        if specific_section:
            if specific_section in sections:
                sections = [specific_section]
            else:
                print(f"❌ Invalid section: {specific_section}")
                print(f"Available sections: {', '.join(sections)}")
                return False
        
        # Run tests for each section
        for section in sections:
            try:
                section_result = self.run_section_tests(section, individual_only, allure_only)
                self.results['sections'][section] = section_result
                
                # Update overall stats
                stats = section_result['total_stats']
                self.results['summary']['total_tests'] += stats['total']
                self.results['summary']['passed_tests'] += stats['passed']
                self.results['summary']['failed_tests'] += stats['failed']
                
            except Exception as e:
                print(f"❌ Error running {section} tests: {e}")
                self.results['sections'][section] = {
                    'error': str(e),
                    'total_stats': {'total': 0, 'passed': 0, 'failed': 0, 'success_rate': 0}
                }
        
        # Calculate final results
        self.results['end_time'] = datetime.now()
        self.results['total_duration'] = (self.results['end_time'] - self.results['start_time']).total_seconds()
        
        if self.results['summary']['total_tests'] > 0:
            self.results['summary']['success_rate'] = (
                self.results['summary']['passed_tests'] / self.results['summary']['total_tests'] * 100
            )
        
        self._print_final_summary()
        return True
    
    def _print_final_summary(self):
        """Print the final test execution summary"""
        print("\n" + "=" * 80)
        print("🏁 FINAL TEST EXECUTION SUMMARY")
        print("=" * 80)
        
        print(f"⏰ Start Time: {self.results['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏰ End Time: {self.results['end_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Total Duration: {self.results['total_duration']:.1f} seconds")
        
        print(f"\n📊 OVERALL STATISTICS:")
        print(f"   Total Tests: {self.results['summary']['total_tests']}")
        print(f"   Passed: {self.results['summary']['passed_tests']}")
        print(f"   Failed: {self.results['summary']['failed_tests']}")
        print(f"   Success Rate: {self.results['summary']['success_rate']:.1f}%")
        
        print(f"\n📋 SECTION BREAKDOWN:")
        for section, result in self.results['sections'].items():
            if 'error' in result:
                print(f"   {section.upper()}: ERROR - {result['error']}")
            else:
                stats = result['total_stats']
                status = "✅ PASSED" if stats['failed'] == 0 and stats['total'] > 0 else "❌ FAILED"
                print(f"   {section.upper()}: {status} - {stats['passed']}/{stats['total']} ({stats['success_rate']:.1f}%)")
        
        # Overall result
        if self.results['summary']['failed_tests'] == 0 and self.results['summary']['total_tests'] > 0:
            print(f"\n🎉 ALL TESTS PASSED! 🎉")
        elif self.results['summary']['success_rate'] >= 90:
            print(f"\n✅ MOSTLY SUCCESSFUL - {self.results['summary']['success_rate']:.1f}% pass rate")
        else:
            print(f"\n⚠️  SOME TESTS FAILED - {self.results['summary']['success_rate']:.1f}% pass rate")
        
        # Save results to file
        self._save_results()
    
    def _save_results(self):
        """Save test results to JSON file"""
        try:
            results_file = os.path.join(self.project_root, 'reports', 'master_test_results.json')
            os.makedirs(os.path.dirname(results_file), exist_ok=True)
            
            # Convert datetime objects to strings for JSON serialization
            json_results = self.results.copy()
            json_results['start_time'] = self.results['start_time'].isoformat()
            json_results['end_time'] = self.results['end_time'].isoformat()
            
            with open(results_file, 'w') as f:
                json.dump(json_results, f, indent=2)
            
            print(f"\n💾 Results saved to: {results_file}")
            
        except Exception as e:
            print(f"⚠️  Could not save results: {e}")

def main():
    parser = argparse.ArgumentParser(description='Run all DemoQA Selenium tests')
    parser.add_argument('--browser', choices=['chrome', 'firefox', 'edge'], 
                       default='chrome', help='Browser to use')
    parser.add_argument('--headless', action='store_true', 
                       help='Run in headless mode')
    parser.add_argument('--individual-only', action='store_true',
                       help='Run only individual tests')
    parser.add_argument('--allure-only', action='store_true',
                       help='Run only allure tests')
    parser.add_argument('--section', choices=['elements', 'forms', 'alerts_frames', 'widgets', 'interactions', 'bookstore'],
                       help='Run specific section only')
    parser.add_argument('--verbose', action='store_true',
                       help='Verbose output')
    parser.add_argument('--generate-report', action='store_true',
                       help='Generate final HTML report')
    
    args = parser.parse_args()
    
    # Set environment variables for browser configuration
    if args.browser:
        os.environ['BROWSER'] = args.browser
    if args.headless:
        os.environ['HEADLESS'] = 'true'
    if args.verbose:
        os.environ['VERBOSE'] = 'true'
    
    # Create and run master test runner
    runner = MasterTestRunner()
    success = runner.run_all_tests(
        individual_only=args.individual_only,
        allure_only=args.allure_only,
        specific_section=args.section
    )
    
    if args.generate_report:
        print("\n📄 Generating HTML report...")
        # TODO: Implement HTML report generation
        print("HTML report generation not yet implemented")
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()