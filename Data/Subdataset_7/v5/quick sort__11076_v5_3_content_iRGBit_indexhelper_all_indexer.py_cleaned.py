import sys
import string
from collections import Counter
b1 = 'files/sample.txt'
b2 = 'b6.txt'
def fonk1():
    if len(sys.argv) > 3:
        print("Usage: python indexer.py <yourFile> <stopWords>")
        print("If no arguments are given, {} and {} will be used as default files".format(b1, b2))
        sys.exit()
    your_file, b3 = fonk2()
    print('Using {} as file and {} as stop word reference.'.format(your_file, b3))
    print()
    fonk3(your_file, b3)
def fonk2():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 2:
        return sys.argv[1], b2
    else:
        return b1, b2
def fonk3(your_file, b3):
    b4 = set(string.punctuation)
    with open(your_file) as file:
        b5 = file.read().lower().split()
        b5 = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in b5]
    with open(b3) as file:
        b6 = file.read().splitlines()
    b7 = [x for x in b5 if x not in b6]
    b8 = Counter(b7)
    b9 = sorted(b8.items(), key=lambda x: x[0])
    for word, count in b9:
        print('{}: {}'.format(word, count))
if b10 = = '__main__':
    fonk1()