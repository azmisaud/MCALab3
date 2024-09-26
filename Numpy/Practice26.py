# Create an array of 100 equally spaced values between 0 and 1. Compute the sum and product of all elements in the array.

import numpy as np

array=np.linspace(0,1,100)

print("ARRAY : ")
print(array)

sum=np.sum(array)

print("SUM : ", sum)

product=np.prod(array)
print("PRODUCT : ", product)