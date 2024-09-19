def find_index(tup,num):
    for i,n in enumerate(tup):
        if n == num:
            return i
        
    return -1

tup=(1,2,3,4,5,6)

print(find_index(tup,6))