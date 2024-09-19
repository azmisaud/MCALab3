def find_second_largest(num_list):
    if len(num_list) < 2:
        return None,[]
    
    largest=second_largest=float('-inf')
    indices=[]

    for num in num_list:
        if num>largest:
            second_largest=largest
            largest=num
        elif num>second_largest and num<largest:
            second_largest=num

    if second_largest==float('-inf'):
        return None,[]
    
    for i,num in enumerate(num_list):
        if num==second_largest:
            indices.append(i)
            
    return second_largest,indices

num_list=[1,2,3,4,5,5,5,5,6]

print(find_second_largest(num_list))