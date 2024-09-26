# Create a 3x3 matrix of random integers. Compute the determinant of the matrix using Numpy.


import numpy as np

matrix_random=np.random.randint(0,15,(3,3))

print("MATRIX : ")
print(matrix_random)

matrix_determinant=np.linalg.det(matrix_random)

print("\nDeterminant : ", matrix_determinant)

