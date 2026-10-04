import sys
from math import log10
def fonk1():
    b1 = None
    a1 = 1
    b2 = {}
    b3 = []
    a2 = 10.0
    for b4 in sys.stdin:
        b4 = b4.strip()
        word, b5 = b4.split('\t', 1)
        b9, b7, b8, b6 = b5.split(' ', 3)
        b7 = float(b7)
        b8 = float(b8)
        b6 = int(b6)
        if b1 = = word:
            a1 += b6
        else:
            if b1 is not None:
                b2[b1] = f'{b7} {b8} {a1}'
                b3.append(f'{b1} {b9}')
            a1 = b6
            b1 = word
    if b1 is not None:
        b2[b1] = f'{b7} {b8} {a1}'
        b3.append(f'{b1} {b9}')
    return b3, b2, a2
def fonk2(b3, b2, a2):
    for item in b3:
        word, b9 = item.split(' ', 1)
        if word in b2:
            b7, b8, b10 = b2[word].split(' ', 2)
            b7 = float(b7)
            b8 = float(b8)
            b10 = float(b10)
            b11 = (b7 / b8) * log10(a2 / b10)
            print(f'{item}\t{b11}')
def fonk3():
    b3, b2, a2 = fonk1()
    fonk2(b3, b2, a2)
if b12 = = "__main__":
    fonk3()