# Casting is a programming concept that
# refers to the changing of a data type
# to a different one
# For example: int -> str

# Here is the sintax for casting and examples:

# If I want to change an integer into a String:
# Variable I want to cast (int)
my_int1 = 10

# Destination variable for the cast (str)
my_str1 = str(my_int1)

# If I want to change a String into an integer
# ** I HAVE TO MAKE SURE THE CAST IS POSSIBLE **
# ** YOU CANT CHANGE LETTERS INTO INTEGERS **
# Variable I want to cast (str)
my_str2 = "50"

# Destination variable for the cast (int)
my_int2 = int(my_str2)

# Lets see the results of our casting:
print("Original (my_int1): " + str(type(my_int1)) + " Data: " + str(my_int1))
print("Casted (my_str1): " + str(type(my_str1)) + " Data: " + my_str1)
print("Original (my_str2): " + str(type(my_str2)) + " Data: " + my_str2)
print("Casted (my_int2): " + str(type(my_int2)) + " Data: " + str(my_int2))