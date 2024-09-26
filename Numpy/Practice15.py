# Create a 1D array of size 12 and resize it into a 2D array of shape (3, 4). Then reshape it into a 3D array of shape (2, 2, 3).

import numpy as np

array_1D=np.arange(12)
print("1D array: ", array_1D)

array_2D=array_1D.reshape(3,4)
print("\n2D Array : ")
print(array_2D)

array_3D=array_2D.reshape(2,2,3)
print("\n3D Array : ")
print(array_3D)