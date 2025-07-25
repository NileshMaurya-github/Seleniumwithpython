#!/usr/bin/env python3
"""
DemoQA Selenium Automation - Project Validation Script

This script validates the completeness and integrity of the entire project.
It checks for:
- All required test files
- Proper file structure
- Import statements
- Basic syntax validation
- Documentation completeness
"""

import os
import sys
import ast
import importlib.util
from pathlib import Path
from datetime import datetime


class ProjectValidator:
    """Validates the DemoQA Selenium automation project"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.validation_results = {
            'files_checked': 0,
            'files_passed': 0,
            'files_failed': 0,
            'errors': [],
            'warnings': [],
            'summary': {}
        }
        
    def validate_project(self):
        """Run complete project validation"""
        print("🔍 DemoQA Selenium Automation - Project Validation")
        print("=" * 60)
        
        # Validate project structure
        self.validate_structure()
        
        # Validate test files
        self.validate_test_files()
        
        # Validate documentation
        self.validate_documentation()
        
        # Validate configuration files
        self.validate_configuration()
        
        # Generate validation report
        self.generate_report()
        
        return self.validation_results
    
    def validate_structure(self):
        """Validate project directory structure"""
        print("\n📁 Validating Project Structure...")
        
        required_dirs = [
            'tests',
            'tests/elements',
            'tests/elements/individual',
            'tests/forms',
            'tests/forms/individual',
            'tests/alerts_frames',
            'tests/alerts_frames/individual',
            'tests/widgets',
            'tests/widgets/individual',
            'tests/interactions',
            'tests/interactions/individual',
            'tests/bookstore',
            'tests/bookstore/individual',
            'pages',
            'utils',
            'reports',
            'docs'
        ]
        
        structure_valid = True
        
        for dir_path in required_dirs:
            full_path = self.project_root / dir_path
            if full_path.exists():
                print(f"  ✅ {dir_path}")
            else:
                print(f"  ❌ {dir_path} - MISSING")
                self.validation_results['errors'].append(f"Missing directory: {dir_path}")
                structure_valid = False
        
        self.validation_results['summary']['structure'] = 'PASSED' if structure_valid else 'FAILED'
    
    def validate_test_files(self):
        """Validate all test files"""
        print("\n🧪 Validating Test Files...")
        
        # Define expected test files
        test_files = {
            'elements': {
                'individual': [
                    'test_text_box_individual.py',
                    'test_checkbox_individual.py',
                    'test_radio_button_individual.py',
                    'test_web_tables_individual.py',
                    'test_buttons_individual.py',
                    'test_links_individual.py',
                    'test_broken_links_individual.py',
                    'test_upload_download_individual.py',
                    'test_dynamic_properties_individual.py'
                ],
                'allure': 'test_elements_allure.py',
                'main': 'demoqa_elements.py',
                'runner': 'run_all_individual_tests.py'
            },
            'forms': {
                'individual': [
                    'test_practice_form_individual.py'
                ],
                'allure': 'test_forms_allure.py',
                'main': 'demoqa_forms.py',
                'runner': 'run_all_individual_tests.py'
            },
            'alerts_frames': {
                'individual': [
                    'test_alerts_individual.py',
                    'test_frames_individual.py',
                    'test_nested_frames_individual.py',
                    'test_modal_dialogs_individual.py',
                    'test_browser_windows_individual.py'
                ],
                'allure': 'test_alerts_frames_allure.py',
                'main': 'demoqa_alerts_frames.py',
                'runner': 'run_all_individual_tests.py'
            },
            'widgets': {
                'individual': [
                    'test_accordian_individual.py',
                    'test_auto_complete_individual.py',
                    'test_date_picker_individual.py',
                    'test_slider_individual.py',
                    'test_progress_bar_individual.py',
                    'test_tabs_individual.py',
                    'test_tool_tips_individual.py',
                    'test_menu_individual.py',
                    'test_select_menu_individual.py'
                ],
                'allure': 'test_widgets_allure.py',
                'main': 'demoqa_widgets.py',
                'runner': 'run_all_individual_tests.py'
            },
            'interactions': {
                'individual': [
                    'test_sortable_individual.py',
                    'test_selectable_individual.py',
                    'test_resizable_individual.py',
                    'test_droppable_individual.py',
                    'test_dragabble_individual.py'
                ],
                'allure': 'test_interactions_allure.py',
                'main': 'demoqa_interactions.py',
                'runner': 'run_all_individual_tests.py'
            },
            'bookstore': {
                'individual': [
                    'test_login_individual.py',
                    'test_register_individual.py',
                    'test_book_store_individual.py',
                    'test_profile_individual.py',
                    'test_book_detail_individual.py',
                    'test_api_individual.py',
                    'test_authentication_individual.py'
                ],
                'allure': 'test_bookstore_allure.py',
                'main': 'demoqa_bookstore.py',
                'runner': 'run_all_individual_tests.py'
            }
        }
        
        total_files = 0
        valid_files = 0
        
        for section, files in test_files.items():
            print(f"\n  📂 {section.upper()} Section:")
            
            # Check individual test files
            for individual_file in files['individual']:
                file_path = self.project_root / 'tests' / section / 'individual' / individual_file
                if self.validate_python_file(file_path):
                    print(f"    ✅ {individual_file}")
                    valid_files += 1
                else:
                    print(f"    ❌ {individual_file}")
                total_files += 1
            
            # Check allure test file
            allure_path = self.project_root / 'tests' / section / files['allure']
            if self.validate_python_file(allure_path):
                print(f"    ✅ {files['allure']}")
                valid_files += 1
            else:
                print(f"    ❌ {files['allure']}")
            total_files += 1
            
            # Check main test file
            main_path = self.project_root / 'tests' / section / files['main']
            if self.validate_python_file(main_path):
                print(f"    ✅ {files['main']}")
                valid_files += 1
            else:
                print(f"    ❌ {files['main']}")
            total_files += 1
            
            # Check runner file
            runner_path = self.project_root / 'tests' / section / 'individual' / files['runner']
            if self.validate_python_file(runner_path):
                print(f"    ✅ {files['runner']}")
                valid_files += 1
            else:
                print(f"    ❌ {files['runner']}")
            total_files += 1
        
        self.validation_results['files_checked'] = total_files
        self.validation_results['files_passed'] = valid_files
        self.validation_results['files_failed'] = total_files - valid_files
        self.validation_results['summary']['test_files'] = 'PASSED' if valid_files == total_files else 'FAILED'
    
    def validate_python_file(self, file_path):
        """Validate a Python file for syntax and basic structure"""
        if not file_path.exists():
            self.validation_results['errors'].append(f"File not found: {file_path}")
            return False
        
        try:
            # Check if file can be parsed as Python
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the AST to check syntax
            ast.parse(content)
            
            # Check for basic imports (selenium should be present in test files)
            if 'test_' in file_path.name and 'selenium' not in content:
                self.validation_results['warnings'].append(f"No selenium import found in {file_path.name}")
            
            return True
            
        except SyntaxError as e:
            self.validation_results['errors'].append(f"Syntax error in {file_path.name}: {e}")
            return False
        except Exception as e:
            self.validation_results['errors'].append(f"Error validating {file_path.name}: {e}")
            return False
    
    def validate_documentation(self):
        """Validate documentation files"""
        print("\n📚 Validating Documentation...")
        
        required_docs = [
            'README.md',
            'docs/comprehensive_test_execution_guide.md',
            'docs/troubleshooting_guide.md',
            'docs/cross_browser_testing_guide.md',
            'reports/final_project_report.md',
            'project_progress_summary.md'
        ]
        
        docs_valid = True
        
        for doc_file in required_docs:
            doc_path = self.project_root / doc_file
            if doc_path.exists():
                print(f"  ✅ {doc_file}")
            else:
                print(f"  ❌ {doc_file} - MISSING")
                self.validation_results['errors'].append(f"Missing documentation: {doc_file}")
                docs_valid = False
        
        self.validation_results['summary']['documentation'] = 'PASSED' if docs_valid else 'FAILED'
    
    def validate_configuration(self):
        """Validate configuration files"""
        print("\n⚙️ Validating Configuration Files...")
        
        config_files = [
            'requirements.txt',
            'setup.py',
            '.github/workflows/selenium-tests.yml'
        ]
        
        config_valid = True
        
        for config_file in config_files:
            config_path = self.project_root / config_file
            if config_path.exists():
                print(f"  ✅ {config_file}")
            else:
                print(f"  ❌ {config_file} - MISSING")
                self.validation_results['errors'].append(f"Missing configuration: {config_file}")
                config_valid = False
        
        self.validation_results['summary']['configuration'] = 'PASSED' if config_valid else 'FAILED'
    
    def generate_report(self):
        """Generate validation report"""
        print("\n" + "=" * 60)
        print("📊 VALIDATION SUMMARY")
        print("=" * 60)
        
        # Overall statistics
        print(f"Files Checked: {self.validation_results['files_checked']}")
        print(f"Files Passed: {self.validation_results['files_passed']}")
        print(f"Files Failed: {self.validation_results['files_failed']}")
        
        # Section results
        print("\nSection Results:")
        for section, status in self.validation_results['summary'].items():
            status_icon = "✅" if status == "PASSED" else "❌"
            print(f"  {status_icon} {section.replace('_', ' ').title()}: {status}")
        
        # Errors
        if self.validation_results['errors']:
            print(f"\n❌ ERRORS ({len(self.validation_results['errors'])}):")
            for error in self.validation_results['errors']:
                print(f"  - {error}")
        
        # Warnings
        if self.validation_results['warnings']:
            print(f"\n⚠️ WARNINGS ({len(self.validation_results['warnings'])}):")
            for warning in self.validation_results['warnings']:
                print(f"  - {warning}")
        
        # Overall result
        all_passed = all(status == "PASSED" for status in self.validation_results['summary'].values())
        overall_status = "PASSED" if all_passed and not self.validation_results['errors'] else "FAILED"
        
        print(f"\n🎯 OVERALL VALIDATION: {overall_status}")
        
        if overall_status == "PASSED":
            print("🎉 Project validation completed successfully!")
            print("✅ All components are present and properly structured.")
        else:
            print("⚠️ Project validation found issues that need attention.")
            print("❌ Please review the errors and warnings above.")
        
        # Save report to file
        self.save_validation_report(overall_status)
        
        return overall_status == "PASSED"
    
    def save_validation_report(self, overall_status):
        """Save validation report to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = self.project_root / 'reports' / f'validation_report_{timestamp}.txt'
        
        # Ensure reports directory exists
        report_file.parent.mkdir(exist_ok=True)
        
        with open(report_file, 'w') as f:
            f.write("DEMOQA SELENIUM AUTOMATION - PROJECT VALIDATION REPORT\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Validation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Overall Status: {overall_status}\n\n")
            
            f.write("STATISTICS:\n")
            f.write(f"Files Checked: {self.validation_results['files_checked']}\n")
            f.write(f"Files Passed: {self.validation_results['files_passed']}\n")
            f.write(f"Files Failed: {self.validation_results['files_failed']}\n\n")
            
            f.write("SECTION RESULTS:\n")
            for section, status in self.validation_results['summary'].items():
                f.write(f"- {section.replace('_', ' ').title()}: {status}\n")
            
            if self.validation_results['errors']:
                f.write(f"\nERRORS ({len(self.validation_results['errors'])}):\n")
                for error in self.validation_results['errors']:
                    f.write(f"- {error}\n")
            
            if self.validation_results['warnings']:
                f.write(f"\nWARNINGS ({len(self.validation_results['warnings'])}):\n")
                for warning in self.validation_results['warnings']:
                    f.write(f"- {warning}\n")
        
        print(f"\n📄 Validation report saved: {report_file}")


def main():
    """Main function to run project validation"""
    validator = ProjectValidator()
    success = validator.validate_project()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()