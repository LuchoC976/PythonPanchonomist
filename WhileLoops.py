# While loops

# While loops work better when you have an
# unknown number of iterations

my_num = 5
while (my_num > 0):
    print("My number: " + str(my_num))
    my_num -= 1 # my_num = my_num - 1  

# Using an iterator (counter)

counter = 0
while (counter != 5):
    print("Counter value: " + str(counter))
    counter += 1

# Break statement
while (True):
    print("This loop has a break statement")
    break

# Continue statement in while loops
# Skips the rest of the iteration
# Jumps to next iteration
passing_value = 3
counter2 = 0
while (counter2 != 5):
    if (counter2 == passing_value):
        counter2 += 1
        continue
    print("Counter value (with continue): " + str(counter2))
    counter2 += 1
