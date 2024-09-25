# Create a 1D array of the first 16 natural numbers. Reshape it into a 4x4 matrix. Then, flatten the matrix back into a 1D array.

import numpy as np

array_one=np.arange(1,17)

print("ONE DIMENSIONAL ARRAY : ")
print(array_one)

array_two=array_one.reshape((4,4))

print("TWO DIMENSIONAL MATRIX : ")
print(array_two)

array_flatten=array_two.flatten()

print("FLATENNED MATRIX : ")
print(array_flatten)