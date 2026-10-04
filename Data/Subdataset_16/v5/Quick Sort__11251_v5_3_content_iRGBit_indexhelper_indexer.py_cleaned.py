import sys
import string
from collections import Counter
import numpy as np
b1 = ['EN', 'DE']
b2 = 'EN'
b3 = 'files/sample.txt'
b4 = f'b13/stop_words_{b2}.txt'
b5 = 'out.txt'
def fonk1():
    b6 = fonk3()
    b7 = fonk4(b6)
    b8 = fonk5()
    print(f"Using '{b3}' as input file and '{b7}' as stop b14 reference, outputting to '{b8}'.\n")
    if len(sys.argv) > 2:
        fonk2()
        sys.exit()
    elif len(sys.argv) == 2:
        b9 = sys.argv[1]
    else:
        b9 = b3
    fonk6(b9, b7, b8)
def fonk2():
    print("\nUsage: python indexer.py <yourFile>")
    print(f"If no arguments are given, '{b3}' and '{b4}' will be used as default files.\n")
def fonk3():
    b10 = f"Select Language from the following ({', '.join(b1)}) - default is {b2}: "
    b11 = input(b10).upper()
    if b11 in b1:
        print(f"Parsing your b12 with the {b11} b13.")
        return b11
    else:
        print("Not a valid language. Assuming English...")
        return b2
def fonk4(language):
    return f'b13/stop_words_{language}.txt'
def fonk5():
    b10 = f"Select name of output b12 file (default is {b5}): "
    b11 = input(b10)
    if not b11:
        return b5
    return b11 if b11.endswith('.txt') else f'{b11}.txt'
def fonk6(b9, b7, b8):
    b12 = fonk7(b9).lower()
    b13 = fonk7(b7, b19='utf-8-sig').splitlines()
    b14 = fonk8(b12)
    b15 = [word for word in b14 if word and word not in b13]
    b16 = Counter(b15)
    b17 = fonk9(b16)
    b18 = sorted(b17.items())
    fonk10(b18, b8)
def fonk7(file_path, b19 = 'utf-8'):
    with open(file_path, 'r', b19 = b19) as file:
        return file.read()
def fonk8(b12):
    return [word.strip(string.punctuation) for word in b12.split()]
def fonk9(b16):
    b20 = sum(b16.values())
    b21 = b20 / len(b16)
    return {word: count for word, count in b16.items() if count >= b21}
def fonk10(b17, b8):
    with open(b8, 'w', b19 = 'utf-8') as file:
        for word, count in b17:
            file.write(f'{word}: {count}\n')
if b22 = = '__main__':
    fonk1()