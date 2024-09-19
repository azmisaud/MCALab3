def max_character(text):
    map={}

    for x in text:
        if x not in map:
            map[x]=1

        else:
            map[x]+=1

    max_char=""
    max_count=0

    for key,value in map.items():
        if value>max_count:
            max_char=key
            max_count=value

    return max_char

text="Saudddddddddddd, Maaazzz"

print(max_character(text))