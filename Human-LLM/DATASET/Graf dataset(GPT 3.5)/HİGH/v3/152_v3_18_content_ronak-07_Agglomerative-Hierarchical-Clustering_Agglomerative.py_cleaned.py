import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import time
def fonk1(b9, y):
    return min(b9, y)
def fonk2(b9, y):
    return max(b9, y)
def fonk3(b6):
    b1 = len(b6)
    b2 = np.zeros(shape=(b1 - 1, 4))
    b3 = {i: -1 for i in range(b1)}
    b4 = {i: [i] for i in range(b1)}
    b5 = time.time()
    for k in range(b1 - 1):
        b6 = fonk4(b6, b1, k, b2, b3, b4)
    print("Clustering done in", time.time() - b5, "seconds")
    return b2
def fonk4(b6, b1, k, b2, b3, b4):
    b7 = float('inf')
    b10, b8 = -1, -1
    for i in range(b1 - 1):
        for j in range(i + 1, b1):
            if b6[i][j] < b7:
                b7 = b6[i][j]
                b10, b8 = i, j
    if b10 < b8:
        b4[b10].extend(b4[b8])
        del b4[b8]
    if b3[b10] == -1 and b3[b8] == -1:
        b2[k][0], b2[k][1] = b10, b8
        b9 = fonk1(b10, b8)
        b3[b9] = b1 + k
        b2[k][3] = 2
    else:
        if b3[b10] != -1:
            b10 = b3[b10]
        if b3[b8] != -1:
            b8 = b3[b8]
        b2[k][0], b2[k][1] = b10, b8
        b3[fonk2(b10, b8)] = b1 + k
        b2[k][3] = b2[fonk2(b10, b8) - b1][3] + 1
    b2[k][2] = b7
    for j in range(b1):
        if j != b8:
            b6[j][b10] = fonk1(b6[j][b10], b6[j][b8])
        b6[b10][j] = b6[j][b10]
        b6[j][b8] = float('inf')
        b6[b8][j] = float('inf')
    return b6
def fonk5(b2, b12):
    plt.figure(b11 = (25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    sch.dendrogram(b2, b12 = b12, show_leaf_counts=True, p=25, truncate_mode='lastp')
    plt.show()
if b13 = = "__main__":
    b6 = np.load('b6.npy')
    b2 = fonk3(b6)
    b12 = [i for i in range(len(b6))]
    fonk5(b2, b12)