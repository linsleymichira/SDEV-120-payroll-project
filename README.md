# SDEV-120-payroll-project

SDEV 120 Payroll Project

## Getting started with the project

### Preliminary

This guide assumes the reader has a very basic understanding of how to fork a branch to begin working on your code changes. If a refresher is needed, more information can be found at these links for using [GitHub tools](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo?tool=webui) or [VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview#_branches-and-tags).

### Pull Requests

Pull requests allow developers to request to merge their branch into another one, usually the main branch of the project. It is best practice to use pull requests to have a peer review your code changes. Since we're all on different schedules, using pull requests can help avoid merge conflicts as the branch you forked from initially might have had other branches merged into it before you created your pull request.

#### How to Create a Pull Request

1. Navigate to the project's [main page](https://github.com/linsleymichira/SDEV-120-payroll-project) on GitHub.
2. Select the ["Pull requests"](https://github.com/linsleymichira/SDEV-120-payroll-project/pulls) tab of the navigation bar at the top left side of the project's main page.
3. Select the green ["New pull request"](https://github.com/linsleymichira/SDEV-120-payroll-project/compare) on the pull requests page.
4. Select the base branch (the branch you want to merge in to) and select your branch as the compare branch and press "Create pull request".
5. From there fill out the form with a title and description for the pull request and press "Create pull request".
6. Once a reviewer has approved the pull request, click the "Merge pull request" button.

## Rough Draft Flow Chart

### Description

This is **not** designed as a hard plan that must be followed. This is a concept of how the application might work to help inspire the team if they find themselves stumped as they develop.

### Basic Design

The main.py module will be the entry point of the application, presenting all aspects of the UI and prompting users for input. The validations.py module takes the input from main.py and verifies the validity of the data, returning a boolean to the main.py if the data is valid. The database.py module will be responsible for reading and writing to the database.csv file, as well as handling the calculations for the application.

In the design it is assumed that options will be chosen via a number. The number could represent the index of the option or in some cases the ID of the employee a user wishes to interact with. In all cases there should be a way to back out to the prior menu or exit the application completely if on the main menu. With this being the case, a set amount of validation options would be helpful taking in user input and returning a bool determining if the input was valid or not

1. Validate Number
    1. Checks if value added was a number
2. Validate String
    1. Checks if input is a valid string
    2. Could set max char size to keep from invalid names being entered and save db resources


### Module Connections

``` mermaid
---
config:
  theme: dark
---
graph LR
    A[main.py] <--> B[validation.py]
    A <--> C[database.py]
    C <--> D[database.csv]
```

### Heirarchy

``` mermaid
---
config:
  theme: dark
---
graph LR
    Entry([Start]) --> Menu[[Print Main Menu]]
    Menu --> GetAll[[GetEmployees]]
    GetAll --> GetDetails[[GetEmployeeDetails]]
    GetAll --> UpdateInfo[[UpdateEmployeeInfo]]
    GetAll --> UpdateTime[[UpdateEmployeeTime]]
    GetAll --> Delete[[DeleteEmployee]]
    Menu --> Create[[AddEmployee]]
    Menu --> Optional[[ResetWeek -- Optional]]
    Menu --> Exit([Exit])
```

## Feature Explaination

### Get Employees

Reads the database and returns the Id, first name, and last name of the employee. After printing out all of the employees the user will be prompted to select an employee by Id or return to main menu. If the user selected an Id the user can choose whether they want to view the details of the employee, update their general info, update the hours worked, delete the employee, or return to the employee list.

### Get Employee By Id

Uses inputed employee to reveal all data for the employees record as well as their current gross and net pay. The user will have the option to return to the employee list.

### Update Employee general info

This feature will iterate through each column of the employee's record offering users to update any part of it.

### Update Employee time

This feature will prompt user to add a number for hours worked. It will take this number and add it to the current number of hours the employee has on their record.

### Delete Employee

This feature will remove the record with the coresponding employee Id provided. This feature could have a warning to let the user know this delete the whole record of the employee and ask if they are sure.

### Add Employee

This feature will add an employee record to the csv on a new line. The logic should ensure that the Id will be unique by checking the max Id already in the table and incrementing by one.

### Reset Week **Optional**

This feature will iterate through every employee record and reset their hours back to 0. This feature could have a warning to let the user know this will reset all hours and ask if they are sure.
