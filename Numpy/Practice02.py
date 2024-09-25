# Create a 2D Numpy array and demonstrate how to select specific rows and columns. Extract the 2nd row, 3rd column element from this array.

import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])


# If we want to select the second row

second_row=array[1,:]

# If we want to select the second column

second_column=array[:,1]

# If we want to check specific element of a row and a column

element=array[1,2]

print(second_row,second_column,element)