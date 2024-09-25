# Create two 3x3 matrices of random numbers. Perform matrix multiplication between them using Numpy.

import numpy as np

array_one=np.random.randint(1,10,(3,3))
array_two=np.random.randint(1,10,(3,3))

print("MATRIX 1 : ")
print(array_one)

print("MATRIX 2 : ")
print(array_two)

product=np.matmul(array_one,array_two)

print("PRODUCT : ")
print(product)