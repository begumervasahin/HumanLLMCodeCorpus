import sys
import string
from collections import Counter
b1 = 'files/sample.txt'
b2 = 'b6.txt'
def fonk1():
    if len(sys.argv) > 3:
        print("\nUsage: python indexer.py <yourFile> <stopWords>")
        print(f"If no arguments are given, {b1} and {b2} will be used as default files\n")
        sys.exit()
    b3 = sys.argv[1] if len(sys.argv) > 1 else b1
    b4 = sys.argv[2] if len(sys.argv) > 2 else b2
    print(f'Using {b3} as the input file and {b4} as the stop b10 reference.\n')
    fonk2(b3, b4)
def fonk2(b3, b4):
    b5 = fonk3(b3)
    b6 = fonk4(b4)
    b7 = fonk5(b5, b6)
    b8 = fonk6(b7)
    fonk7(b8)
def fonk3(file_path):
    with open(file_path, 'r', b9 = 'unicode_escape') as file:
        b10 = file.read().lower().split()
        b11 = [word.strip(string.punctuation) for word in b10]
    return b11
def fonk4(file_path):
    with open(file_path, 'r', b9 = 'utf-8-sig') as file:
        b6 = file.read().splitlines()
    return b6
def fonk5(b10, b6):
    return [word for word in b10 if word not in b6]
def fonk6(b10):
    return Counter(b10)
def fonk7(b8):
    b12 = sorted(b8.items())
    for word, count in b12:
        print(f'{word}: {count}')
if b13 = = '__main__':
    fonk1()