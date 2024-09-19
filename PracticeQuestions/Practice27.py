def remove_duplicates(list_1):
    map={}
    for i,num in enumerate(list_1):
        if num not in map:
            map[num]=1
        else:
            list_1.pop(i)

list_1={1,1,2,3,4,5,5,6,6,7}

def remove_duplicates_using_set(list_1):
    list_1=list(set(list_1))
    
remove_duplicates_using_set(list_1)

print(list_1)