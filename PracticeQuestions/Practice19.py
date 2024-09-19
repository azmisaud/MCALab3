def modify_string(word):
    if len(word)<3:
        return word
    if word[-1]!='e':
        return word
    return word[:-1]

print(modify_string("Give"))