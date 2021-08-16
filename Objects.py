# Objects

# Define an object with 'class' ClassName:
class MyObj:
    # Object variables
    my_var = 5

# Create an instance of the object
obj1 = MyObj() 

# Print variables of object
print("Object variable: " + str(obj1.my_var))

class MyObj2:
    # Constructor with __init__ function
    # Use it to assign values in instancing of object
    def __init__(self,my_var): # Person -> Person()
        self.my_var = my_var

# Object instance
obj2 = MyObj2(10)

print("Object 2 init value: " + str(obj2.my_var))

# Member functions
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Member function
    def printValues(self):
        print("The member function shows -> Name: " + self.name + ", Age: " + str(self.age))

# Instance of object
p1 = Person("John", 25)

# Call for member function
p1.printValues()