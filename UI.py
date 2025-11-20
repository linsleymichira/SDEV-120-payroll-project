# 
import database
import validation
import itertools

def PrintAllEmployeesMenu():
    employees = database.GetAllEmployees()
    print("Select Employee to view:")
    for employee in employees:
        print(f"{employee.EmployeeId}: {employee.FirstName} {employee.LastName}")
    isRunning = True
    while isRunning:
        choice = validation.GetValidEmployeeChoice("Please enter employee Id or -1 to return to main menu", employees)
        if choice == "-1":
            isRunning == False
        else:
            employee = list(filter(lambda x: int(x.EmployeeId) == choice, employees))[0]
            print(employee.ToRow())

EMPLOYEEOPTIONS = [
    ("View Employee Details", "test"),
    ("Update Employee Info", "test"),
    ("Update Employee Hours worked", "test"),
    ("Delete Employee", "test"),
]


def AddEmployee():
    print('Please enter details for employee')
    employee = database.Employee()
    employee.FirstName = validation.GetValidStringInput("Please enter first name: ", 50)
    employee.LastName = validation.GetValidStringInput("Please enter last name: ", 50)
    employee.NumOfDependents = validation.GetValidInt("Please enter number of dependents: ")
    employee.PayRate = validation.GetValidFloat("Please enter rate of pay: ")
    employee.HoursWorked = 0
    database.AddEmployee(employee)

MAINMENUOPTIONS = [
    ("View Employees", PrintAllEmployeesMenu),
    ("Add Employee", AddEmployee),
    ("Restart Week", "test"),
    ("Exit", "test")
]

def MainMenu():
    '''Responsible for displaying main menu of app'''
    isRunning = True
    while isRunning:
        print("Enter number and hit enter to select choice")
        for index, option in enumerate(MAINMENUOPTIONS):
            print(f'{index} {option[0]}')
        choice = validation.GetValidChoice("Please enter valid option: ", 0, len(MAINMENUOPTIONS))  
        if MAINMENUOPTIONS[choice][0] == "Exit":
            isRunning = False  
        MAINMENUOPTIONS[choice][1]()
    

