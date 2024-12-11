import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import time
def fonk1(double1, double2):
    return min(double1, double2)
def fonk2(double1, double2):
    return max(double1, double2)
def fonk3(a, b4, k, b5, b6, b7):
    b1 = float('inf')
    a1 = -1
    a2 = -1
    for i in range(b4 - 1):
        for j in range(i + 1, b4):
            if a[i][j] < b1:
                b1 = a[i][j]
                a1 = i
                a2 = j
    b2 = []
    if a1 < a2:
        b2.append(b7[a1])
        b2.append(b7[a2])
        b7[a1] = b2
        del b7[a2]
    if b6[a1] == -1 and b6[a2] == -1:
        b5[k][0] = a1
        b5[k][1] = a2
        b3 = fonk1(a1, a2)
        b6[b3] = b4 + k
        b5[k][3] = 2
    elif b6[a1] != -1 and b6[a2] != -1:
        b5[k][0] = b6[a1]
        b5[k][1] = b6[a2]
        if a1 < a2:
            b6[a1] = b4 + k
        else:
            b6[a2] = b4 + k
        b5[k][3] = b5[int(fonk2(b5[k][0], b5[k][1]) - b4)][3] + 1
    elif b6[a1] != -1 and b6[a2] == -1:
        if a1 < a2:
            b5[k][0] = b6[a1]
            b5[k][1] = a2
            b5[k][3] = b5[int(fonk2(b5[k][0], b5[k][1]) - b4)][3] + 1
            b6[a1] = b4 + k
        else:
            b5[k][0] = a1
            b5[k][1] = b6[a2]
            b5[k][3] = b5[int(fonk2(b5[k][0], b5[k][1]) - b4)][3] + 1
            b6[a2] = b4 + k
    elif b6[a1] == -1 and b6[a2] != -1:
        if a1 < a2:
            b5[k][0] = a1
            b5[k][1] = b6[a2]
            b5[k][3] = b5[int(fonk2(b5[k][0], b5[k][1]) - b4)][3] + 1
            b6[a1] = b4 + k
        else:
            b5[k][0] = b6[a1]
            b5[k][1] = a2
            b5[k][3] = b5[int(fonk2(b5[k][0], b5[k][1]) - b4)][3] + 1
            b6[a2] = b4 + k
    else:
        print("Error")
    b5[k][2] = b1
    for j in range(b4):
        if j != a2:
            a[j][a1] = fonk1(a[j][a1], a[j][a2])
        a[a1][j] = a[j][a1]
        a[j][a2] = float('inf')
        a[a2][j] = float('inf')
    return a
def fonk4(b9):
    b4 = len(b9)
    b5 = np.zeros(shape=(b4 - 1, 4))
    b6 = {i: -1 for i in range(b4)}
    b7 = {i: [i] for i in range(b4)}
    b8 = time.time()
    for k in range(b4 - 1):
        b9 = fonk3(b9, b4, k, b5, b6, b7)
    print("Clustering done in", time.time() - b8, "seconds")
    return b5
def fonk5(b5, b11):
    plt.figure(b10 = (25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    sch.dendrogram(b5, b11 = b11, show_leaf_counts=True, p=25, truncate_mode='lastp')
    plt.show()
if b12 = = "__main__":
    b9 = np.load('b9.npy')
    b5 = fonk4(b9)
    b13 = [i for i in range(len(b9))]
    fonk5(b5, b13)