# Testing Results Documentation
## The Pythonex - SDEV 120 Group Project

---

## Testing Team
**Testing Lead:** Jacob Solomon (Assistant)  
**Test Data Creation:** Thaija Wilson (Stenographer)  
**Testing Support:** All Team Members

---

## Testing Approach

### Types of Testing Conducted:
1. **Unit Testing** - Individual function testing
2. **Integration Testing** - Module interaction testing
3. **System Testing** - Full program flow testing
4. **Boundary Testing** - Edge cases and limits
5. **Negative Testing** - Invalid input handling
6. **Security Testing** - Input validation and data integrity

---

## Test Cases

### Normal Operation Test Cases (10 Employees)

#### Test Case 1: Regular 40 Hours - No Overtime
- **Employee ID:** E001
- **Name:** James Anderson
- **Dependents:** 2
- **Hours Worked:** 40.0
- **Hourly Rate:** $15.50
- **Expected Results:**
  - Regular Pay: $620.00
  - Overtime Pay: $0.00
  - Gross Pay: $620.00
  - State Tax (5.6%): $34.72
  - Federal Tax (7.9%): $48.98
  - Total Tax: $83.70
  - Net Pay: $536.30
- **Status:** To be tested

---

#### Test Case 2: Regular + Overtime
- **Employee ID:** E002
- **Name:** Maria Garcia
- **Dependents:** 3
- **Hours Worked:** 45.5
- **Hourly Rate:** $18.75
- **Expected Results:**
  - Regular Hours: 40
  - Overtime Hours: 5.5
  - Regular Pay: $750.00
  - Overtime Pay: 5.5 × $18.75 × 1.5 = $154.69
  - Gross Pay: $904.69
  - State Tax (5.6%): $50.66
  - Federal Tax (7.9%): $71.47
  - Total Tax: $122.13
  - Net Pay: $782.56
- **Status:** To be tested

---

#### Test Case 3: Significant Overtime
- **Employee ID:** E003
- **Name:** Robert Johnson
- **Dependents:** 1
- **Hours Worked:** 50.0
- **Hourly Rate:** $22.00
- **Expected Results:**
  - Regular Hours: 40
  - Overtime Hours: 10
  - Regular Pay: $880.00
  - Overtime Pay: 10 × $22.00 × 1.5 = $330.00
  - Gross Pay: $1,210.00
  - State Tax (5.6%): $67.76
  - Federal Tax (7.9%): $95.59
  - Total Tax: $163.35
  - Net Pay: $1,046.65
- **Status:** To be tested

---

#### Test Case 4: Part-Time Employee
- **Employee ID:** E004
- **Name:** Jennifer Williams
- **Dependents:** 0
- **Hours Worked:** 35.0
- **Hourly Rate:** $16.25
- **Expected Results:**
  - Regular Hours: 35
  - Overtime Hours: 0
  - Regular Pay: $568.75
  - Overtime Pay: $0.00
  - Gross Pay: $568.75
  - State Tax (5.6%): $31.85
  - Federal Tax (7.9%): $44.93
  - Total Tax: $76.78
  - Net Pay: $491.97
- **Status:** To be tested

---

#### Test Case 5: Moderate Overtime
- **Employee ID:** E005
- **Name:** Michael Brown
- **Dependents:** 4
- **Hours Worked:** 48.0
- **Hourly Rate:** $20.00
- **Expected Results:**
  - Regular Hours: 40
  - Overtime Hours: 8
  - Regular Pay: $800.00
  - Overtime Pay: 8 × $20.00 × 1.5 = $240.00
  - Gross Pay: $1,040.00
  - State Tax (5.6%): $58.24
  - Federal Tax (7.9%): $82.16
  - Total Tax: $140.40
  - Net Pay: $899.60
- **Status:** To be tested

---

