"""
UI Module for Payroll System
The Pythonex - SDEV 120 Group Project
Handles user interface and data entry with validation
"""

import database_module
import calculations_module
import validation_module

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
        
        is_valid, error_msg = validation_module.validate_employee_id(employee_id)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate First Name
    while True:
        first_name = input("Enter First Name: ").strip()
        is_valid, error_msg = validation_module.validate_name(first_name)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate Last Name
    while True:
        last_name = input("Enter Last Name: ").strip()
        is_valid, error_msg = validation_module.validate_name(last_name)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate Number of Dependents
    while True:
        dependents_input = input("Enter Number of Dependents: ").strip()
        is_valid, dependents, error_msg = validation_module.validate_dependents(dependents_input)
        if is_valid:
            break
        print(f"Error: {error_msg}")
    
    # Get and validate Hours Worked
    while True:
        hours_input = input("Enter Hours Worked: ").strip()
        is_valid, hours_worked, error_msg = validation_module.validate_hours(hours_input)
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
