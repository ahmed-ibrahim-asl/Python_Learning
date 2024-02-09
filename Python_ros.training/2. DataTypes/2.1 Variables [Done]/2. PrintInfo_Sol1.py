###################################################################################
# Name of Program: PrintInfo
# author:          mr-h0n3y
# purpose:         Is to utilize Numbers, boolean data Types and print function
###################################################################################


# we call these (Assignments statements)

fname = "Ahmed"
lname = 'Asl'
age = 22

is_hardWorking = True

# another way to do Assignment statement
# fname, lname, age, is_hardWorking = "Ahmed", 'Asl', 22, True


print("\nStudent Info: ")
print("Full Name: " + fname + ' ' + lname)
# old way in string formating were being used in python2
print("Age: {}".format(age))
print(f"he or she is hard working student: {is_hardWorking}")
