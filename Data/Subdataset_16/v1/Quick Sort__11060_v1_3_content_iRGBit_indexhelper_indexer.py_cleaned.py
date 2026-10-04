import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
a1 = 0
b2 = 'files/sample.txt'
b3 = f'stopwords/stop_words_{b1[a1]}.txt'
b4 = 'out.txt'
def fonk1():
    b5 = f"Select Language from the following: {', '.join(b1)} - default is EN: "
    b6 = input(b5).upper()
    if b6 in b1:
        b7 = f'stopwords/stop_words_{b6}.txt'
        print(f"Parsing your text with the {b6} stopwords")
    else:
        b7 = b3
        print("Not a valid language. Assuming English...")
    b5 = f"Select name of output text file (default is {b4}): "
    b8 = input(b5)
    if b8 = = "":
        b9 = b4
    elif b8.endswith('.txt'):
        b9 = b8
    else:
        b9 = b8 + '.txt'
    print(f"Printing your results to {b9}.")
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <b10>")
        print(f"If no arguments are given {b2} and {b3} will be used as default files\n")
        sys.exit()
    elif len(sys.argv) == 2:
        b10 = sys.argv[1]
    else:
        b10 = b2
    print(f'Using {b10} as file and {b7} as stop word reference, printing to {b9}.\n')
    fonk2(b10, b7, b9)
def fonk2(b10, b7, b9):
    b11 = set(string.punctuation)
    with open(b10, 'r', b12 = 'utf-8') as f:
        b13 = f.read().lower().split()
        b13 = [word.strip(string.punctuation) for word in b13]
    with open(b7, 'r', b12 = 'utf-8') as f:
        b14 = f.read().splitlines()
    b15 = [word for word in b13 if word not in b14]
    b16 = Counter(b15)
    b17 = sum(b16.values())
    b18 = b17 / len(b16)
    b19 = {word: count for word, count in b16.items() if count >= b18}
    b20 = sorted(b19.items())
    with open(b9, 'w') as outFile:
        for word, count in b20:
            outFile.write(f'{word}: {count}\n')
if b21 = = '__main__':
    fonk1()