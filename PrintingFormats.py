# Printing formats

# The print command can only print
# STRINGS in console
# If you want to print numbers (int, float)
# or other types, you have to make a cast
# For example, if I want to print a floating point:

my_float = 5.05

print("My Float: " + str(my_float))

# As you can see on the example, we use
# the '+' operator as a concatenation operator
# when we want to print different data types
# with a single use of the print() statement
# If we want to print only a number (no concatenation)
# there is no need to make a cast, for example:

# Another way to print is using the 'format' expression:
# For example: using the print() command like a the C expression printf()
# This prints a formatted string: with a syntax like this one:

students = 240
boys = 100
print("Total students: %2d, Boys: %2d" % (students, boys))

# We use the modulus operator (%) to define our format
# The number (2) after % is the spaces
# The letter (d) stands for decimals, which we use to print integers (f for floats, o for octal, etc.)
# Finally, we use again % tu define a tuple with the data we want to print (It has to be the same
# as the data type we specified with the letter)

# Another way to print is using the .format method
# Here is the syntax

name = "John"
age = 23

print('Hello, my name is {} and I am {} years old!'.format(name, str(age)))

# We define the spaces we want to place our data with the '{ }' expression
# Then, we call the format method using '.'
# We place the data in the order we want to print it in () separated by commas
