import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import time
def fonk1(b12, b13):
    b1 = float('inf')
    cluster1, b2 = -1, -1
    for i in range(b13 - 1):
        for j in range(i + 1, b13):
            if b12[i][j] < b1:
                b1 = b12[i][j]
                cluster1, b2 = i, j
    return cluster1, b2, b1
def fonk2(cluster1, b2, b13, step, b14, b16):
    if b16[cluster1] == -1 and b16[b2] == -1:
        b14[step, 0] = cluster1
        b14[step, 1] = b2
        b16[min(cluster1, b2)] = b13 + step
        b14[step, 3] = 2
    elif b16[cluster1] != -1 and b16[b2] != -1:
        b14[step, 0] = b16[cluster1]
        b14[step, 1] = b16[b2]
        b16[min(cluster1, b2)] = b13 + step
        b14[step, 3] = b14[int(max(b14[step, 0], b14[step, 1]) - b13), 3] + 1
    elif b16[cluster1] != -1:
        b14[step, 0] = b16[cluster1]
        b14[step, 1] = b2
        b14[step, 3] = b14[int(max(b14[step, 0], b14[step, 1]) - b13), 3] + 1
        b16[cluster1] = b13 + step
    else:
        b14[step, 0] = cluster1
        b14[step, 1] = b16[b2]
        b14[step, 3] = b14[int(max(b14[step, 0], b14[step, 1]) - b13), 3] + 1
        b16[b2] = b13 + step
def fonk3(cluster1, b2, b15):
    if cluster1 < b2:
        b15[cluster1].extend(b15.pop(b2))
    else:
        b15[b2].extend(b15.pop(cluster1))
def fonk4(b12, cluster1, b2, b13):
    for j in range(b13):
        if j != b2:
            b12[j][cluster1] = min(b12[j][cluster1], b12[j][b2])
            b12[cluster1][j] = b12[j][cluster1]
        b12[j][b2] = float('inf')
        b12[b2][j] = float('inf')
def fonk5(b12, b13, b14, b15, b16):
    for step in range(b13 - 1):
        cluster1, b2, b1 = fonk1(b12, b13)
        fonk3(cluster1, b2, b15)
        fonk2(cluster1, b2, b13, step, b14, b16)
        b14[step, 2] = b1
        fonk4(b12, cluster1, b2, b13)
def fonk6(b14, b13):
    plt.figure(b3 = (25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    b4 = hierarchy.dendrogram(
        b14,
        b5 = list(range(b13)),
        b6 = True,
        b7 = 25,
        b8 = 'lastp'
    )
    for x_coords, y_coords in zip(b4['icoord'], b4['dcoord']):
        b9 = 0.5 * sum(x_coords[1:3])
        b10 = y_coords[1]
        plt.plot(b9, b10, 'ro')
        plt.annotate(f"{b10:.3g}", (b9, b10), b11 = (0, 12), textcoords='offset points', va='top', ha='center')
    plt.show()
def fonk7():
    b12 = np.load('b12.npy')
    b13 = len(b12)
    b14 = np.zeros((b13 - 1, 4))
    b15 = {i: [i] for i in range(b13)}
    b16 = {i: -1 for i in range(b13)}
    b17 = time.time()
    fonk5(b12, b13, b14, b15, b16)
    print(f"Clustering done in {time.time() - b17:.2f} seconds")
    fonk6(b14, b13)
if b18 = = "__main__":
    fonk7()