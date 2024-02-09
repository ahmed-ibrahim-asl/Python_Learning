######################################################################################
# Name of Program: PrintInfo
# author:          mr-h0n3y
# purpose:         Practice your knowledge with list methods and string manipulation
#####################################################################################


'''
prompt - 'Enter your password'
output - 'Your password {*(number according to length) } is {n} letter' long
'''


password = input("Enter your password: ")
print(f"Your password {'*'*len(password)} is {len(password)} letter long")
