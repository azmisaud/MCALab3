def sort_alphabetically(string):
    word=string.split()
    
    sorted_word=sorted(word,key=str.lower)

    return " ".join(sorted_word)

print(sort_alphabetically("Saud is me"))