# Hollow Right Angled Pattern

n=int(input("Enter the value of n : "))

for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*i)
    else:
        print('*'+' '*(i-2)+'*')