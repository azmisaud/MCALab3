# Create a Numpy array with repeated elements. Use Numpy to find and return an array of the unique elements.

import numpy as np

array=np.array([1,2,2,2,4,4,4,10,10,10,11,1,1,1,12])

print("ARRAY WITH REPEATED ELEMENTS : ")
print(array)

unique_array=np.unique(array)
print("\nARRAY WITH UNIQUE ELEMENETS : ")
print(unique_array)
