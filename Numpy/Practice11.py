# Create a random 1D Numpy array of size 20. Use masking to extract all elements greater than 50 from the array.

import numpy as np

array_random=np.random.randint(1,101,20)

print("The array which is generated : ")
print(array_random)

mask=array_random>50

result=array_random[mask]

print("\nElements greater than 50 : ")
print(result)

