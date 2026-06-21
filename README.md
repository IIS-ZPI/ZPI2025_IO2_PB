# Currency Exchange Rate Analysis Project

## Project Implementation Technology

The project was developed using **Python** and is designed to analyze currency exchange rates obtained from the National Bank of Poland (NBP) API. The application performs statistical calculations, session trend analysis, histogram generation, and exports analysis results to CSV files.

### Technologies and Libraries

- **Python 3.14** – main programming language.
- **Requests (v2.34.2)** – communication with the NBP API and retrieval of exchange rate data.
- **Statistics** (Python standard library) – calculation of descriptive statistics such as median, mode, standard deviation, and coefficient of variation.
- **Matplotlib** – visualization of exchange rate changes using histograms.
- **CSV** (Python standard library) – exporting analysis results to CSV files.
- **Pytest** – unit testing framework.
- **Pytest-Mock** – mocking utilities for unit tests.
- **Git** – version control system.
- **GitHub** – source code hosting and project management platform.
- **GitHub Actions** – Continuous Integration (CI) and Continuous Deployment (CD) automation.

## User Manual

### Starting the Application

After installing the required dependencies, start the application from the root directory:

```bash
python src/main.py
```

After launch, the main menu will be displayed:

```text
=== NBP CURRENCY ANALYSIS SYSTEM ===
Choose analysis type:

1. Calculate the number of rising, falling and unchanged sessions
2. Calculate statistical measures (Median, Mode, Standard deviation, Coefficient of variation)
3. Determine distribution of monthly and quarterly changes between currency pairs
4. Exit application

Type 1-4 and press Enter to choose the corresponding option:
```

Select an option by entering the corresponding number.

---

### 1. Session Analysis

This option analyzes exchange rate movements for a selected currency and determines the number of:

- Rising sessions
- Falling sessions
- Unchanged sessions

#### Steps

1. Select a currency from the available NBP currency list.
2. Select an analysis period:
   - 1 week
   - 2 weeks
   - 1 month
   - 1 quarter (3 months)
   - 1/2 year (6 months)
   - 1 year

3. Choose whether the results should be displayed on the screen.
4. Optionally export the results to a CSV file.

#### Example Output

```text
=== SESSION ANALYSIS RESULT ===
Rising sessions: 12
Falling sessions: 8
Unchanged sessions: 1
```

---

### 2. Statistical Analysis

This option calculates descriptive statistics for the selected currency exchange rate data.

#### Calculated Measures

- Median
- Mode
- Standard Deviation
- Coefficient of Variation

#### Steps

1. Select a currency.
2. Select an analysis period.
3. Choose whether to display the calculated statistics.
4. Optionally export the results to a CSV file.

#### Example Output

```text
=== STATISTICAL MEASURES ===
Median: 0.059
Mode: 0.059
Standard deviation: 0.001
Coefficient of variation: 1.117 %
```

---

### 3. Currency Pair Histogram Analysis

This option creates a custom currency pair and analyzes the distribution of exchange rate changes.

#### Steps

1. Select the first currency.
2. Select the second currency.
3. Enter the analysis start date in the format:

```text
YYYY-MM-DD
```

4. Choose the analysis type:
   - MONTHLY
   - QUARTERLY

5. The application generates:
   - A histogram table
   - A graphical histogram using Matplotlib

6. Optionally export the histogram data to a CSV file.

#### Example Histogram Output

```text
Interval                  Number of changes
-0.127 -0.108             1
-0.108 -0.090             0
-0.090 -0.072             1
-0.072 -0.053             3
...
```

---

### Exporting Results

For every analysis type, the application allows exporting results to CSV files.

When prompted:

```text
Do you want to export the calculated data into a CSV file? Type YES or NO:
```

enter:

```text
YES
```

and provide a file name, for example:

```text
statistics_eur.csv
```

Exported files are stored in:

```text
/exports
```

---

### Returning to Previous Menus

Most application menus provide a **Return** option allowing the user to cancel the current operation and return to the menu without restarting the application.

---

### Exiting the Application

The application can be closed by:

- Selecting option **4** in the main menu, or
- Answering **NO** when prompted:

```text
Do you want to continue using the application? Type YES or NO:
```

After exiting, the application terminates gracefully and returns control to the operating system.

### Dependencies

The project dependencies are defined in the `requirements.txt` file:

```text
requests
matplotlib
pytest
pytest-mock
pytest-cov
requests-mock
flake8
black
```

---

## Software Deployment and Execution

The application is intended to be executed locally using the Python interpreter.

### Prerequisites

- Python 3.14 or newer
- Installed project dependencies

### Installing Dependencies

```bash
pip install -r requirements.txt
```

### Running the Application

From the root directory of the repository:

```bash
python src/main.py
```

---

## Project Documentation Location

All project documentation is stored in the following directory:

