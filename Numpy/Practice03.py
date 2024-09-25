# Generate a 5x5 array of random integers between 1 and 100. Find the minimum and maximum values in the array.

import numpy as np

array=np.random.randint(1,101,(5,5))

print(array)

min_value=np.min(array)
max_value=np.max(array)

print("Minimum Value : ", min_value)
print("Maximum Value : ", max_value)