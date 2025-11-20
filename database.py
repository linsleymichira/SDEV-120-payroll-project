from typing import List
import os
import csv

class Employee:
    '''Class encapsulating a single row from database.py'''
    def __init__(self, row=[]):
        if(len(row) > 0):
            self.EmployeeId = row[0]
            self.FirstName = row[1]
            self.LastName = row[2]
            self.NumOfDependents = row[3]
            self.PayRate = row[4]
            self.HoursWorked = row[5]
        else:
            self.EmployeeId = ''
            self.FirstName = ''
            self.LastName = ''
            self.NumOfDependents = ''
            self.PayRate = ''
            self.HoursWorked = ''

    def ToRow(self):
        return f"{self.EmployeeId},{self.FirstName},{self.LastName},{self.NumOfDependents},{self.PayRate},{self.HoursWorked}\n"

DB = 'database.csv'

def UpdateFile(employees):
    with open(DB, 'w',) as file:
        for employee in employees:
            file.write(employee.ToRow())

def GetAllEmployees() -> List[Employee]:
    '''Get all employees in DB'''
    employees = []
    if os.path.getsize(DB) != 0:
        with open(DB, newline='') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                print(f"contents of row: {row}")
                print(f"rows type: {type(row)}")
                employees.append(Employee(row))
    return employees

def GetEmployee(employeeId):
    employees = GetAllEmployees()
    targetEmployee = next((Employee for obj in employees if obj.EmployeeId == employeeId))
    if targetEmployee != None:
        return targetEmployee
    else:
        raise IndexError('employee id not present')
    
def DeleteEmployee(employeeId):
    allEmployees = GetAllEmployees()
    employee = GetEmployee(employeeId)
    allEmployees.remove(employee)
    UpdateFile(allEmployees)

def AddEmployee(employee):
    allEmployees = GetAllEmployees()
    if len(allEmployees) < 0:
        maxId = max(allEmployees, key = lambda id: id.EmployeeId)
    else: 
        maxId = -1
    employee.EmployeeId = maxId + 1
    allEmployees.append(employee)
    UpdateFile(allEmployees)


