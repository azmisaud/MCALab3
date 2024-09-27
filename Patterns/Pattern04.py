# Inverted Pyramid Pattern of Stars:

n=int(input("Enter the number of lines : "))

for i in range(n-1,-1,-1):
    print(' ' *(n-i-1),end='')
    print('*'*(2*i+1))