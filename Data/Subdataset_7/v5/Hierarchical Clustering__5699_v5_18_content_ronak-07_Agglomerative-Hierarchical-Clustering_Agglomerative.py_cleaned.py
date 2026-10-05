import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
def fonk1(b10):
    b1 = float('inf')
    min_i, b2 = -1, -1
    for i in range(len(b10)):
        for b6 in range(i + 1, len(b10)):
            if b10[i][b6] < b1:
                b1 = b10[i][b6]
                min_i, b2 = i, b6
    return min_i, b2
def fonk2(b4, k, i, b6, b1, b5, b3):
    b4[k][0], b4[k][1] = i, b6
    b5[b3 + k] = k
    if b5[i] == -1 and b5[b6] == -1:
        b4[k][3] = 2
    elif b5[i] != -1 and b5[b6] != -1:
        b4[k][3] = b4[b5[i]][3] + 1
    else:
        b4[k][3] = b4[max(b5[i], b5[b6])][3] + 1
    b4[k][2] = b1
def fonk3(b10, i, b6):
    for k in range(len(b10)):
        if k != b6:
            b10[i][k] = min(b10[i][k], b10[b6][k])
            b10[k][i] = b10[i][k]
    b10[b6] = [float('inf')] * len(b10)
    b10[:, b6] = float('inf')
def fonk4(b10):
    b3 = len(b10)
    b4 = np.zeros(shape=(b3 - 1, 4))
    b5 = {i: -1 for i in range(b3)}
    for k in range(b3 - 1):
        i, b6 = fonk1(b10)
        b1 = b10[i][b6]
        fonk2(b4, k, i, b6, b1, b5, b3)
        fonk3(b10, i, b6)
    return b4
def fonk5(b4, b8):
    plt.figure(b7 = (25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    sch.dendrogram(b4, b8 = b8, show_leaf_counts=True, p=25, truncate_mode='lastp')
    plt.show()
if b9 = = "__main__":
    b10 = np.load('b10.npy')
    b4 = fonk4(b10)
    b8 = list(range(len(b10)))
    fonk5(b4, b8)