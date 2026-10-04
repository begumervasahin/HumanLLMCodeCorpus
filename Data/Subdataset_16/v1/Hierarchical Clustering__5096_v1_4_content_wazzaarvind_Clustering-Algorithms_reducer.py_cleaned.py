import numpy as np
import sys
def fonk1():
    b1 = []
    b2 = []
    a1 = -2
    a2 = -1
    for b3 in sys.stdin:
        b3 = b3.strip()
        b6, b7, b4 = b3.split('\t')
        b5 = np.array([float(x) for x in b4.split(',')])
        a2 = len(b5)
        b6 = int(b6)
        b7 = int(b7)
        if a1 != b6:
            if a1 != -2:
                b8 = b2 / len(b1)
                print(f'{a1}\t{",".join(map(str, b1))}\t{",".join(map(str, b8))}')
            b1 = []
            b2 = np.zeros(len(b5))
            a1 = b6
        b1.append(b7)
        b2 += b5
    b8 = b2 / len(b1)
    print(f'{a1}\t{",".join(map(str, b1))}\t{",".join(map(str, b8))}')
if b9 = = "__main__":
    fonk1()