#### Test Case 6: Small Overtime
- **Employee ID:** E006
- **Name:** Sarah Davis
- **Dependents:** 2
- **Hours Worked:** 42.5
- **Hourly Rate:** $19.50
- **Expected Results:**
  - Regular Hours: 40
  - Overtime Hours: 2.5
  - Regular Pay: $780.00
  - Overtime Pay: 2.5 × $19.50 × 1.5 = $73.13
  - Gross Pay: $853.13
  - State Tax (5.6%): $47.78
  - Federal Tax (7.9%): $67.40
  - Total Tax: $115.18
  - Net Pay: $737.95
- **Status:** To be tested

---

#### Test Case 7: Part-Time (38 hours)
- **Employee ID:** E007
- **Name:** David Martinez
- **Dependents:** 1
- **Hours Worked:** 38.0
- **Hourly Rate:** $17.80
- **Expected Results:**
  - Regular Hours: 38
  - Overtime Hours: 0
  - Regular Pay: $676.40
  - Overtime Pay: $0.00
  - Gross Pay: $676.40
  - State Tax (5.6%): $37.88
  - Federal Tax (7.9%): $53.44
  - Total Tax: $91.32
  - Net Pay: $585.08
- **Status:** To be tested

---

#### Test Case 8: High Overtime
- **Employee ID:** E008
- **Name:** Lisa Rodriguez
- **Dependents:** 3
- **Hours Worked:** 55.0
- **Hourly Rate:** $21.25
- **Expected Results:**
  - Regular Hours: 40
  - Overtime Hours: 15
  - Regular Pay: $850.00
  - Overtime Pay: 15 × $21.25 × 1.5 = $478.13
  - Gross Pay: $1,328.13
  - State Tax (5.6%): $74.38
  - Federal Tax (7.9%): $104.92
  - Total Tax: $179.30
  - Net Pay: $1,148.83
- **Status:** To be tested

---

#### Test Case 9: Very Part-Time
- **Employee ID:** E009
- **Name:** Christopher Wilson
- **Dependents:** 0
- **Hours Worked:** 20.0
- **Hourly Rate:** $14.50
- **Expected Results:**
  - Regular Hours: 20
  - Overtime Hours: 0
  - Regular Pay: $290.00
  - Overtime Pay: $0.00
  - Gross Pay: $290.00
  - State Tax (5.6%): $16.24
  - Federal Tax (7.9%): $22.91
  - Total Tax: $39.15
  - Net Pay: $250.85
- **Status:** To be tested

---

#### Test Case 10: Maximum Recommended Overtime
- **Employee ID:** E010
- **Name:** Amanda Taylor
- **Dependents:** 2
- **Hours Worked:** 60.0
- **Hourly Rate:** $23.00
- **Expected Results:**
  - Regular Hours: 40
  - Overtime Hours: 20
  - Regular Pay: $920.00
  - Overtime Pay: 20 × $23.00 × 1.5 = $690.00
  - Gross Pay: $1,610.00
  - State Tax (5.6%): $90.16
  - Federal Tax (7.9%): $127.19
  - Total Tax: $217.35
  - Net Pay: $1,392.65
- **Status:** To be tested

---

## Edge Case Testing

### Edge Case 1: Zero Hours Boundary
- **Employee ID:** E999
- **Name:** Test Case
- **Dependents:** 0
- **Hours Worked:** 0.0
- **Expected Results:**
  - Gross Pay: $0.00
  - Tax: $0.00
  - Net Pay: $0.00
- **Expected Behavior:** Should process successfully with zero pay
- **Status:** To be tested

---

### Edge Case 2: Maximum Hours Boundary
- **Employee ID:** E997
- **Name:** Boundary Test
- **Dependents:** 0
- **Hours Worked:** 80.0
- **Expected Results:**
  - Should process successfully
  - Regular Hours: 40
  - Overtime Hours: 40
- **Expected Behavior:** Should accept exactly 80 hours
- **Status:** To be tested

---

### Edge Case 3: Exceeds Maximum Hours
- **Employee ID:** E998
- **Name:** Error Test
- **Dependents:** 0
- **Hours Worked:** 85.0
- **Expected Results:**
  - Error Message: "Hours worked exceeds maximum of 80 hours per week"
- **Expected Behavior:** Should reject and display error
- **Status:** To be tested

---

## Validation Testing

