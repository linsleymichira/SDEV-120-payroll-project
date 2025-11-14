# Group Project Development Plan
## The Pythonex - SDEV 120 Payroll System

---

## Team Information

**Group Name:** The Pythonex

**Team Members:**
- Linsley Michira (Team Leader)
- Jacob Solomon (Assistant) 
- Thaija Wilson (Stenographer)
- Bran Mai Nhkum
- Elijah Penman
- Ronald Rudolph

**Instructor:** Professor Carla Uycoque  
**Course:** SDEV 120  
**Institution:** Ivy Tech Community College

---

## Communication and Collaboration Plan

### Tools Used:
- **GitHub Repository:** Central repository for version control and code collaboration
- **Email and Messaging:** Team communication via email threads and in-person meetings
- **Regular Meetings:** Weekly meetings on Sundays at 4pm

### Meeting Schedule:
- Regular team meetings: Sundays at 4pm
- Ad-hoc meetings as needed for urgent issues

---

## Project Approach

### Technology Choice:
The team has chosen to use **Python** as the primary development tool for this payroll system project.

### Program Structure:
The program is designed with a modular architecture consisting of three main modules:

1. **UI Module (ui_module.py)** - User Interface
   - Handles all user interactions
   - Prompts for employee data entry
   - Displays results to the user
   - Input validation

2. **Database Module (database_module.py)** - Data Storage
   - Stores employee information
   - Pay rate lookup table
   - Employee data management functions
   - Database operations

3. **Calculations Module (calculations_module.py)** - Business Logic
   - Gross pay calculations
   - Overtime calculations (1.5x for hours over 40)
   - Tax calculations (State 5.6%, Federal 7.9%)
   - Net pay calculations
   - Input validation for hours worked

---

## Task Assignment and Responsibilities

### Module Development:
- **Linsley Michira:** Team coordination, main.py integration, overall project structure
- **Jacob Solomon:** Testing framework, unit testing implementation
- **Thaija Wilson:** Test data creation (10 fake employee records)
- **Bran Mai Nhkum:** Database module development
- **Elijah Penman:** Calculations module development
- **Ronald Rudolph:** UI module development

### Additional Responsibilities:
- **Testing Lead:** Jacob Solomon
- **Test Data Creation:** Thaija Wilson
- **Documentation:** All team members (collaborative effort)
- **Security Implementation:** Team collaboration

---

## Program Requirements Implementation

### 1. Employee Data Entry
- ✅ First and last name
- ✅ Employee ID
- ✅ Number of dependents
- ✅ Hours worked

### 2. Gross Pay Calculation
- ✅ Regular hours (up to 40) at regular rate
- ✅ Overtime hours (over 40) at 1.5x rate
- ✅ Total gross pay

### 3. Error Checking
- ✅ Maximum hours validation (80 hours per week)
- ✅ Negative hours validation
- ✅ Input format validation
- ✅ Name validation
- ✅ Employee ID validation
- ✅ Dependents validation

### 4. Tax Calculations
- ✅ State Tax: 5.6% of gross pay
- ✅ Federal Tax: 7.9% of gross pay
- ✅ Total tax deductions

### 5. Net Pay Calculation
- ✅ Net Pay = Gross Pay - Total Taxes

### 6. Data Storage
- ✅ Results stored in employee database
- ✅ Results saved to lists/arrays

### 7. Output
- ✅ Results displayed on screen
- ✅ Results saved to file (payroll_results.txt)

---

## Security Measures

### Input Validation:
1. **Hours Worked Validation:**
   - Minimum: 0 hours
   - Maximum: 80 hours per week
   - Must be a valid number
   - Prevents negative values

2. **Name Validation:**
   - Cannot be empty
   - Only allows letters, spaces, hyphens, and apostrophes
   - Prevents special characters and numbers

3. **Employee ID Validation:**
   - Cannot be empty
   - Minimum length requirement
   - Format checking

4. **Dependents Validation:**
   - Must be a valid integer
   - Cannot be negative
   - Maximum limit of 20 (reasonableness check)

### Data Integrity:
- Try-catch blocks for error handling
- Function return validation
- Type checking for all inputs
- Default values for missing data

### Security Best Practices:
- Input sanitization
- Error messages without sensitive information
- Data validation at multiple layers
- Boundary testing for all inputs

---

## Testing Strategy

### Test Cases (10 Employees):
Created by Thaija Wilson

1. **James Anderson (E001)** - Regular 40 hours, no overtime
2. **Maria Garcia (E002)** - 45.5 hours with overtime
3. **Robert Johnson (E003)** - 50 hours with overtime
4. **Jennifer Williams (E004)** - Part-time 35 hours
5. **Michael Brown (E005)** - 48 hours with overtime
6. **Sarah Davis (E006)** - 42.5 hours with overtime
7. **David Martinez (E007)** - Part-time 38 hours
8. **Lisa Rodriguez (E008)** - 55 hours with significant overtime
9. **Christopher Wilson (E009)** - Part-time 20 hours
10. **Amanda Taylor (E010)** - 60 hours with maximum overtime

### Edge Case Testing:
1. **Zero Hours Test** - Employee with 0 hours worked
2. **Maximum Hours Test** - Employee at exactly 80 hours (boundary)
3. **Over Maximum Test** - Employee exceeding 80 hours (should fail)

