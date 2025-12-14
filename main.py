"""
Main Payroll System Program
The Pythonex - SDEV 120 Group Project

Handles overall program flow and integrates modules.
"""

import database_module
import calculations_module
import validation_module
import test_data
from datetime import datetime
import pandas as pd


def save_results_to_file(payroll_results, filename="payroll_results.txt"):
    """
    Save payroll results to a file
    
    Parameters:
        payroll_results (list): List of payroll results
        filename (str): Output filename
    """
    try:
        with open(filename, 'w') as file:
            file.write("="*70 + "\n")
            file.write("PAYROLL SYSTEM RESULTS\n")
            file.write("The Pythonex - SDEV 120 Group Project\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*70 + "\n\n")
            
            total_gross = 0
            total_net = 0
            total_tax = 0
            
            for result in payroll_results:
                emp_info = result['employee_info']
                payroll = result['payroll_data']
                
                file.write("-"*70 + "\n")
                file.write(f"Employee ID: {emp_info['employee_id']}\n")
                file.write(f"Name: {emp_info['first_name']} {emp_info['last_name']}\n")
                file.write(f"Dependents: {emp_info['dependents']}\n")
                file.write(f"\n")
                
                if payroll.get('error'):
                    file.write(f"ERROR: {payroll.get('error_message')}\n")
                    file.write("-"*70 + "\n\n")
                    continue
                
                file.write(f"Hours Worked: {payroll['hours_worked']:.2f}\n")
                file.write(f"  Regular Hours: {payroll['regular_hours']:.2f}\n")
                file.write(f"  Overtime Hours: {payroll['overtime_hours']:.2f}\n")
                file.write(f"Hourly Rate: ${payroll['hourly_rate']:.2f}\n")
                file.write(f"\n")
                file.write(f"Regular Pay: ${payroll['regular_pay']:.2f}\n")
                file.write(f"Overtime Pay: ${payroll['overtime_pay']:.2f}\n")
                file.write(f"Gross Pay: ${payroll['gross_pay']:.2f}\n")
                file.write(f"\n")
                file.write(f"State Tax (5.6%): ${payroll['state_tax']:.2f}\n")
                file.write(f"Federal Tax (7.9%): ${payroll['federal_tax']:.2f}\n")
                file.write(f"Total Tax: ${payroll['total_tax']:.2f}\n")
                file.write(f"\n")
                file.write(f"NET PAY: ${payroll['net_pay']:.2f}\n")
                file.write("-"*70 + "\n\n")
                
                total_gross += payroll['gross_pay']
                total_net += payroll['net_pay']
                total_tax += payroll['total_tax']
            
            file.write("="*70 + "\n")
            file.write("SUMMARY TOTALS\n")
            file.write("="*70 + "\n")
            file.write(f"Total Gross Pay: ${total_gross:.2f}\n")
            file.write(f"Total Tax Withheld: ${total_tax:.2f}\n")
            file.write(f"Total Net Pay: ${total_net:.2f}\n")
            file.write(f"Number of Employees Processed: {len(payroll_results)}\n")
            file.write("="*70 + "\n")
        
        print(f"\nResults saved to {filename}")
        return True
    except (IOError, OSError) as e:
        print(f"Error saving results to file: {e}")
        return False


def process_all_employees():
    """
    Process payroll for all employees in database and save results
    """
    employees = database_module.get_all_employees()
    
    if not employees:
        print("\nNo employees to process.")
        return
    
    payroll_results = []
    
    print("\n" + "="*70)
    print("PROCESSING ALL EMPLOYEES")
    print("="*70)
    
    for emp_id, emp_data in employees.items():
        print(f"\nProcessing {emp_data['first_name']} {emp_data['last_name']}...")
        
        # Get pay rate from database
        hourly_rate = database_module.get_pay_rate(emp_id)
        
        # Calculate payroll
        payroll_data = calculations_module.process_employee_payroll(
            emp_data['hours_worked'],
            hourly_rate
        )
        
        # Store employee info
        employee_info = {
            'employee_id': emp_id,
            'first_name': emp_data['first_name'],
            'last_name': emp_data['last_name'],
            'dependents': emp_data['dependents']
        }
        
        payroll_results.append({
            'employee_info': employee_info,
            'payroll_data': payroll_data
        })
        
        # Display result
        ui_module.display_payroll_result(employee_info, payroll_data)
    
    # Save results to file
    save_results_to_file(payroll_results)
    
    print(f"\nProcessed {len(payroll_results)} employees.")


def load_test_data():
    """
    Load test employee data into the database
    """
    print("\nLoading test data...")
    test_employees = test_data.get_test_employees()
    
    for emp in test_employees:
        database_module.add_employee(
            emp['employee_id'],
            emp['first_name'],
            emp['last_name'],
            emp['dependents'],
            emp['hours_worked']
        )
    
    print(f"Loaded {len(test_employees)} test employees into database.")


def run_interactive_mode():
    """
    Run the payroll system in interactive mode
    """
    while True:
        ui_module.display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Enter employee data
            employee_info = ui_module.get_employee_input()
            
            if employee_info is None:
                print("Data entry cancelled.")
                continue
            
            # Add to database
            database_module.add_employee(
                employee_info['employee_id'],
                employee_info['first_name'],
                employee_info['last_name'],
                employee_info['dependents'],
                employee_info['hours_worked']
            )
            
            # Get pay rate
            hourly_rate = database_module.get_pay_rate(employee_info['employee_id'])
            
            # Calculate payroll
            payroll_data = calculations_module.process_employee_payroll(
                employee_info['hours_worked'],
                hourly_rate
            )
            
            # Display results
            ui_module.display_payroll_result(employee_info, payroll_data)
            
        elif choice == '2':
            # View all employee records
            ui_module.display_all_employees()
            
        elif choice == '3':
            # Process all employees
            process_all_employees()
            
        elif choice == '4':
            # Exit
            print("\nThank you for using The Pythonex Payroll System!")
            print("Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


def main():
    """
    Main program entry point
    """
    print("="*70)
    print("PAYROLL SYSTEM")
    print("="*70)
    
    # Ask if user wants to load test data
    print("\nWould you like to load the 10 test employees?")
    load_test = input("Enter 'yes' to load test data, or 'no' to start fresh: ").strip().lower()
    
    if load_test in ['yes', 'y']:
        load_test_data()
        test_data.print_test_summary()
    
    # Run interactive mode
    run_interactive_mode()


if __name__ == "__main__":
    main()
