# Inverted Right-Angled Triangle of Stars


n=int(input("Enter the number of lines :"))

for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")

    print()