```text
/docs
```

This directory contains project documentation, including requirements, projects Gannt chart, test's reports, and project's UML graphs.

---

## Backlog Location

The product backlog and sprint backlogs are maintained using **GitHub Projects** in the form of Kanban boards.

**Location:**

```text
GitHub Repository → Projects
```

The Kanban boards are used to manage tasks, track progress, and organize project development activities.

---

## Continuous Integration (CI) and Automated Unit Testing

The project uses **GitHub Actions** to implement Continuous Integration.

**Workflow file:**

```text
.github/workflows/ci.yml
```

### CI Trigger Conditions

The CI workflow is automatically triggered when:

- Code is pushed to the `develop`, `main`, or `release` branches.
- A Pull Request is opened against the `develop`, `main`, or `release` branches.

### CI Process

The workflow performs the following steps:

1. Checks out the repository source code.
2. Sets up a Python 3.14 environment.
3. Installs dependencies from `requirements.txt`.
4. Executes automated unit tests using Pytest.

### Test Execution

```bash
python -m pytest
```

### Test Location

```text
/tests
```

This process ensures that every change introduced into the repository is automatically verified before integration.

In this folder there is also folder for integrations tests:

```text
/tests/integration
```

This folder contains integration tests that verify complete data processing workflows, such as histogram generation, session analysis, and statistical computation.

There is also folder for acceptance tests:

```text
/tests/acceptance
```

This file contains acceptance tests that validate the application’s core functionality, including session analysis, statistical computations, histogram generation, data export, input validation, error handling, and overall system stability during typical user workflows.

---

## Continuous Deployment (CD)

The project implements Continuous Deployment using GitHub Actions.

**Workflow file:**

```text
.github/workflows/cd.yml
```

### CD Trigger Conditions

The deployment workflow is automatically triggered when changes are pushed to the `release` branch.

### CD Process

The workflow performs the following actions:

1. Retrieves existing Git tags.
2. Automatically determines the next semantic version number.
3. Creates a ZIP archive containing the application source code.
4. Creates and pushes a new Git tag.
5. Publishes a GitHub Release.
6. Attaches the generated ZIP archive as a release artifact.

### Release Package Contents

```text
src/
README.md
```

### Versioning

The release process follows semantic versioning conventions and starts from:

```text
v2.0.0
```

---

## Testing and Bug-Fixing Reports

Documentation of the testing and bug-fixing process is maintained using **GitHub Issues**.

In accordance with the project requirements, every detected defect is documented as a dedicated **BugFix issue** containing:

- a description of the identified problem,
- steps required to reproduce the issue,
- analysis of the root cause,
- information about the implemented fix,
- comments documenting the debugging process,
- verification and testing results confirming the correctness of the solution.

### Location

```text
GitHub Repository → Issues → BugFix
```

This approach ensures complete traceability of defects, corrective actions, discussions, and validation activities directly within the repository.

---

## Repository Structure

```text
.
│   .gitignore
│   pytest.ini
│   README.md
│   requirements.txt
│
├───.github
│   └───workflows
│           cd.yml
│           ci.yml
│
├───docs
│   ├───burndown_charts
│   │       BurndownChart sprint 1.xlsx
│   │       BurndownChart sprint 2.xlsx
│   │
│   ├───gannt
│   │       zpi_PB_gannt_chart.xlsx
│   │
│   ├───architecture
│   │       System Architecture Description.docx
│   │
│   ├───requirements
│   │       system_specification_document.pdf
│   │
│   ├───test_reports
│   │       Test Execution and Defect Report.md
│   │
│   ├───sprint_reports
│   │       Sprint 1 raport.docx
│   │       Sprint 2 raport.docx
│   │
│   └───uml
│           System Activity Diagram.jpg
│           System Components Diagram.jpg
│           System Sequence Diagram.jpg
│           System Diagrams Description.docx
│
├───exports
│
├───src
│       analysis.py
│       api.py
│       export.py
│       main.py
│       menus.py
│       utils.py
│       visualization.py
│
└───tests
    │   test_analysis.py
    │   test_api.py
    │   test_export.py
    │   test_menus.py
    │   test_utils.py
    │   test_visualization.py
    │
    ├───acceptance
    │       acceptance_tests.md
    │
    └───integration
            test_histogram_flow.py
            test_session_analysis_flow.py
            test_statistics_flow.py
```

---

## Features

The application provides the following functionality:

- Retrieval of exchange rate data from the NBP API.
- Analysis of rising, falling, and unchanged trading sessions.
- Calculation of statistical indicators:
  - Median
  - Mode
  - Standard Deviation
  - Coefficient of Variation

- Creation of custom currency pairs.
- Generation and visualization of histograms.
- Export of analysis results to CSV files.
- Automated testing through CI pipelines.
- Automated release creation through CD pipelines.
