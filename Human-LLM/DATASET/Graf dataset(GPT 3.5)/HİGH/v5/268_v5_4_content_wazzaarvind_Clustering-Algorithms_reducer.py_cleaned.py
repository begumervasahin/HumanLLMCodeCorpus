import numpy as np
import sys
def fonk1(line):
    b2, b3, b1 = line.strip().split('\t')
    b2 = int(b2)
    b3 = int(b3)
    b4 = np.array([float(x) for x in b1.split(',')])
    return b2, b3, b4
def fonk2(b2, b6, b8):
    b5 = '%s\t%s\t%s' % (b2, ','.join(map(str, b6)), ','.join(map(str, b8)))
    print(b5)
b6 = []
b7 = []
a1 = -2
a2 = -1
for line in sys.stdin:
    b2, b3, b4 = fonk1(line)
    a2 = len(b4)
    if a1 != b2:
        if a1 != -2:
            b8 = b7 / len(b6)
            fonk2(a1, b6, b8)
        b6 = []
        b7 = np.zeros(a2)
        a1 = b2
    b6.append(b3)
    b7 += b4
b8 = b7 / len(b6)
fonk2(a1, b6, b8)