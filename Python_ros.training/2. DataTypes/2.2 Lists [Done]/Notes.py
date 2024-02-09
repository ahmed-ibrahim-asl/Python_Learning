# [what is it ?]
# Collection of different dataTypes. (There elements can be changed)
# list are mutable

# How to create one ?
dataBase = ['Ahmed', 'Asl', 22]


print(dataBase[0])  # output: Ahmed
print(dataBase[1])  # output: Asl
print(dataBase[2])  # output: 22


# [Do you want to see the whole data base at once ?]
print(dataBase)


# [list slicing]
# list[start:stop:step] - return entire new list on it's own
# list = ['1', '2', '3', '4']


# [list unpacking]
# a, b, c, *other = [1, 2, 3, 4,5, 6]

# print(a)
# print(b)
# print(c)
# print(other)


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
    sorted(list)            -> create new sorted object of the list 


figure out difference between deep copy and shallow copy


4. Additional Useful Methods
    https://www.w3schools.com/python/python_lists_methods.asp
'''