### Test Case V1: Invalid Employee ID
- **Input:** Empty string ""
- **Expected Result:** Error message "Employee ID cannot be empty"
- **Status:** To be tested

---

### Test Case V2: Invalid Name (Numbers)
- **Input:** "John123"
- **Expected Result:** Error message "Name can only contain letters, spaces, hyphens, and apostrophes"
- **Status:** To be tested

---

### Test Case V3: Invalid Name (Empty)
- **Input:** ""
- **Expected Result:** Error message "Name cannot be empty"
- **Status:** To be tested

---

### Test Case V4: Negative Dependents
- **Input:** -5
- **Expected Result:** Error message "Number of dependents cannot be negative"
- **Status:** To be tested

---

### Test Case V5: Excessive Dependents
- **Input:** 25
- **Expected Result:** Error message "Number of dependents seems unusually high (max 20)"
- **Status:** To be tested

---

### Test Case V6: Non-numeric Dependents
- **Input:** "abc"
- **Expected Result:** Error message "Number of dependents must be a valid number"
- **Status:** To be tested

---

### Test Case V7: Negative Hours
- **Input:** -10.0
- **Expected Result:** Error message "Hours worked cannot be negative"
- **Status:** To be tested

---

### Test Case V8: Non-numeric Hours
- **Input:** "twenty"
- **Expected Result:** Error message "Hours worked must be a valid number"
- **Status:** To be tested

---

## Integration Testing

### Integration Test 1: Database and Calculations Module
- **Test:** Add employee to database, retrieve pay rate, calculate payroll
- **Expected Result:** Data flows correctly between modules
- **Status:** To be tested

---

### Integration Test 2: UI and Database Module
- **Test:** User input validation and storage in database
- **Expected Result:** Validated data stored correctly
- **Status:** To be tested

---

### Integration Test 3: Complete Flow
- **Test:** User input → Validation → Database → Calculations → Display → File Output
- **Expected Result:** End-to-end processing works correctly
- **Status:** To be tested

---

## Security Testing

### Security Test 1: SQL-like Injection Attempt
- **Input:** Employee ID = "E001'; DROP TABLE--"
- **Expected Result:** Treated as string, no security breach
- **Status:** To be tested

---

### Security Test 2: XSS-like Attempt
- **Input:** Name = "<script>alert('test')</script>"
- **Expected Result:** Rejected by name validation
- **Status:** To be tested

---

### Security Test 3: Buffer Overflow Attempt
- **Input:** Very long string (1000+ characters)
- **Expected Result:** Handled gracefully without crash
- **Status:** To be tested

---

## Performance Testing

### Performance Test 1: Process 10 Employees
- **Scenario:** Load and process all 10 test employees
- **Expected Result:** Completes in under 5 seconds
- **Status:** To be tested

---

### Performance Test 2: File Output
- **Scenario:** Generate payroll_results.txt file
- **Expected Result:** File created successfully with all data
- **Status:** To be tested

---

## Test Results Summary

### Test Statistics (To be updated after testing):
- Total Test Cases: 30+
- Passed: TBD
- Failed: TBD
- Success Rate: TBD

### Critical Issues Found:
(To be documented during testing)

### Non-Critical Issues Found:
(To be documented during testing)

### Recommendations:
(To be documented after testing)

---

## Test Execution Log

### Session 1: Initial Testing
- **Date:** TBD
- **Tester:** Jacob Solomon
- **Environment:** Python 3.x
- **Results:** To be recorded

### Session 2: Edge Case Testing
- **Date:** TBD
- **Tester:** Team
- **Results:** To be recorded

### Session 3: Security Testing
- **Date:** TBD
- **Tester:** Team
- **Results:** To be recorded

---

## Conclusion

This comprehensive testing plan ensures:
- All functionality works as expected
- Security measures are effective
- Input validation catches all errors
- Calculations are accurate
- File output is correct
- System handles edge cases properly

All tests will be executed by the testing team and results will be documented in this file.

---

**Document Version:** 1.0  
**Last Updated:** November 14, 2024  
**Status:** Ready for Testing Execution
