"""
Calculations Module for Payroll System
Handles all payroll calculations including gross pay, taxes, and net pay
"""

# Tax rates
STATE_TAX_RATE = 0.056  # 5.6%
FEDERAL_TAX_RATE = 0.079  # 7.9%

# Constants for pay calculations
REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5
MAX_HOURS_PER_WEEK = 80  # Maximum hours an employee can work


def validate_hours(hours_worked):
    """
    Validate that hours worked is within acceptable range
    
    Parameters:
        hours_worked (float): Hours worked
    
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if hours_worked < 0:
        return False, "Hours worked cannot be negative"
    
    if hours_worked > MAX_HOURS_PER_WEEK:
        return False, f"Hours worked exceeds maximum of {MAX_HOURS_PER_WEEK} hours per week"
    
    return True, ""


def calculate_gross_pay(hours_worked, hourly_rate):
    """
    Calculate gross pay including overtime
    Regular hours (up to 40): paid at regular rate
    Overtime hours (over 40): paid at 1.5x rate
    
    Parameters:
        hours_worked (float): Total hours worked
        hourly_rate (float): Regular hourly pay rate
    
    Returns:
        tuple: (float, float, float) - (gross_pay, regular_pay, overtime_pay)
    """
    # Validate hours
    is_valid, error_msg = validate_hours(hours_worked)
    if not is_valid:
        raise ValueError(error_msg)
    
    if hours_worked <= REGULAR_HOURS:
        # No overtime
        regular_pay = hours_worked * hourly_rate
        overtime_pay = 0.0
        gross_pay = regular_pay
    else:
        # Calculate overtime
        regular_pay = REGULAR_HOURS * hourly_rate
        overtime_hours = hours_worked - REGULAR_HOURS
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        gross_pay = regular_pay + overtime_pay
    
    return gross_pay, regular_pay, overtime_pay


def calculate_state_tax(gross_pay):
    """
    Calculate state tax at 5.6%
    
    Parameters:
        gross_pay (float): Gross pay amount
    
    Returns:
        float: State tax amount
    """
    return gross_pay * STATE_TAX_RATE


def calculate_federal_tax(gross_pay):
    """
    Calculate federal tax at 7.9%
    
    Parameters:
        gross_pay (float): Gross pay amount
    
    Returns:
        float: Federal tax amount
    """
    return gross_pay * FEDERAL_TAX_RATE


def calculate_total_tax(gross_pay):
    """
    Calculate total tax (state + federal)
    
    Parameters:
        gross_pay (float): Gross pay amount
    
    Returns:
        tuple: (float, float, float) - (total_tax, state_tax, federal_tax)
    """
    state_tax = calculate_state_tax(gross_pay)
    federal_tax = calculate_federal_tax(gross_pay)
    total_tax = state_tax + federal_tax
    
    return total_tax, state_tax, federal_tax


def calculate_net_pay(gross_pay):
    """
    Calculate net pay (gross pay - taxes)
    
    Parameters:
        gross_pay (float): Gross pay amount
    
    Returns:
        tuple: (float, float, float, float) - (net_pay, gross_pay, total_tax, state_tax, federal_tax)
    """
    total_tax, state_tax, federal_tax = calculate_total_tax(gross_pay)
    net_pay = gross_pay - total_tax
    
    return net_pay, gross_pay, total_tax, state_tax, federal_tax


def process_employee_payroll(hours_worked, hourly_rate):
    """
    Process complete payroll calculation for an employee
    
    Parameters:
        hours_worked (float): Hours worked
        hourly_rate (float): Hourly pay rate
    
    Returns:
        dict: Complete payroll information
    """
    # Validate hours
    is_valid, error_msg = validate_hours(hours_worked)
    if not is_valid:
        return {
            'error': True,
            'error_message': error_msg
        }
    
    # Calculate gross pay
    gross_pay, regular_pay, overtime_pay = calculate_gross_pay(hours_worked, hourly_rate)
    
    # Calculate taxes
    total_tax, state_tax, federal_tax = calculate_total_tax(gross_pay)
    
    # Calculate net pay
    net_pay = gross_pay - total_tax
    
    # Determine overtime hours
    overtime_hours = max(0, hours_worked - REGULAR_HOURS)
    regular_hours = min(hours_worked, REGULAR_HOURS)
    
    return {
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