### Testing Approach:
- **Unit Testing:** Individual function testing
- **Integration Testing:** Module interaction testing
- **System Testing:** Full program testing
- **Boundary Testing:** Edge cases and limits
- **Negative Testing:** Invalid input handling

### Testing Execution:
- Automated test cases run by Jacob Solomon
- Manual testing by all team members
- Test results documented and reviewed
- Issues tracked and resolved

---

## Program Flow (Pseudocode)

```
START

    DISPLAY welcome message and team information
    
    PROMPT user: "Load test data?"
    IF yes THEN
        LOAD 10 test employees into database
        DISPLAY test data summary
    END IF
    
    LOOP until user exits
        DISPLAY menu:
            1. Enter Employee Data
            2. View All Employee Records
            3. Process All Employees
            4. Exit
        
        GET user choice
        
        CASE choice:
            CASE 1: Enter Employee Data
                PROMPT for Employee ID
                VALIDATE Employee ID
                PROMPT for First Name
                VALIDATE First Name
                PROMPT for Last Name
                VALIDATE Last Name
                PROMPT for Number of Dependents
                VALIDATE Dependents (>= 0, <= 20)
                PROMPT for Hours Worked
                VALIDATE Hours (>= 0, <= 80)
                
                ADD employee to database
                LOOKUP hourly rate from database
                
                IF hours <= 40 THEN
                    regular_pay = hours * rate
                    overtime_pay = 0
                ELSE
                    regular_pay = 40 * rate
                    overtime_hours = hours - 40
                    overtime_pay = overtime_hours * rate * 1.5
                END IF
                
                gross_pay = regular_pay + overtime_pay
                
                state_tax = gross_pay * 0.056
                federal_tax = gross_pay * 0.079
                total_tax = state_tax + federal_tax
                
                net_pay = gross_pay - total_tax
                
                DISPLAY payroll results
            
            CASE 2: View All Employee Records
                GET all employees from database
                FOR each employee
                    DISPLAY employee information
                END FOR
            
            CASE 3: Process All Employees
                GET all employees from database
                FOR each employee
                    LOOKUP hourly rate
                    CALCULATE payroll
                    STORE results
                    DISPLAY results
                END FOR
                SAVE all results to file
                DISPLAY summary
            
            CASE 4: Exit
                DISPLAY goodbye message
                EXIT program
            
            DEFAULT:
                DISPLAY "Invalid choice"
        END CASE
    END LOOP

END
```

---

## Program Standards

### Variable Definitions:
- Clear, descriptive variable names
- Constants defined at module level (tax rates, regular hours, max hours)
- Type hints where appropriate
- Comments for complex logic

### Code Organization:
- Modular design (3 main modules + main program + test data)
- Single responsibility principle
- Reusable functions
- Proper separation of concerns

### Documentation:
- Module docstrings
- Function docstrings with parameters and return types
- Inline comments for complex logic
- README file with usage instructions

### Error Handling:
- Try-catch blocks for file operations
- Input validation functions
- Error messages for users
- Graceful error recovery

---

## Testing Evidence

### Test Execution Results:
All test cases will be executed and results documented in `TESTING_RESULTS.md`

### Expected Outcomes:
- All 10 normal test cases should process successfully
- Zero hours case should calculate $0 pay
- 80-hour boundary case should process successfully
- Over 80-hour case should fail validation with appropriate error message

### Documentation:
- Test case descriptions
- Input values
- Expected outputs
- Actual outputs
- Pass/Fail status
- Screenshots of results

---

## File Structure

```
SDEV-120-payroll-project/
│
├── main.py                     # Main program
├── database_module.py          # Database module
├── calculations_module.py      # Calculations module
├── ui_module.py               # UI module
├── test_data.py               # Test data (10 employees)
├── payroll_results.txt        # Output file (generated)
├── PROJECT_PLAN.md            # This file
├── TESTING_RESULTS.md         # Testing documentation
├── PSEUDOCODE.md              # Detailed pseudocode
└── README.md                  # Project README

```

---

## Timeline and Milestones

### Week 1:
- ✅ Team formation and role assignment
- ✅ Repository setup
- ✅ Initial planning

### Week 2:
- ✅ Module design
- ✅ Code development
- ✅ Test data creation

### Week 3:
- Testing execution
- Bug fixes
- Documentation completion

### Week 4:
- Final testing
- Code review
- Submission preparation

---

## Deliverables

1. ✅ Source code files (all modules)
2. ✅ Test data (10 employee records)
3. ✅ Project development plan (this document)
4. ✅ Pseudocode documentation
5. Testing results documentation (to be completed)
6. ✅ Working program demonstration
7. Individual contribution records

---

## Conclusion

This project demonstrates the team's ability to:
- Break down complex tasks into manageable modules
- Collaborate effectively using version control
- Implement security and validation measures
- Create comprehensive test cases
- Document development process
- Apply software development best practices

The modular design allows for easy maintenance, testing, and future enhancements. Each team member has contributed to different aspects of the project, ensuring a well-rounded final product.

---

**Document Version:** 1.0  
**Last Updated:** November 14, 2024  
**Status:** Complete
