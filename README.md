Thanglish to Tamil Translation Testing Project
Project Overview

This project automates the testing of a Thanglish (Tamil written in English) to Tamil transliteration converter using the Changathi Tamil Converter. The project uses Playwright for browser automation and pytest for test execution.

The goal is to validate the accuracy and reliability of the transliteration system across various linguistic scenarios, including positive functional tests, negative functional tests, and UI behavior tests.

Test Case Summary
Total Test Cases: 35
Category	Count	Description
Positive Functional	24	Valid Thanglish inputs that should convert correctly to Tamil
Negative Functional	10	Edge cases and invalid inputs that test system limitations
UI Tests	1	Real-time output update verification
Test Case Categories
Positive Functional Tests (24 cases)

These test cases verify that the converter correctly transliterates valid Thanglish input to Tamil:

Basic Greetings & Statements: vanakkam!, naan veetukku pogiren.
Tense Variations: Past, present, future tense sentences
Sentence Structures: Simple, compound, and complex sentences
Politeness Levels: Formal requests, informal phrasing, polite greetings
Pronoun Variations: Singular and plural forms
Word Emphasis: Repeated words for emphasis
Question Forms: Interrogative sentences
Negative Functional Tests (10 cases)

These test cases verify that the converter handles edge cases and limitations:

English Words Preservation: Common English words like school, office, WhatsApp
Place Names: Geographic locations like Chennai
Technical Terms: Abbreviations like OTP, PC, RAM
Numbers & Units: Numeric values and measurement units (5 kg, 2 km)
Currency Formats: Rs. 1500
Date Formats: 25/12/2025
Time Formats: 7.30 AM
Long Words: Words without spaces to test word segmentation
UI Tests (1 case)
Real-time Output Update: Verifies that the Tamil output appears instantly as the user types
Project Structure
playwright_project/
├── test_thanglish_tamil.py    # Main test script with all 35 test cases
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This file

Installation & Setup
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Step 1: Create a Virtual Environment
python -m venv venv

Step 2: Activate Virtual Environment

On Windows:

venv\Scripts\activate


On macOS/Linux:

source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Install Playwright Browsers
playwright install

Running the Tests
Run All Tests
pytest test_thanglish_tamil.py -v

Run Tests with Detailed Output
pytest test_thanglish_tamil.py -v -s

Run Specific Test Category
# Run only positive functional tests
pytest test_thanglish_tamil.py -k "Pos_Fun" -v

# Run only negative functional tests
pytest test_thanglish_tamil.py -k "Neg_Fun" -v

# Run only UI tests
pytest test_thanglish_tamil.py -k "UI" -v

Run with HTML Report
pytest test_thanglish_tamil.py -v --html=report.html

Test Execution Details
How the Tests Work
Browser Launch: Playwright opens Chromium browser
Navigation: Navigates to https://tamil.changathi.com/
Input Entry: Types Thanglish text into the textarea with a 50ms delay between characters
Wait for Conversion: Waits 1 second for real-time conversion to complete
Output Capture: Retrieves the Tamil output from the textarea
Assertion: Compares actual output with expected output
Result Recording: Prints test results for Excel documentation
Test Execution Flow
For each test case:
  1. Clear textarea
  2. Type Thanglish input (with delay)
  3. Wait for conversion (1 second)
  4. Get actual Tamil output
  5. Compare with expected output
  6. Print results (ID, Input, Expected, Actual, Type)
  7. Assert Pass/Fail

Test Results
Summary
Total Tests: 35
Passed: 27
Failed: 8 (Expected - these are negative functional tests)
Errors: 0
Key Findings
Positive Functional Tests (24 cases)
Passed: 19 cases
Failed: 5 cases (due to converter limitations or minor output differences)
Negative Functional Tests (10 cases)
Passed: 8 cases (correctly identified system limitations)
Failed: 2 cases (converter handled edge cases better than expected)
UI Tests (1 case)
Passed: 1 case (real-time output update works correctly)
Converter Behavior Observations
Strengths

✅ Accurate transliteration of pure Tamil words
✅ Correct handling of tense variations
✅ Proper word spacing in most cases
✅ Real-time conversion as user types
✅ Handles punctuation correctly

Limitations

❌ Inconsistent handling of English words (sometimes transliterates, sometimes preserves)
❌ Minor spacing issues in compound words
❌ Formal vs informal pronoun variations not always accurate
❌ Some technical abbreviations not preserved

Dependencies
Python Packages
pytest: Test framework
pytest-playwright: Playwright plugin for pytest
playwright: Browser automation library
System Requirements
Chromium browser (installed via playwright install)
100MB+ disk space for browser binaries
Configuration Files
pytest.ini
[pytest]
addopts = --tb=short
testpaths = .
python_files = test_*.py
python_classes = Test*
python_functions = test_*

requirements.txt
pytest==9.0.2
pytest-playwright==0.7.2
playwright==1.48.0

Troubleshooting
Issue: Tests timeout or fail to load page

Solution: Increase the wait time in the script:

time.sleep(2)  # Increase from 1 to 2 seconds

Issue: Playwright browsers not found

Solution: Reinstall browsers:

playwright install

Issue: Permission denied on macOS/Linux

Solution: Make the script executable:

chmod +x test_thanglish_tamil.py

Issue: Tests run very slowly

Solution: Run tests in parallel (requires pytest-xdist):

pip install pytest-xdist
pytest test_thanglish_tamil.py -n auto

Test Case Examples
Positive Functional Test Example
ID: Pos_Fun_0001
Name: Convert a short daily greeting
Input: vanakkam!
Expected: வணக்கம்!
Type: positive
Status: PASS

Negative Functional Test Example
ID: Neg_Fun_0001
Name: Common English word should remain unchanged (school)
Input: pasanga school-ku ponaanga.
Expected: பசங்க school-க்கு போனாங்க.
Type: negative
Status: FAIL (converter transliterated "school" to "ஸ்கூல்")

UI Test Example
ID: Pos_UI_0001
Name: Real-time output update
Input: naan varuven
Expected: நான் வருவேன்
Type: ui
Status: PASS (output appeared instantly)

Excel Results Template

The test results are documented in an Excel file with the following columns:

Column	Description
TC ID	Unique test case identifier
Test Case Name	Descriptive name of the test
Input Length Type	Short/Medium/Long
Input (Thanglish)	The Thanglish input text
Expected Output (Tamil)	What the converter should produce
Actual Output	What the converter actually produced
Status	PASS or FAIL
What is covered by the test	4 bullet points describing test coverage
Accuracy justification/Description of issue type	Explanation of pass/fail reason
Author & Submission

Registration Number: IT23229266
Assignment: Option 2 - Thanglish to Tamil Translation Testing

References
Changathi Tamil Converter
Playwright Documentation
pytest Documentation
Tamil Language Guide

Last Updated: January 31, 2026