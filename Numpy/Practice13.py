# Create two Numpy arrays of size 10 with random integers between 0 and 1. Perform logical AND, OR, and XOR operations element-wise on these arrays.

import numpy as np

array_one=np.random.randint(0,10,10)
print("ARRAY 1 : ")
print(array_one)

array_two=np.random.randint(0,10,10)
print("\nARRAY 2 : ")
print(array_two)

array_and=np.logical_and(array_one,array_two)
print("\nLogical AND : ")
print(array_and)

array_or=np.logical_or(array_one,array_two)
print("\nLogical OR : ")
print(array_or)

array_xor=np.logical_xor(array_one,array_two)
print("\nLogical XOR : ")
print(array_xor)

