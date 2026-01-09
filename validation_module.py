import database_module
import calculations_module


def InRange(value, min, max) -> bool:
    '''Determines if int is within acceptible range'''
    return min <= value & value <= max

def GetInt(message) -> int: 
    '''Gets int from user input, looping until valid int is entered'''
    isPrompting = True
    while isPrompting:
        try:
            value = int(input(message))
            isPrompting = False
        except:
            print("Please enter valid int")
    return value

def GetIntInRange(message, min, max) -> int:
    '''Gets int from user input, looping until valid int is entered, ensures the int is within range'''
    isPrompting = True
    while isPrompting:
        try:
            value = int(input(message))
            if not InRange(value, min, max):
                raise Exception()
            isPrompting = False
        except:
            print(f"Please enter valid int between {min} and {max}")
    return value

def GetIntFromList(message, numbers) -> int:
    '''Gets int from user input, looping until valid int is entered, ensures int is option within numbers list'''
    isPrompting = True
    while isPrompting:
        try:
            value = int(input(message))
            if not value in numbers:
                raise Exception()
            isPrompting = False
        except:
            print(f"Please enter valid int between {min} and {max}")
    return value

def GetFloat(message) -> int: 
    '''Gets float from user input, looping until valid float is entered'''
    isPrompting = True
    while isPrompting:
        try:
            value = float(input(message))
            isPrompting = False
        except:
            print("Please enter valid int")
    return value


def validate_name(name):
    """
    Validate that name is not empty and contains only letters, spaces, hyphens, and apostrophes
    
    Parameters:
        name (str): Name to validate
    
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Name cannot be empty"
    
    # Check if name contains only letters, spaces, hyphens, and apostrophes
    if not all(c.isalpha() or c in " -'" for c in name):
        return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
    
    return True, ""


def validate_employee_id(employee_id):
    """
    Validate employee ID format
    
    Parameters:
        employee_id (str): Employee ID to validate
    
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not employee_id or not employee_id.strip():
        return False, "Employee ID cannot be empty"
    
    # Check if ID follows format (e.g., E001)
    if not (employee_id.startswith('E') and len(employee_id) == 4 and employee_id[1:].isdigit()):
        return False, "Employee ID must follow the format 'E' followed by 3 digits (e.g., E001)."
    
    return True, ""


def validate_dependents(dependents):
    """
    Validate number of dependents
    
    Parameters:
        dependents: Number of dependents (can be string or int)
    
    Returns:
        tuple: (bool, int, str) - (is_valid, dependents_value, error_message)
    """
    try:
        deps = int(dependents)
        if deps < 0:
            return False, 0, "Number of dependents cannot be negative"
        if deps > 20:
            return False, 0, "Number of dependents seems unusually high (max 20)"
        return True, deps, ""
    except ValueError:
        return False, 0, "Number of dependents must be a valid number"

def validate_hours(hours):
    """
    Validate hours worked
    
    Parameters:
        hours: Hours worked (can be string or float)
    
    Returns:
        tuple: (bool, float, str) - (is_valid, hours_value, error_message)
    """
    try:
        hrs = float(hours)
        is_valid, error_msg = calculations_module.validate_hours(hrs)
        if not is_valid:
            return False, 0.0, error_msg
        return True, hrs, ""
    except ValueError:
        return False, 0.0, "Hours worked must be a valid number"
