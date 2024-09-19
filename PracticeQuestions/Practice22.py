combined_list=[1,2,3,4,5,6,7,8,9,10]

even_list=[]
odd_list=[]

for x in combined_list:
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)

print(even_list)
print(odd_list)