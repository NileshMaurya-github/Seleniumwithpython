@echo off
echo ========================================
echo DemoQA Elements - Allure Test Runner
echo ========================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found in PATH
    echo Please install Python or add it to PATH
    pause
    exit /b 1
)

REM Run the Allure test suite
echo Running Allure test suite...
python run_allure_tests.py

REM Keep window open
echo.
echo Press any key to exit...
pause >nul