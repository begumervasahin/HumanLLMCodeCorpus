import sys
import numpy as np
def fonk1():
    def fonk2(b10, b5, b6):
        if b5:
            b1 = b6 / len(b5)
            b2 = ",".join(map(str, b1))
            b3 = ",".join(map(str, b5))
            print(f'{b10}\t{b3}\t{b2}')
    b4 = None
    b5 = []
    b6 = None
    for b7 in sys.stdin:
        b7 = b7.strip()
        b10, b11, b8 = b7.split('\t')
        b9 = np.array([float(value) for value in b8.split(',')])
        b10 = int(b10)
        b11 = int(b11)
        if b4 is None or b4 != b10:
            if b4 is not None:
                fonk2(b4, b5, b6)
            b4 = b10
            b5 = []
            b6 = np.zeros(len(b9))
        b5.append(b11)
        b6 += b9
    if b4 is not None:
        fonk2(b4, b5, b6)
if b12 = = "__main__":
    fonk1()