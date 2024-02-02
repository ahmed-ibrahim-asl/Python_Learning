# collection which is unordered and unindexed. (No duplicate members)


# How to create one ?


# you not allowed to have two of same thing 
gifts = {'monitor', 'keyboard', 'mouse', 'monitor'}



print(gifts)


# Useful use case for sets 
# in given small dataBase <list> we have bug (we can't have repeated names)

owners_names = ['ahmed', 'ahmed', 'ibrahim', 'omar', 'mohamed']
print(f"Before implementig solution:\n{owners_names}")

#solution: 
# we can {cast} list to set data type and then {cast} it again to list 
# cast - change the data type to another data type 
    

# owners_names = set(owners_names)
# owners_names = list(owners_names)


owners_names = list( set(owners_names) )

print(f"\nAfter Solution:\n{owners_names}")



