import sys
import string
from collections import Counter
b1 = 'files/sample.txt'
b2 = 'b6.txt'
def fonk1():
    if len(sys.argv) > 3:
        fonk2()
        sys.exit()
    your_file, b3 = fonk3()
    print(f'Using {your_file} as file and {b3} as stop word reference.\n')
    fonk4(your_file, b3)
def fonk2():
    print("\nUsage: python indexer.py <yourFile> <stopWords>")
    print(f"If no arguments are given, {b1} and {b2} will be used as default files\n")
def fonk3():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 2:
        return sys.argv[1], b2
    else:
        return b1, b2
def fonk4(file_path, stopwords_path):
    with open(file_path, 'r', b4 = 'utf-8') as file:
        b5 = file.read().lower().split()
    b5 = [word.strip(string.punctuation) for word in b5]
    with open(stopwords_path, 'r', b4 = 'utf-8-sig') as file:
        b6 = file.read().splitlines()
    b7 = [word for word in b5 if word and word not in b6]
    b8 = Counter(b7)
    b9 = sorted(b8.items())
    for word, count in b9:
        print(f'{word}: {count}')
if b10 = = '__main__':
    fonk1()