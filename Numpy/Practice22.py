# Create a Numpy array of 20 random integers between 1 and 50. Replace all values greater than 25 with 25.

import numpy as np

array_1D=np.random.randint(1,51,20)
print("BEFORE REPLACING : ", array_1D)

array_1D[array_1D>25]=25
print("AFTER REPLACING : ", array_1D)