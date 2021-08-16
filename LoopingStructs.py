# Looping structures (to do in class)

# [1, 2] + [3, 4] = [4, 6]

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print("Value: " + str(item))

for i in range(len(my_list)):
    print("Index: " + str(i) + " Value: " + str(my_list[i]))

list1 = [1, 5, 3]
list2 = [6, 7, 8]
list3 = []
# List3 = [7, 9, 11]

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])

print("List3: " + str(list3))

