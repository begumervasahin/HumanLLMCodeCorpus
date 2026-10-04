import numpy as np
import sys
def fonk1():
    b1 = None
    b2 = []
    b3 = None
    for b4 in sys.stdin:
        b4 = b4.strip()
        b7, b8, b5 = b4.split('\t')
        b6 = np.array([float(value) for value in b5.split(',')])
        b7 = int(b7)
        b8 = int(b8)
        if b1 is None or b1 != b7:
            if b1 is not None:
                b9 = b3 / len(b2)
                print(f'{b1}\t{",".join(map(str, b2))}\t{",".join(map(str, b9))}')
            b1 = b7
            b2 = []
            b3 = np.zeros(len(b6))
        b2.append(b8)
        b3 += b6
    if b1 is not None:
        b9 = b3 / len(b2)
        print(f'{b1}\t{",".join(map(str, b2))}\t{",".join(map(str, b9))}')
if b10 = = "__main__":
    fonk1()