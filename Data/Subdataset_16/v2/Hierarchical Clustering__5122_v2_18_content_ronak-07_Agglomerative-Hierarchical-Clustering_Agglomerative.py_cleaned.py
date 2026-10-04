import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import time
def fonk1(value1, value2):
    return value1 if value1 < value2 else value2
def fonk2(value1, value2):
    return value1 if value1 > value2 else value2
def fonk3(b7, b8, step, b9, b10, b11):
    a1 = 9999.0
    b1 = b2 = -1
    for i in range(b8 - 1):
        for j in range(i + 1, b8):
            if b7[i][j] < a1:
                a1 = b7[i][j]
                b1, b2 = i, j
    if b1 < b2:
        b10[b1].extend(b10.pop(b2))
    else:
        b10[b2].extend(b10.pop(b1))
    if b11[b1] == -1 and b11[b2] == -1:
        b9[step, 0] = b1
        b9[step, 1] = b2
        b11[fonk1(b1, b2)] = b8 + step
        b9[step, 3] = 2
    elif b11[b1] != -1 and b11[b2] != -1:
        b9[step, 0] = b11[b1]
        b9[step, 1] = b11[b2]
        b11[b1 if b1 < b2 else b2] = b8 + step
        b9[step, 3] = b9[int(fonk2(b9[step, 0], b9[step, 1]) - b8), 3] + 1
    elif b11[b1] != -1 and b11[b2] == -1:
        b9[step, 0] = b11[b1]
        b9[step, 1] = b2
        b9[step, 3] = b9[int(fonk2(b9[step, 0], b9[step, 1]) - b8), 3] + 1
        b11[b1] = b8 + step
    elif b11[b1] == -1 and b11[b2] != -1:
        b9[step, 0] = b1
        b9[step, 1] = b11[b2]
        b9[step, 3] = b9[int(fonk2(b9[step, 0], b9[step, 1]) - b8), 3] + 1
        b11[b2] = b8 + step
    else:
        raise ValueError("Error in cluster assignment.")
    b9[step, 2] = a1
    for j in range(b8):
        if j != b2:
            b7[j][b1] = fonk1(b7[j][b1], b7[j][b2])
            b7[b1][j] = b7[j][b1]
        b7[j][b2] = 9999.0
        b7[b2][j] = 9999.0
    return b7
def fonk4(*args, **kwargs):
    b3 = hierarchy.dendrogram(*args, **kwargs)
    if not kwargs.get('no_plot', False):
        for x_coords, y_coords in zip(b3['icoord'], b3['dcoord']):
            b4 = 0.5 * sum(x_coords[1:3])
            b5 = y_coords[1]
            plt.plot(b4, b5, 'ro')
            plt.annotate(f"{b5:.3g}", (b4, b5), b6 = (0, 12), textcoords='offset points', va='top', ha='center')
    return b3
b7 = np.load('b7.npy')
b8 = len(b7)
b9 = np.zeros((b8 - 1, 4))
b10 = {i: [i] for i in range(b8)}
b11 = {i: -1 for i in range(b8)}
b12 = time.time()
for step in range(b8 - 1):
    b7 = fonk3(b7, b8, step, b9, b10, b11)
print(f"Clustering done in {time.time() - b12:.2f} seconds")
plt.figure(b13 = (25, 25))
plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
plt.xlabel('Sequence No.')
plt.ylabel('Distance')
fonk4(b9, b14 = list(range(b8)), show_leaf_counts=True, p=25, truncate_mode='lastp')
plt.show()