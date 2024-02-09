###################################################################################
# Name of Program: PrintInfo
# author:          mr-h0n3y
# purpose:         Is to utilize Numbers, boolean data Types and print function
###################################################################################


# we call these (Assignments statements)


# fname = "Ahmed"
# lname = 'Asl'
# age = 22


print("Enter Information you want to display: ")

fname = input("Enter First Name of Student: ")
lname = input("Enter Last Name of Student: ")
age = int(input("Enter age of Student: "))
is_hardWorking = True


print("\nStudent Info: ")
print("Full Name: " + fname + ' ' + lname)
print("Age: {}".format(age))
print(f"he or she is hard working student: {is_hardWorking}")
