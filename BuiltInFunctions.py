# Built-in functions

# Here are some examples of built-in python functions

# Absolute value
my_num = -5
my_abs = abs(my_num)
print("The absolute value of " + str(my_num) + " is: " + str(my_abs))

# Casting operators
my_var = str(5)
my_int = int("10")
print("Casted variables: " + my_var + ", " + str(my_int))

# Structures
list2set = set([1,1,2,2,3])
set2list = list(list2set)

print("Structures: " + str(list2set) + ", " + str(set2list))

# Input() is also a built-in function such as print()
# Syntax: input(...) , print(...)

# Length of objects
my_str = "hello world"
print("The length of " + my_str + " is: " + str(len(my_str)))

# Maximum and minimum values
var1 = 5
var2 = 10
max_val = max(var1, var2)
min_val = min(var1, var2)

print("The maximum and minimum values are: Max: " + str(max_val) + ", Min: " + str(min_val))

# Other examples
'''
type(x) -> variable types
reversed() -> working with reversed lists, strings, or objects
range() -> ranged limits for loops
sum() -> sum of values
open() -> working with files
round() -> rounding floating values
ord() -> returns unicode value of character -> ASCII
pow() -> exponential operations
...
'''
