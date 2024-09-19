def is_palindrome(word):
    return word==word[::-1]

a=input("Enter a string : ")

if is_palindrome(a):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")