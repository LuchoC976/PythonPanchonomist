# Conditionals
# This is a fundamental programming concept

# If / else statements

# Conditionals work in such a way that
# If a condition is met, then something happens,
# if not, then something different happens

# For example:
my_int1 = 5

# We use the 'if' statement to establish our condition:
if (my_int1 > 0):
    print(str(my_int1) + " is greater than 0")

# Our condition is between ( ) and we and de condition definition with ':'
# It has to be tabbed
# How it works:
'''
(my_int1 > 0) produces a boolean value -> True or False
If the condition is True, then it will print our result
It the condition is False, nothing will happen in this case
For example:
'''
my_int2 = -2

# We use the 'if' statement to establish our condition:
if (my_int2 > 0):
    print(str(my_int2) + " is greater than 0")
    # Nothing will happen because our condition is False

# Here we can use the else statement:
# For example:
if (my_int2 > 0):
    print(str(my_int2) + " is greater than 0")
else:
    print(str(my_int2) + " is not greater than 0")

# The 'else' statement works like this:
'''
If the condition is not met, any other case will
be printed
'''

# If we want multiple cases we can use the 'elif' statement
# This one works such as another if condition (so we need to define our
# new condition)
# For example:
my_int2 = 0

if (my_int2 > 0):
    print(str(my_int2) + " is greater than 0")
elif (my_int2 == 0): # else if 
    print(str(my_int2) + " is equal to 0")
else:
    print(str(my_int2) + " is not greater than 0")

# To look for negative conditions (False ones) we use 'if not'
# For example:
my_int3 = -1
if not (my_int3 > 0):
    print(str(my_int3) + " is smaller than 0")