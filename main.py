import database
import sys
import os
import validation 
import constants
## Linsley Michira - main.py run & build
#region General Purpose

LEAVECONIDITION = -1
CLEAR = 'cls'

def PrintMenu(menu):
    for index, option in enumerate(menu):
        print(f"{index}) {option[0]}")  

def ClearScreen():
    os.system(CLEAR)

#endregion

#region Employee Menu
CONTINUEMESSAGE = "Press enter to continue"
PICKEMPLOYEEREQUEST = f"Please select an employee or enter {LEAVECONIDITION} to go back: "
EMPLOYEEMENUREQUEST = f"Please select an option or enter {LEAVECONIDITION} to go back: "
QUICKVIEWCOLUMNS = [constants.FIRSTNAME, constants.LASTNAME, constants.HOURSWORKED]

def ViewEmployeeDetails(index):
    ClearScreen()
    print(database.GetEmployeeByIndex(index))
    option = input(CONTINUEMESSAGE)

EMPLOYEEMENU = [
    ["View Employee Details", ViewEmployeeDetails],
    ["Update Employee Details", database.UpdateEmployeeDetails],
    ["Update Hours Worked", database.UpdateEmployeeHours],
    ["Delete Employee", database.DeleteEmployee]
]

def EmployeeMenu(employee, index):
    ClearScreen()
    print(employee[QUICKVIEWCOLUMNS])
    isRunning = True
    while isRunning:
        PrintMenu(EMPLOYEEMENU)
        option = validation.GetIntInRange(EMPLOYEEMENUREQUEST, -1, len(EMPLOYEEMENU) - 1)
        if option == LEAVECONIDITION:
            isRunning = False
        elif EMPLOYEEMENU[option][0] == "Delete Employee":
            EMPLOYEEMENU[option][1](index)
            ClearScreen()
            isRunning = False
        else:
            EMPLOYEEMENU[option][1](index)
            ClearScreen()

def AllEmployeesMenu():
    ClearScreen()
    employees = database.GetAllEmployees()
    print(employees[QUICKVIEWCOLUMNS])
    option = validation.GetIntInRange(PICKEMPLOYEEREQUEST, LEAVECONIDITION, len(employees) - 1)
    if option != -1:
        EmployeeMenu(employees.iloc[option], option)
#endregion
    
#region Main Menu

MAINMENUREQUEST = "Please select an option: "
MAINMENU = [
    ["View All Employees", AllEmployeesMenu],
    ["Restart work week", database.ZeroAllEmployeesTime],
    ["Add new employee", database.CreateEmployee],
    ["Leave", sys.exit]
]

def MainMenu():
    while True:
        ClearScreen()
        PrintMenu(MAINMENU)
        option = validation.GetIntInRange(MAINMENUREQUEST, 0, len(MAINMENU) - 1)
        MAINMENU[option][1]()

#endregion
      

MainMenu()