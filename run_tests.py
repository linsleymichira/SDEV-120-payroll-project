"""
Automated Testing Script for Payroll System
The Pythonex - SDEV 120 Group Project
Testing Lead: Jacob Solomon
"""

import database_module
import calculations_module
import test_data


def test_calculations():
    """Test the calculations module"""
    print("\n" + "="*70)
    print("TESTING CALCULATIONS MODULE")
    print("="*70)
    
    test_cases = [
        # (hours, rate, expected_gross)
        (40.0, 15.50, 620.00),
        (45.5, 18.75, 904.69),
        (50.0, 22.00, 1210.00),
        (35.0, 16.25, 568.75),
        (0.0, 15.00, 0.00),
    ]
    
    passed = 0
    failed = 0
    
    for hours, rate, expected_gross in test_cases:
        result = calculations_module.process_employee_payroll(hours, rate)
        
        if result['error']:
            print(f"✗ FAILED: Hours={hours}, Rate=${rate} - Error: {result['error_message']}")
            failed += 1
        else:
            actual_gross = result['gross_pay']
            if abs(actual_gross - expected_gross) < 0.01:  # Allow small floating point difference
                print(f"✓ PASSED: Hours={hours}, Rate=${rate} - Gross=${actual_gross:.2f}")
                passed += 1
            else:
                print(f"✗ FAILED: Hours={hours}, Rate=${rate} - Expected ${expected_gross:.2f}, Got ${actual_gross:.2f}")
                failed += 1
    
    print(f"\nCalculations Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_validation():
    """Test input validation"""
    print("\n" + "="*70)
    print("TESTING VALIDATION")
    print("="*70)
    
    passed = 0
    failed = 0
    
    # Test valid hours
    is_valid, _ = calculations_module.validate_hours(40.0)
    if is_valid:
        print("✓ PASSED: Valid hours (40.0) accepted")
        passed += 1
    else:
        print("✗ FAILED: Valid hours (40.0) rejected")
        failed += 1
    
    # Test negative hours
    is_valid, _ = calculations_module.validate_hours(-10.0)
    if not is_valid:
        print("✓ PASSED: Negative hours (-10.0) rejected")
        passed += 1
    else:
        print("✗ FAILED: Negative hours (-10.0) accepted")
        failed += 1
    
    # Test excessive hours
    is_valid, _ = calculations_module.validate_hours(85.0)
    if not is_valid:
        print("✓ PASSED: Excessive hours (85.0) rejected")
        passed += 1
    else:
        print("✗ FAILED: Excessive hours (85.0) accepted")
        failed += 1
    
    # Test boundary (max hours)
    is_valid, _ = calculations_module.validate_hours(80.0)
    if is_valid:
        print("✓ PASSED: Boundary hours (80.0) accepted")
        passed += 1
    else:
        print("✗ FAILED: Boundary hours (80.0) rejected")
        failed += 1
    
    print(f"\nValidation Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_database():
    """Test database module"""
    print("\n" + "="*70)
    print("TESTING DATABASE MODULE")
    print("="*70)
    
    passed = 0
    failed = 0
    
    # Clear database
    database_module.clear_database()
    
    # Test add employee
    success = database_module.add_employee("TEST01", "Test", "User", 2, 40.0)
    if success:
        print("✓ PASSED: Employee added successfully")
        passed += 1
    else:
        print("✗ FAILED: Could not add employee")
        failed += 1
    
    # Test retrieve employee
    employee = database_module.get_employee("TEST01")
    if employee and employee['first_name'] == "Test":
        print("✓ PASSED: Employee retrieved successfully")
        passed += 1
    else:
        print("✗ FAILED: Could not retrieve employee")
        failed += 1
    
    # Test pay rate lookup
    rate = database_module.get_pay_rate("E001")
    if rate == 15.50:
        print(f"✓ PASSED: Pay rate lookup correct (${rate})")
        passed += 1
    else:
        print(f"✗ FAILED: Pay rate lookup incorrect (Expected $15.50, Got ${rate})")
        failed += 1
    
    # Test default rate for unknown employee
    rate = database_module.get_pay_rate("UNKNOWN")
    if rate == 15.00:
        print(f"✓ PASSED: Default pay rate returned (${rate})")
        passed += 1
    else:
        print(f"✗ FAILED: Default pay rate incorrect (Expected $15.00, Got ${rate})")
        failed += 1
    
    print(f"\nDatabase Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_tax_calculations():
    """Test tax calculation accuracy"""
    print("\n" + "="*70)
    print("TESTING TAX CALCULATIONS")
    print("="*70)
    
    passed = 0
    failed = 0
    
    # Test case: $1000 gross pay
    gross = 1000.00
    expected_state = 56.00  # 5.6%
    expected_federal = 79.00  # 7.9%
    expected_total = 135.00
    
    state_tax = calculations_module.calculate_state_tax(gross)
    federal_tax = calculations_module.calculate_federal_tax(gross)
    total_tax, _, _ = calculations_module.calculate_total_tax(gross)
    
    if abs(state_tax - expected_state) < 0.01:
        print(f"✓ PASSED: State tax correct (${state_tax:.2f})")
        passed += 1
    else:
        print(f"✗ FAILED: State tax incorrect (Expected ${expected_state:.2f}, Got ${state_tax:.2f})")
        failed += 1
    
    if abs(federal_tax - expected_federal) < 0.01:
        print(f"✓ PASSED: Federal tax correct (${federal_tax:.2f})")
        passed += 1
    else:
        print(f"✗ FAILED: Federal tax incorrect (Expected ${expected_federal:.2f}, Got ${federal_tax:.2f})")
        failed += 1
    
    if abs(total_tax - expected_total) < 0.01:
        print(f"✓ PASSED: Total tax correct (${total_tax:.2f})")
        passed += 1
    else:
        print(f"✗ FAILED: Total tax incorrect (Expected ${expected_total:.2f}, Got ${total_tax:.2f})")
        failed += 1
    
    print(f"\nTax Calculation Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_overtime_calculation():
    """Test overtime calculation accuracy"""
    print("\n" + "="*70)
    print("TESTING OVERTIME CALCULATIONS")
    print("="*70)
    
    passed = 0
    failed = 0
    
    # Test case: 50 hours at $20/hour
    # Regular: 40 × $20 = $800
    # Overtime: 10 × $20 × 1.5 = $300
    # Total: $1100
    
    result = calculations_module.process_employee_payroll(50.0, 20.00)
    
    if abs(result['regular_pay'] - 800.00) < 0.01:
        print(f"✓ PASSED: Regular pay correct (${result['regular_pay']:.2f})")
        passed += 1
    else:
        print(f"✗ FAILED: Regular pay incorrect (Expected $800.00, Got ${result['regular_pay']:.2f})")
        failed += 1
    
    if abs(result['overtime_pay'] - 300.00) < 0.01:
        print(f"✓ PASSED: Overtime pay correct (${result['overtime_pay']:.2f})")
        passed += 1
    else:
        print(f"✗ FAILED: Overtime pay incorrect (Expected $300.00, Got ${result['overtime_pay']:.2f})")
        failed += 1
    
    if abs(result['gross_pay'] - 1100.00) < 0.01:
        print(f"✓ PASSED: Gross pay correct (${result['gross_pay']:.2f})")
        passed += 1
    else:
        print(f"✗ FAILED: Gross pay incorrect (Expected $1100.00, Got ${result['gross_pay']:.2f})")
        failed += 1
    
    print(f"\nOvertime Calculation Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_with_test_data():
    """Test with the 10 test employee cases"""
    print("\n" + "="*70)
    print("TESTING WITH 10 EMPLOYEE TEST CASES")
    print("="*70)
    
    test_employees = test_data.get_test_employees()
    
    passed = 0
    failed = 0
    
    for emp in test_employees:
        emp_id = emp['employee_id']
        hours = emp['hours_worked']
        rate = database_module.get_pay_rate(emp_id)
        
        result = calculations_module.process_employee_payroll(hours, rate)
        
        if result['error']:
            print(f"✗ FAILED: {emp['first_name']} {emp['last_name']} - Error: {result['error_message']}")
            failed += 1
        else:
            print(f"✓ PASSED: {emp['first_name']} {emp['last_name']} - Net Pay: ${result['net_pay']:.2f}")
            passed += 1
    
    print(f"\nTest Data Tests: {passed} passed, {failed} failed")
    return passed, failed


def main():
    """Run all tests"""
    print("="*70)
    print("PAYROLL SYSTEM AUTOMATED TESTING")
    print("The Pythonex - SDEV 120 Group Project")
    print("Testing Lead: Jacob Solomon")
    print("="*70)
    
    total_passed = 0
    total_failed = 0
    
    # Run all test suites
    p, f = test_database()
    total_passed += p
    total_failed += f
    
    p, f = test_validation()
    total_passed += p
    total_failed += f
    
    p, f = test_calculations()
    total_passed += p
    total_failed += f
    
    p, f = test_tax_calculations()
    total_passed += p
    total_failed += f
    
    p, f = test_overtime_calculation()
    total_passed += p
    total_failed += f
    
    p, f = test_with_test_data()
    total_passed += p
    total_failed += f
    
    # Print summary
    print("\n" + "="*70)
    print("FINAL TEST SUMMARY")
    print("="*70)
    print(f"Total Tests Run: {total_passed + total_failed}")
    print(f"Tests Passed: {total_passed}")
    print(f"Tests Failed: {total_failed}")
    
    if total_failed == 0:
        print("\n✓ ALL TESTS PASSED! ✓")
        success_rate = 100.0
    else:
        success_rate = (total_passed / (total_passed + total_failed)) * 100
        print(f"\nSuccess Rate: {success_rate:.1f}%")
    
    print("="*70)
    
    return total_failed == 0


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
