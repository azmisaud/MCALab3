# Given two Numpy arrays of the same shape, perform element-wise addition, subtraction, multiplication, and division. Use Numpy functions for each operation.

import numpy as np

# Randomly Generating 2 matrices of same size

matrix_1=np.random.randint(1,10,(4,4))
matrix_2=np.random.randint(1,10,(4,4))

print("MATRIX 1 : ")
print(matrix_1)

print("\nMATRIX 2 : ")
print(matrix_2)

matrix_add=np.add(matrix_1,matrix_2)
print("ADDITION : ")
print(matrix_add)

matrix_subtract=np.subtract(matrix_1,matrix_2)
print("\nSUBTRACTION : ")
print(matrix_subtract)

matrix_multiply=np.multiply(matrix_1,matrix_2)
print("\nMULTIPLICATION : ")
print(matrix_multiply)

matrix_divide=np.divide(matrix_1,matrix_2)
print("\nDIVISION : ")
print(matrix_divide)