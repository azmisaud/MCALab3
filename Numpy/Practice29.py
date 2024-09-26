# Create an array of 100 random integers between 0 and 10. Compute and plot the histogram of the array.

import numpy as np
import matplotlib.pyplot as plt

array=np.random.randint(0,11,100)

hist,bins=np.histogram(array,bins=range(12))

plt.bar(bins[:-1],hist)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Integers')
plt.show()
