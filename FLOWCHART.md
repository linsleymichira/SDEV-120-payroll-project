# Payroll System Flowchart
## The Pythonex - SDEV 120 Group Project

---

## Main Program Flow

```
┌─────────────────────────────────────┐
│         START PROGRAM               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Display Welcome Message           │
│   & Team Information                │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Prompt: Load Test Data?           │
└──────────────┬──────────────────────┘
               │
        ┌──────┴──────┐
        │             │
      YES            NO
        │             │
        ▼             │
┌─────────────────┐   │
│  Load 10 Test   │   │
│  Employees      │   │
│  into Database  │   │
└────────┬────────┘   │
         │            │
         └─────┬──────┘
               │
               ▼
┌─────────────────────────────────────┐
│     Display Main Menu:              │
│     1. Enter Employee Data          │
│     2. View All Employees           │
│     3. Process All Employees        │
│     4. Exit                         │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────┴──────┐
        │             │
    User Choice       │
        │             │
   ┌────┼────┬────────┼───┐
   │    │    │        │   │
   1    2    3        4   Invalid
   │    │    │        │   │
   │    │    │        │   ▼
   │    │    │        │ Display Error
   │    │    │        │   │
   │    │    │        │   └──┐
   │    │    │        │      │
   │    │    │        ▼      │
   │    │    │    ┌────────────┐
   │    │    │    │   EXIT     │
   │    │    │    │  PROGRAM   │
   │    │    │    └────────────┘
   │    │    │
   │    │    ▼
   │    │ ┌───────────────────┐
   │    │ │ Process All       │
   │    │ │ Employees         │
   │    │ │ (See Detail Flow) │
   │    │ └────────┬──────────┘
   │    │          │
   │    ▼          │
   │ ┌───────────────────┐
   │ │ View All          │
   │ │ Employee Records  │
   │ │ (Display List)    │
   │ └────────┬──────────┘
   │          │
   ▼          │
┌───────────────────┐
│ Enter Employee    │
│ Data              │
│ (See Detail Flow) │
└────────┬──────────┘
         │
         └────────────────┐
                          │
         Loop back to menu│
         ◄────────────────┘
```

---

## Enter Employee Data Flow

```
┌─────────────────────────────────────┐
│   START: Enter Employee Data        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Prompt: Employee ID               │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────┴──────┐
        │  Validate   │
        │  Employee   │
        │     ID      │
        └──────┬──────┘
               │
        ┌──────┴──────┐
        │             │
     Valid        Invalid
        │             │
        │             ▼
        │      ┌──────────────┐
        │      │ Display Error│
        │      └──────┬───────┘
        │             │
        │             └────┐ Loop back
        │                  │
        ▼◄─────────────────┘
┌─────────────────────────────────────┐
│   Prompt: First Name                │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────┴──────┐
        │  Validate   │
        │    Name     │
        │   (Letters, │
        │   spaces,   │
        │   hyphens,  │
        │ apostrophes)│
        └──────┬──────┘
               │
        ┌──────┴──────┐
        │             │
     Valid        Invalid
        │             │
        │             ▼
        │      ┌──────────────┐
        │      │ Display Error│
        │      └──────┬───────┘
        │             │
        │             └────┐ Loop back
        │                  │
        ▼◄─────────────────┘
┌─────────────────────────────────────┐
│   Prompt: Last Name                 │
└──────────────┬──────────────────────┘
               │
               ▼
        [Same validation as First Name]
               │
               ▼
┌─────────────────────────────────────┐
│   Prompt: Number of Dependents      │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────┴──────┐
        │  Validate   │
        │  Dependents │
        │  (0-20)     │
        └──────┬──────┘
               │
        ┌──────┴──────┐
        │             │
     Valid        Invalid
        │             │
        │             ▼
        │      ┌──────────────┐
        │      │ Display Error│
        │      └──────┬───────┘
        │             │
        │             └────┐ Loop back
        │                  │
        ▼◄─────────────────┘
┌─────────────────────────────────────┐
│   Prompt: Hours Worked              │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────┴──────┐
        │  Validate   │
        │    Hours    │
        │   (0-80)    │
        └──────┬──────┘
               │
        ┌──────┴──────┐
        │             │
     Valid        Invalid
        │             │
        │             ▼
        │      ┌──────────────┐
        │      │ Display Error│
        │      └──────┬───────┘
        │             │
        │             └────┐ Loop back
        │                  │
        ▼◄─────────────────┘
┌─────────────────────────────────────┐
│   Add Employee to Database          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Look Up Hourly Rate from Database │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Calculate Payroll                 │
│   (See Calculation Flow)            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Display Results to User           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   RETURN to Main Menu               │
└─────────────────────────────────────┘
```

