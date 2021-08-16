# This .py file contains all of introductory
# concepts for Python programming

# 1. Comments on code
# There are 2 ways to comment on python:
    # 1. With the '#' character
    # 2. With the ''' ''' expression, for example:
'''
This is a comment
It serves better for multiple lines of info
'''
# 2. Data types and variables
# There are multiple data types which can be stored in variables, such as:

# Strings
a_string = "Hello"

# Integers
b_int = 5

# Floats (or doubles)
c_float = 3.06

# Booleans (True / False)
d_bool = False

# Characters (char)
e_char = 's'

# Setting multiple variables:
var1, var2 = "Hello", 5

# 3. Print statement
# The print statement lets you show some text or information on console
# For example:
# print("Hello World!") 

# Este comando imprime texto en pantalla
# print("Hola")

# Another way to use the print statement using variables:

print("String: " + a_string)
print("Integer: " + str(b_int))
print("Float: " + str(c_float))
print("Bool: " + str(d_bool))
print("Character: " + e_char)

# 4. User input
# If you want to ask for user input, here's how:
# First you store it in a variable, then use: input(), like this:
# input_raw = input()

# If you want to show a message for the input, use this example:
# input_message = input("Enter some kind of data: ")

# Lastly, if you want to ask for a number, use this example:
input_number = int(input("Enter a number: "))

nombre = input("Ingrese los datos: ")
