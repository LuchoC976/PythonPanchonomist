# Tuples and Dictionaries

# Both save pairs or multiple instances of values

# Tuples
my_tuple1 = (1, 2, 3)

print("My tuple: " + str(my_tuple1))

# Single item tuple
single_tuple = ("item1",)

print("Single item tuple: " + str(single_tuple))

# Tuples are unchangeable
# If you want to change a value, transoform to list then back to tuple
provisional_list = list(my_tuple1)

provisional_list.append(4)

my_tuple2 = tuple(provisional_list)

print("Original tuple: " + str(my_tuple1))
print("Changed tuple: " + str(my_tuple2))

# Unpacking tuples
# Getting values into variables
(var1, var2, var3, var4) = (my_tuple2)

print("Unpacked variable 1: " + str(var1))
print("Unpacked variable 2: " + str(var2))
print("Unpacked variable 3: " + str(var3))
print("Unpacked variable 4: " + str(var4))

# Asterisk for unpacking
(ast1, *ast2) = my_tuple1

print("Normal unpacked: " + str(ast1))
print("Asterisk unpacked: " + str(ast2)) # Returns list

# Dictionaries
# Stores {KEY : VALUE} pairs
# JSON (JavaScript Object Notaion)

my_dict1 = {
    "name": "Henry",
    "last": "Johnson",
    "age": 23,
}

print("My dictionary: " + str(my_dict1))

# Printing keys of dictionary

print("Key for name: " + str(my_dict1["name"]))
print("Key for age: " + str(my_dict1["age"]))

# DUPLICATES of keys will OVERWRITE the existing value

# Multiple structures in dictionary
my_dict2 = {
    "name": "Mike",
    "last": "Sanders",
    "age": 43,
    "children": ["Daniel", "Sophia"]
}

print("Mike's children are: " + str(my_dict2["children"]))

# Get keys in a dictionary
keys_1 = my_dict1.keys()

print("Keys for Dictionary 1: " + str(keys_1))

# Adding keys to dictionary

my_dict1["country"] = "Canada"

print("Added key to dictionary: " + str(keys_1)) # Updated keys automatically

# Get values of dictionary
values_1 = my_dict1.values()

print("Values of dictionary: " + str(values_1))

# Modify values in dictionary
my_dict1["age"] = 16 # Using existing key to overwrite result value

print("Updated values of dictionary: " + str(values_1))

# Get paired items of dictionary
items_1 = my_dict1.items()

print("Paired dictionary items: " + str(items_1))

# Change value pairs
my_dict1.update({"name": "Shawn"})

print("Updated dictionary: " + str(my_dict1))

# Check if key exists in dictionary
if ("age" in my_dict1):
    print("Age exists in my dictionary")

# Remove pair by key using pop
my_dict1.pop("last")

print("Removed by key: " + str(my_dict1))

# Clear dictionary using clear()
