# Create a 5x5 matrix of random integers and extract its diagonal elements using Numpy.

import numpy as np

matrix_random=np.random.randint(1,50,(5,5))

print("MATRIX GENERATED : ")
print(matrix_random)

diagonal_elements=np.diag(matrix_random)

print("\nDiagonal Elements : ")
print(diagonal_elements)