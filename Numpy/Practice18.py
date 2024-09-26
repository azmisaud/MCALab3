# Create a 1D array of random numbers. Compute its Euclidean norm using Numpy's linalg.norm function.

import numpy as np

array_1D=np.random.randint(0,15,20)

print("ARRAY : ")
print(array_1D)

euclidean_norm=np.linalg.norm(array_1D)
print("\nEuclidean Norm : ", euclidean_norm)