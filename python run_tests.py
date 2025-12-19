# ---------------------------------------------------------
# Automated Test Cases for Payroll Program
# The Code Calculators
# ---------------------------------------------------------

MAX_HOURS = 60

# -----------------------------
# Payroll Calculation Function
# -----------------------------
def calculate_pay(hours, rate):
    if hours <= 40:
        gross = hours * rate
    else:
        overtime_hours = hours - 40
        gross = (40 * rate) + (overtime_hours * rate * 1.5)

    state_tax = gross * 0.056
    federal_tax = gross * 0.079
    net_pay = gross - (state_tax + federal_tax)

    return gross, state_tax, federal_tax, net_pay


# -----------------------------
# Validation Function
# -----------------------------
def validate_data(first, last, emp_id, dependents, hours, rate):
    if not first or not last:
        return False, "Invalid name"

    if not emp_id.isalnum():
        return False, "Invalid employee ID"

    if dependents < 0:
        return False, "Dependents cannot be negative"

    if hours < 0 or hours > MAX_HOURS:
        return False, f"Hours must be between 0 and {MAX_HOURS}"

    if rate <= 0:
        return False, "Hourly rate must be positive"

    return True, "Valid"


# -----------------------------
# Ten Test Cases
# -----------------------------
test_cases = [
    ("John", "Doe", "A123", 2, 38, 20),
    ("Jane", "Smith", "B456", 1, 40, 22),
    ("Bob", "Lee", "C789", 3, 45, 18),
    ("Sarah", "King", "D101", 0, 52, 25),
    ("Mark", "Hill", "E202", 1, 60, 20),
    ("Invalid", "Hours", "F303", 2, 75, 20),
    ("Negative", "Hours", "G404", 1, -5, 19),
    ("Zero", "Case", "H505", 0, 0, 19),
    ("BadID", "Case", "###", 1, 30, 20),
    ("Missing", "", "I606", 1, 30, 20)
]


# -----------------------------
# Run All Test Cases
# -----------------------------
def run_tests():
    print("\n========== PAYROLL TEST RESULTS ==========\n")

    for i, case in enumerate(test_cases, start=1):
        first, last, emp_id, dependents, hours, rate = case

        print(f"Test Case {i}: {first} {last} (ID: {emp_id})")

        # Validate
        valid, message = validate_data(first, last, emp_id, dependents, hours, rate)
        if not valid:
            print(f"  ❌ FAILED VALIDATION: {message}\n")
            continue

        # Calculate payroll
        gross, state_tax, federal_tax, net_pay = calculate_pay(hours, rate)

        print(f"  ✔ Gross Pay: ${gross:.2f}")
        print(f"  ✔ State Tax: ${state_tax:.2f}")
        print(f"  ✔ Federal Tax: ${federal_tax:.2f}")
        print(f"  ✔ Net Pay: ${net_pay:.2f}\n")

    print("========== END OF TESTS ==========\n")


# Run the test suite
run_tests()
