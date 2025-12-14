# Payroll Precision Pro - Payroll Processing System
# Developed by: [The Pythonex]

# MODULE 1: Data Input & Validation
def get_employee_data():
    """Gets and validates employee data from user input"""
    print("\n=== Employee Data Entry ===")
    
    # Get basic employee information
    first_name = input("Enter employee first name: ").strip()
    last_name = input("Enter employee last name: ").strip()
    employee_id = input("Enter employee ID: ").strip()
    
    # Security: Input validation for hours worked
    max_hours = 80
    while True:
        try:
            hours_worked = float(input("Enter hours worked (0 - 80): "))
            if hours_worked < 0 or hours_worked > max_hours:
                print(f"Error: Hours must be between 0 and {max_hours}.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number for hours worked.")
    
    # Security: Input validation for pay rate
    while True:
        try:
            pay_rate = float(input("Enter hourly pay rate: $"))
            if pay_rate < 0:
                print("Error: Pay rate cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number for pay rate.")
    
    # Security: Input validation for dependents
    while True:
        try:
            dependents = int(input("Enter number of dependents: "))
            if dependents < 0:
                print("Error: Number of dependents cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid whole number for dependents.")
    
    return {
        'first_name': first_name,
        'last_name': last_name,
        'employee_id': employee_id,
        'hours_worked': hours_worked,
        'pay_rate': pay_rate,
        'dependents': dependents
    }

# MODULE 2: Payroll Calculations
def calculate_payroll(hours_worked, pay_rate):
    """Calculates all payroll components"""
    # Calculate regular and overtime hours
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
    
    # Calculate pay components
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
    
    # Calculate taxes
    state_tax = gross_pay * 0.056
    federal_tax = gross_pay * 0.079
    net_pay = gross_pay - state_tax - federal_tax
    
    return {
        'regular_hours': regular_hours,
        'overtime_hours': overtime_hours,
        'regular_pay': regular_pay,
        'overtime_pay': overtime_pay,
        'gross_pay': gross_pay,
        'state_tax': state_tax,
        'federal_tax': federal_tax,
        'net_pay': net_pay
    }

# MODULE 3: Output & Data Management
def display_employee_payroll(employee_data, payroll_data):
    """Displays payroll summary to the user"""
    print("\n" + "=" * 50)
    print("PAYROLL SUMMARY")
    print("=" * 50)
    print(f"Employee: {employee_data['first_name']} {employee_data['last_name']}")
    print(f"ID: {employee_data['employee_id']}")
    print(f"Dependents: {employee_data['dependents']}")
    print(f"Hours Worked: {employee_data['hours_worked']}")
    print(f"Regular Hours: {payroll_data['regular_hours']}")
    print(f"Overtime Hours: {payroll_data['overtime_hours']}")
    print("-" * 50)
    print(f"Regular Pay: ${payroll_data['regular_pay']:.2f}")
    print(f"Overtime Pay: ${payroll_data['overtime_pay']:.2f}")
    print(f"Gross Pay: ${payroll_data['gross_pay']:.2f}")
    print(f"State Tax (5.6%): ${payroll_data['state_tax']:.2f}")
    print(f"Federal Tax (7.9%): ${payroll_data['federal_tax']:.2f}")
    print("-" * 50)
    print(f"NET PAY: ${payroll_data['net_pay']:.2f}")
    print("=" * 50)

def save_to_file(employee_record):
    """Saves employee payroll record to a file"""
    try:
        with open("payroll_results.txt", "a") as file:
            file.write("Employee Record\n")
            file.write("-" * 30 + "\n")
            file.write(f"Name: {employee_record['first_name']} {employee_record['last_name']}\n")
            file.write(f"ID: {employee_record['employee_id']}\n")
            file.write(f"Hours: {employee_record['hours_worked']}\n")
            file.write(f"Rate: ${employee_record['pay_rate']:.2f}\n")
            file.write(f"Gross Pay: ${employee_record['gross_pay']:.2f}\n")
            file.write(f"Net Pay: ${employee_record['net_pay']:.2f}\n")
            file.write("-" * 30 + "\n\n")
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

# MAIN PROGRAM LOGIC
def main():
    """Main program function"""
    print("Welcome to Payroll Precision Pro!")
    print("=================================")
    
    # Initialize employee list
    employee_payroll_list = []
    
    # Main program loop
    while True:
        # Get employee data
        emp_data = get_employee_data()
        
        # Calculate payroll
        pay_data = calculate_payroll(emp_data['hours_worked'], emp_data['pay_rate'])
        
        # Combine all data into a single record
        employee_record = {**emp_data, **pay_data}
        employee_payroll_list.append(employee_record)
        
        # Display results
        display_employee_payroll(emp_data, pay_data)
        
        # Save to file
        if save_to_file(employee_record):
            print("Payroll record saved to 'payroll_results.txt'")
        
        # Ask if user wants to process another employee
        another = input("\nProcess another employee? (y/n): ").lower().strip()
        if another != 'y':
            break
    
    # Display summary
    print(f"\nProcessing complete. Total employees processed: {len(employee_payroll_list)}")
    print("Thank you for using Payroll Precision Pro!")

# Run the program
if __name__ == "__main__":
    main()
