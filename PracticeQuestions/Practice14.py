def add_digits(number):
    sum=0
    while number>0:
        sum+=number%10
        number=number//10

    return sum

a=int(input("Enter the number : "))

print(f"The sum of digits of {a} are {add_digits(a)}")