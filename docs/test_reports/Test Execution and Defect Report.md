
# Test Execution and Defect Report

## 1. Project Overview

-   **Project:** Application for statistical analysis of exchange rates data
-   **Test Levels:** Acceptance + Integration
-   **Test Execution Types:** Manual testing with exploratory techniques
-   **Scope:** Session analysis, statistical analysis, histogram analysis, export functionality, API integration

## 2. Test Execution Summary

| Test ID | Test Area | Description | Result | Notes |
|---|---|---|---|---|
| AT-01 | Session analysis | Session growth/decline analysis | PASS | No issues detected |
| AT-02 | Statistics analysis | Median, mode, std dev calculations | PASS | Correct numeric output |
| AT-03 | Histogram analysis | Distribution visualization | PASS | Stable output |
| AT-04 | Export functionality | CSV export generation | FAIL | Path inconsistency + rounding issue |
| AT-05 | Input validation | Menu robustness | PASS | Handles invalid input |
| AT-06 | Date validation | Date format handling | PASS | Proper rejection |
| AT-07 | API failure handling | External API failure handling | FAIL | Unhandled exception crash |
| AT-08 | Edge statistics | Stability on edge data | PASS | No crashes |
| AT-09 | Histogram correctness | Bin correctness | PASS | Valid grouping |
| AT-10 | Currency selection | PLN support in pairs | FAIL | PLN missing in selection |
| AT-11 | App shutdown | Exit flow | PASS | Clean shutdown |

## 3. Defect Log (GitHub Issues)

### BUG-001 (AT-10)  
- Title: "PLN currency is not supported in currency pair analysis"
- Issue: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/issues/36 
- Summary: The application does not allow PLN to be selected as part of currency pair analysis.  
  
- Expected:  
	- PLN is available in the currency selection list  
	- Currency pair analysis supports PLN  
	- No errors occur during selection or processing  
  
- Actual:  
	- PLN is not available in the selection list  
	- Analysis cannot be performed for PLN-based pairs

- Fix:  
	- Developer: Kamil Wakuła
	- Updated: Application now prevents users from selecting the same currency twice when determining changes between currency pairs.
	- Pull request history: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/pull/39
	- Branch: `bugfix_PLN_in_histogram`

---

### BUG-002 (AT-07)  
- Title: "Application crashes on NBP API failure"
- Issue: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/issues/37  
- Summary: When the NBP API is unavailable or returns an error response, the application raises an unhandled exception instead of handling the failure gracefully.  
  
- Expected:  
	- Application does not crash  
	- User is shown a clear error message  
	- Control is returned safely to the main menu  
  
- Actual:  
	- Unhandled exception is raised  
	- Application terminates  
	- No user-friendly error message is shown

- Fix:  
	- Developer: Kacper Saletra
	- Updated: Added exception handling for NBP API request failures, preventing unhandled exceptions and ensuring safe return to the main CLI loop.
	- Pull request history: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/pull/40
	- Branch: `bugfix_api_connection_and_rounding_error`
---

### BUG-003 (AT-04)
- Title: "Exported CSV does not round numeric values to 3 decimal places"
- Issue: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/issues/38
- Summary: The exported CSV file does not format numerical values to 3 decimal places, despite this being required by the acceptance criteria.
- Expected: 
	- CSV file is created successfully
	- All numeric values are rounded to 3 decimal places
	- Output format is consistent across all exported analyses
- Actual: 
	-   CSV file is created successfully
	-   Numeric values are not consistently rounded to 3 decimal places

- Fix:  
	- Developer: Kacper Saletra
	- Updated: Export logic was refactored to enforce rounding of all numeric values to 3 decimal places before writing to CSV.
	- Pull request history: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/pull/40
	- Branch: `bugfix_api_connection_and_rounding_error`
---

### BUG-004 (AT-04)  
- Title: "Inconsistent export path causes files to be created outside project directory"
- Issue: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/issues/41 
- Summary: Export functionality writes CSV files to inconsistent locations depending on execution context.  
  
- Expected:  
	- CSV file is created in the designated exports/ directory inside the project  
	- Export location is consistent across application and test execution  
	- No files are created outside project structure  
  
- Actual:  
	- CSV file may be created in inconsistent or unexpected locations  
	- Integration tests create/export files outside intended project directory  
	- File placement differs between runtime contexts

- Fix:  
	- Developer: Kamil Wakuła
	- Updated: Replaced relative export paths with a stable project-bound export directory to ensure consistent file generation across environments and test runs.
	- Pull request history: https://github.com/IIS-ZPI/ZPI2025_IO2_PB/pull/43
	- Branch: `bugfix_export`
---

## 4. Defect Summary and Resolution Overview

During the testing phase, a total of 4 defects was identified and documented through GitHub Issues. All reported issues were subsequently analyzed, resolved, and verified through repeated test execution.

### Raised Issues
- BUG-001 — Missing support for PLN currency in pair analysis (AT-10 violation)
- BUG-002 — Unhandled exception during NBP API failure (AT-07 violation)
- BUG-003 — Incorrect export formatting for numeric precision (AT-04 violation)
- BUG-004 — Inconsistent export path (AT-04 violation)


### Resolution Status
All identified defects were successfully resolved prior to final submission:

- Export functionality was corrected to ensure consistent file placement and proper numeric formatting.
- API integration was updated to handle failure scenarios gracefully without application crash.
- Currency selection logic was extended to include PLN support in pair analysis.