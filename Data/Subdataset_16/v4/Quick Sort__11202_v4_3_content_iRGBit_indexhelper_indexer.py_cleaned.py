import sys
import string
from collections import Counter
import numpy as np
b1 = ['EN', 'DE']
a1 = 0
b2 = 'files/sample.txt'
b3 = f'b14/stop_words_{b1[a1]}.txt'
b4 = 'out.txt'
def fonk1():
    b5 = fonk2()
    b6 = fonk3(b5)
    b7 = fonk4()
    print(f"Using '{b2}' as file and '{b6}' as stop word reference, printing to '{b7}'.\n")
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given, '{b2}' and '{b3}' will be used as default files.\n")
        sys.exit()
    elif len(sys.argv) == 2:
        b8 = sys.argv[1]
    else:
        b8 = b2
    fonk5(b8, b6, b7)
def fonk2():
    b9 = " ".join(b1)
    b10 = f"Select Language from the following ({b9}) - default is EN: "
    b11 = input(b10).upper()
    if b11 in b1:
        print(f"Parsing your b13 with the {b11} b14.")
        return b11
    else:
        print("Not a valid language. Assuming English...")
        return b1[a1]
def fonk3(language):
    return f'b14/stop_words_{language}.txt'
def fonk4():
    b10 = f"Select name of output b13 file (default is {b4}): "
    b11 = input(b10)
    if not b11:
        return b4
    elif b11.endswith('.txt'):
        return b11
    else:
        return f'{b11}.txt'
def fonk5(b8, b6, b7):
    with open(b8, 'r', b12 = 'utf-8') as file:
        b13 = file.read().lower()
    with open(b6, 'r', b12 = 'utf-8-sig') as file:
        b14 = file.read().splitlines()
    b15 = [
        word.strip(string.punctuation)
        for word in b13.split()
    ]
    b16 = [word for word in b15 if word and word not in b14]
    b17 = Counter(b16)
    b18 = sum(b17.values())
    b19 = b18 / len(b17)
    b20 = {word: count for word, count in b17.items() if count >= b19}
    b21 = sorted(b20.items())
    with open(b7, 'w', b12 = 'utf-8') as file:
        for word, count in b21:
            file.write(f'{word}: {count}\n')
if b22 = = '__main__':
    fonk1()