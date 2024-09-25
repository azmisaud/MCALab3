# Generate a random 1D array of size 15 with values between 1 and 100. Sort the array in ascending order using Numpy.

import numpy as np

array=np.random.randint(1,101,15)

print("ORIGINAL ARRAY : ")
print(array)

sorted_array=np.sort(array)

print("SORTED ARRAY : ")
print(sorted_array)