---

## Payroll Calculation Flow

```
┌─────────────────────────────────────┐
│   START: Calculate Payroll          │
│   Input: hours_worked, hourly_rate  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Validate Hours (0-80)             │
└──────────────┬──────────────────────┘
               │
        ┌──────┴──────┐
        │             │
     Valid        Invalid
        │             │
        │             ▼
        │      ┌──────────────┐
        │      │ Return ERROR │
        │      └──────────────┘
        │
        ▼
┌─────────────────────────────────────┐
│   Check: hours_worked <= 40?        │
└──────────────┬──────────────────────┘
               │
        ┌──────┴──────┐
        │             │
       YES            NO
   (No Overtime)  (Has Overtime)
        │             │
        ▼             ▼
┌──────────────┐  ┌──────────────────┐
│ regular_pay  │  │ regular_pay =    │
│ = hours ×    │  │   40 × rate      │
│   rate       │  │                  │
│              │  │ overtime_hours = │
│ overtime_pay │  │   hours - 40     │
│ = 0          │  │                  │
│              │  │ overtime_pay =   │
│ gross_pay =  │  │   overtime_hours │
│ regular_pay  │  │   × rate × 1.5   │
└──────┬───────┘  └──────┬───────────┘
       │                  │
       └────────┬─────────┘
                │
                ▼
┌─────────────────────────────────────┐
│   gross_pay = regular_pay +         │
│               overtime_pay          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Calculate State Tax               │
│   state_tax = gross_pay × 0.056     │
│   (5.6%)                            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Calculate Federal Tax             │
│   federal_tax = gross_pay × 0.079   │
│   (7.9%)                            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   total_tax = state_tax +           │
│               federal_tax           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   net_pay = gross_pay - total_tax   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Return Payroll Data:              │
│   - hours_worked                    │
│   - regular_hours, overtime_hours   │
│   - regular_pay, overtime_pay       │
│   - gross_pay                       │
│   - state_tax, federal_tax          │
│   - total_tax                       │
│   - net_pay                         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   END: Calculation Complete         │
└─────────────────────────────────────┘
```

---

## Process All Employees Flow

```
┌─────────────────────────────────────┐
│   START: Process All Employees      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Get All Employees from Database   │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────┴──────┐
        │  Database   │
        │   Empty?    │
        └──────┬──────┘
               │
        ┌──────┴──────┐
        │             │
       YES            NO
        │             │
        ▼             ▼
┌──────────────┐  ┌────────────────────┐
│ Display "No  │  │ Initialize:        │
│ employees"   │  │ - payroll_results  │
│              │  │ - total_gross = 0  │
│ RETURN       │  │ - total_net = 0    │
└──────────────┘  │ - total_tax = 0    │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ FOR EACH employee  │
                  │ in database:       │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Display: Processing│
                  │ [employee name]    │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Look up hourly rate│
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Calculate Payroll  │
                  │ (See Calc Flow)    │
                  └─────────┬──────────┘
                            │
                            ▼
                     ┌──────┴──────┐
                     │   Error?    │
                     └──────┬──────┘
                            │
                     ┌──────┴──────┐
                     │             │
                    YES            NO
                     │             │
                     ▼             ▼
              ┌──────────────┐ ┌──────────────────┐
              │Display Error │ │ Add to totals    │
              └──────┬───────┘ │ Display results  │
                     │         │ Store in list    │
                     │         └──────┬───────────┘
                     │                │
                     └────────┬───────┘
                              │
                              ▼
                     ┌────────────────┐
                     │ Next employee  │
                     └────────┬───────┘
                              │
                    ◄─────────┘ Loop
                              │
                              ▼
                  ┌────────────────────┐
                  │ All processed?     │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Display Summary:   │
                  │ - Total employees  │
                  │ - Total gross pay  │
                  │ - Total taxes      │
                  │ - Total net pay    │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Save Results to    │
                  │ payroll_results.txt│
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Display: File saved│
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ RETURN to Main Menu│
                  └────────────────────┘
```

