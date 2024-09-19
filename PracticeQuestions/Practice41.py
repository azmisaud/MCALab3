import numpy as np

array_2d=np.array([[1,2,3,4,5],[4,5,6,7,8],[9,10,11,12,13]])

second_column=array_2d[:,1]

average=np.mean(second_column)

print(f"The average value of second column is : {average}")