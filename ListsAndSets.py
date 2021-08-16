# Lists and Sets

# Lists
# Define lists with '[]'
my_list = [1, 2, "Hello"] 

# Print all list (or just 1 item)
print("My list: " + str(my_list))
print("List item " + str(1) + ": " + str(my_list[1]))

# Add items to list with append()
my_list.append(3)

print("Appended item " + str(3) + ": " + str(my_list[3]))

# Remove items form list with remove()
my_list.remove('Hello')
print("My list (Removed 'hello' element): " + str(my_list))

# Remove items form list with pop()
my_list.pop(0)
print("My list (Popped element 0): " + str(my_list))

# Clear list with clear()
my_list.clear()

print("My list (cleared): " + str(my_list))

# Sorting lists
my_list2 = [5,8,1,4,2,3,7,6]
print("My list 2 original: " + str(my_list2))

my_list2.sort() # sort(-1)
print("My list 2 sorted: " + str(my_list2))

# Join lists (with '+' operator)
my_list.append(2)
my_list.insert(0, 1) # Adding items with index using insert()

print("My lists: " + str(my_list) + ", " + str(my_list2))

my_list3 = my_list + my_list2

print("Joined list (My list 3): " + str(my_list3))

# Sets
# Sets dont allow duplicates
# We can transform a list into a set using set()
# len(list)

my_set = set(my_list3)

print("My list 3 turned into set: " + str(my_set))

# Or write sets manually with '{}'
my_set2 = {"apple", "banana", "orange"}

print("Manually defined set: " + str(my_set2))

# Add items to set using add()
my_set2.add("watermelon")

print("Added item in set: " + str(my_set2))

# Remove items in set using remove()

my_set2.remove("banana")

print("Removed item in set: " + str(my_set2))

# Joining sets using union() and update()
# Union requires new variable

my_set3 = my_set2.union(my_set)

print("Union set (My set 3): " + str(my_set3))

my_set4 = {10, 9, 2, 4, "apple", "banana"}
# Update doesnt require a new variable
# Sets exclude duplicate items

my_set3.update(my_set4)

print("Updated set (My set 3 with set 4 items): " + str(my_set3))

# If you want to sort sets, you must convert into list, and use sort()
# Converting set back to list
my_list4 = list(my_set3)
my_set5 = set(my_list)

# You can only sort numbers with the sort method or only strings, not both at once

# list = [1,2,3,4,1,2] 
# set(list) = {1,2,3,4} -> len(set)