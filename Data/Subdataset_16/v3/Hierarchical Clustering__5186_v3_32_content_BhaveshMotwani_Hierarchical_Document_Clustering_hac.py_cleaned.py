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
def fonk4(matrix1, matrix2):
    b12 = matrix1.multiply(matrix2).sum()
    b13 = np.sqrt(matrix1.power(2).sum()) * np.sqrt(matrix2.power(2).sum())
    b14 = b12 / b13
    return b14
def fonk5(b11, b3, b22):
    b15 = {i: b11[i] for i in range(b3)}
    b16 = {}
    b17 = []
    for i in b15:
        for j in b15:
            if i < j:
                b14 = fonk4(b15[i], b15[j])
                hp.heappush(b17, (1 - b14, i, j))
    while len(b15) > b22:
        _, cluster1, b18 = hp.heappop(b17)
        if cluster1 in b16 or b18 in b16:
            continue
        b16[cluster1] = None
        b16[b18] = None
        b19 = (cluster1,) + (b18,) if isinstance(cluster1, int) else cluster1 + (b18,)
        b20 = fonk1(b19, b11)
        del b15[cluster1]
        del b15[b18]
        for i in b15:
            if i not in b16:
                b14 = fonk4(b20, b15[i])
                hp.heappush(b17, (1 - b14, b19, i))
        b15[b19] = b20
    return b15
def fonk6(b15):
    for cluster in b15:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            print(','.join(str(idx + 1) for idx in sorted(cluster)))
def fonk7():
    b21 = sys.argv[1]
    b22 = int(sys.argv[2])
    b3, b4, row_indices, col_indices, b5 = fonk2(b21)
    b11 = fonk3(b3, b4, row_indices, col_indices, b5)
    b15 = fonk5(b11, b3, b22)
    fonk6(b15)
if b23 = = "__main__":
    fonk7()