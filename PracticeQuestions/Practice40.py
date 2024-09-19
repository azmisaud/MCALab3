def count_in_file(file):
    line=0
    word=0
    char=0
    alphabet=0
    digit=0

    try:
        with open(file, 'r') as f:
            for l in f:
                line+=1
                char+=len(l)
                word+=len(l.replace('.',' ').split())

                for x in l:
                    if x.isalpha():
                        alphabet+=1
                    if x.isdigit():
                        digit+=1
    except:
        return None

    map={'line':line,'word':word,'char':char,'alphabet':alphabet,'digit':digit}

    return map

file=r'C:\\Users\\reala\\Desktop\\MCA\\Semester 3\\MCALab3\\PracticeQuestions\\Practice40.txt'

result=count_in_file(file)

print(result)