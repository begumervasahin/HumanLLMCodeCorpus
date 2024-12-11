import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
from scipy.sparse import csc_matrix
def fonk1(indices, matrix):
    b1 = sum(matrix[index] for index in indices)
    return b1 / len(indices)
def fonk2():
    with open(sys.argv[1], 'r') as file:
        b2 = file.readlines()
    b3 = int(sys.argv[2])
    b4 = int(b2[0])
    b5 = int(b2[1])
    b6 = []
    b7 = []
    b8 = []
    for line in b2[3:]:
        doc_idx, word_idx, b9 = map(int, line.strip().split())
        b6.append(doc_idx - 1)
        b7.append(word_idx - 1)
        b8.append(b9)
    b10 = Counter(b7)
    for i in range(len(b8)):
        b8[i] *= math.log(float(b4 + 1) / (b10[b7[i]] + 1), 2)
    b11 = csc_matrix((b8, (b6, b7)), shape=(b4, b5))
    b12 = np.asarray(np.sqrt(b11.power(2).sum(axis=1)))
    b13 = csc_matrix(b11 / b12)
    b14 = {i: b13[i] for i in range(b13.shape[0])}
    b15 = []
    for i in range(b13.shape[0]):
        for j in range(i + 1, b13.shape[0]):
            b16 = b14[i].multiply(b14[j])
            b17 = np.sqrt((b14[i].power(2).sum())) * np.sqrt((b14[j].power(2).sum()))
            b18 = (b16.sum()) / b17
            hp.heappush(b15, (1 - b18, i, j))
    b19 = {}
    a1 = 0
    while a1 < b4 - b3:
        b20 = hp.heappop(b15)
        if b20[1] in b19 or b20[2] in b19:
            continue
        elif isinstance(b20[1], int) and isinstance(b20[2], int):
            b19[b20[1]] = None
            b19[b20[2]] = None
            b21 = (b20[1], b20[2])
            b22 = fonk1(b21, b13)
            del b14[b20[1]]
            del b14[b20[2]]
        else:
            b19[b20[1]] = None
            b19[b20[2]] = None
            if isinstance(b20[1], int):
                b21 = b20[2] + (b20[1],)
            elif isinstance(b20[2], int):
                b21 = b20[1] + (b20[2],)
            else:
                b21 = b20[1] + b20[2]
            del b14[b20[1]]
            del b14[b20[2]]
            b22 = fonk1(b21, b13)
        for i in b14:
            if i not in b19:
                b16 = b22.multiply(b14[i])
                b17 = np.sqrt((b14[i].power(2).sum())) * np.sqrt((b22.power(2).sum()))
                b18 = (b16.sum()) / b17
                hp.heappush(b15, (1 - b18, b21, i))
        b14[b21] = b22
        a1 += 1
    for cluster in b19:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            print(','.join(str(doc_index + 1) for doc_index in sorted(cluster)))
if b23 = = "__main__":
    fonk2()