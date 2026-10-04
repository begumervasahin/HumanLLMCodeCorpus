from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def fonk1(cluster_indices, matrix):
    return sum(matrix[i] for i in cluster_indices) / len(cluster_indices)
def fonk2(b18):
    with open(b18, 'r') as file:
        b1 = file.readlines()
    b2 = int(b1[0].strip())
    b3 = int(b1[1].strip())
    row_indices, col_indices, b4 = [], [], []
    for line in b1[2:]:
        doc_id, word_id, b5 = map(int, line.split())
        row_indices.append(doc_id - 1)
        col_indices.append(word_id - 1)
        b4.append(b5)
    return b2, b3, row_indices, col_indices, b4
def fonk3(b2, b3, row_indices, col_indices, b4):
    b6 = Counter(col_indices)
    for i in range(len(b4)):
        b7 = math.log((b2 + 1) / (b6[col_indices[i]] + 1), 2)
        b4[i] *= b7
    b8 = csc_matrix((b4, (row_indices, col_indices)), shape=(b2, b3))
    b9 = np.sqrt(b8.power(2).sum(axis=1))
    b10 = b8 / b9
    return b10
def fonk4(b2, b19, b10):
    b11 = {i: b10[i] for i in range(b2)}
    b12 = set()
    b13 = []
    for i in b11:
        for j in range(i + 1, b2):
            b14 = (b11[i].multiply(b11[j]).sum()) / \
                         (np.sqrt(b11[i].power(2).sum()) * np.sqrt(b11[j].power(2).sum()))
            hp.heappush(b13, (1 - b14, i, j))
    while len(b11) > b19:
        _, cluster1, b15 = hp.heappop(b13)
        if cluster1 in b12 or b15 in b12:
            continue
        b12.add(cluster1)
        b12.add(b15)
        b16 = (cluster1, b15) if isinstance(cluster1, int) else cluster1 + (b15,)
        b17 = fonk1(b16, b10)
        del b11[cluster1]
        del b11[b15]
        for i in b11:
            if i not in b12:
                b14 = (b17.multiply(b11[i]).sum()) / \
                             (np.sqrt(b11[i].power(2).sum()) * np.sqrt(b17.power(2).sum()))
                hp.heappush(b13, (1 - b14, b16, i))
        b11[b16] = b17
    return b11
def fonk5(b11):
    for cluster in b11:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            print(','.join(str(idx + 1) for idx in sorted(cluster)))
def fonk6():
    b18 = sys.argv[1]
    b19 = int(sys.argv[2])
    b2, b3, row_indices, col_indices, b4 = fonk2(b18)
    b10 = fonk3(b2, b3, row_indices, col_indices, b4)
    b11 = fonk4(b2, b19, b10)
    fonk5(b11)
if b20 = = "__main__":
    fonk6()