# Collection of different dataTypes. (There elements can be changed)

# How to create one ?
dataBase = ['Ahmed', 'Asl', 22]

# How a list is ordered ? by index

print(dataBase[0]) #output: Ahmed
print(dataBase[1]) #output: Asl
print(dataBase[2]) #output: 22


# Do you want to see the whole data base at once ?
print(dataBase)

'''
Common-List Methods:
1. Insert Methods
    .append(element)        -> adds elements to the end of the list 
    .insert(index, element) -> inserts elements at the sepcified index other elements are shifted to the right
    .extend(iterable)       -> Merging two lists together 

2. Remove Methods
    .remove(element)        -> removes the first occurrence of element. if the element is not found, it raises 'ValueError'
    .pop()                  -> it removes and returns the last element of the list. if the list is empty or index is out of bounds it raises an IndexError
    .clear()                -> removes all items from the list, resulting 

3. Order Methods
    .sort(reverse=False)    -> sorts the items of a list. ascending order
    .sort(reverse=True)     -> sorts the items of a list. descending order
    .reverse()              -> reverses the elements of lists in place, affecting the original list.    

4. Additional Useful Methods
    https://www.w3schools.com/python/python_lists_methods.asp
'''



