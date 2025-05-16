<h1 align="center"><strong>ASCEND-MOBILE-TESTING</strong></h1>

<p align="center"><em>Elevate Your Mobile Testing Experience Effortlessly</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/last%20commit-may-blue.svg" />
  <img src="https://img.shields.io/badge/python-100%25-blue.svg" />
  <img src="https://img.shields.io/badge/languages-1-brightgreen.svg" />
</p>

---

<p align="center"><em>Built with the tools and technologies:</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/-JSON-black?logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/-Appium-purple?logo=appium&logoColor=white" />
  <img src="https://img.shields.io/badge/-Selenium-43B02A?logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/-Pytest-yellow?logo=pytest&logoColor=black" />
</p>



## Project Overview

This project ensures the quality and reliability of the Ascend app through comprehensive and scalable test automation.

### Features:

* Automated tests for 11 key modules of the app
* Modular page-object model for maintainability
* Requirement Traceability Matrix for full coverage mapping
* Stress testing
* Auto-generated bug documentation and test reports

---

## Project Structure

```
APK/
│
├── Admin_panel/                  # Page object for Admin Panel
├── Authentication/              # Authentication module
├── Company/                     # Company-related features
├── Connections/                 # User connections
├── Feed/                        # App's feed/timeline
├── Jobs/                        # Job listings module
├── Messaging/                   # Messaging functionality
├── Navigation/                  # Navigation handling
├── Notifications/               # In-app notifications
├── Payment_to_premium/          # Premium payment flow
├── Privacy_and_security/        # Privacy and settings
├── Profile/                     # User profile
│
├── base_page.py                 # Base class for page objects
├── reports/                     # Test execution reports
├── screenshots/                 # Screenshots from test runs
├── Test_Cases_Data/            # Test data files
├── Documentation/              # Supporting documentation (see below)
│
├── Tests/                       # Test cases
│   ├── test_admin_panel.py
│   ├── test_authentication.py
│   ├── test_company.py
│   ├── test_connections.py
│   ├── test_feed.py
│   ├── test_jobs.py
│   ├── test_messaging.py
│   ├── test_notifications.py
│   ├── test_premium_plan_page.py
│   ├── test_privacy_and_security.py
│   ├── test_profile.py
│   └── conftest.py              # Fixtures and hooks
│
├── config.json                  # Configuration settings
├── logger.py                    # Custom logging utility
├── utility.py                  
```

---

## Testing Highlights

* **Modules Tested**: Authentication, Feed, Jobs, Messaging, Notifications, Privacy, Profile, etc.
* **Modules Not Tested on LinkedIn**: Admin Panel, Payment, Company, Settings (due to platform constraints).
* **Modules Tested on Ascend**: 6 out of 11 functional modules.
* **Stress Testing**: Conducted collaboratively with the web QA team.
* **Bug Reporting**: All Ascend bugs documented and categorized.

---

## Getting Started

### Prerequisites

* Python 3.8+
* Appium or relevant mobile automation tool
* Dependencies (add `requirements.txt` if available)

### Running Tests

```bash
pytest Tests/
```

Use appropriate flags for reporting or device targeting as needed.

---

## Documentation

All related documents are located in the `Documentation/` folder:

* `RequirementTraceabilityMatrix.xlsx` – Links each test case to project requirements.
* `Stress_Test_Report.pdf` – Describes stress testing procedures, tools, and findings.
* `Bug_Report_Document.docx` – Logs all bugs found in the Ascend mobile app during testing.

---


