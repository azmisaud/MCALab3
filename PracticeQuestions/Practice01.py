# Write a program to read five real numbers from user and find the average and standard 
# deviation.


import math

list=[]
for i in range(5):
    a=int(input(f"Enter the number {i+1} : "))
    list.append(a)

sum=0

for x in list:
    sum+=x

average=sum/5

sum2=0

for x in list:
    sum2+=(x-average)**2

s_d=math.sqrt(sum2/5)

print()
print(f"The average is : {sum}")
print(f"The standard deviation is {s_d}")