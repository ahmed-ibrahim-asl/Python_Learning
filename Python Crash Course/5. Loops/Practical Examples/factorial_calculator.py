#######################################################################################
# Name of Program: FactorialCalculator
# Author:         mr-h0n3y
# Purpose:        This program calculates the factorial of a given non-negative integer.
#                 It demonstrates the use of for loops for iterative calculations and
#                 introduces the concept of mathematical factorial in programming.
#######################################################################################



def calculate_factorial(n):
    factorial = 1

    # we added one because the end limit is not included to end
    # the looping at n not n-1

    for i in range(1, n + 1):
        factorial *= i
    return factorial



# Example usage

user_number = int(input("I can calculate the factorial of any number you want\nEnter a Number: "))

print(f"The factorial of {user_number} is {calculate_factorial(user_number)}")
