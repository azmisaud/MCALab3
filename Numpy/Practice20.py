# Generate a 3x3 matrix of random integers. Calculate its inverse using Numpy, and verify the result by multiplying the matrix with its inverse.

import numpy as np

matrix_random=np.random.randint(1,15,(3,3))

print("MATRIX : ")
print(matrix_random)

matrix_inverse=np.linalg.inv(matrix_random)
print("\nInverse Matrix : ")
print(matrix_inverse)

identity_matrix=np.dot(matrix_random,matrix_inverse)

print("\nMatrix * Inverse Matrix : ")
print(identity_matrix)

print(np.allclose(identity_matrix,np.eye(3)))