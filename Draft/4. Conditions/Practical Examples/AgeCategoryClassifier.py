#######################################################################################
# Name of Program: AgeCategoryClassifier
# Author:         mr-h0n3y
# Purpose:        This program categorizes a person based on their age into one of four
#                 categories: child, teenager, adult, or senior. It demonstrates the use
#                 of if/else/elif statements, functions, and handling user input.
#######################################################################################


def categorize_age(age):
    if age < 13:
        return "child"
    
    elif (age < 20):
        return "teenager"
    
    elif (age < 65):
        return "adult"
    
    else:
        return "!unknown!"
    


def main():
    # Ask the user for their age 
    user_age = int(input("Please enter your age: "))

     # Call the function with the user's age and print the result
    print(f"You are classified as a(n) {categorize_age(user_age)}.")




# calling the main function
main()