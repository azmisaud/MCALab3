def max_length(word_list):
    max=float('-inf')
    for word in word_list:
        if len(word)>max:
            max=len(word)

    return max

word_list=["Saud","Python","Sajid","Faisal","Computer"]

print(max_length(word_list))