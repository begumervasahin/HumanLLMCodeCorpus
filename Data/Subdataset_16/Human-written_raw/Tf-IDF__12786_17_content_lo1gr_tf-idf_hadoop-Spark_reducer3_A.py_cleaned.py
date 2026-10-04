from operator import itemgetter
import sys
from math import log10, sqrt
b1 = None
a1 = 1
b2 = None
b3 = {}
b4 = []
a2 = 10.0
a3 = 0
for b5 in sys.stdin:
    b5 = b5.strip()
    b2, b6 = b5.split('\t', 1)
    b10, b12, b13, b7 = b6.split(' ', 3)
    if b1 = = b2:
        a1 += int(b7)
    else:
        if b1 != None:
            b8 = b12 + ' ' + b13 + ' ' + str(a1)
            b3[b1] = b8
            b9 = b1 + ' ' + b10
            b4.append(b9)
        a1 = 1
        b1 = b2
b8 = b12 + ' ' + b13 + ' ' + str(a1)
b3[b1] = b8
b9 = b1 + ' ' + b10
b4.append(b9)
for i in b4:
    b2, b10 = i.split(' ', 1)
    for w in b3:
        if b2 = = w:
            b12, b13, b11 = b3[w].split(' ', 2)
            b12 = float(b12)
            b13 = float(b13)
            b11 = float(b11)
            a3 = (b12 / b13) * log10(a2 / b11)
            print '%b6\t%b6' % (i, a3)