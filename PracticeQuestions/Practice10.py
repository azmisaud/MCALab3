import math

input_string=input("Enter x and y (separated by comma) : ")
x,y=map(int,input_string.split(','))

input_string_2=input("Enter x and y (separated by comma) : ")
a,b=map(int,input_string_2.split(','))

distance=math.sqrt(math.pow(x-a,2)+math.pow(y-b,2))

print(f"The distance between ({x},{y}) and ({a},{b}) is {distance}")