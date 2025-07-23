#!/usr/bin/env python3
"""
Allure Test Runner for DemoQA Elements
=====================================
"""

import os
import subprocess
import sys
import time
from pathlib import Path


class AllureTestRunner:
    """Runner for executing tests and generating Allure reports"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.reports_dir = self.project_root / "reports"
        self.allure_results_dir = self.reports_dir / "allure-results"
        self.allure_report_dir = self.reports_dir / "allure-report"
        
    def setup_directories(self):
        """Create necessary directories"""
        print("🔧 Setting up directories...")
        self.reports_dir.mkdir(exist_ok=True)
        self.allure_results_dir.mkdir(exist_ok=True)
        self.allure_report_dir.mkdir(exist_ok=True)
        print("✅ Directories created")
    
    def clean_previous_results(self):
        """Clean previous test results"""
        print("🧹 Cleaning previous results...")
        if self.allure_results_dir.exists():
            import shutil
            shutil.rmtree(self.allure_results_dir)
            self.allure_results_dir.mkdir()
        print("✅ Previous results cleaned")
    
    def run_pytest_with_allure(self):
        """Run pytest with Allure reporting"""
        print("🚀 Running Elements tests with Allure reporting...")
        
        cmd = [
            sys.executable, "-m", "pytest",
            "tests/elements/test_elements_allure.py",
            "--alluredir=reports/allure-results",
            "--clean-alluredir",
            "-v",
            "--tb=short"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            print("📊 Test execution completed")
            print(f"Return code: {result.returncode}")
            
            if result.stdout:
                print("STDOUT:")
                print(result.stdout)
            
            if result.stderr:
                print("STDERR:")
                print(result.stderr)
                
            return result.returncode == 0
            
        except Exception as e:
            print(f"❌ Error running pytest: {e}")
            return False
    
    def generate_allure_report(self):
        """Generate Allure HTML report"""
        print("📈 Generating Allure HTML report...")
        
        try:
            # Check if allure command is available
            allure_check = subprocess.run(["allure", "--version"], capture_output=True, text=True)
            if allure_check.returncode != 0:
                print("❌ Allure command not found. Please install Allure CLI.")
                print("   Download from: https://github.com/allure-framework/allure2/releases")
                return False
            
            # Generate report
            cmd = [
                "allure", "generate", 
                str(self.allure_results_dir),
                "--output", str(self.allure_report_dir),
                "--clean"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode == 0:
                print("✅ Allure report generated successfully")
                print(f"📁 Report location: {self.allure_report_dir}")
                return True
            else:
                print(f"❌ Error generating Allure report: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error generating Allure report: {e}")
            return False
    
    def open_allure_report(self):
        """Open Allure report in browser"""
        print("🌐 Opening Allure report in browser...")
        
        try:
            cmd = ["allure", "open", str(self.allure_report_dir)]
            subprocess.Popen(cmd, cwd=self.project_root)
            print("✅ Allure report opened in browser")
            return True
        except Exception as e:
            print(f"❌ Error opening Allure report: {e}")
            print(f"📁 You can manually open: {self.allure_report_dir / 'index.html'}")
            return False
    
    def create_test_summary(self):
        """Create a test execution summary"""
        print("📋 Creating test summary...")
        
        summary_file = self.reports_dir / "test_summary.txt"
        
        with open(summary_file, "w") as f:
            f.write("DemoQA Elements - Allure Test Report Summary\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Execution Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Test Suite: Elements Section\n")
            f.write(f"Framework: Selenium WebDriver with Pytest\n")
            f.write(f"Reporting: Allure Framework\n\n")
            
            f.write("Test Coverage:\n")
            f.write("- Text Box (Form Input)\n")
            f.write("- Check Box (Multi-selection)\n")
            f.write("- Radio Button (Single Selection)\n")
            f.write("- Web Tables (CRUD Operations)\n")
            f.write("- Buttons (Click Interactions)\n")
            f.write("- Links (Navigation & API)\n")
            f.write("- Broken Links (Validation)\n")
            f.write("- Upload Download (File Operations)\n")
            f.write("- Dynamic Properties (Timing)\n\n")
            
            f.write("Report Locations:\n")
            f.write(f"- Allure Results: {self.allure_results_dir}\n")
            f.write(f"- Allure Report: {self.allure_report_dir}\n")
            f.write(f"- HTML Report: {self.allure_report_dir / 'index.html'}\n\n")
            
            f.write("Features:\n")
            f.write("- Detailed step-by-step execution\n")
            f.write("- Screenshots on failure\n")
            f.write("- Test data attachments\n")
            f.write("- Timing information\n")
            f.write("- Categorized by Epic/Feature/Story\n")
            f.write("- Severity levels\n")
            f.write("- Test markers (smoke/regression)\n")
        
        print(f"✅ Test summary created: {summary_file}")
    
    def run_complete_suite(self):
        """Run complete test suite with Allure reporting"""
        print("🎯 Starting DemoQA Elements Allure Test Suite")
        print("=" * 60)
        
        start_time = time.time()
        
        # Setup
        self.setup_directories()
        self.clean_previous_results()
        
        # Run tests
        test_success = self.run_pytest_with_allure()
        
        # Generate report
        if test_success:
            report_success = self.generate_allure_report()
            
            if report_success:
                self.create_test_summary()
                
                # Ask user if they want to open the report
                try:
                    response = input("\n🌐 Open Allure report in browser? (y/n): ").lower().strip()
                    if response in ['y', 'yes']:
                        self.open_allure_report()
                except KeyboardInterrupt:
                    print("\n⏹️ User cancelled")
            
        else:
            print("⚠️ Tests failed, but generating report anyway...")
            self.generate_allure_report()
            self.create_test_summary()
        
        end_time = time.time()
        duration = end_time - start_time
        
        print("\n" + "=" * 60)
        print("📊 ALLURE TEST SUITE SUMMARY")
        print("=" * 60)
        print(f"⏱️ Total execution time: {duration:.2f} seconds")
        print(f"📁 Report location: {self.allure_report_dir}")
        print(f"🌐 Open report: {self.allure_report_dir / 'index.html'}")
        
        if test_success:
            print("✅ Test suite completed successfully!")
        else:
            print("⚠️ Some tests may have failed - check the report")
        
        return test_success


def main():
    """Main function"""
    runner = AllureTestRunner()
    success = runner.run_complete_suite()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()