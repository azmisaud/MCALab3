# Diamond Pattern with Numbers:

n=int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(2*i-1):
        print(i,end='')

    print()

for j in range(n-1,0,-1):
    for k in range(n-j):
        print(' ',end='')
    for k in range(2*j-1):
        print(j,end='')

    print()