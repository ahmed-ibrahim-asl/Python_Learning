# Original string
original_string = "hello"

# Trying to change a character
# This will result in an error
# original_string[0] = 'H'

# Instead, you create a new string
modified_string = "H" + original_string[1:]

print("Original string:", original_string)
print("Modified string:", modified_string)
