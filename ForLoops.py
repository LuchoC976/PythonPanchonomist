# For loops

# For loops work better when you know how
# many iterations you want to run

for x in range(10): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print("Iteration: " + str(x))

# i = index

# You can iterate with a String
# For example:

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    print(letter) # '\n'

# Another example:

# len(alphabet) = 26
for i in range(len(alphabet)):
    print("Letter #" + str(i+1) + ": " + alphabet[i])

# Continue statement in for loops
# Skips the rest of the iteration
# Jumps to next iteration
for i in range(5):
    if (i == 3):
        continue
    print("Continued iteration: " + str(i))

# Different ranges and skipping iterations
# Different ranges
for i in range(5,10): # range(10)
    print("Ranged iteration: " + str(i))

# Skipping iterations
# Format in range: (Lower limit, Upper limit [not included], Distance of iteration)
for i in range(0,7,2): # for (int i = 0; i<5; i += 2) JAVA
    print("Paired iteration: " + str(i))

# Reversed for loop
for i in range(0,-5,-1):
    print("Reversed iteration: " + str(i))