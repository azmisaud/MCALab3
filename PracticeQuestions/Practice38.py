class prime:
    def __init__(self, n,m,prime_list):
        self.n=n
        self.m=m
        self.prime_list=self.generate_primes(n,m)

    def is_prime(self,number):
        if number<2:
            return False
        for i in range(2,number//2+1):
            if number%i==0:
                return False
            
        return True
    
    def generate_primes(self,n,m):
        prime_list=[]
        for num in range(n,m+1):
            if self.is_prime(num):
                prime_list.append(num)
        return prime_list

n=int(input("Enter the first number : "))
m=int(input("Enter the second number : "))

prime_list=[]
my_prime=prime(n,m,prime_list)

print(my_prime.prime_list)