# Given two 1D arrays x and y, compute their Euclidean distance using vectorization without explicit loops.

import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])

distance=np.sqrt(np.sum((x-y)**2))

print("Euclidean distance : ", distance)