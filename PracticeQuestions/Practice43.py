import numpy as np

def row_wise_sum(numpy_array):
    return np.sum(numpy_array, axis=1)

numpy_array=[[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20],
             [21,22,23,24,25]]

print(row_wise_sum(numpy_array))