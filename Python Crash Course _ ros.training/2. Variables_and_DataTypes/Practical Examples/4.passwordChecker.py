'''
prompt - 'Enter your password'
output - 'Your password {*(number according to length) } is {n} letter' long
'''




password = input("Enter your password: ")
print(f"Your password {'*'*len(password)} is {len(password)} letter long")