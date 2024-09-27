# Half Diamond Pattern

n=int(input("Enter the value of n : "))

for i in range(n):
    print('*'*(i+1))
for i in range(n-2,-1,-1):
    print('*'*(i+1))  # print the half diamond pattern