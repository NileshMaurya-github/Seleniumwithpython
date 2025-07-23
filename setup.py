#!/usr/bin/env python3
"""
Setup script for DemoQA Selenium Test Suite
"""

import os
import subprocess
import sys


def run_command(command):
    """Run a command and return success status"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {command}")
        print(f"Error: {e.stderr}")
        return False


def main():
    """Main setup function"""
    print("🚀 Setting up DemoQA Selenium Test Suite")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Install requirements
    print("\n📦 Installing Python dependencies...")
    if not run_command("pip install -r requirements.txt"):
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create necessary directories
    print("\n📁 Creating directories...")
    directories = [
        "reports",
        "reports/screenshots",
        "reports/allure-results",
        "downloads"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created {directory}/")
    
    # Check Chrome installation
    print("\n🌐 Checking browser installations...")
    chrome_check = run_command("google-chrome --version")
    if not chrome_check:
        print("⚠️  Chrome not found. Please install Google Chrome")
        print("   Download from: https://www.google.com/chrome/")
    
    print("\n✅ Setup completed successfully!")
    print("\n🎯 Quick Start:")
    print("   Run all tests: python run_all_tests.py")
    print("   Run specific section: python run_all_tests.py --sections elements")
    print("   Run individual test: python tests/elements/demoqa_elements.py")


if __name__ == "__main__":
    main()