# Payroll System Pseudocode
## The Pythonex - SDEV 120 Group Project

---

## Main Program Flow

```
PROGRAM PayrollSystem

    // Constants
    CONSTANT STATE_TAX_RATE = 0.056      // 5.6%
    CONSTANT FEDERAL_TAX_RATE = 0.079    // 7.9%
    CONSTANT REGULAR_HOURS = 40
    CONSTANT OVERTIME_MULTIPLIER = 1.5
    CONSTANT MAX_HOURS_PER_WEEK = 80

    // Global Data Structures
    DECLARE employee_database AS DICTIONARY
    DECLARE pay_rates AS DICTIONARY

    // Initialize pay rates for 10 employees
    pay_rates["E001"] = 15.50
    pay_rates["E002"] = 18.75
    pay_rates["E003"] = 22.00
    pay_rates["E004"] = 16.25
    pay_rates["E005"] = 20.00
    pay_rates["E006"] = 19.50
    pay_rates["E007"] = 17.80
    pay_rates["E008"] = 21.25
    pay_rates["E009"] = 14.50
    pay_rates["E010"] = 23.00

    // Main Program Execution
    BEGIN
        CALL DisplayWelcome()
        
        PROMPT "Load test data? (yes/no)"
        INPUT load_test_data
        
        IF load_test_data == "yes" THEN
            CALL LoadTestData()
            CALL DisplayTestSummary()
        END IF
        
        CALL RunInteractiveMode()
        
        DISPLAY "Thank you for using The Pythonex Payroll System!"
    END

END PROGRAM
```

---

## Module 1: Database Module

```
MODULE DatabaseModule

    // Add or update employee in database
    FUNCTION AddEmployee(employee_id, first_name, last_name, dependents, hours_worked)
        BEGIN
            TRY
                hourly_rate = CALL GetPayRate(employee_id)
                
                employee_database[employee_id] = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'dependents': dependents,
                    'hours_worked': hours_worked,
                    'hourly_rate': hourly_rate
                }
                
                RETURN True
            CATCH exception
                DISPLAY "Error adding employee: " + exception
                RETURN False
            END TRY
        END
    END FUNCTION

    // Retrieve employee information
    FUNCTION GetEmployee(employee_id)
        BEGIN
            IF employee_id EXISTS IN employee_database THEN
                RETURN employee_database[employee_id]
            ELSE
                RETURN None
            END IF
        END
    END FUNCTION

    // Look up pay rate for employee
    FUNCTION GetPayRate(employee_id)
        BEGIN
            IF employee_id EXISTS IN pay_rates THEN
                RETURN pay_rates[employee_id]
            ELSE
                RETURN 15.00  // Default rate
            END IF
        END
    END FUNCTION

    // Get all employees
    FUNCTION GetAllEmployees()
        BEGIN
            RETURN employee_database
        END
    END FUNCTION

    // Update pay rate
    FUNCTION UpdatePayRate(employee_id, new_rate)
        BEGIN
            IF new_rate > 0 THEN
                pay_rates[employee_id] = new_rate
                
                IF employee_id EXISTS IN employee_database THEN
                    employee_database[employee_id]['hourly_rate'] = new_rate
                END IF
                
                RETURN True
            ELSE
                RETURN False
            END IF
        END
    END FUNCTION

END MODULE
```

---

## Module 2: Calculations Module

