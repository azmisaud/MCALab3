def remove_empty(list_1):
    for i,x in enumerate(list_1):
        if not x:
            list_1.pop(i)


list_1=[(1,1),(2,3,4),(),(3,3),(),(4,5)]

remove_empty(list_1)

print(list_1)