# Create an array with several zeros and non-zero values. Find the indices of all non-zero elements using Numpy.

import numpy as np

array_1D=np.random.randint(0,4,20)
print("1D Array : ",array_1D)

non_zero_1D=np.nonzero(array_1D)

print("Indices of non-zero element : ", non_zero_1D)


print()

array_2D=np.random.randint(0,4,(5,4))
print("2D Array : ")
print(array_2D)

non_zero_2D=np.nonzero(array_2D)

print("\nIndices of non zero elements : ")
print(non_zero_2D)