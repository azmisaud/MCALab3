# Create a random 4x4 matrix. Find the determinant and rank of the matrix using Numpy.

import numpy as np

matrix=np.random.randint(0,11,(4,4))

print("MATRIX : ")
print(matrix)

matrix_determinant=np.linalg.det(matrix)
print("\nDETERMINANT : ", matrix_determinant)

matrixrank=np.linalg.matrix_rank(matrix)
print("RANK : ", matrixrank)