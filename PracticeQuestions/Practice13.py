def is_prime_2(number):
    if number<2:
        return False
    for i in range(2,number//2+1):
        if number%i==0:
            return False
    return True

a=int(input("Enter the lowest range : "))
b=int(input("Enter the highest range : " ))

prime_between_a_b=[]

for i in range(a,b+1):
    if(is_prime_2(i)):
        prime_between_a_b.append(i)

print(f"The prime numbers between {a} and {b} are : ")
print(prime_between_a_b)