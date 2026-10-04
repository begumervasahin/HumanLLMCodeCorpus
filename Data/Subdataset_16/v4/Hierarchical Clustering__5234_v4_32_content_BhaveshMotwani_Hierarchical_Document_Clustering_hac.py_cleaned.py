from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def fonk1(cluster_indices, matrix):
    b1 = sum(matrix[i] for i in cluster_indices) / len(cluster_indices)
    return b1
def fonk2(b19):
    with open(b19, 'r') as file:
        b2 = file.readlines()
    b3 = int(b2[0].strip())
    b4 = int(b2[1].strip())
    row_indices, col_indices, b5 = [], [], []
    for line in b2[2:]:
        doc_id, word_id, b6 = map(int, line.split())
        row_indices.append(doc_id - 1)
        col_indices.append(word_id - 1)
        b5.append(b6)
    return b3, b4, row_indices, col_indices, b5
def fonk3(b3, b4, row_indices, col_indices, b5):
    b7 = Counter(col_indices)
    for i in range(len(b5)):
        b8 = math.log((b3 + 1) / (b7[col_indices[i]] + 1), 2)
        b5[i] *= b8
    b9 = csc_matrix((b5, (row_indices, col_indices)), shape=(b3, b4))
    b10 = np.sqrt(b9.power(2).sum(axis=1))
    b11 = b9 / b10
    return b11
def fonk4(b3, b20, b11):
    b12 = {i: b11[i] for i in range(b11.shape[0])}
    b13 = {}
    b14 = []
    for i in b12:
        for j in b12:
            if i < j:
                b15 = (b12[i].multiply(b12[j]).sum()) / \
                             (np.sqrt(b12[i].power(2).sum()) * np.sqrt(b12[j].power(2).sum()))
                hp.heappush(b14, (1 - b15, i, j))
    while len(b12) > b20:
        _, cluster1, b16 = hp.heappop(b14)
        if cluster1 in b13 or b16 in b13:
            continue
        b13[cluster1] = None
        b13[b16] = None
        b17 = (cluster1, b16) if isinstance(cluster1, int) else cluster1 + (b16,)
        b18 = fonk1(b17, b11)
        del b12[cluster1]
        del b12[b16]
        for i in b12:
            if i not in b13:
                b15 = (b18.multiply(b12[i]).sum()) / \
                             (np.sqrt(b12[i].power(2).sum()) * np.sqrt(b18.power(2).sum()))
                hp.heappush(b14, (1 - b15, b17, i))
        b12[b17] = b18
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
    b3, b4, row_indices, col_indices, b5 = fonk2(b19)
    b11 = fonk3(b3, b4, row_indices, col_indices, b5)
    b12 = fonk4(b3, b20, b11)
    fonk5(b12)
if b21 = = "__main__":
    fonk6()