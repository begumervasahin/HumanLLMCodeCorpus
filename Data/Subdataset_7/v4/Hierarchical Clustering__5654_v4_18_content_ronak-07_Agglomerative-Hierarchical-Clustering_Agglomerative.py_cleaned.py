import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import time
def fonk1(x, y):
    return min(x, y)
def fonk2(x, y):
    return max(x, y)
def fonk3(b10):
    b1 = len(b10)
    b2 = np.zeros(shape=(b1 - 1, 4))
    b3 = {i: [i] for i in range(b1)}
    b4 = {i: -1 for i in range(b1)}
    for k in range(b1 - 1):
        b6, m, b5 = fonk4(b10, b3, b4, b1)
        fonk5(b2, k, m, b5, b6, b4, b1)
        fonk6(b10, b3, m, b5)
    return b2
def fonk4(b10, b3, b4, b1):
    b6 = float('inf')
    m, b5 = -1, -1
    for i in range(b1 - 1):
        for j in range(i + 1, b1):
            if b10[i][j] < b6:
                b6 = b10[i][j]
                m, b5 = i, j
    if m > b5:
        m, b5 = b5, m
    return b6, m, b5
def fonk5(b2, k, m, b5, b6, b4, b1):
    b2[k][0] = m
    b2[k][1] = b5
    b4[b1 + k] = k
    if b4[m] == -1 and b4[b5] == -1:
        b2[k][3] = 2
    elif b4[m] != -1 and b4[b5] != -1:
        b2[k][3] = b2[b4[m]][3] + 1
    else:
        b2[k][3] = b2[fonk2(b4[m], b4[b5])][3] + 1
    b2[k][2] = b6
def fonk6(b10, b3, m, b5):
    for i in range(len(b10)):
        if i != b5:
            b10[m][i] = fonk1(b10[m][i], b10[b5][i])
            b10[i][m] = b10[m][i]
            b10[b5][i] = float('inf')
            b10[i][b5] = float('inf')
def fonk7(b2, b8):
    plt.figure(b7 = (25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    sch.dendrogram(b2, b8 = b8, show_leaf_counts=True, p=25, truncate_mode='lastp')
    plt.show()
if b9 = = "__main__":
    b10 = np.load('b10.npy')
    b2 = fonk3(b10)
    b8 = [i for i in range(len(b10))]
    fonk7(b2, b8)