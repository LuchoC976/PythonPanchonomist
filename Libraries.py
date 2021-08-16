# Standard libraries in python
# Libraries are useful to use code
# that was written by someone else
# Saves time and resources
# All import statements must be at the start of the code

# Syntax: import "library_name"
# For example:

# Mathematical operations
import math

# Random numbers
import random

# You can import a library and
# assign a name to save space every time
# you call for the librarys functions
# Syntax: import "library_name" as "desired_acronym"
# Statistics analysis
import statistics as st

# Now lets use some of the libraries we imported
# Call library functions like this:
# "library_name"."library_function()"

# Math library

# Factorial (4! = 4 * 3 * 2 * 1 = 24)
my_num = 4
factorial = math.factorial(my_num)

print("Factorial of " + str(my_num) + " is: " + str(factorial))

# Square root
s_root = math.sqrt(my_num)
print("Square root of " + str(my_num) + " is: " + str(s_root))

# Trigonometric functions (cos(),sin(),tan())
angle = math.pi # Constant value pi = 3.1416...
cosine = math.cos(angle) # Angle is in radians

print("Cosine of " + str(angle) + " is: " + str(cosine))

# Other math functions:
# comb(n,k) -> Combinatory number formula
# pow(x,base) -> Exponential operations
# degrees(x) -> Conversion to degrees (use radians(x) to radians)
# math.e -> CONSTANT of e value
# log(x,base) -> Logarithmic operations
# perm(n,k) -> Permutation formula

# Random library

# Random number between 1 and 1000
my_rand = random.randint(1,1001)

print("Random number between 1 and 1000: " + str(my_rand))

# Statistics library

my_data = [10,23,15,28,22,15,17,27,30]

# Mean of a data structure (list)
mean_value = st.mean(my_data) # Use st (no statistics because of line 21 "as" keyword)

print("The mean value of " + str(my_data) + " is: " + str(mean_value))

# Median value (Middle value)
median_value = st.median(my_data)

print("The median value of " + str(my_data) + " is: " + str(median_value))

# Variance value
variance_value = st.variance(my_data)

print("The variance value of " + str(my_data) + " is: " + str(variance_value))

# Search documentation to see all functions available
'''
Here is the list of libraries we used:
https://docs.python.org/3/library/math.html
https://docs.python.org/3/library/random.html
https://docs.python.org/3/library/statistics.html

If you want to see al standard libraries, enter this link:
https://docs.python.org/3/library/
'''