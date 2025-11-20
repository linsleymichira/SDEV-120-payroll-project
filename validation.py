import database

def GetValidStringInput(request, maxLength):
    isValid = False
    while isValid != True:
        value = input(request)
        if(len(value) <= maxLength):
            isValid = True
        else:
            print(f"Value too long, please enter value under {maxLength} characters.\n")
    return value


def GetValidInt(request):
    isValid = False
    while isValid != True:
        value = input(request)
        try:
            validValue = int(value)
            isValid = True
        except ValueError:
            print("Please enter valid int\n")
    return validValue
            

def GetValidFloat(request):
    isValid = False
    while isValid != True:
        value = input(request)
        try:
            validValue = float(value)
            return validValue
        except ValueError:
            print("Please enter valid int\n")

def GetValidChoice(request, min, max):
    isValid = False
    while isValid != True:
        value = GetValidInt(request)
        if (min <= value and value <= max):
            isValid = True
        else:
            print(f"please enter choice between {min} and {max}\n")
    return value

def GetValidEmployeeChoice(request, employees):
    isValid = False
    while isValid != True:
        value = input(request)
        if value == "-1":
            isValid = True
        else:
            try:
                print(employees)
                validValue = int(value)
                print(f"valid value: {validValue}")
                targetEmployee = filter(lambda x: int(x.EmployeeId) == validValue, employees)
                targetEmployee = list(targetEmployee)
                print(f"target employee: {targetEmployee}")
                
                if len(targetEmployee) == 1:
                    isValid = True
                    value = validValue
            except ValueError:
                print("Please enter valid int\n")
    return value
