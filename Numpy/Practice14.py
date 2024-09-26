# Create a 3x5 matrix and find its transpose using Numpy. Verify that the shape of the transposed matrix is correct.

import numpy as np

# Generating random array of 3x5

array=np.random.randint(1,15,(3,5))

print("MATRIX : ")
print(array)

transposed_array=array.T

print("\nTRANSPOSED MATRIX : ")
print(transposed_array)

print("\nShape of the original matrix : ", array.shape)
print("\nShape of the transposed matrix : ", transposed_array.shape)
