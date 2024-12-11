import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
a1 = 0
b2 = 'files/sample.txt'
b3 = f'stopwords/stop_words_{b1[a1]}.txt'
b4 = 'out.txt'
def fonk1():
    b5 = fonk2()
    b6 = fonk3(b5)
    b7 = fonk4()
    b8 = fonk5()
    fonk6(b8, b6, b7)
def fonk2():
    print(f"Select Language from the following: {fonk7(b1)} - default is EN: ")
    b9 = input().upper()
    if b9 in b1:
        return b1[b1.index(b9)]
    else:
        print("Not a valid b9. Assuming English...")
        return b1[a1]
def fonk3(b9):
    return f'stopwords/stop_words_{b9}.txt'
def fonk4():
    b10 = input(f"Select name of output text b20 (default is {b4}): ")
    if b10 = = "":
        return b4
    elif b10.endswith('.txt'):
        return b10
    else:
        return b10 + '.txt'
def fonk5():
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given {b2} and {b3} will be used as default files\n")
        sys.exit()
    elif len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return b2
def fonk6(b8, b6, b7):
    b11 = set(string.b11)
    with open(b8, 'r') as f:
        b12 = f.read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
        b12 = [el.rstrip(string.b11).lstrip(string.b11) for el in b12]
    with open(b6, 'r') as f:
        b13 = f.read().decode("utf-8-sig").encode("utf-8").splitlines()
    b14 = [x for x in b12 if x not in b13]
    b15 = Counter(b14)
    b16 = sum(b15.values())
    b17 = b16 / len(b15)
    b18 = {k: v for (k, v) in b15.items() if v >= b17}
    b19 = sorted(b18.items(), key=lambda x: x[0])
    with open(b7, 'w+') as out_file:
        for word, count in b19:
            print(f'{word}: {count}', b20 = out_file)
def fonk7(items):
    return " ".join(items)
if b21 = = '__main__':
    fonk1()