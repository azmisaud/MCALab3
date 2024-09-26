# Create an array of random integers between 1 and 20. Identify the most frequent value in the array.

import numpy as np

array_random=np.random.randint(1,21,50)

values, frequencies=np.unique(array_random, return_counts=True)

max_index=np.argmax(frequencies)

most_frequent_value=values[max_index]

print("ARRAY : ")
print(array_random)

print("Most Frequent Value : ", most_frequent_value)
print("Frequency : ", frequencies[max_index])
