def find_repeated(item_tuple):
    repeated=[]

    map={}

    for x in item_tuple:
        if x not in map:
            map[x]=1
        else:
            map[x]+=1

    for key,value in map.items():
        if value>1:
            repeated.append(key)

    return repeated

tuple_1=(1,2,3,4,4,5,5,6,6,6,6,7,7,8)

print(find_repeated(tuple_1))