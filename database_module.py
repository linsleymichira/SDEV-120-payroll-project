"""
Database Module for Payroll System
The Pythonex - SDEV 120 Group Project
Handles employee data storage and pay rate lookups
"""

# Employee database - stores employee information
employee_database = {}

# Pay rate lookup table - stores hourly rates by employee ID
pay_rates = {
    "E001": 15.50,
    "E002": 18.75,
    "E003": 22.00,
    "E004": 16.25,
    "E005": 20.00,
    "E006": 19.50,
    "E007": 17.80,
    "E008": 21.25,
    "E009": 14.50,
    "E010": 23.00
}


def add_employee(employee_id, first_name, last_name, dependents, hours_worked):
    """
    Add or update an employee in the database
    
    Parameters:
        employee_id (str): Unique employee identifier
        first_name (str): Employee's first name
        last_name (str): Employee's last name
        dependents (int): Number of dependents
        hours_worked (float): Hours worked in the period
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        employee_database[employee_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'dependents': dependents,
            'hours_worked': hours_worked,
            'hourly_rate': pay_rates.get(employee_id, 15.00)  # Default rate if not found
        }
        return True
    except Exception as e:
        print(f"Error adding employee: {e}")
        return False


def get_employee(employee_id):
    """
    Retrieve employee information from database
    
    Parameters:
        employee_id (str): Unique employee identifier
    
    Returns:
        dict: Employee information or None if not found
    """
    return employee_database.get(employee_id, None)


def get_pay_rate(employee_id):
    """
    Look up hourly pay rate for an employee
    
    Parameters:
        employee_id (str): Unique employee identifier
    
    Returns:
        float: Hourly pay rate or default rate of 15.00
    """
    return pay_rates.get(employee_id, 15.00)


def get_all_employees():
    """
    Retrieve all employees from database
    
    Returns:
        dict: All employee records
    """
    return employee_database


def update_pay_rate(employee_id, new_rate):
    """
    Update the hourly pay rate for an employee
    
    Parameters:
        employee_id (str): Unique employee identifier
        new_rate (float): New hourly pay rate
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if new_rate > 0:
            pay_rates[employee_id] = new_rate
            # Update in employee database if exists
            if employee_id in employee_database:
                employee_database[employee_id]['hourly_rate'] = new_rate
            return True
        return False
    except Exception as e:
        print(f"Error updating pay rate: {e}")
        return False


def clear_database():
    """
    Clear all employee data from database
    Used primarily for testing
    """
    global employee_database
    employee_database = {}
