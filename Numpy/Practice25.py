# Create a 5x5 matrix filled with zeros and add a border of ones around it.

import numpy as np

matrix_zeroes=np.zeros((5,5), dtype=int)

matrix_border_ones=np.pad(matrix_zeroes,1,mode='constant',constant_values=1)

print(matrix_border_ones)

# Alternatively

matrix_ones=np.ones((7,7),dtype=int)

matrix_ones[1:6,1:6]=0

print(matrix_ones)

