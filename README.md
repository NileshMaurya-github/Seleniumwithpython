# DemoQA Selenium Automation Project

A comprehensive Selenium automation framework for testing DemoQA website (https://demoqa.com) using Python, following real-world standards and best practices.

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd Selenium

# 2. Setup the project
python setup.py

# 3. Run all tests
python run_all_tests.py

# 4. Run specific section
python run_all_tests.py --sections elements forms
```

## 📁 Project Structure

```
Selenium/
├── tests/                     # Test cases organized by DemoQA sections
│   ├── elements/             # Elements section (Text Box, Buttons, etc.)
│   ├── forms/                # Forms section (Practice Form)
│   ├── alerts_frames/        # Alerts, Frame & Windows
│   ├── widgets/              # Widgets (Date Picker, Slider, etc.)
│   ├── interactions/         # Interactions (Drag & Drop, Sortable)
│   └── bookstore/            # Book Store Application
├── pages/                    # Page Object Model classes
├── utils/                    # Utility functions and helpers
├── config/                   # Configuration files
├── reports/                  # Test reports and screenshots
├── .github/workflows/        # CI/CD pipeline
├── run_all_tests.py         # Main test runner
├── setup.py                 # Project setup script
└── requirements.txt         # Python dependencies
```

## 🧪 Test Sections Coverage

### 1. Elements (9 Tests)
- ✅ Text Box - Form filling and validation
- ✅ Check Box - Multi-selection and tree navigation
- ✅ Radio Button - Single selection validation
- ✅ Web Tables - CRUD operations and search
- ✅ Buttons - Click, Double-click, Right-click
- ✅ Links - Navigation and API response testing
- ✅ Broken Links - Image and link validation
- ✅ Upload and Download - File operations
- ✅ Dynamic Properties - Element state changes

### 2. Forms (2 Tests)
- ✅ Practice Form - Complete form submission
- ✅ Form Validation - Error handling and validation

### 3. Alerts, Frame & Windows (5 Tests)
- ✅ Browser Windows - New tab/window handling
- ✅ Alerts - Simple, Timer, Confirm, Prompt alerts
- ✅ Frames - iframe switching and content verification
- ✅ Nested Frames - Parent-child frame navigation
- ✅ Modal Dialogs - Modal open/close operations

### 4. Widgets (9 Tests)
- ✅ Accordian - Expand/collapse functionality
- ✅ Auto Complete - Single and multiple selection
- ✅ Date Picker - Date and time selection
- ✅ Slider - Range input manipulation
- ✅ Progress Bar - Dynamic progress tracking
- ✅ Tabs - Tab switching and content verification
- ✅ Tool Tips - Hover interactions
- ✅ Menu - Dropdown and nested menu navigation
- ✅ Select Menu - Various dropdown types

### 5. Interactions (5 Tests)
- ✅ Sortable - List and grid item reordering
- ✅ Selectable - Single and multiple item selection
- ✅ Resizable - Element resize operations
- ✅ Droppable - Drag and drop with various scenarios
- ✅ Dragabble - Element dragging with constraints

### 6. Book Store Application (7 Tests)
- ✅ User Registration - Account creation flow
- ✅ Login - Authentication testing
- ✅ Book Store - Book browsing and search
- ✅ Pagination - Table navigation controls
- ✅ Profile Page - User profile management
- ✅ API Demo - Swagger documentation testing
- ✅ Book Details - Individual book information

## 🛠️ Features

- **Simple Structure** - Easy to understand and maintain
- **Real-world Standards** - Following industry best practices
- **Comprehensive Coverage** - All DemoQA sections included
- **CI/CD Ready** - GitHub Actions workflow included
- **Cross-browser Support** - Chrome and Firefox testing
- **Screenshot Capture** - Automatic failure screenshots
- **Detailed Reporting** - Console output with emojis and status
- **Modular Design** - Each section can be run independently

## 🏃‍♂️ Running Tests

### Run All Tests
```bash
python run_all_tests.py
```

### Run Specific Sections
```bash
# Single section
python run_all_tests.py --sections elements

# Multiple sections
python run_all_tests.py --sections elements forms widgets
```

### Run Individual Test Files
```bash
# Elements tests
python tests/elements/demoqa_elements.py

# Forms tests
python tests/forms/demoqa_forms.py

# Alerts & Frames tests
python tests/alerts_frames/demoqa_alerts_frames.py

# Widgets tests
python tests/widgets/demoqa_widgets.py

# Interactions tests
python tests/interactions/demoqa_interactions.py

# Book Store tests
python tests/bookstore/demoqa_bookstore.py
```

## 🔧 Configuration

The framework uses simple configuration:
- **Browser**: Chrome (default)
- **Headless**: Configurable via environment variable
- **Timeouts**: 10 seconds implicit wait
- **Screenshots**: Saved to `reports/screenshots/`

## 📊 CI/CD Pipeline

The project includes a complete GitHub Actions workflow:

```yaml
# Triggers
- Push to main/develop branches
- Pull requests
- Daily scheduled runs (2 AM UTC)
- Manual workflow dispatch

# Matrix Testing
- Browsers: Chrome, Firefox
- Python versions: 3.9, 3.10, 3.11

# Features
- Automatic dependency installation
- Cross-browser testing
- Test result artifacts
- Screenshot capture on failures
- Allure report generation
```

## 📈 Test Execution Flow

1. **Setup** → Initialize WebDriver and navigate to DemoQA
2. **Test Execution** → Run section-specific tests
3. **Verification** → Assert expected behaviors
4. **Cleanup** → Close browser and generate reports
5. **Reporting** → Console output with pass/fail status

## 🎯 Best Practices Implemented

- **Page Object Model** - Separation of test logic and page elements
- **Explicit Waits** - Reliable element interactions
- **Error Handling** - Graceful failure management
- **Modular Structure** - Easy maintenance and extension
- **Clear Naming** - Self-documenting code
- **Comprehensive Logging** - Detailed execution information

## 🚨 Important Notes

- Some tests require manual reCAPTCHA verification (Book Store registration/login)
- Tests are designed to run independently
- Screenshots are captured automatically on failures
- All tests include proper cleanup and browser closure

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your tests following the existing pattern
4. Ensure all tests pass
5. Submit a pull request

## 📝 License

This project is for educational and testing purposes.