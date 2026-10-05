from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def fonk1(indices, matrix):
    b1 = sum(matrix[i] for i in indices)
    return b1 / len(indices)
def fonk2(b19):
    with open(b19, 'r') as file:
        b2 = file.readlines()
    b3 = int(b2[0])
    b4 = int(b2[1])
    b5 = [list(map(int, line.strip().split())) for line in b2[3:]]
    return b3, b4, b5
def fonk3(b5, b3):
    b6 = [word_idx - 1 for _, word_idx, _ in b5]
    b7 = [value * math.log(float(b3 + 1) / (Counter(b6)[word_idx] + 1), 2)
              for _, word_idx, value in b5]
    return b6, b7
def fonk4(b3, b4, row_indices, b6, b7):
    b8 = csc_matrix((b7, (row_indices, b6)), shape=(b3, b4))
    b9 = np.asarray(np.sqrt(b8.power(2).sum(axis=1)))
    b10 = csc_matrix(b8 / b9)
    return b10
def fonk5(b21):
    b11 = []
    for i in range(len(b21)):
        for j in range(i + 1, len(b21)):
            b12 = b21[i].multiply(b21[j])
            b13 = np.sqrt((b21[i].power(2).sum())) * np.sqrt((b21[j].power(2).sum()))
            b14 = (b12.sum()) / b13
            hp.heappush(b11, (1 - b14, i, j))
    return b11
def fonk6(b11, b3, b20, b21):
    b15 = {}
    a1 = 0
    while a1 < b3 - b20:
        b16 = hp.heappop(b11)
        if b16[1] in b15 or b16[2] in b15:
            continue
        elif isinstance(b16[1], int) and isinstance(b16[2], int):
            b15[b16[1]] = None
            b15[b16[2]] = None
            b17 = (b16[1], b16[2])
            b18 = fonk1(b17, b21)
            del b21[b16[1]]
            del b21[b16[2]]
        else:
            b15[b16[1]] = None
            b15[b16[2]] = None
            if isinstance(b16[1], int):
                b17 = b16[2] + (b16[1],)
            elif isinstance(b16[2], int):
                b17 = b16[1] + (b16[2],)
            else:
                b17 = b16[1] + b16[2]
            del b21[b16[1]]
            del b21[b16[2]]
            b18 = fonk1(b17, b21)
        for i in b21:
            if i not in b15:
                b12 = b18.multiply(b21[i])
                b13 = np.sqrt((b21[i].power(2).sum())) * np.sqrt((b18.power(2).sum()))
                b14 = (b12.sum()) / b13
                hp.heappush(b11, (1 - b14, b17, i))
        b21[b17] = b18
        a1 += 1
    return b15
def fonk7(b15):
    for cluster in b15:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            print(','.join(str(doc_index + 1) for doc_index in sorted(cluster)))
def fonk8():
    b19 = sys.argv[1]
    b20 = int(sys.argv[2])
    b3, b4, b5 = fonk2(b19)
    row_indices, b7 = fonk3(b5, b3)
    b21 = fonk4(b3, b4, row_indices, b6, b7)
    b11 = fonk5(b21)
    b15 = fonk6(b11, b3, b20, b21)
    fonk7(b15)
if b22 = = "__main__":
    fonk8()