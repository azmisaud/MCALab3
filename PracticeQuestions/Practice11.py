def factorial(number):
    if number==0:
        return 1
    return number*factorial(number-1)

a=int(input("Enter a number : "))

print(f"The factorial of {a} is {factorial(a)}")