```
MODULE CalculationsModule

    // Validate hours worked
    FUNCTION ValidateHours(hours_worked)
        BEGIN
            IF hours_worked < 0 THEN
                RETURN (False, "Hours cannot be negative")
            END IF
            
            IF hours_worked > MAX_HOURS_PER_WEEK THEN
                RETURN (False, "Hours exceed maximum of 80 per week")
            END IF
            
            RETURN (True, "")
        END
    END FUNCTION

    // Calculate gross pay with overtime
    FUNCTION CalculateGrossPay(hours_worked, hourly_rate)
        BEGIN
            // Validate input
            (is_valid, error_msg) = CALL ValidateHours(hours_worked)
            IF NOT is_valid THEN
                THROW ERROR error_msg
            END IF
            
            // Calculate regular and overtime pay
            IF hours_worked <= REGULAR_HOURS THEN
                regular_pay = hours_worked * hourly_rate
                overtime_pay = 0
            ELSE
                regular_pay = REGULAR_HOURS * hourly_rate
                overtime_hours = hours_worked - REGULAR_HOURS
                overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
            END IF
            
            gross_pay = regular_pay + overtime_pay
            
            RETURN (gross_pay, regular_pay, overtime_pay)
        END
    END FUNCTION

    // Calculate state tax
    FUNCTION CalculateStateTax(gross_pay)
        BEGIN
            RETURN gross_pay * STATE_TAX_RATE
        END
    END FUNCTION

    // Calculate federal tax
    FUNCTION CalculateFederalTax(gross_pay)
        BEGIN
            RETURN gross_pay * FEDERAL_TAX_RATE
        END
    END FUNCTION

    // Calculate total taxes
    FUNCTION CalculateTotalTax(gross_pay)
        BEGIN
            state_tax = CALL CalculateStateTax(gross_pay)
            federal_tax = CALL CalculateFederalTax(gross_pay)
            total_tax = state_tax + federal_tax
            
            RETURN (total_tax, state_tax, federal_tax)
        END
    END FUNCTION

    // Calculate net pay
    FUNCTION CalculateNetPay(gross_pay)
        BEGIN
            (total_tax, state_tax, federal_tax) = CALL CalculateTotalTax(gross_pay)
            net_pay = gross_pay - total_tax
            
            RETURN (net_pay, gross_pay, total_tax, state_tax, federal_tax)
        END
    END FUNCTION

    // Process complete employee payroll
    FUNCTION ProcessEmployeePayroll(hours_worked, hourly_rate)
        BEGIN
            // Validate hours
            (is_valid, error_msg) = CALL ValidateHours(hours_worked)
            IF NOT is_valid THEN
                RETURN {
                    'error': True,
                    'error_message': error_msg
                }
            END IF
            
            // Calculate gross pay
            (gross_pay, regular_pay, overtime_pay) = 
                CALL CalculateGrossPay(hours_worked, hourly_rate)
            
            // Calculate taxes
            (total_tax, state_tax, federal_tax) = 
                CALL CalculateTotalTax(gross_pay)
            
            // Calculate net pay
            net_pay = gross_pay - total_tax
            
            // Determine hours breakdown
            IF hours_worked <= REGULAR_HOURS THEN
                regular_hours = hours_worked
                overtime_hours = 0
            ELSE
                regular_hours = REGULAR_HOURS
                overtime_hours = hours_worked - REGULAR_HOURS
            END IF
            
            RETURN {
                'error': False,
                'hours_worked': hours_worked,
                'regular_hours': regular_hours,
                'overtime_hours': overtime_hours,
                'hourly_rate': hourly_rate,
                'regular_pay': regular_pay,
                'overtime_pay': overtime_pay,
                'gross_pay': gross_pay,
                'state_tax': state_tax,
                'federal_tax': federal_tax,
                'total_tax': total_tax,
                'net_pay': net_pay
            }
        END
    END FUNCTION

END MODULE
```

---

## Module 3: UI Module

