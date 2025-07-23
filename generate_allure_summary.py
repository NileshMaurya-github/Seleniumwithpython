#!/usr/bin/env python3
"""
Generate Allure Test Summary Report
==================================
"""

import json
import os
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET


class AllureSummaryGenerator:
    """Generate HTML summary from Allure results"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.allure_results_dir = self.project_root / "reports" / "allure-results"
        self.reports_dir = self.project_root / "reports"
        
    def parse_allure_results(self):
        """Parse Allure JSON results"""
        results = {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'broken': 0,
            'skipped': 0,
            'tests': []
        }
        
        if not self.allure_results_dir.exists():
            return results
            
        # Parse test result files
        for file_path in self.allure_results_dir.glob("*-result.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    test_data = json.load(f)
                    
                results['total'] += 1
                status = test_data.get('status', 'unknown')
                
                if status == 'passed':
                    results['passed'] += 1
                elif status == 'failed':
                    results['failed'] += 1
                elif status == 'broken':
                    results['broken'] += 1
                elif status == 'skipped':
                    results['skipped'] += 1
                
                # Extract test info
                test_info = {
                    'name': test_data.get('name', 'Unknown'),
                    'status': status,
                    'duration': test_data.get('stop', 0) - test_data.get('start', 0),
                    'description': test_data.get('description', ''),
                    'steps': len(test_data.get('steps', [])),
                    'attachments': len(test_data.get('attachments', [])),
                    'labels': {label['name']: label['value'] for label in test_data.get('labels', [])},
                    'statusDetails': test_data.get('statusDetails', {})
                }
                
                results['tests'].append(test_info)
                
            except Exception as e:
                print(f"Error parsing {file_path}: {e}")
                
        return results
    
    def generate_html_report(self, results):
        """Generate HTML report"""
        
        # Calculate success rate
        success_rate = (results['passed'] / results['total'] * 100) if results['total'] > 0 else 0
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DemoQA Elements - Allure Test Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .stat-label {{
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .passed {{ color: #28a745; }}
        .failed {{ color: #dc3545; }}
        .broken {{ color: #fd7e14; }}
        .skipped {{ color: #6c757d; }}
        .success-rate {{
            background: linear-gradient(135deg, #28a745, #20c997);
            color: white;
        }}
        .tests-section {{
            padding: 30px;
        }}
        .section-title {{
            font-size: 1.8em;
            margin-bottom: 20px;
            color: #333;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }}
        .test-item {{
            background: #f8f9fa;
            margin-bottom: 15px;
            border-radius: 8px;
            overflow: hidden;
            border-left: 4px solid #ddd;
        }}
        .test-item.passed {{
            border-left-color: #28a745;
        }}
        .test-item.failed {{
            border-left-color: #dc3545;
        }}
        .test-item.broken {{
            border-left-color: #fd7e14;
        }}
        .test-header {{
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .test-name {{
            font-weight: bold;
            color: #333;
        }}
        .test-status {{
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .test-status.passed {{
            background: #d4edda;
            color: #155724;
        }}
        .test-status.failed {{
            background: #f8d7da;
            color: #721c24;
        }}
        .test-status.broken {{
            background: #ffeaa7;
            color: #856404;
        }}
        .test-details {{
            padding: 0 20px 15px 20px;
            color: #666;
            font-size: 0.9em;
        }}
        .test-meta {{
            display: flex;
            gap: 20px;
            margin-top: 10px;
        }}
        .meta-item {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        .progress-bar {{
            width: 100%;
            height: 20px;
            background: #e9ecef;
            border-radius: 10px;
            overflow: hidden;
            margin: 20px 0;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #28a745, #20c997);
            transition: width 0.3s ease;
        }}
        .footer {{
            background: #343a40;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .emoji {{
            font-size: 1.2em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧪 DemoQA Elements Test Report</h1>
            <p>Allure Test Results Summary - Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card success-rate">
                <div class="stat-number">{success_rate:.1f}%</div>
                <div class="stat-label">Success Rate</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{results['total']}</div>
                <div class="stat-label">Total Tests</div>
            </div>
            <div class="stat-card">
                <div class="stat-number passed">{results['passed']}</div>
                <div class="stat-label">Passed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number failed">{results['failed']}</div>
                <div class="stat-label">Failed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number broken">{results['broken']}</div>
                <div class="stat-label">Broken</div>
            </div>
            <div class="stat-card">
                <div class="stat-number skipped">{results['skipped']}</div>
                <div class="stat-label">Skipped</div>
            </div>
        </div>
        
        <div class="progress-bar">
            <div class="progress-fill" style="width: {success_rate}%"></div>
        </div>
        
        <div class="tests-section">
            <h2 class="section-title">📋 Test Results Details</h2>
"""
        
        # Add individual test results
        for test in results['tests']:
            duration_ms = test['duration'] / 1000000  # Convert nanoseconds to milliseconds
            duration_str = f"{duration_ms:.0f}ms" if duration_ms < 1000 else f"{duration_ms/1000:.1f}s"
            
            status_class = test['status']
            status_emoji = {
                'passed': '✅',
                'failed': '❌', 
                'broken': '🔧',
                'skipped': '⏭️'
            }.get(test['status'], '❓')
            
            html_content += f"""
            <div class="test-item {status_class}">
                <div class="test-header">
                    <div class="test-name">{status_emoji} {test['name']}</div>
                    <div class="test-status {status_class}">{test['status']}</div>
                </div>
                <div class="test-details">
                    <div>{test['description']}</div>
                    <div class="test-meta">
                        <div class="meta-item">
                            <span class="emoji">⏱️</span>
                            <span>Duration: {duration_str}</span>
                        </div>
                        <div class="meta-item">
                            <span class="emoji">📝</span>
                            <span>Steps: {test['steps']}</span>
                        </div>
                        <div class="meta-item">
                            <span class="emoji">📎</span>
                            <span>Attachments: {test['attachments']}</span>
                        </div>
                    </div>
"""
            
            # Add error details for failed tests
            if test['status'] in ['failed', 'broken'] and test['statusDetails']:
                error_msg = test['statusDetails'].get('message', 'No error message')
                html_content += f"""
                    <div style="margin-top: 10px; padding: 10px; background: #fff3cd; border-radius: 4px; border-left: 3px solid #ffc107;">
                        <strong>Error:</strong> {error_msg[:200]}{'...' if len(error_msg) > 200 else ''}
                    </div>
"""
            
            html_content += """
                </div>
            </div>
"""
        
        html_content += f"""
        </div>
        
        <div class="footer">
            <p>🚀 Generated by DemoQA Selenium Automation Framework</p>
            <p>Framework: Selenium WebDriver + Pytest + Allure | Browser: Chrome | Platform: Windows</p>
        </div>
    </div>
</body>
</html>
"""
        
        return html_content
    
    def generate_summary_report(self):
        """Generate complete summary report"""
        print("📊 Generating Allure Summary Report...")
        
        # Parse results
        results = self.parse_allure_results()
        
        if results['total'] == 0:
            print("⚠️ No Allure results found. Please run tests first.")
            return False
        
        # Generate HTML report
        html_content = self.generate_html_report(results)
        
        # Save HTML report
        report_file = self.reports_dir / "allure_summary_report.html"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Generate text summary
        self.generate_text_summary(results)
        
        print(f"✅ Allure summary report generated: {report_file}")
        print(f"🌐 Open in browser: file://{report_file.absolute()}")
        
        return True
    
    def generate_text_summary(self, results):
        """Generate text summary"""
        summary_file = self.reports_dir / "allure_test_summary.txt"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("DemoQA Elements - Allure Test Summary\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Framework: Selenium WebDriver + Pytest + Allure\n\n")
            
            f.write("📊 OVERALL RESULTS\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total Tests: {results['total']}\n")
            f.write(f"Passed: {results['passed']} ✅\n")
            f.write(f"Failed: {results['failed']} ❌\n")
            f.write(f"Broken: {results['broken']} 🔧\n")
            f.write(f"Skipped: {results['skipped']} ⏭️\n")
            
            success_rate = (results['passed'] / results['total'] * 100) if results['total'] > 0 else 0
            f.write(f"Success Rate: {success_rate:.1f}%\n\n")
            
            f.write("📋 TEST DETAILS\n")
            f.write("-" * 20 + "\n")
            
            for test in results['tests']:
                status_emoji = {
                    'passed': '✅',
                    'failed': '❌',
                    'broken': '🔧', 
                    'skipped': '⏭️'
                }.get(test['status'], '❓')
                
                duration_ms = test['duration'] / 1000000
                duration_str = f"{duration_ms:.0f}ms" if duration_ms < 1000 else f"{duration_ms/1000:.1f}s"
                
                f.write(f"{status_emoji} {test['name']}\n")
                f.write(f"   Status: {test['status'].upper()}\n")
                f.write(f"   Duration: {duration_str}\n")
                f.write(f"   Steps: {test['steps']}, Attachments: {test['attachments']}\n")
                
                if test['description']:
                    f.write(f"   Description: {test['description']}\n")
                
                if test['status'] in ['failed', 'broken'] and test['statusDetails']:
                    error_msg = test['statusDetails'].get('message', 'No error message')
                    f.write(f"   Error: {error_msg[:100]}{'...' if len(error_msg) > 100 else ''}\n")
                
                f.write("\n")
        
        print(f"✅ Text summary generated: {summary_file}")


def main():
    """Main function"""
    generator = AllureSummaryGenerator()
    success = generator.generate_summary_report()
    
    if success:
        print("\n🎉 Allure summary report generation completed!")
    else:
        print("\n❌ Failed to generate Allure summary report")


if __name__ == "__main__":
    main()