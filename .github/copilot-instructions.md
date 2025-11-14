# Copilot Instructions: SDEV-120 Payroll Project

This repo is a modular, console-based payroll system written in Python with clean separation of concerns and a small automated test harness.

## Big picture architecture
- Orchestration: `main.py` drives the app: prompts to load test data, menu loop, per-employee processing, and saving results to file.
- UI boundary: `ui_module.py` owns ALL user I/O and input validation (ID/name/dependents/hours). It prints results via `display_payroll_result`.
- Data layer: `database_module.py` is an in-memory store (`employee_database` dict) plus a pay rate lookup table (`pay_rates`). Unknown IDs fall back to $15.00.
- Business logic: `calculations_module.py` is pure computation (no I/O). It validates hours and computes regular/overtime, taxes (5.6% state, 7.9% federal), and net.
- Test data & demo: `test_data.py` provides 10 named scenarios (+ edge cases). `demo_run.py` loads them and writes `payroll_results_demo.txt`.

## Key contracts and data shapes
- Hours validation: `calculations_module.validate_hours(hours) -> (is_valid: bool, error_msg: str)`
- Core calculation: `process_employee_payroll(hours_worked: float, hourly_rate: float) -> dict`
  - On success, dict includes: `hours_worked, regular_hours, overtime_hours, hourly_rate, regular_pay, overtime_pay, gross_pay, state_tax, federal_tax, total_tax, net_pay, error=False`.
  - On failure (e.g., hours > 80), returns `{ 'error': True, 'error_message': str }`.
- File output: `main.save_results_to_file(results, filename)` writes a human-readable report and a summary block.

## How to run, test, and debug
- Run interactively: `python3 main.py` (choose to load test data; use menu options 1–4).
- Automated tests: `python3 run_tests.py` (runs validation, calculations, tax, overtime, DB, and 10 test-employee checks). Tests clear the in-memory database before use.
- Demo run: `python3 demo_run.py` (loads 10 test employees and writes `payroll_results_demo.txt`).

## Conventions and patterns
- Keep I/O out of business logic: all `print/input` lives in `ui_module.py`; calculations return data, not side effects.
- Validation layering: UI validates format (names/IDs/dependents) and converts types; calculations validate business rules (hours 0–80).
- Rates and defaults: edit pay rates in `database_module.pay_rates`; unknown IDs default to `15.00` and are copied into the employee record on add.
- Overtime rule: first 40 hours at 1.0×, remainder at 1.5× (`OVERTIME_MULTIPLIER`). Tax rates are module-level constants.
- Error-first flow: callers must check `result.get('error')` before reading amounts; UI already follows this pattern.

## Extension tips (follow these seams)
- New input fields (e.g., department):
  - Add validation + prompts in `ui_module`, store on `database_module.add_employee`, and thread through displays/file output.
- New pay logic (e.g., bonuses/deductions):
  - Extend `calculations_module` to compute new fields and include them in the returned dict; update `ui_module.display_payroll_result` and file writers in `main.py`/`demo_run.py`.
- Import/export:
  - CSV import: parse in a new helper (no external deps), call `database_module.add_employee` per row; reuse existing processing.

## Useful file references
- Menu/UI: `ui_module.py` (entry validation helpers: `validate_name`, `validate_employee_id`, `validate_dependents`, `validate_hours`).
- Core calc constants: `calculations_module.py` (`STATE_TAX_RATE`, `FEDERAL_TAX_RATE`, `REGULAR_HOURS`, `OVERTIME_MULTIPLIER`, `MAX_HOURS_PER_WEEK`).
- Rates + DB ops: `database_module.py` (`get_pay_rate`, `update_pay_rate`, `clear_database`).
- End-to-end flow + reporting: `main.py` (`process_all_employees`, `save_results_to_file`).
- Quick guide: `HOW_TO_RUN.md`; architecture docs: `README.md`, `PSEUDOCODE.md`, `FLOWCHART.md`.
