def count_frequency(text):
    text_without_space=text.replace(' ','')

    map={}

    for x in text_without_space:
        if x not in map:
            map[x]=1
        else:
            map[x]+=1

    return map

text="abc d ef g h i j k l m n ooooooooooo pppp qq ss aa !!"

print(count_frequency(text))