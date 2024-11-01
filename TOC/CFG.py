import nltk
from nltk import CFG

grammar=CFG.fromstring("""
    S -> 'a'S'b' | ''               
""")

#Display the grammar
print(grammar)

#Initialize the parser with the grammar
parser=nltk.ChartParser(grammar)

test_strings=["","ab","aabb","aaabbb"]

for sentence in test_strings:
    tokens=list(sentence)

    print(f"Parsing {sentence} : ")

    try:
        for tree in parser.parse(tokens):
            print(tree)
            tree.draw()
    except ValueError:
        print("NO Valid Parse Found")