"""
Test Data for Payroll System
The Pythonex - SDEV 120 Group Project
Contains 10 test cases with fake employee data
Created by: Thaija Wilson (Stenographer)
"""

# Test case data for 10 employees
test_employees = [
    {
        'employee_id': 'E001',
        'first_name': 'James',
        'last_name': 'Anderson',
        'dependents': 2,
        'hours_worked': 40.0,
        'description': 'Regular 40 hours - no overtime'
    },
    {
        'employee_id': 'E002',
        'first_name': 'Maria',
        'last_name': 'Garcia',
        'dependents': 3,
        'hours_worked': 45.5,
        'description': 'Regular + 5.5 hours overtime'
    },
    {
        'employee_id': 'E003',
        'first_name': 'Robert',
        'last_name': 'Johnson',
        'dependents': 1,
        'hours_worked': 50.0,
        'description': 'Regular + 10 hours overtime'
    },
    {
        'employee_id': 'E004',
        'first_name': 'Jennifer',
        'last_name': 'Williams',
        'dependents': 0,
        'hours_worked': 35.0,
        'description': 'Part-time - 35 hours'
    },
    {
        'employee_id': 'E005',
        'first_name': 'Michael',
        'last_name': 'Brown',
        'dependents': 4,
        'hours_worked': 48.0,
        'description': 'Regular + 8 hours overtime'
    },
    {
        'employee_id': 'E006',
        'first_name': 'Sarah',
        'last_name': 'Davis',
        'dependents': 2,
        'hours_worked': 42.5,
        'description': 'Regular + 2.5 hours overtime'
    },
    {
        'employee_id': 'E007',
        'first_name': 'David',
        'last_name': 'Martinez',
        'dependents': 1,
        'hours_worked': 38.0,
        'description': 'Part-time - 38 hours'
    },
    {
        'employee_id': 'E008',
        'first_name': 'Lisa',
        'last_name': 'Rodriguez',
        'dependents': 3,
        'hours_worked': 55.0,
        'description': 'Regular + 15 hours overtime'
    },
    {
        'employee_id': 'E009',
        'first_name': 'Christopher',
        'last_name': 'Wilson',
        'dependents': 0,
        'hours_worked': 20.0,
        'description': 'Part-time - 20 hours'
    },
    {
        'employee_id': 'E010',
        'first_name': 'Amanda',
        'last_name': 'Taylor',
        'dependents': 2,
        'hours_worked': 60.0,
        'description': 'Regular + 20 hours overtime (maximum recommended)'
    }
]


# Edge case test scenarios for validation testing
edge_case_tests = [
    {
        'employee_id': 'E999',
        'first_name': 'Test',
        'last_name': 'Case',
        'dependents': 0,
        'hours_worked': 0.0,
        'description': 'Zero hours worked - boundary test'
    },
    {
        'employee_id': 'E998',
        'first_name': 'Error',
        'last_name': 'Test',
        'dependents': 0,
        'hours_worked': 85.0,
        'description': 'Exceeds maximum hours (80) - should fail validation'
    },
    {
        'employee_id': 'E997',
        'first_name': 'Boundary',
        'last_name': 'Test',
        'dependents': 0,
        'hours_worked': 80.0,
        'description': 'Exactly at maximum hours (80) - boundary test'
    }
]


def get_test_employees():
    """
    Returns the list of test employees
    
    Returns:
        list: Test employee data
    """
    return test_employees


def get_edge_case_tests():
    """
    Returns edge case test scenarios
    
    Returns:
        list: Edge case test data
    """
    return edge_case_tests


def print_test_summary():
    """
    Print summary of all test cases
    """
    print("\n" + "="*70)
    print("TEST DATA SUMMARY - 10 EMPLOYEE TEST CASES")
    print("="*70)
    print("\nNormal Test Cases:")
    for i, emp in enumerate(test_employees, 1):
        print(f"\n{i}. {emp['first_name']} {emp['last_name']} (ID: {emp['employee_id']})")
        print(f"   Dependents: {emp['dependents']}, Hours: {emp['hours_worked']}")
        print(f"   Test Scenario: {emp['description']}")
    
    print("\n" + "="*70)
    print("EDGE CASE TEST SCENARIOS")
    print("="*70)
    for i, emp in enumerate(edge_case_tests, 1):
        print(f"\n{i}. {emp['first_name']} {emp['last_name']} (ID: {emp['employee_id']})")
        print(f"   Hours: {emp['hours_worked']}")
        print(f"   Test Scenario: {emp['description']}")
    
    print("\n" + "="*70)
