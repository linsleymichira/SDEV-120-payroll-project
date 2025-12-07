
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