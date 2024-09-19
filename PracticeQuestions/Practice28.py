def odd_times(list_1):
    odd_list=[]
    map={}

    for x in list_1:
        if x not in map:
            map[x]=1
        else:
            map[x]+=1

    for key,value in map.items():
        if value%2!=0:
            odd_list.append(key)

    return odd_list

list_1=["Saud","Saud","Saud","Moaz","Moaz","Shuja","Shuja","Shuja"]

print(odd_times(list_1))