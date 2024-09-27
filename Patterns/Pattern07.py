# Left-Justified Right-Angled Triangle

n=int(input("Enter the value of n : "))

for i in range(n):
    print(' '*(n-i-1),end='')
    print('*'*(i+1))