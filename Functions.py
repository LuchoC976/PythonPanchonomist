# Functions and utilities
import math

# Functions help reuse code more efficiently
# and helps us to work with large blocks of
# code 
# They work by:
#   1. Defining a function
#   2. (Optional) Assigning return values
#   3. Calling the function in the main program

# Defining functions: def
def my_func(): # function ...()
    print("This is the result of my_func()")

# Calling functions
my_func()
# This will execute the function

# Passing arguments in functions
def my_func2(a):
    print("My function passes this argument: " + a)

my_str = "String"
my_func2(my_str)
# You can also pass variables as arguments

# Default arguments
def my_func3(default = "Default argument!"):
    print("This function has a default argument: " + default)

my_func3("Not default")
my_func3()

# Passing lists as arguments
def my_func4(x):
    for i in range(len(x)):
        print("List item #" + str(i) + ": " + str(x[i]))

my_list = [1,3,5]

my_func4(my_list)

# Passing multiple arguments
def my_func5(a,b,c):
    print("Argument 1: " + a)
    print("Argument 2: " + str(b))
    print("Argument 3: " + str(c))

my_str = "String"
my_int = 4
my_float = 1.03

my_func5(my_str,my_int,my_float)

# Return values in functions
# If your function has a return value,
# the function must be assigned to a variable
# For example:
def return_function():
    my_str = "This function has a return value"
    return my_str

return_result = return_function()
print(return_result)

# Another example with arguments
def triple_product(x):
    return x * x * x

my_int2 = 3
triple_result = triple_product(my_int2)

print("The result of the function is: " + str(triple_result))

# Passing statement
# It works when you have an incomplete function
# and you dont want compilation errors
# For example:
def pass_func():
    pass # To do later for instance

# Utilities of functions
# Dot product of two vectors
def dotProduct(u,v):
    if (len(u) == 3) and (len(v) == 3):
        return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
    return u[0]*v[0] + u[1]*v[1]
    
# Main program

# 2 vectors represented as lists
v1 = [2,3] # u = 2i + 3j + 4k
v2 = [3,4] # v = 3i + 4j + k

# 6 + 12 + 4 = 22
# 6 + 12 = 18

# Returned value into result variable
result = dotProduct(v1,v2)

# Printing results with format()
print("The dot product between <{},{}> and <{},{}> is: {}".format(v1[0],v1[1],v2[0],v2[1],result))

# Factorial calculator
def factorial(x):
    result = 1
    if (x == 0):
        return 1
    for i in range(1, x+1):
        result *= i
    return result

num1 = 5 # 5 * 4 * 3 * 2 * 1
fact = factorial(num1)

print("Factorial of " + str(num1) + " is: " + str(fact))

# Quadratic equation solver example
# Solver function
def solve(a,b,c): # AX2 + BX + C = 0
    # Calculate discriminant using formula: { bb - 4ac }
    discriminant = (b ** 2) - (4 * a * c)

    # No real solution case and solving equation
    if (discriminant < 0):
        # No solution because negative root
        print("This system has no real solution")
    else:
        # Solve equation
        ans_1 = (-b - math.sqrt(discriminant)) / (2 * a)
        ans_2 = (-b + math.sqrt(discriminant)) / (2 * a)

        print("The solution to the system are: ")
        print("x1 = " + str(ans_1))
        print("x2 = " + str(ans_2))

# Main program
# Initial message and usage (Form: Ax^2 + Bx + C = 0)
print("Enter the values corresponding to the equation form: ")
print("--| Ax^2 + Bx + C = 0 |--")


# Inputs of equation
a1 = float(input("A = "))
b2 = float(input("B = "))
c3 = float(input("C = "))

solve(a1,b2,c3)
