from operator import itemgetter
import sys
from math import log10
b1 = None
a1 = 1
b2 = {}
b3 = []
a2 = 10.0
for b4 in sys.stdin:
    b4 = b4.strip()
    b10, b5 = b4.split('\t', 1)
    b9, word_count, doc_word_total, b6 = b5.split(' ', 3)
    if b1 = = b10:
        a1 += int(b6)
    else:
        if b1 is not None:
            b7 = word_count + ' ' + doc_word_total + ' ' + str(a1)
            b2[b1] = b7
            b8 = b1 + ' ' + b9
            b3.append(b8)
        a1 = 1
        b1 = b10
b7 = word_count + ' ' + doc_word_total + ' ' + str(a1)
b2[b1] = b7
b8 = b1 + ' ' + b9
b3.append(b8)
for b8 in b3:
    b10, b9 = b8.split(' ', 1)
    for w in b2:
        if b10 = = w:
            b12, b13, b11 = b2[w].split(' ', 2)
            b12 = float(b12)
            b13 = float(b13)
            b11 = float(b11)
            b14 = (b12 / b13) * log10(a2 / b11)
            print('%s\t%s' % (b8, b14))