```
MODULE UIModule

    // Validate name input
    FUNCTION ValidateName(name)
        BEGIN
            IF name IS EMPTY OR name IS BLANK THEN
                RETURN (False, "Name cannot be empty")
            END IF
            
            FOR EACH character IN name DO
                IF NOT (character IS LETTER OR character IS SPACE OR 
                        character IS HYPHEN OR character IS APOSTROPHE) THEN
                    RETURN (False, "Name can only contain letters, spaces, hyphens, apostrophes")
                END IF
            END FOR
            
            RETURN (True, "")
        END
    END FUNCTION

    // Validate employee ID
    FUNCTION ValidateEmployeeID(employee_id)
        BEGIN
            IF employee_id IS EMPTY OR employee_id IS BLANK THEN
                RETURN (False, "Employee ID cannot be empty")
            END IF
            
            IF LENGTH(employee_id) < 2 THEN
                RETURN (False, "Employee ID must be at least 2 characters")
            END IF
            
            RETURN (True, "")
        END
    END FUNCTION

    // Validate dependents
    FUNCTION ValidateDependents(dependents)
        BEGIN
            TRY
                deps = CONVERT dependents TO INTEGER
                
                IF deps < 0 THEN
                    RETURN (False, 0, "Dependents cannot be negative")
                END IF
                
                IF deps > 20 THEN
                    RETURN (False, 0, "Dependents exceed maximum of 20")
                END IF
                
                RETURN (True, deps, "")
            CATCH exception
                RETURN (False, 0, "Dependents must be a valid number")
            END TRY
        END
    END FUNCTION

    // Get employee input from user
    FUNCTION GetEmployeeInput()
        BEGIN
            DISPLAY "EMPLOYEE DATA ENTRY"
            DISPLAY "Enter 'quit' to cancel"
            
            // Get Employee ID
            REPEAT
                PROMPT "Enter Employee ID (e.g., E001)"
                INPUT employee_id
                
                IF employee_id == "quit" THEN
                    RETURN None
                END IF
                
                (is_valid, error_msg) = CALL ValidateEmployeeID(employee_id)
                IF is_valid THEN
                    BREAK
                ELSE
                    DISPLAY "Error: " + error_msg
                END IF
            UNTIL is_valid
            
            // Get First Name
            REPEAT
                PROMPT "Enter First Name"
                INPUT first_name
                
                (is_valid, error_msg) = CALL ValidateName(first_name)
                IF is_valid THEN
                    BREAK
                ELSE
                    DISPLAY "Error: " + error_msg
                END IF
            UNTIL is_valid
            
            // Get Last Name
            REPEAT
                PROMPT "Enter Last Name"
                INPUT last_name
                
                (is_valid, error_msg) = CALL ValidateName(last_name)
                IF is_valid THEN
                    BREAK
                ELSE
                    DISPLAY "Error: " + error_msg
                END IF
            UNTIL is_valid
            
            // Get Dependents
            REPEAT
                PROMPT "Enter Number of Dependents"
                INPUT dependents_input
                
                (is_valid, dependents, error_msg) = 
                    CALL ValidateDependents(dependents_input)
                IF is_valid THEN
                    BREAK
                ELSE
                    DISPLAY "Error: " + error_msg
                END IF
            UNTIL is_valid
            
            // Get Hours Worked
            REPEAT
                PROMPT "Enter Hours Worked"
                INPUT hours_input
                
                TRY
                    hours_worked = CONVERT hours_input TO FLOAT
                    (is_valid, error_msg) = 
                        CALL CalculationsModule.ValidateHours(hours_worked)
                    IF is_valid THEN
                        BREAK
                    ELSE
                        DISPLAY "Error: " + error_msg
                    END IF
                CATCH exception
                    DISPLAY "Error: Hours must be a valid number"
                END TRY
            UNTIL is_valid
            
            RETURN {
                'employee_id': employee_id,
                'first_name': first_name,
                'last_name': last_name,
                'dependents': dependents,
                'hours_worked': hours_worked
            }
        END
    END FUNCTION

    // Display payroll results
    FUNCTION DisplayPayrollResult(employee_info, payroll_data)
        BEGIN
            DISPLAY "PAYROLL CALCULATION RESULTS"
            DISPLAY "========================================"
            
            IF payroll_data['error'] == True THEN
                DISPLAY "Error: " + payroll_data['error_message']
                RETURN
            END IF
            
            DISPLAY "Employee ID: " + employee_info['employee_id']
            DISPLAY "Name: " + employee_info['first_name'] + " " + 
                    employee_info['last_name']
            DISPLAY "Dependents: " + employee_info['dependents']
            DISPLAY ""
            DISPLAY "Hours Worked: " + payroll_data['hours_worked']
            DISPLAY "  Regular Hours: " + payroll_data['regular_hours']
            DISPLAY "  Overtime Hours: " + payroll_data['overtime_hours']
            DISPLAY "Hourly Rate: $" + payroll_data['hourly_rate']
            DISPLAY ""
            DISPLAY "Regular Pay: $" + payroll_data['regular_pay']
            DISPLAY "Overtime Pay: $" + payroll_data['overtime_pay']
            DISPLAY "Gross Pay: $" + payroll_data['gross_pay']
            DISPLAY ""
            DISPLAY "State Tax (5.6%): $" + payroll_data['state_tax']
            DISPLAY "Federal Tax (7.9%): $" + payroll_data['federal_tax']
            DISPLAY "Total Tax: $" + payroll_data['total_tax']
            DISPLAY ""
            DISPLAY "NET PAY: $" + payroll_data['net_pay']
            DISPLAY "========================================"
        END
    END FUNCTION

    // Display main menu
    FUNCTION DisplayMenu()
        BEGIN
            DISPLAY "PAYROLL SYSTEM - THE PYTHONEX"
            DISPLAY "================================"
            DISPLAY "1. Enter Employee Data"
            DISPLAY "2. View All Employee Records"
            DISPLAY "3. Process All Employees"
            DISPLAY "4. Exit"
        END
    END FUNCTION

    // Display all employees
    FUNCTION DisplayAllEmployees()
        BEGIN
            employees = CALL DatabaseModule.GetAllEmployees()
            
            IF employees IS EMPTY THEN
                DISPLAY "No employees in database"
                RETURN
            END IF
            
            DISPLAY "ALL EMPLOYEE RECORDS"
            DISPLAY "========================================"
            
            FOR EACH (emp_id, emp_data) IN employees DO
                DISPLAY "Employee ID: " + emp_id
                DISPLAY "Name: " + emp_data['first_name'] + " " + 
                        emp_data['last_name']
                DISPLAY "Dependents: " + emp_data['dependents']
                DISPLAY "Hours Worked: " + emp_data['hours_worked']
                DISPLAY "Hourly Rate: $" + emp_data['hourly_rate']
                DISPLAY "----------------------------------------"
            END FOR
        END
    END FUNCTION

END MODULE
```

