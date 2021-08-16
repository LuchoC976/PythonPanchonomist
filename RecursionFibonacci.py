# Example of recursion 
# using the Fibonacci numbers sequence
'''

Fibonacci sequence:
Seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...]
Ind = [0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12,  13, ...]

Fibonacci key:
n = (n-1) + (n-2)
Sum of the two previous numbers on sequence

Base cases for recursion:
n = 0 -> 0
n = 1 -> 1

'''

# Define function to obtain index n in fib sequence
def fib_index(n): # 4
    # Base cases (0 and 1)
    if (n == 0) or (n == 1):
        return n
    else: # Return extra cases using recursion
        return fib_index(n-1) + fib_index(n-2) # n = (n-1) + (n-2)
# Main program
print("This program searches for the index you enter and prints the number corresponding to that index in the Fibonacci number sequence (using recursion)")

# Enter index
index = int(input("Enter the index you want to search: "))

# Print results
print("The number at index " + str(index) + " is: " + str(fib_index(index)))