import numpy as np

def max_average(numpy_array):
    average=np.average(numpy_array,axis=1)

    return max(average)

numpy_array=[[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20],
             [21,22,23,24,25]]

print(max_average(numpy_array))