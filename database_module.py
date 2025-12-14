import pandas as pd
import constants
import validation
import os

# Written by: Jacob Solomon

DATAFILE = 'test_data.csv'
UPDATEREQUEST = "Please enter new value for"
HOURREQUEST = "Please enter hours worked: "

def InitializeDatabase():
    if not os.path.isfile(DATAFILE):
        open(DATAFILE, 'x')

#region Update Employees
def UpdateEmployees(employees):
    # employees["pay"] = employees[Rate] * employees[hours worked] 
    employees.to_csv(DATAFILE, index=False)

def UpdateEmployeeDetails(index):
    employees = GetAllEmployees()
    values = []
    for col in employees.columns:
        request = f"{UPDATEREQUEST} {col} "
        if col in constants.INTOPTIONS:
            values.append(validation.GetInt(request))
        elif col in constants.FLOATOPTIONS:
            values.append(validation.GetFloat(request))
        elif col in constants.STRINGOPTIONS:
            values.append(input(request))
    values.append(values[len(values) - 1] * values[len(values) - 2])
    employees.loc[index] = values
    UpdateEmployees(employees)

def UpdateEmployeeHours(index):
    hours = validation.GetFloat(HOURREQUEST)
    employees = GetAllEmployees()
    employees.at[index, constants.HOURSWORKED] = hours
    UpdateEmployees(employees)

def ZeroAllEmployeesTime():
    employees = GetAllEmployees()
    employees.loc[employees["Hours Worked"] > 0, "Hours Worked"] = 0.0
    UpdateEmployees(employees)
#endregion

#region Delete Employees

def DeleteEmployee(index):
    employees = GetAllEmployees()
    employees.drop(labels=index, axis=0, inplace=True)
    UpdateEmployees(employees)

#endregion

#region Create Employees

def CreateEmployee():
    employees = GetAllEmployees()
    values = {}
    for col in employees.columns:
        request = f"{UPDATEREQUEST} {col} "
        if col in constants.INTOPTIONS:
            values[col] = [validation.GetInt(request)]
        elif col in constants.FLOATOPTIONS:
            values[col] = [validation.GetFloat(request)]
        elif col in constants.STRINGOPTIONS:
            values[col] = [input(request)]
    values[constants.PAY] = [values[constants.RATE][0] * values[constants.HOURSWORKED][0]]
    newEmployee = pd.DataFrame(values)
    updatedEmployees = pd.concat([employees, newEmployee], ignore_index=True)
    UpdateEmployees(updatedEmployees)

#endregion

#region Get Employees
def GetAllEmployees() -> pd.DataFrame:
    InitializeDatabase()
    return pd.read_csv(DATAFILE)

def GetEmployeeByIndex(index) -> pd.Series:
    return GetAllEmployees().iloc[index]

def SearchEmployeesByName(name):
    df = GetAllEmployees()
    return df.loc[df["First Name"].str.contains(name)]
#endregion
