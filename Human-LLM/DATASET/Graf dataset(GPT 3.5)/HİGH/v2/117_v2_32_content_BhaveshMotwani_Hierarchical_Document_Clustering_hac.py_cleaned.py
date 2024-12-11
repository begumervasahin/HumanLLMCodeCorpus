import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
from scipy.sparse import csc_matrix
def fonk1(indices, matrix):
    a1 = 0
    for index in indices:
        a1 += matrix[index]
    return a1 / len(indices)
def fonk2():
    b1 = list(open(sys.argv[1], 'r'))
    b2 = int(sys.argv[2])
    b3 = int(b1[0])
    b4 = int(b1[1])
    b5 = []
    b6 = []
    b7 = []
    for line in b1[3:]:
        b8 = line.strip("\n").split(" ")
        b5.append(int(b8[0]) - 1)
        b6.append(int(b8[1]) - 1)
        b7.append(int(b8[2]))
    b9 = dict(Counter(b6))
    for i in range(len(b7)):
        b7[i] = b7[i] * (math.log(float(b3 + 1) / (b9[b6[i]] + 1), 2))
    b10 = csc_matrix((b7, (b5, b6)), shape=(b3, b4))
    b11 = np.asarray(np.sqrt(b10.power(2).sum(axis=1)))
    b12 = csc_matrix(b10 / b11)
    b13 = {}
    for i in range(b12.shape[0]):
        b13[i] = b12[i]
    b14 = []
    for i in b13:
        for j in b13:
            if i < j:
                b15 = b13[i].multiply(b13[j])
                b16 = (np.sqrt(b13[i].power(2).sum())) * (np.sqrt(b13[j].power(2).sum()))
                b17 = (b15.sum()) / b16
                hp.heappush(b14, (1 - b17, i, j))
    b18 = {}
    a2 = 0
    while a2 < b3 - b2:
        b19 = hp.heappop(b14)
        if (b19[1] in b18) or (b19[2] in b18):
            continue
        elif isinstance(b19[1], int) and isinstance(b19[2], int):
            b18[b19[1]] = None
            b18[b19[2]] = None
            b20 = (b19[1], b19[2])
            b21 = fonk1(b20, b12)
            del b13[b19[1]]
            del b13[b19[2]]
        else:
            b18[b19[1]] = None
            b18[b19[2]] = None
            if isinstance(b19[1], int):
                b20 = b19[2] + (b19[1],)
            elif isinstance(b19[2], int):
                b20 = b19[1] + (b19[2],)
            else:
                b20 = b19[1] + b19[2]
            del b13[b19[1]]
            del b13[b19[2]]
            b21 = fonk1(b20, b12)
        for i in b13:
            if i not in b18:
                b15 = b21.multiply(b13[i])
                b16 = (np.sqrt(b13[i].power(2).sum())) * (np.sqrt(b21.power(2).sum()))
                b17 = (b15.sum()) / b16
                hp.heappush(b14, (1 - b17, b20, i))
        b13[b20] = b21
        a2 += 1
    for cluster in b18:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            b22 = ''
            for document_index in sorted(cluster):
                b22 += str(document_index + 1) + ','
            print(b22[:-1])
if b23 = = "__main__":
    fonk2()