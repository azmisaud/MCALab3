combined_list=["Saud",1,"Aisha",2,"Fahad",3,"Erum",4,"MJ",5,"Sana",6]

integer_list=[]
string_list=[]

for x in combined_list:
    if isinstance(x,int):
        integer_list.append(x)
    if isinstance(x,str):
        string_list.append(x)

print(integer_list)
print(string_list)