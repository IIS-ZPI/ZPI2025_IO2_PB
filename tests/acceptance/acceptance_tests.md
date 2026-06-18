
# Acceptance Tests

## AT-01 — Session analysis happy path

### Steps
1. Start the app
2. Choose session analysis
3. Select a currency
4. Select a time period
5. Display the data
6. Do not export the results
7.  Continue using application

### Expected result
- Up/down/unchanged sessions are shown
- App does not crash
- User returns to main menu

---

## AT-02 — Statistics analysis happy path

### Steps
1. Start the app
2. Choose statistical analysis
3. Select a currency
4. Select a time period
5. Display the data
6. Do not export the results
7. Continue using application

### Expected result
- Median, mode, std dev, variation are displayed
- Values are non-empty and numeric
- User returns to main menu

---

## AT-03 — Histogram analysis

### Steps
1. Start the app
2. Select distribution analysis
3. Choose first currency
4. Choose second currency
5. Enter valid start date
6. Choose monthly or quarterly mode
7. Display the data
8. Do not export the results
9. Continue using application

### Expected result
- Histogram is printed in console
- Graph window appears
- No runtime errors

---

## AT-04 — Export functionality check

### Steps
1. Run any analysis
2. Choose to export the results.
3. Enter filename
4. Verify file exists in exports folder

### Expected result
- CSV file is created
- File contains expected headers and data
- The data is rounded to 3 decimal places
- Export completes without errors

---

## AT-05 — Invalid input handling (menu robustness)

### Steps
1. Enter invalid main menu option (e.g. 999)
2. Enter invalid currency selection
3. Enter invalid YES/NO response

### Expected result
- App does not crash
- User is prompted again
- Invalid input is rejected

---

## AT-06 — Invalid date format handling

### Steps
1. Start any analysis requiring date input
2. Enter invalid date format (e.g. `2026/01/01`)
3. Enter valid format after rejection

### Expected result
- Invalid date is rejected
- User is prompted again
- App continues normally after correction

---

## AT-07 — API failure handling

### Steps
1. Start analysis
2. Attempt to fetch currency data

### Expected result
- App does not crash
- Flow is safely terminated or returned

---

## AT-08 — Statistics stability with edge values

### Steps
1. Run statistics analysis on stable dataset

### Expected result
- Std deviation may be 0 or near 0
- No crashes from mode/std calculations
- Output is still valid

---

## AT-09 — Histogram analysis works correctly with valid data

### Steps
1. Run histogram analysis with known dataset
2. Inspect output bins

### Expected result
- Values are grouped into intervals
- Last bin includes boundary values correctly
- No missing or negative bin errors
---

## AT-10 — PLN currency support

### Steps
1. Start distribution analysis
2. Select PLN as first currency
3. Select USD as second currency
4. Continue analysis

### Expected result
- PLN is available in selection list
- PLN-based pair analysis works without errors

---

## AT-11 — Application shutdown flow

### Steps
1. Start application
2. Navigate through main menu
3. Select exit option

### Expected result
- Application closes cleanly
- No hanging processes or errors