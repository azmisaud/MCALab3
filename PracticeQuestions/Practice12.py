def is_prime(number):
    if number<2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
        
    return True

a=int(input("Enter a number : "))

if is_prime(a):
    print(a,"is a prime number")
else:
    print(a,"is not a prime number")