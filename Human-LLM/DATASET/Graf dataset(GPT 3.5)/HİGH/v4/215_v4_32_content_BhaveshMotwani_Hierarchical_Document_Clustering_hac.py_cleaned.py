from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def fonk1(indices, matrix):
    b1 = sum(matrix[i] for i in indices)
    return b1 / len(indices)
b2 = sys.argv[1]
b3 = int(sys.argv[2])
with open(b2, 'r') as file:
    b4 = file.readlines()
b5 = int(b4[0])
b6 = int(b4[1])
b7 = []
b8 = []
b9 = []
for line in b4[3:]:
    doc_idx, word_idx, b10 = map(int, line.strip().split())
    b7.append(doc_idx - 1)
    b8.append(word_idx - 1)
    b9.append(b10)
b11 = Counter(b8)
for i in range(len(b9)):
    b9[i] *= math.log(float(b5 + 1) / (b11[b8[i]] + 1), 2)
b12 = csc_matrix((b9, (b7, b8)), shape=(b5, b6))
b13 = np.asarray(np.sqrt(b12.power(2).sum(axis=1)))
b14 = csc_matrix(b12 / b13)
b15 = {i: b14[i] for i in range(b14.shape[0])}
b16 = []
for i in range(b14.shape[0]):
    for j in range(i + 1, b14.shape[0]):
        b17 = b15[i].multiply(b15[j])
        b18 = np.sqrt((b15[i].power(2).sum())) * np.sqrt((b15[j].power(2).sum()))
        b19 = (b17.sum()) / b18
        hp.heappush(b16, (1 - b19, i, j))
b20 = {}
a1 = 0
while a1 < b5 - b3:
    b21 = hp.heappop(b16)
    if b21[1] in b20 or b21[2] in b20:
        continue
    elif isinstance(b21[1], int) and isinstance(b21[2], int):
        b20[b21[1]] = None
        b20[b21[2]] = None
        b22 = (b21[1], b21[2])
        b23 = fonk1(b22, b14)
        del b15[b21[1]]
        del b15[b21[2]]
    else:
        b20[b21[1]] = None
        b20[b21[2]] = None
        if isinstance(b21[1], int):
            b22 = b21[2] + (b21[1],)
        elif isinstance(b21[2], int):
            b22 = b21[1] + (b21[2],)
        else:
            b22 = b21[1] + b21[2]
        del b15[b21[1]]
        del b15[b21[2]]
        b23 = fonk1(b22, b14)
    for i in b15:
        if i not in b20:
            b17 = b23.multiply(b15[i])
            b18 = np.sqrt((b15[i].power(2).sum())) * np.sqrt((b23.power(2).sum()))
            b19 = (b17.sum()) / b18
            hp.heappush(b16, (1 - b19, b22, i))
    b15[b22] = b23
    a1 += 1
for cluster in b20:
    if isinstance(cluster, int):
        print(cluster + 1)
    else:
        print(','.join(str(doc_index + 1) for doc_index in sorted(cluster)))