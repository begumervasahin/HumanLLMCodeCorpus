import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import time
def minimum(double1, double2):
    return double1 if double1 < double2 else double2
def maximum(double1, double2):
    return double1 if double1 > double2 else double2
def clust(a, size, k, Z, dict, new_clusters):
    min_dist = 9999.0
    m = n = -1
    for i in range(size-1):
        for j in range(i+1, size):
            if a[i][j] < min_dist:
                min_dist = a[i][j]
                m, n = i, j
    if m < n:
        dict[m].extend(dict[n])
        del dict[n]
    else:
        dict[n].extend(dict[m])
        del dict[m]
    if new_clusters[m] == -1 and new_clusters[n] == -1:
        Z[k, 0] = m
        Z[k, 1] = n
        new_clusters[minimum(m, n)] = size + k
        Z[k, 3] = 2
    elif new_clusters[m] != -1 and new_clusters[n] != -1:
        Z[k, 0] = new_clusters[m]
        Z[k, 1] = new_clusters[n]
        new_clusters[m if m < n else n] = size + k
        Z[k, 3] = Z[int(maximum(Z[k, 0], Z[k, 1]) - size), 3] + 1
    elif new_clusters[m] != -1 and new_clusters[n] == -1:
        Z[k, 0] = new_clusters[m]
        Z[k, 1] = n
        Z[k, 3] = Z[int(maximum(Z[k, 0], Z[k, 1]) - size), 3] + 1
        new_clusters[m] = size + k
    elif new_clusters[m] == -1 and new_clusters[n] != -1:
        Z[k, 0] = m
        Z[k, 1] = new_clusters[n]
        Z[k, 3] = Z[int(maximum(Z[k, 0], Z[k, 1]) - size), 3] + 1
        new_clusters[n] = size + k
    else:
        raise ValueError("Error in cluster assignment.")
    Z[k, 2] = min_dist
    for j in range(size):
        if j != n:
            a[j][m] = minimum(a[j][m], a[j][n])
            a[m][j] = a[j][m]
        a[j][n] = 9999.0
        a[n][j] = 9999.0
    return a
def augmented_dendrogram(*args, **kwargs):
    data = hierarchy.dendrogram(*args, **kwargs)
    if not kwargs.get('no_plot', False):
        for i, d in zip(data['icoord'], data['dcoord']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            plt.plot(x, y, 'ro')
            plt.annotate("%.3g" % y, (x, y), xytext=(0, 12), textcoords='offset points', va='top', ha='center')
    return data
a = np.load('distance_matrix.npy')
size = len(a)
Z = np.zeros((size-1, 4))
dict = {i: [i] for i in range(size)}
new_clusters = {i: -1 for i in range(size)}
start = time.time()
for k in range(size-1):
    a = clust(a, size, k, Z, dict, new_clusters)
print("Clustering done\t" + str(time.time() - start))
plt.figure(figsize=(25, 25))
plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
plt.xlabel('Sequence No.')
plt.ylabel('Distance')
augmented_dendrogram(Z, labels=[i for i in range(size)], show_leaf_counts=True, p=25, truncate_mode='lastp')
plt.show()
Q
Q