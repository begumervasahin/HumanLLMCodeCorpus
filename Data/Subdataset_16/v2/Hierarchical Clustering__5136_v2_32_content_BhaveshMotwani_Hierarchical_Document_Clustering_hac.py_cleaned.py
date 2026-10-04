from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
from collections import Counter
import sys
def fonk1(cluster_indices, matrix):
    b1 = sum(matrix[i] for i in cluster_indices) / len(cluster_indices)
    return b1
def fonk2(b21):
    with open(b21, 'r') as file:
        b2 = file.readlines()
    b3 = int(b2[0].strip())
    b4 = int(b2[1].strip())
    b5 = []
    b6 = []
    b7 = []
    for line in b2[2:]:
        doc_id, word_id, b8 = map(int, line.split())
        b5.append(doc_id - 1)
        b6.append(word_id - 1)
        b7.append(b8)
    return b3, b4, b5, b6, b7
def fonk3(b3, b4, b5, b6, b7):
    b9 = Counter(b6)
    for i in range(len(b7)):
        b10 = math.log((b3 + 1) / (b9[b6[i]] + 1), 2)
        b7[i] *= b10
    b11 = csc_matrix((b7, (b5, b6)), shape=(b3, b4))
    b12 = np.sqrt(b11.power(2).sum(axis=1))
    b13 = b11 / b12
    return b13
def fonk4(b13, b3, b22):
    b14 = {i: b13[i] for i in range(b13.shape[0])}
    b15 = {}
    b16 = []
    for i in b14:
        for j in b14:
            if i < j:
                b17 = (b14[i].multiply(b14[j]).sum()) / \
                             (np.sqrt(b14[i].power(2).sum()) * np.sqrt(b14[j].power(2).sum()))
                hp.heappush(b16, (1 - b17, i, j))
    while len(b14) > b22:
        _, cluster1, b18 = hp.heappop(b16)
        if cluster1 in b15 or b18 in b15:
            continue
        b15[cluster1] = None
        b15[b18] = None
        b19 = (cluster1,) + (b18,) if isinstance(cluster1, int) else cluster1 + (b18,)
        b20 = fonk1(b19, b13)
        del b14[cluster1]
        del b14[b18]
        for i in b14:
            if i not in b15:
                b17 = (b20.multiply(b14[i]).sum()) / \
                             (np.sqrt(b14[i].power(2).sum()) * np.sqrt(b20.power(2).sum()))
                hp.heappush(b16, (1 - b17, b19, i))
        b14[b19] = b20
    return b14
def fonk5(b14):
    for cluster in b14:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            print(','.join(str(idx + 1) for idx in sorted(cluster)))
def fonk6():
    b21 = sys.argv[1]
    b22 = int(sys.argv[2])
    b3, b4, b5, b6, b7 = fonk2(b21)
    b13 = fonk3(b3, b4, b5, b6, b7)
    b14 = fonk4(b13, b3, b22)
    fonk5(b14)
if b23 = = "__main__":
    fonk6()