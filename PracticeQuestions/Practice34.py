def count_and_max(text):
    count_sentences=len(text.split('.'))
    count_words=len(text.replace('.',' ').split())
    
    words=text.replace('.',' ').split()

    map={}

    for word in words:
        if word not in map:
            map[word]=1
        else:
            map[word]+=1

    max_word=""
    max_count=0

    for key,value in map.items():
        if value>max_count:
            max_word=key
            max_count=value

    return count_sentences,count_words,max_word

text="Saud Saud Saud.Zindagi na milegi dubara"

print(count_and_max(text))