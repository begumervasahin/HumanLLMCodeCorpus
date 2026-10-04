import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hierarchy
import time
def fonk1(b8, b9):
    b1 = float('inf')
    cluster1, b2 = -1, -1
    for i in range(b9 - 1):
        for j in range(i + 1, b9):
            if b8[i][j] < b1:
                b1 = b8[i][j]
                cluster1, b2 = i, j
    return cluster1, b2, b1
def fonk2(b11, cluster1, b2):
    if cluster1 < b2:
        b11[cluster1].extend(b11.pop(b2))
    else:
        b11[b2].extend(b11.pop(cluster1))
def fonk3(b10, b12, cluster1, b2, step, b9, b1):
    if b12[cluster1] == -1 and b12[b2] == -1:
        b10[step, 0] = cluster1
        b10[step, 1] = b2
        b12[min(cluster1, b2)] = b9 + step
        b10[step, 3] = 2
    elif b12[cluster1] != -1 and b12[b2] != -1:
        b10[step, 0] = b12[cluster1]
        b10[step, 1] = b12[b2]
        b12[min(cluster1, b2)] = b9 + step
        b10[step, 3] = b10[int(max(b10[step, 0], b10[step, 1]) - b9), 3] + 1
    elif b12[cluster1] != -1:
        b10[step, 0] = b12[cluster1]
        b10[step, 1] = b2
        b10[step, 3] = b10[int(max(b10[step, 0], b10[step, 1]) - b9), 3] + 1
        b12[cluster1] = b9 + step
    else:
        b10[step, 0] = cluster1
        b10[step, 1] = b12[b2]
        b10[step, 3] = b10[int(max(b10[step, 0], b10[step, 1]) - b9), 3] + 1
        b12[b2] = b9 + step
    b10[step, 2] = b1
def fonk4(b8, cluster1, b2, b9):
    for j in range(b9):
        if j != b2:
            b8[j][cluster1] = min(b8[j][cluster1], b8[j][b2])
            b8[cluster1][j] = b8[j][cluster1]
        b8[j][b2] = float('inf')
        b8[b2][j] = float('inf')
def fonk5(b8, b9, b10, b11, b12):
    for step in range(b9 - 1):
        cluster1, b2, b1 = fonk1(b8, b9)
        fonk2(b11, cluster1, b2)
        fonk3(b10, b12, cluster1, b2, step, b9, b1)
        fonk4(b8, cluster1, b2, b9)
def fonk6(b10, b9):
    plt.figure(b3 = (25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    b4 = hierarchy.dendrogram(b10, labels=list(range(b9)), show_leaf_counts=True, p=25, truncate_mode='lastp')
    for x_coords, y_coords in zip(b4['icoord'], b4['dcoord']):
        b5 = 0.5 * sum(x_coords[1:3])
        b6 = y_coords[1]
        plt.plot(b5, b6, 'ro')
        plt.annotate(f"{b6:.3g}", (b5, b6), b7 = (0, 12), textcoords='offset points', va='top', ha='center')
    plt.show()
def fonk7():
    b8 = np.load('b8.npy')
    b9 = len(b8)
    b10 = np.zeros((b9 - 1, 4))
    b11 = {i: [i] for i in range(b9)}
    b12 = {i: -1 for i in range(b9)}
    b13 = time.time()
    fonk5(b8, b9, b10, b11, b12)
    print(f"Clustering done in {time.time() - b13:.2f} seconds")
    fonk6(b10, b9)
if b14 = = "__main__":
    fonk7()