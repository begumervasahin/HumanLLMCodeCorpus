import numpy as np
import sys
b1 = []
a1 = 0
b2 = dict()
b3 = []
a2 = -2
a3 = -1
for b4 in sys.stdin:
    b4 = b4.strip()
    b7, b8, b5 = b4.split('\t')
    b6 = [float(x) for x in b5.split(',')]
    b6 = np.array(b6)
    a3 = len(b6)
    b7 = int(b7)
    b8 = int(b8)
    if a2 != b7:
        if a2 != -2:
            b9 = b3 / len(b1)
            print('%s\t%s\t%s' % (a2, ','.join(map(str, b1)), ','.join(map(str, b9))))
        b1 = []
        b3 = np.zeros(len(b6))
        a2 = b7
    b1.append(b8)
    b3 += b6
b9 = b3 / len(b1)
print('%s\t%s\t%s' % (a2, ','.join(map(str, b1)), ','.join(map(str, b9))))