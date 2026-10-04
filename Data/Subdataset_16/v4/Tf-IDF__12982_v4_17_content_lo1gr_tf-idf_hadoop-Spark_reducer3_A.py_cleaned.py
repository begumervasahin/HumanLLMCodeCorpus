from operator import itemgetter
import sys
from math import log10
b1 = None
a1 = 1
b2 = None
b3 = {}
b4 = []
a2 = 10.0
for b5 in sys.stdin:
    b5 = b5.strip()
    b2, b6 = b5.split('\t', 1)
    b9, b11, b12, b7 = b6.split(' ', 3)
    if b1 = = b2:
        a1 += int(b7)
    else:
        if b1 is not None:
            b8 = f"{b11} {b12} {a1}"
            b3[b1] = b8
            b4.append(f"{b1} {b9}")
        a1 = 1
        b1 = b2
b8 = f"{b11} {b12} {a1}"
b3[b1] = b8
b4.append(f"{b1} {b9}")
for item in b4:
    b2, b9 = item.split(' ', 1)
    if b2 in b3:
        b11, b12, b10 = b3[b2].split(' ', 2)
        b11 = float(b11)
        b12 = float(b12)
        b10 = float(b10)
        b13 = (b11 / b12) * log10(a2 / b10)
        print(f'{item}\t{b13}')