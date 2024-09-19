def count_words(text):
    lines=text.split('.')

    map={}

    for i,line in enumerate(lines):
        words = line.split()

        map[f"Line {i+1}"]=len(words)

    return map

text="Saud is pursuing MCA. Moaz is pursuing MCA. Shuja is doing something else. Azhar is sleeping."

map=count_words(text)

print(map)