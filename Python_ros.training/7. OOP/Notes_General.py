# A class is like a blueprint for creating objects. 
# An object has properties and methods(Functions) associated with it.
# Almost Everything in python is an object 



# How can create a create class ?
class student:
    # Any class should has constructor should has constructor 
    # constructor: Think of it as thing in python intended to be used to initialize objects, 
    #              typically by setting initial values for their properties.  
    
    # __init__: In python this method is called automatically when any object is created 


    # class object Attribute
    college_name = "delta"

    def __init__(self, name, id):

        # Attributes
        self.name = name
        self.id = id


    # First Action the new object can do 
    def sayName(self):
        return f"My name is {self.name}"




# How can we create an ojbect ?
ahmed = student("Ahmed", id)


print(ahmed.sayName())





'''
Dunder Method:
short for double underscore, enable you to give super power for your 
object when they are used with certain operators or builtin-in functions




[examples]
__str__         >           str(object)

__len__         >           len(object)

__del__         >           del object

__call__        >           object()

__getitem__     >           object[i]


Note: you can overwrite these dunder methods in your class 

'''

