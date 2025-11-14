# SDEV-120 Payroll Project
## The Pythonex - Group Payroll Management System

### Team Members
- **Linsley Michira** - Team Leader
- **Jacob Solomon** - Assistant & Testing Lead
- **Thaija Wilson** - Stenographer & Test Data Creation
- **Bran Mai Nhkum** - Developer
- **Elijah Penman** - Developer
- **Ronald Rudolph** - Developer

**Instructor:** Professor Carla Uycoque  
**Course:** SDEV 120  
**Institution:** Ivy Tech Community College

---

## Project Overview

This is a comprehensive payroll management system developed using Python. The system manages payroll for 10 employees with features including:

- Employee data entry and validation
- Gross pay calculation with overtime support
- Tax calculations (State and Federal)
- Net pay calculation
- File output for payroll results
- Comprehensive error checking and validation

---

## Features

### Core Functionality
- ✅ Employee data entry (ID, name, dependents, hours worked)
- ✅ Pay rate lookup from database
- ✅ Gross pay calculation (40 regular hours + overtime at 1.5x)
- ✅ Tax calculation (State 5.6%, Federal 7.9%)
- ✅ Net pay calculation
- ✅ Results display and file output

### Security & Validation
- ✅ Input validation for all fields
- ✅ Hours worked validation (0-80 hours)
- ✅ Name format validation
- ✅ Dependents validation (0-20)
- ✅ Error handling and user feedback

### Testing
- ✅ 10 comprehensive test cases
- ✅ Edge case testing
- ✅ Boundary testing
- ✅ Security validation testing

---

## System Architecture

The system is built with a modular architecture:

### Modules

1. **main.py** - Main program entry point
   - Orchestrates all modules
   - Handles user interaction flow
   - Manages file output

2. **database_module.py** - Data Management
   - Employee data storage
   - Pay rate lookup
   - Database operations

3. **calculations_module.py** - Business Logic
   - Gross pay calculations
   - Overtime calculations
   - Tax calculations
   - Net pay calculations
   - Hours validation

4. **ui_module.py** - User Interface
   - Data entry interface
   - Input validation
   - Results display
   - Menu system

5. **test_data.py** - Test Cases
   - 10 test employee records
   - Edge case scenarios
   - Testing utilities

---

## Installation & Requirements

### Prerequisites
- Python 3.x

### Installation
```bash
# Clone the repository
git clone https://github.com/linsleymichira/SDEV-120-payroll-project.git

# Navigate to project directory
cd SDEV-120-payroll-project

# Run the program
python main.py
```

No external dependencies required - uses only Python standard library.

---

## Usage

### Running the Program

```bash
python main.py
```

### Main Menu Options

1. **Enter Employee Data** - Add individual employee records
2. **View All Employee Records** - Display all stored employees
3. **Process All Employees** - Calculate payroll for all employees and save to file
4. **Exit** - Close the program

### Loading Test Data

When starting the program, you'll be prompted to load test data:
- Enter 'yes' to load 10 pre-configured test employees
- Enter 'no' to start with an empty database

### Output Files

- **payroll_results.txt** - Generated after processing all employees
  - Contains detailed payroll information for each employee
  - Includes summary totals

---

## Payroll Calculation Rules

### Regular Pay
- Hours 0-40: Paid at regular hourly rate

### Overtime Pay
- Hours over 40: Paid at 1.5x hourly rate
- Formula: `overtime_hours × hourly_rate × 1.5`

### Taxes
- **State Tax:** 5.6% of gross pay
- **Federal Tax:** 7.9% of gross pay
- **Total Tax:** State + Federal

### Net Pay
- **Formula:** `Gross Pay - Total Taxes`

### Validation Rules
- **Hours:** 0 to 80 hours per week
- **Dependents:** 0 to 20
- **Names:** Letters, spaces, hyphens, apostrophes only

---

## Test Employees

The system includes 10 pre-configured test employees:

| ID   | Name                  | Rate    | Test Scenario        |
|------|-----------------------|---------|----------------------|
| E001 | James Anderson        | $15.50  | Regular 40 hours     |
| E002 | Maria Garcia          | $18.75  | 45.5 hours           |
| E003 | Robert Johnson        | $22.00  | 50 hours             |
| E004 | Jennifer Williams     | $16.25  | Part-time 35 hours   |
| E005 | Michael Brown         | $20.00  | 48 hours             |
| E006 | Sarah Davis           | $19.50  | 42.5 hours           |
| E007 | David Martinez        | $17.80  | Part-time 38 hours   |
| E008 | Lisa Rodriguez        | $21.25  | 55 hours             |
| E009 | Christopher Wilson    | $14.50  | Part-time 20 hours   |
| E010 | Amanda Taylor         | $23.00  | 60 hours             |

---

## Documentation

- **PROJECT_PLAN.md** - Comprehensive project development plan
- **PSEUDOCODE.md** - Detailed pseudocode for all modules
- **TESTING_RESULTS.md** - Testing documentation and results
- **README.md** - This file

---

## Project Structure

```
SDEV-120-payroll-project/
│
├── main.py                    # Main program
├── database_module.py         # Database operations
├── calculations_module.py     # Payroll calculations
├── ui_module.py              # User interface
├── test_data.py              # Test data
├── payroll_results.txt       # Output file (generated)
│
├── PROJECT_PLAN.md           # Project plan
├── PSEUDOCODE.md             # Pseudocode documentation
├── TESTING_RESULTS.md        # Testing documentation
└── README.md                 # This file
```

---

## Standards Applied

### Code Standards
- Clear variable naming
- Comprehensive docstrings
- Modular design (3+ modules)
- Single responsibility principle
- Error handling
- Input validation

### Security Standards
- Input sanitization
- Boundary checking
- Type validation
- Error messages without sensitive info

### Testing Standards
- Unit testing
- Integration testing
- Boundary testing
- Edge case testing
- Security testing

---

## Example Output

```
PAYROLL CALCULATION RESULTS
============================================================
Employee ID: E001
Name: James Anderson
Dependents: 2

Hours Worked: 40.00
  Regular Hours: 40.00
  Overtime Hours: 0.00
Hourly Rate: $15.50

Regular Pay: $620.00
Overtime Pay: $0.00
Gross Pay: $620.00

State Tax (5.6%): $34.72
Federal Tax (7.9%): $48.98
Total Tax: $83.70

NET PAY: $536.30
============================================================
```

---

## Contributing

This is a group project for SDEV 120. Team members collaborate through:
- GitHub repository
- Weekly meetings (Sundays at 4pm)
- Email communication

---

## License

This project is for educational purposes as part of SDEV 120 coursework at Ivy Tech Community College.

---

## Contact

**Team Leader:** Linsley Michira  
**Course:** SDEV 120  
**Instructor:** Professor Carla Uycoque  
**Institution:** Ivy Tech Community College

---

## Acknowledgments

- Professor Carla Uycoque for guidance and instruction
- All team members for their contributions
- Ivy Tech Community College SDEV 120 program

---

**Last Updated:** November 14, 2024  
**Version:** 1.0
