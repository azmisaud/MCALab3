import numpy as np

def find_average_value(numpy_array):
    result=numpy_array[0:5,2:4]

    return np.mean(result)


numpy_array=np.array([[1,2,3,4,5],
                      [1,2,3,4,5],
                      [1,2,3,4,5],
                      [1,2,3,4,5],
                      [1,2,3,4,5],
                      [1,2,3,4,5]])

print(find_average_value(numpy_array))
