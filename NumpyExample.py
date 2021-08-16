# Numpy example

import numpy as np
from numpy.core.numeric import cross, ones

# Using numpy arrays
# Multidimensional arrays
'''
Matrix modelation
[
[1,2,3],
[4,5,6],
[7,8,9]
]
3x3 matrix
'''

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Matrix 1:")
print(matrix)

# Creating arrays

array_1d = np.arange(10)

print("1 Dimensional array: ")
print(array_1d)

array_2d = np.arange(10).reshape(5,2)

print("2 Dimensional array: ")
print(array_2d)

array_3d = np.arange(16).reshape(2,2,4)

print("3 Dimensional array: ")
print(array_3d)

# Reshaping 3D -> (num_of_arrays, x_size, y_size)

# Zeros and ones function for arrays

zeros_arr = np.zeros((3,4))

print("Zeros array:")
print(zeros_arr)

ones_arr = np.ones((3,4))

print("Ones array:")
print(ones_arr)

# Operations with arrays
arr1 = np.array([3,-2,3])
arr2 = np.array([0,2,4])

dotp = np.dot(arr1,arr2)

print("Dot product: " + str(dotp))

crossp = np.cross(arr1,arr2)

print("Cross product: " + str(crossp))