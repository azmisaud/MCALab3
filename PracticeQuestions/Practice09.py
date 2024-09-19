a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

d= a if a>b else b
e= d if d>c else c

print(f"The maximum of {a}, {b} and {c} is {e}")
