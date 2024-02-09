# Functions: Is a block of code designed to perform a specific task, and it only when its called.
# Function definition:  where the function's implementation resided is also accurate and an important aspect of understanding functions.
# Functions parameters: variables that are declared in the function definition. They act as placeholders for the values that will be passed to the function when the function is called.
# Arguments: Arguments: Arguments are the actual values that are passed to the function when it is called.


# [How to create function?] [syntax for functions in python]


def sum(number1, number2):
    return number1 + number2


print(sum(1, 2))


# Difference between
# [ *args - **kwargs ]


# 1. args
def Arg_List(*args):
    return args


print(type(Arg_List(1, 2, 3, 4)))
print(Arg_List(1, 2, 3, 4))

# 2. **kwargs


def Arg_dict(**kwargs):
    print(kwargs)


print(type(Arg_dict(1, 2, 3, 4)))
print(Arg_dict(1, 2, 3, 4))


# scope concept (global - local - nonlocal)
'''
global 
l 
nonlocal - refers to not global variable and not global variable
'''
