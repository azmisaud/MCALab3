# Create a 2D array of random integers. Find the indices of the maximum and minimum values in the array.

import numpy as np
import random as r

n1=r.randint(1,10)
n2=r.randint(1,10)

array_2d=np.random.randint(1,100,(n1,n2))

print("Original Matrix : ")
print(array_2d)

max=np.max(array_2d)
max_index=np.unravel_index(np.argmax(array_2d),array_2d.shape)

print("\n MAXIMUM VALUE : " , max, " at ", max_index)

min=np.min(array_2d)
min_index=np.unravel_index(np.argmin(array_2d),array_2d.shape)

print("\nMINIMUM VALUE : ", min, " at ", min_index)