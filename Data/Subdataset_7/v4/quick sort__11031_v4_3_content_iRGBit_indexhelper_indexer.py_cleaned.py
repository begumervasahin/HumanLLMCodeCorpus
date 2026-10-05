import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
a1 = 0
b2 = 'files/sample.txt'
b3 = f'stopwords/stop_words_{b1[a1]}.txt'
b4 = 'out.txt'
def fonk1():
    print(f"Select Language from the following: {fonk2(b1)} - default is EN: ")
    b5 = input().upper()
    if b5 in b1:
        b6 = b1[b1.index(b5)]
        b7 = f'stopwords/stop_words_{b6}.txt'
        print(f"Parsing your text with the {b6} stopwords")
    else:
        b7 = b3
        print("Not a valid language. Assuming English...")
    b8 = input(f"Select name of output text b21 (default is {b4}): ")
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
    elif len(sys.argv) == 1:
        b10 = b2
    print(f'Using {b10} as b21 and {b7} as stop word reference, printing to {b9}.\n')
    fonk3(b10, b7, b9)
def fonk2(alist):
    b11 = ""
    for a in alist:
        b11 = b11 + " " + a
    return b11
def fonk3(b10, b7, b9):
    b12 = set(string.punctuation)
    with open(b10, 'r') as f:
        b13 = f.read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
        b13 = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in b13]
    with open(b7, 'r') as f:
        b14 = f.read().decode("utf-8-sig").encode("utf-8").splitlines()
    b15 = [x for x in b13 if x not in b14]
    b16 = Counter(b15)
    b17 = sum(b16.values())
    b18 = b17 / len(b16)
    b19 = {k: v for (k, v) in b16.items() if v >= b18}
    b20 = sorted(b19.items(), key=lambda x: x[0])
    with open(b9, 'w+') as outFile:
        for x in range(len(b20)):
            print(f'{b20[x][0]}: {b20[x][1]}', b21 = outFile)
if b22 = = '__main__':
    fonk1()