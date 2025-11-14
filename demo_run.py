"""
Demo Run of Payroll System
Demonstrates the system with test data
"""

import database_module
import calculations_module
import test_data
from datetime import datetime


def demo_run():
    """Run a demonstration of the payroll system"""
    print("="*70)
    print("PAYROLL SYSTEM DEMONSTRATION")
    print("The Pythonex - SDEV 120 Group Project")
    print("="*70)
    
    # Load test data
    print("\nLoading test employees...")
    test_employees = test_data.get_test_employees()
    
    for emp in test_employees:
        database_module.add_employee(
            emp['employee_id'],
            emp['first_name'],
            emp['last_name'],
            emp['dependents'],
            emp['hours_worked']
        )
    
    print(f"Loaded {len(test_employees)} test employees.")
    
    # Process all employees
    print("\n" + "="*70)
    print("PROCESSING ALL EMPLOYEES")
    print("="*70)
    
    payroll_results = []
    total_gross = 0
    total_net = 0
    total_tax = 0
    
    for emp_id, emp_data in database_module.get_all_employees().items():
        print(f"\nProcessing {emp_data['first_name']} {emp_data['last_name']}...")
        
        # Get pay rate
        hourly_rate = database_module.get_pay_rate(emp_id)
        
        # Calculate payroll
        payroll_data = calculations_module.process_employee_payroll(
            emp_data['hours_worked'],
            hourly_rate
        )
        
        if not payroll_data['error']:
            print(f"  Hours: {payroll_data['hours_worked']:.2f} " +
                  f"(Regular: {payroll_data['regular_hours']:.2f}, " +
                  f"Overtime: {payroll_data['overtime_hours']:.2f})")
            print(f"  Gross Pay: ${payroll_data['gross_pay']:.2f}")
            print(f"  Total Tax: ${payroll_data['total_tax']:.2f}")
            print(f"  Net Pay: ${payroll_data['net_pay']:.2f}")
            
            total_gross += payroll_data['gross_pay']
            total_net += payroll_data['net_pay']
            total_tax += payroll_data['total_tax']
            
            payroll_results.append({
                'employee_info': {
                    'employee_id': emp_id,
                    'first_name': emp_data['first_name'],
                    'last_name': emp_data['last_name'],
                    'dependents': emp_data['dependents']
                },
                'payroll_data': payroll_data
            })
        else:
            print(f"  ERROR: {payroll_data['error_message']}")
    
    # Display summary
    print("\n" + "="*70)
    print("PAYROLL SUMMARY")
    print("="*70)
    print(f"Total Employees Processed: {len(payroll_results)}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total Tax Withheld: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net:.2f}")
    print("="*70)
    
    # Save to file
    print("\nSaving results to payroll_results_demo.txt...")
    
    try:
        with open('payroll_results_demo.txt', 'w') as file:
            file.write("="*70 + "\n")
            file.write("PAYROLL SYSTEM RESULTS - DEMONSTRATION\n")
            file.write("The Pythonex - SDEV 120 Group Project\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*70 + "\n\n")
            
            for result in payroll_results:
                emp_info = result['employee_info']
                payroll = result['payroll_data']
                
                file.write("-"*70 + "\n")
                file.write(f"Employee ID: {emp_info['employee_id']}\n")
                file.write(f"Name: {emp_info['first_name']} {emp_info['last_name']}\n")
                file.write(f"Dependents: {emp_info['dependents']}\n\n")
                file.write(f"Hours Worked: {payroll['hours_worked']:.2f}\n")
                file.write(f"  Regular Hours: {payroll['regular_hours']:.2f}\n")
                file.write(f"  Overtime Hours: {payroll['overtime_hours']:.2f}\n")
                file.write(f"Hourly Rate: ${payroll['hourly_rate']:.2f}\n\n")
                file.write(f"Regular Pay: ${payroll['regular_pay']:.2f}\n")
                file.write(f"Overtime Pay: ${payroll['overtime_pay']:.2f}\n")
                file.write(f"Gross Pay: ${payroll['gross_pay']:.2f}\n\n")
                file.write(f"State Tax (5.6%): ${payroll['state_tax']:.2f}\n")
                file.write(f"Federal Tax (7.9%): ${payroll['federal_tax']:.2f}\n")
                file.write(f"Total Tax: ${payroll['total_tax']:.2f}\n\n")
                file.write(f"NET PAY: ${payroll['net_pay']:.2f}\n")
                file.write("-"*70 + "\n\n")
            
            file.write("="*70 + "\n")
            file.write("SUMMARY TOTALS\n")
            file.write("="*70 + "\n")
            file.write(f"Total Gross Pay: ${total_gross:.2f}\n")
            file.write(f"Total Tax Withheld: ${total_tax:.2f}\n")
            file.write(f"Total Net Pay: ${total_net:.2f}\n")
            file.write(f"Number of Employees Processed: {len(payroll_results)}\n")
            file.write("="*70 + "\n")
        
        print("✓ Results saved successfully!")
    except Exception as e:
        print(f"✗ Error saving results: {e}")
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)


if __name__ == "__main__":
    demo_run()
