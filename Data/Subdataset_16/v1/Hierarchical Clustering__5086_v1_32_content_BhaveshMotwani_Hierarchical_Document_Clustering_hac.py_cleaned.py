from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
from collections import Counter
import sys
def fonk1(indices, matrix):
    return sum(matrix[i] for i in indices) / len(indices)
def fonk2(b19):
    with open(b19, 'r') as file:
        b1 = file.readlines()
    b2 = int(b1[0].strip())
    b3 = int(b1[1].strip())
    b4 = []
    b5 = []
    b6 = []
    for line in b1[2:]:
        doc_id, word_id, b7 = map(int, line.split())
        b4.append(doc_id - 1)
        b5.append(word_id - 1)
        b6.append(b7)
    return b2, b3, b4, b5, b6
def fonk3(b2, b3, b4, b5, b6):
    b8 = dict(Counter(b5))
    for i in range(len(b6)):
        b6[i] *= math.log((b2 + 1) / (b8[b5[i]] + 1), 2)
    b9 = csc_matrix((b6, (b4, b5)), shape=(b2, b3))
    b10 = np.sqrt(b9.power(2).sum(axis=1))
    b11 = b9 / b10
    return b11
def fonk4(b11, b2, b20):
    b12 = {i: b11[i] for i in range(b11.shape[0])}
    b13 = {}
    b14 = []
    for i in b12:
        for j in b12:
            if i < j:
                b15 = (b12[i].multiply(b12[j]).sum()) / \
                             (np.sqrt(b12[i].power(2).sum()) * np.sqrt(b12[j].power(2).sum()))
                hp.heappush(b14, (1 - b15, i, j))
    a1 = 0
    while a1 < b2 - b20:
        _, cluster1, b16 = hp.heappop(b14)
        if cluster1 in b13 or b16 in b13:
            continue
        b13[cluster1] = None
        b13[b16] = None
        if isinstance(cluster1, int) and isinstance(b16, int):
            b17 = (cluster1, b16)
        elif isinstance(cluster1, int):
            b17 = (cluster1,) + b16
        elif isinstance(b16, int):
            b17 = cluster1 + (b16,)
        else:
            b17 = cluster1 + b16
        b18 = fonk1(b17, b11)
        del b12[cluster1]
        del b12[b16]
        for i in b12:
            if i not in b13:
                b15 = (b18.multiply(b12[i]).sum()) / \
                             (np.sqrt(b12[i].power(2).sum()) * np.sqrt(b18.power(2).sum()))
                hp.heappush(b14, (1 - b15, b17, i))
        b12[b17] = b18
        a1 += 1
    return b12
def fonk5(b12):
    for cluster in b12:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            print(','.join(str(idx + 1) for idx in sorted(cluster)))
def fonk6():
    b19 = sys.argv[1]
    b20 = int(sys.argv[2])
    b2, b3, b4, b5, b6 = fonk2(b19)
    b11 = fonk3(b2, b3, b4, b5, b6)
    b12 = fonk4(b11, b2, b20)
    fonk5(b12)
if b21 = = "__main__":
    fonk6()