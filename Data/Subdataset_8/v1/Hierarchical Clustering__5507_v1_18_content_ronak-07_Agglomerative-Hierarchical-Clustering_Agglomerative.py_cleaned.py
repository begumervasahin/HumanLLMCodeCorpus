import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import time
def minimum(double1, double2):
    return min(double1, double2)
def maximum(double1, double2):
    return max(double1, double2)
def clust(a, size, k, Z, new_clusters, dict):
    min_val = float('inf')
    m = -1
    n = -1
    for i in range(size - 1):
        for j in range(i + 1, size):
            if a[i][j] < min_val:
                min_val = a[i][j]
                m = i
                n = j
    big_list = []
    if m < n:
        big_list.append(dict[m])
        big_list.append(dict[n])
        dict[m] = big_list
        del dict[n]
    if new_clusters[m] == -1 and new_clusters[n] == -1:
        Z[k][0] = m
        Z[k][1] = n
        x = minimum(m, n)
        new_clusters[x] = size + k
        Z[k][3] = 2
    elif new_clusters[m] != -1 and new_clusters[n] != -1:
        Z[k][0] = new_clusters[m]
        Z[k][1] = new_clusters[n]
        if m < n:
            new_clusters[m] = size + k
        else:
            new_clusters[n] = size + k
        Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1
    elif new_clusters[m] != -1 and new_clusters[n] == -1:
        if m < n:
            Z[k][0] = new_clusters[m]
            Z[k][1] = n
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1
            new_clusters[m] = size + k
        else:
            Z[k][0] = m
            Z[k][1] = new_clusters[n]
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1
            new_clusters[n] = size + k
    elif new_clusters[m] == -1 and new_clusters[n] != -1:
        if m < n:
            Z[k][0] = m
            Z[k][1] = new_clusters[n]
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1
            new_clusters[m] = size + k
        else:
            Z[k][0] = new_clusters[m]
            Z[k][1] = n
            Z[k][3] = Z[int(maximum(Z[k][0], Z[k][1]) - size)][3] + 1
            new_clusters[n] = size + k
    else:
        print("Error")
    Z[k][2] = min_val
    for j in range(size):
        if j != n:
            a[j][m] = minimum(a[j][m], a[j][n])
        a[m][j] = a[j][m]
        a[j][n] = float('inf')
        a[n][j] = float('inf')
    return a
def hierarchical_clustering(distance_matrix):
    size = len(distance_matrix)
    Z = np.zeros(shape=(size - 1, 4))
    new_clusters = {i: -1 for i in range(size)}
    dict = {i: [i] for i in range(size)}
    start_time = time.time()
    for k in range(size - 1):
        distance_matrix = clust(distance_matrix, size, k, Z, new_clusters, dict)
    print("Clustering done in", time.time() - start_time, "seconds")
    return Z
def plot_dendrogram(Z, labels):
    plt.figure(figsize=(25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    sch.dendrogram(Z, labels=labels, show_leaf_counts=True, p=25, truncate_mode='lastp')
    plt.show()
if __name__ == "__main__":
    distance_matrix = np.load('distance_matrix.npy')
    Z = hierarchical_clustering(distance_matrix)
    names = [i for i in range(len(distance_matrix))]
    plot_dendrogram(Z, names)