---

## Main Program Functions

```
// Save results to file
FUNCTION SaveResultsToFile(payroll_results, filename)
    BEGIN
        TRY
            OPEN filename FOR WRITING AS file
            
            WRITE "PAYROLL SYSTEM RESULTS" TO file
            WRITE "The Pythonex - SDEV 120 Group Project" TO file
            WRITE "Generated: " + CURRENT_DATETIME TO file
            WRITE "" TO file
            
            total_gross = 0
            total_net = 0
            total_tax = 0
            
            FOR EACH result IN payroll_results DO
                emp_info = result['employee_info']
                payroll = result['payroll_data']
                
                WRITE "Employee ID: " + emp_info['employee_id'] TO file
                WRITE "Name: " + emp_info['first_name'] + " " + 
                      emp_info['last_name'] TO file
                
                IF payroll['error'] == True THEN
                    WRITE "ERROR: " + payroll['error_message'] TO file
                    CONTINUE
                END IF
                
                WRITE "Hours Worked: " + payroll['hours_worked'] TO file
                WRITE "Gross Pay: $" + payroll['gross_pay'] TO file
                WRITE "Total Tax: $" + payroll['total_tax'] TO file
                WRITE "NET PAY: $" + payroll['net_pay'] TO file
                WRITE "" TO file
                
                total_gross = total_gross + payroll['gross_pay']
                total_net = total_net + payroll['net_pay']
                total_tax = total_tax + payroll['total_tax']
            END FOR
            
            WRITE "SUMMARY TOTALS" TO file
            WRITE "Total Gross Pay: $" + total_gross TO file
            WRITE "Total Tax Withheld: $" + total_tax TO file
            WRITE "Total Net Pay: $" + total_net TO file
            
            CLOSE file
            DISPLAY "Results saved to " + filename
            RETURN True
        CATCH exception
            DISPLAY "Error saving results: " + exception
            RETURN False
        END TRY
    END
END FUNCTION

// Process all employees
FUNCTION ProcessAllEmployees()
    BEGIN
        employees = CALL DatabaseModule.GetAllEmployees()
        
        IF employees IS EMPTY THEN
            DISPLAY "No employees to process"
            RETURN
        END IF
        
        DECLARE payroll_results AS LIST
        
        DISPLAY "PROCESSING ALL EMPLOYEES"
        
        FOR EACH (emp_id, emp_data) IN employees DO
            DISPLAY "Processing " + emp_data['first_name'] + " " + 
                    emp_data['last_name']
            
            hourly_rate = CALL DatabaseModule.GetPayRate(emp_id)
            
            payroll_data = CALL CalculationsModule.ProcessEmployeePayroll(
                emp_data['hours_worked'],
                hourly_rate
            )
            
            employee_info = {
                'employee_id': emp_id,
                'first_name': emp_data['first_name'],
                'last_name': emp_data['last_name'],
                'dependents': emp_data['dependents']
            }
            
            ADD {
                'employee_info': employee_info,
                'payroll_data': payroll_data
            } TO payroll_results
            
            CALL UIModule.DisplayPayrollResult(employee_info, payroll_data)
        END FOR
        
        CALL SaveResultsToFile(payroll_results, "payroll_results.txt")
        
        DISPLAY "Processed " + COUNT(payroll_results) + " employees"
    END
END FUNCTION

// Run interactive mode
FUNCTION RunInteractiveMode()
    BEGIN
        LOOP INDEFINITELY
            CALL UIModule.DisplayMenu()
            
            PROMPT "Enter your choice (1-4)"
            INPUT choice
            
            CASE choice OF
                1:  // Enter Employee Data
                    employee_info = CALL UIModule.GetEmployeeInput()
                    
                    IF employee_info IS None THEN
                        DISPLAY "Data entry cancelled"
                        CONTINUE
                    END IF
                    
                    CALL DatabaseModule.AddEmployee(
                        employee_info['employee_id'],
                        employee_info['first_name'],
                        employee_info['last_name'],
                        employee_info['dependents'],
                        employee_info['hours_worked']
                    )
                    
                    hourly_rate = CALL DatabaseModule.GetPayRate(
                        employee_info['employee_id']
                    )
                    
                    payroll_data = CALL CalculationsModule.ProcessEmployeePayroll(
                        employee_info['hours_worked'],
                        hourly_rate
                    )
                    
                    CALL UIModule.DisplayPayrollResult(employee_info, payroll_data)
                
                2:  // View All Employee Records
                    CALL UIModule.DisplayAllEmployees()
                
                3:  // Process All Employees
                    CALL ProcessAllEmployees()
                
                4:  // Exit
                    DISPLAY "Thank you for using The Pythonex Payroll System!"
                    EXIT LOOP
                
                DEFAULT:
                    DISPLAY "Invalid choice. Please enter 1, 2, 3, or 4"
            END CASE
        END LOOP
    END
END FUNCTION

// Load test data
FUNCTION LoadTestData()
    BEGIN
        DISPLAY "Loading test data..."
        
        test_employees = CALL TestData.GetTestEmployees()
        
        FOR EACH emp IN test_employees DO
            CALL DatabaseModule.AddEmployee(
                emp['employee_id'],
                emp['first_name'],
                emp['last_name'],
                emp['dependents'],
                emp['hours_worked']
            )
        END FOR
        
        DISPLAY "Loaded " + COUNT(test_employees) + " test employees"
    END
END FUNCTION
```

