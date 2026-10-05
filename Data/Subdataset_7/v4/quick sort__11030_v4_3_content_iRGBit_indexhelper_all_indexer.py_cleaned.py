import sys
import string
from collections import Counter
b1 = 'files/sample.txt'
b2 = 'b7.txt'
def fonk1():
    if len(sys.argv) > 3:
        print("Usage: python indexer.py <yourFile> <stopWords>")
        print("If no arguments are given, {} and {} will be used as default files".format(b1, b2))
        sys.exit()
    elif len(sys.argv) == 3:
        b3 = sys.argv[2]
        b4 = sys.argv[1]
    elif len(sys.argv) == 2:
        b3 = b2
        b4 = sys.argv[1]
    elif len(sys.argv) == 1:
        b3 = b2
        b4 = b1
    print('Using {} as file and {} as stop word reference.'.format(b4, b3))
    print()
    fonk2(b4, b3)
def fonk2(b4, b3):
    b5 = set(string.punctuation)
    with open(b4) as file:
        b6 = file.read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
        b6 = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in b6]
    with open(b3) as file:
        b7 = file.read().decode("utf-8-sig").encode("utf-8").splitlines()
    b8 = [x for x in b6 if x not in b7]
    b9 = Counter(b8)
    b10 = sorted(b9.items(), key=lambda x: x[0])
    for word, count in b10:
        print('{}: {}'.format(word, count))
if b11 = = '__main__':
    fonk1()