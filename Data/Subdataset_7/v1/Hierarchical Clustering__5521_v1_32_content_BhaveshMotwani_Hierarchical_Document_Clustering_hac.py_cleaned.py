from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def fonk1(sic, b8):
    a1 = 0
    for i in sic:
        a1 += b8[i]
    return a1 / len(sic)
def fonk2():
    b1 = list(open(sys.argv[1], 'r'))
    b2 = int(sys.argv[2])
    b3 = int(b1[0])
    b4 = int(b1[1])
    b5 = np.zeros((b3, b4))
    b6 = []
    b7 = []
    b8 = []
    for i in range(3, len(b1)):
        b9 = b1[i].strip("\n").split(" ")
        b6.append(int(b9[0]) - 1)
        b7.append(int(b9[1]) - 1)
        b8.append(int(b9[2]))
    b10 = dict(Counter(b7))
    for i in range(len(b7)):
        b8[i] = b8[i] * (math.log(float(b3 + 1) / (b10[b7[i]] + 1), 2))
    b11 = csc_matrix((b8, (b6, b7)), shape=(b3, b4))
    b12 = np.asarray(np.sqrt(b11.power(2).sum(axis=1)))
    b5 = csc_matrix(b11 / b12)
    print(b5[24])
    b13 = {}
    for i in range(b5.shape[0]):
        b13[i] = b5[i]
    b14 = []
    for i in b13:
        for j in b13:
            if (i < j):
                b15 = b13[i].multiply(b13[j])
                b16 = (np.sqrt(b13[i].power(2).sum())) * (np.sqrt(b13[j].power(2).sum()))
                b15 = (b15.sum()) / b16
                hp.heappush(b14, (1 - b15, i, j))
    b17 = {}
    a2 = 0
    while a2 < b3 - b2:
        b18 = hp.heappop(b14)
        if (b18[1] in b17) or (b18[2] in b17):
            continue
        elif isinstance(b18[1], int) and isinstance(b18[2], int):
            b17[b18[1]] = None
            b17[b18[2]] = None
            b19 = (b18[1], b18[2])
            b20 = fonk1(b19, b5)
            del b13[b18[1]]
            del b13[b18[2]]
        else:
            b17[b18[1]] = None
            b17[b18[2]] = None
            if isinstance(b18[1], int):
                b19 = b18[2] + (b18[1],)
            elif isinstance(b18[2], int):
                b19 = b18[1] + (b18[2],)
            else:
                b19 = b18[1] + b18[2]
            del b13[b18[1]]
            del b13[b18[2]]
            b20 = fonk1(b19, b5)
        for i in b13:
            if i not in b17:
                b15 = b20.multiply(b13[i])
                b16 = (np.sqrt(b13[i].power(2).sum())) * (np.sqrt(b20.power(2).sum()))
                b15 = (b15.sum()) / b16
                hp.heappush(b14, (1 - b15, b19, i))
        b13[b19] = b20
        a2 += 1
    for i in b13:
        if isinstance(i, int):
            print(i + 1)
        else:
            b21 = ''
            for j in sorted(i):
                b21 += str(j + 1) + ','
            print(b21[:-1])
if b22 = = "__main__":
    fonk2()