---

## Security Validation Pseudocode

```
// Comprehensive input validation
FUNCTION ValidateAllInputs(employee_id, first_name, last_name, dependents, hours)
    BEGIN
        errors = []
        
        // Validate Employee ID
        IF employee_id IS EMPTY OR LENGTH(employee_id) < 2 THEN
            ADD "Invalid Employee ID" TO errors
        END IF
        
        // Validate Names
        IF first_name IS EMPTY OR NOT IsValidName(first_name) THEN
            ADD "Invalid First Name" TO errors
        END IF
        
        IF last_name IS EMPTY OR NOT IsValidName(last_name) THEN
            ADD "Invalid Last Name" TO errors
        END IF
        
        // Validate Dependents
        IF dependents < 0 OR dependents > 20 THEN
            ADD "Invalid number of dependents" TO errors
        END IF
        
        // Validate Hours
        IF hours < 0 OR hours > MAX_HOURS_PER_WEEK THEN
            ADD "Invalid hours worked" TO errors
        END IF
        
        IF errors IS NOT EMPTY THEN
            RETURN (False, errors)
        ELSE
            RETURN (True, [])
        END IF
    END
END FUNCTION

// Check if name is valid
FUNCTION IsValidName(name)
    BEGIN
        FOR EACH character IN name DO
            IF NOT (IsLetter(character) OR character IN [' ', '-', "''"]) THEN
                RETURN False
            END IF
        END FOR
        RETURN True
    END
END FUNCTION
```

---

**Document Version:** 1.0  
**Last Updated:** November 14, 2024  
**Team:** The Pythonex
