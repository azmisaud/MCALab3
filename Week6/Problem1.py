def combine(tuple1,tuple2):
    list1=list(tuple1)
    list2=list(tuple2)

    list3=list1+list2
    tuple3=tuple(list3)

    return tuple3

tuple1=tuple(map(int,input("Enter elements of first tuple : ").split()))
tuple2=tuple(map(int,input("Enter elements of second tuple : ").split()))

print()
print("COMBINED TUPLE : ")
tuple=combine(tuple1,tuple2)

print(tuple)