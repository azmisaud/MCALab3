# Create a 5x5 matrix of random numbers. Add 10 to every element of the matrix using broadcasting, without using explicit loops.

import numpy as np

matrix_5_5=np.random.randint(1,101,(5,5))

print("MATRIX BEFORE ADDING : ")
print(matrix_5_5)

matrix_5_5+=10

print("MATRIX AFTER ADDING 10 : ")
print(matrix_5_5)