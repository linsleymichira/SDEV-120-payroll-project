"""
UI Module for Payroll System
The Pythonex - SDEV 120 Group Project
Handles user interface and data entry with validation
"""

import database_module
import calculations_module


def validate_name(name):
    """
    Validate that name is not empty and contains only letters and spaces
    
    Parameters:
        name (str): Name to validate
    
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Name cannot be empty"
    
    # Check if name contains only letters, spaces, hyphens, and apostrophes
    if not all(c.isalpha() or c in " -'" for c in name):
        return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
    
    return True, ""


def validate_employee_id(employee_id):
    """
    Validate employee ID format
    
    Parameters:
        employee_id (str): Employee ID to validate
    
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not employee_id or not employee_id.strip():
        return False, "Employee ID cannot be empty"
    
    # Check if ID follows format (e.g., E001)
    if not (employee_id.startswith('E') and len(employee_id) == 4 and employee_id[1:].isdigit()):
        return False, "Employee ID must follow the format 'E' followed by 3 digits (e.g., E001)."
    
    return True, ""


def validate_dependents(dependents):
    """
    Validate number of dependents
    
    Parameters:
        dependents: Number of dependents (can be string or int)
    
    Returns:
        tuple: (bool, int, str) - (is_valid, dependents_value, error_message)
    """
    try:
        deps = int(dependents)
        if deps < 0:
            return False, 0, "Number of dependents cannot be negative"
        if deps > 20:
            return False, 0, "Number of dependents seems unusually high (max 20)"
        return True, deps, ""
    except ValueError:
        return False, 0, "Number of dependents must be a valid number"


def validate_hours(hours):
    """
    Validate hours worked
    
    Parameters:
        hours: Hours worked (can be string or float)
    
    Returns:
        tuple: (bool, float, str) - (is_valid, hours_value, error_message)
    """
    try:
        hrs = float(hours)
        is_valid, error_msg = calculations_module.validate_hours(hrs)
        if not is_valid:
            return False, 0.0, error_msg
        return True, hrs, ""
    except ValueError:
        return False, 0.0, "Hours worked must be a valid number"


def get_employee_input():
    """
    Get employee information from user input with validation
    
    Returns:
        dict: Employee information or None if cancelled
    """
    print("\n" + "="*60)
    print("EMPLOYEE DATA ENTRY")
    print("="*60)
    
    # Get and validate Employee ID
    while True:
        employee_id = input("\nEnter Employee ID (e.g., E001) or 'quit' to exit: ").strip()
        if employee_id.lower() == 'quit':
            return None
        
        is_valid, error_msg = validate_employee_id(employee_id)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate First Name
    while True:
        first_name = input("Enter First Name: ").strip()
        is_valid, error_msg = validate_name(first_name)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate Last Name
    while True:
        last_name = input("Enter Last Name: ").strip()
        is_valid, error_msg = validate_name(last_name)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate Number of Dependents
    while True:
        dependents_input = input("Enter Number of Dependents: ").strip()
        is_valid, dependents, error_msg = validate_dependents(dependents_input)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate Hours Worked
    while True:
        hours_input = input("Enter Hours Worked: ").strip()
        is_valid, hours_worked, error_msg = validate_hours(hours_input)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    return {
        'employee_id': employee_id,
        'first_name': first_name,
        'last_name': last_name,
        'dependents': dependents,
        'hours_worked': hours_worked
    }


def display_payroll_result(employee_info, payroll_data):
    """
    Display payroll calculation results
    
    Parameters:
        employee_info (dict): Employee information
        payroll_data (dict): Payroll calculation results
    """
    print("\n" + "="*60)
    print("PAYROLL CALCULATION RESULTS")
    print("="*60)
    
    if payroll_data.get('error'):
        print(f"\nError: {payroll_data.get('error_message')}")
        return
    
    print(f"\nEmployee ID: {employee_info['employee_id']}")
    print(f"Name: {employee_info['first_name']} {employee_info['last_name']}")
    print(f"Dependents: {employee_info['dependents']}")
    print(f"\n{'-'*60}")
    print(f"Hours Worked: {payroll_data['hours_worked']:.2f}")
    print(f"  Regular Hours: {payroll_data['regular_hours']:.2f}")
    print(f"  Overtime Hours: {payroll_data['overtime_hours']:.2f}")
    print(f"Hourly Rate: ${payroll_data['hourly_rate']:.2f}")
    print(f"\n{'-'*60}")
    print(f"Regular Pay: ${payroll_data['regular_pay']:.2f}")
    print(f"Overtime Pay: ${payroll_data['overtime_pay']:.2f}")
    print(f"Gross Pay: ${payroll_data['gross_pay']:.2f}")
    print(f"\n{'-'*60}")
    print(f"State Tax (5.6%): ${payroll_data['state_tax']:.2f}")
    print(f"Federal Tax (7.9%): ${payroll_data['federal_tax']:.2f}")
    print(f"Total Tax: ${payroll_data['total_tax']:.2f}")
    print(f"\n{'-'*60}")
    print(f"NET PAY: ${payroll_data['net_pay']:.2f}")
    print("="*60)


def display_menu():
    """
    Display main menu options
    """
    print("\n" + "="*60)
    print("PAYROLL SYSTEM - THE PYTHONEX")
    print("="*60)
    print("\n1. Enter Employee Data")
    print("2. View All Employee Records")
    print("3. Process All Employees")
    print("4. Exit")
    print("\n" + "="*60)


def display_all_employees():
    """
    Display all employees in the database
    """
    employees = database_module.get_all_employees()
    
    if not employees:
        print("\nNo employees in database.")
        return
    
    print("\n" + "="*60)
    print("ALL EMPLOYEE RECORDS")
    print("="*60)
    
    for emp_id, emp_data in employees.items():
        print(f"\nEmployee ID: {emp_id}")
        print(f"Name: {emp_data['first_name']} {emp_data['last_name']}")
        print(f"Dependents: {emp_data['dependents']}")
        print(f"Hours Worked: {emp_data['hours_worked']:.2f}")
        print(f"Hourly Rate: ${emp_data['hourly_rate']:.2f}")
        print("-"*60)
