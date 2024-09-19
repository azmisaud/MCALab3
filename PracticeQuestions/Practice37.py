def is_pangram(text):
    text_lower=text.lower()

    alphabets=set('abcdefghijklmnopqrstuvwxyz')

    text_set=set(char for char in text_lower if char.isalpha())

    return text_set.issubset(alphabets)

text="abc def gh i jk l m no p q r s t u v w x y z"

print(is_pangram(text))