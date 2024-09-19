def count_digits_alphabets(text):
    digits = 0
    alphabets = 0

    for x in text:
        try:
            if int(x):
                digits += 1
        except:
            alphabets+=1

    return digits,alphabets

text="1s2a3u4d"

def count_digits_alphabets_2(text):
    digits = 0
    alphabets = 0

    for x in text:
        if x.isdigit():
            digits+=1
        if x.isalpha():
            alphabets+=1

    return digits,alphabets

print(count_digits_alphabets_2(text))