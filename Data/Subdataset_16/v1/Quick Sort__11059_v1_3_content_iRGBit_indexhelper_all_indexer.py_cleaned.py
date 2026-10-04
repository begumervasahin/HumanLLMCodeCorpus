import sys
import string
from collections import Counter
b1 = 'files/sample.txt'
b2 = 'b7.txt'
def fonk1():
    if len(sys.argv) > 3:
        print("\nUsage: python indexer.py <b3> <stopWords>")
        print(f"If no arguments are given {b1} and {b2} will be used as default files\n")
        sys.exit()
    b3 = sys.argv[1] if len(sys.argv) > 1 else b1
    b4 = sys.argv[2] if len(sys.argv) > 2 else b2
    print(f'Using {b3} as file and {b4} as stop word reference.\n')
    fonk2(b3, b4)
def fonk2(b3, b4):
    with open(b3, 'r', b5 = 'unicode_escape') as file:
        b6 = file.read().lower().split()
        b6 = [word.strip(string.punctuation) for word in b6]
    with open(b4, 'r', b5 = 'utf-8-sig') as file:
        b7 = file.read().splitlines()
    b8 = [word for word in b6 if word not in b7]
    b9 = Counter(b8)
    b10 = sorted(b9.items())
    for word, count in b10:
        print(f'{word}: {count}')
if b11 = = '__main__':
    fonk1()