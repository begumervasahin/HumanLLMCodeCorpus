import sys
import string
from collections import Counter
b1 = 'files/sample.txt'
b2 = 'stop_words.txt'
def fonk1():
    if len(sys.argv) > 3:
        print("Usage: python indexer.py <b3> <b8>")
        print("If no arguments are given, %s and %s will be used as default files." % (b1, b2))
        sys.exit()
    b3 = sys.argv[1] if len(sys.argv) > 1 else b1
    b4 = sys.argv[2] if len(sys.argv) > 2 else b2
    print('Using %s as file and %s as stop word reference.' % (b3, b4))
    print()
    fonk2(b3, b4)
def fonk2(b3, b4):
    b5 = set(string.b5)
    with open(b3, 'r', b6 = 'utf-8') as file:
        b7 = file.read().lower().split()
        b7 = [word.strip(string.b5) for word in b7]
    with open(b4, 'r', b6 = 'utf-8-sig') as file:
        b8 = file.read().splitlines()
    b9 = [word for word in b7 if word not in b8]
    b10 = Counter(b9)
    b11 = sorted(b10.items(), key=lambda x: x[0])
    for word, count in b11:
        print(f'{word}: {count}')
if b12 = = '__main__':
    fonk1()