# Create a 1D array of integers from 1 to 10. Compute the cumulative sum and cumulative product of the array.

import numpy as np

array=np.arange(1,11)

print("Array : ")
print(array)

cumulative_sum=np.cumsum(array)
print("\nCumulative Sum : ")
print(cumulative_sum)

cumulative_product=np.cumprod(array)
print("\nCumulative Product : ")
print(cumulative_product)