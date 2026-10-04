import sys
from math import log10
def fonk1():
    b1 = None
    a1 = 1
    b2 = {}
    b3 = []
    a2 = 10.0
    a3 = 0
    for b4 in sys.stdin:
        b4 = b4.strip()
        word, b5 = b4.split('\t', 1)
        b11, b7, b8, b6 = b5.split(' ', 3)
        b7 = float(b7)
        b8 = float(b8)
        b6 = int(b6)
        if b1 = = word:
            a1 += b6
        else:
            if b1 is not None:
                b9 = f'{b7} {b8} {a1}'
                b2[b1] = b9
                b10 = f'{b1} {b11}'
                b3.append(b10)
            a1 = b6
            b1 = word
    b9 = f'{b7} {b8} {a1}'
    b2[b1] = b9
    b10 = f'{b1} {b11}'
    b3.append(b10)
    for i in b3:
        word, b11 = i.split(' ', 1)
        if word in b2:
            b7, b8, b12 = b2[word].split(' ', 2)
            b7 = float(b7)
            b8 = float(b8)
            b12 = float(b12)
            a3 = (b7 / b8) * log10(a2 / b12)
            print(f'{i}\t{a3}')
if b13 = = "__main__":
    fonk2()
import sys
from math import log10
def fonk2():
    b1 = None
    a1 = 1
    b2 = {}
    b3 = []
    a2 = 10.0
    a3 = 0
    for b4 in sys.stdin:
        b4 = b4.strip()
        word, b5 = b4.split('\t', 1)
        b11, b7, b8, b6 = b5.split(' ', 3)
        b7 = float(b7)
        b8 = float(b8)
        b6 = int(b6)
        if b1 = = word:
            a1 += b6
        else:
            if b1 is not None:
                b9 = f'{b7} {b8} {a1}'
                b2[b1] = b9
                b10 = f'{b1} {b11}'
                b3.append(b10)
            a1 = b6
            b1 = word
    b9 = f'{b7} {b8} {a1}'
    b2[b1] = b9
    b10 = f'{b1} {b11}'
    b3.append(b10)
    for i in b3:
        word, b11 = i.split(' ', 1)
        if word in b2:
            b7, b8, b12 = b2[word].split(' ', 2)
            b7 = float(b7)
            b8 = float(b8)
            b12 = float(b12)
            a3 = (b7 / b8) * log10(a2 / b12)
            print(f'{i}\t{a3}')
if b13 = = "__main__":
    fonk2()