---

## Input Validation Flow

```
┌─────────────────────────────────────┐
│   Input Validation Process          │
└─────────────────────────────────────┘

╔═══════════════════════════════════════╗
║        EMPLOYEE ID VALIDATION         ║
╚═══════════════════════════════════════╝
         │
         ▼
    ┌─────────┐
    │ Empty?  │ YES → ERROR: "Cannot be empty"
    └────┬────┘
         │ NO
         ▼
    ┌──────────┐
    │ Length   │ <2 → ERROR: "Must be 2+ chars"
    │ >= 2?    │
    └────┬─────┘
         │ YES
         ▼
    ┌─────────┐
    │ VALID   │
    └─────────┘

╔═══════════════════════════════════════╗
║          NAME VALIDATION              ║
╚═══════════════════════════════════════╝
         │
         ▼
    ┌─────────┐
    │ Empty?  │ YES → ERROR: "Cannot be empty"
    └────┬────┘
         │ NO
         ▼
    ┌──────────────┐
    │ Contains     │ YES → ERROR: "Invalid characters"
    │ invalid      │
    │ characters?  │
    └────┬─────────┘
         │ NO (only letters, spaces, -, ')
         ▼
    ┌─────────┐
    │ VALID   │
    └─────────┘

╔═══════════════════════════════════════╗
║       DEPENDENTS VALIDATION           ║
╚═══════════════════════════════════════╝
         │
         ▼
    ┌─────────┐
    │ Valid   │ NO → ERROR: "Must be a number"
    │ number? │
    └────┬────┘
         │ YES
         ▼
    ┌─────────┐
    │ < 0?    │ YES → ERROR: "Cannot be negative"
    └────┬────┘
         │ NO
         ▼
    ┌─────────┐
    │ > 20?   │ YES → ERROR: "Max 20 dependents"
    └────┬────┘
         │ NO
         ▼
    ┌─────────┐
    │ VALID   │
    └─────────┘

╔═══════════════════════════════════════╗
║         HOURS VALIDATION              ║
╚═══════════════════════════════════════╝
         │
         ▼
    ┌─────────┐
    │ Valid   │ NO → ERROR: "Must be a number"
    │ number? │
    └────┬────┘
         │ YES
         ▼
    ┌─────────┐
    │ < 0?    │ YES → ERROR: "Cannot be negative"
    └────┬────┘
         │ NO
         ▼
    ┌─────────┐
    │ > 80?   │ YES → ERROR: "Exceeds max hours"
    └────┬────┘
         │ NO
         ▼
    ┌─────────┐
    │ VALID   │
    └─────────┘
```

---

## Database Operations Flow

```
╔═══════════════════════════════════════╗
║         ADD EMPLOYEE                  ║
╚═══════════════════════════════════════╝
         │
         ▼
    ┌──────────────┐
    │ Look up pay  │
    │ rate for ID  │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Create       │
    │ employee     │
    │ record       │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Store in     │
    │ database     │
    │ dictionary   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Return       │
    │ SUCCESS      │
    └──────────────┘

╔═══════════════════════════════════════╗
║         GET EMPLOYEE                  ║
╚═══════════════════════════════════════╝
         │
         ▼
    ┌──────────────┐
    │ ID exists in │ NO → Return None
    │ database?    │
    └──────┬───────┘
           │ YES
           ▼
    ┌──────────────┐
    │ Return       │
    │ employee     │
    │ record       │
    └──────────────┘

╔═══════════════════════════════════════╗
║        GET PAY RATE                   ║
╚═══════════════════════════════════════╝
         │
         ▼
    ┌──────────────┐
    │ ID exists in │ NO → Return $15.00
    │ pay_rates?   │      (default)
    └──────┬───────┘
           │ YES
           ▼
    ┌──────────────┐
    │ Return       │
    │ pay rate     │
    └──────────────┘
```

---

**Document Version:** 1.0  
**Last Updated:** November 14, 2024  
**Team:** The Pythonex  
**Course:** SDEV 120 - Ivy Tech Community College
