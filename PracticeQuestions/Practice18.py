def new_string(word):
    if len(word)<4:
        return ""
    
    else:
        return word[0:2]+word[-2:]
    
print(new_string("New Delhi"))
print(new_string("New"))