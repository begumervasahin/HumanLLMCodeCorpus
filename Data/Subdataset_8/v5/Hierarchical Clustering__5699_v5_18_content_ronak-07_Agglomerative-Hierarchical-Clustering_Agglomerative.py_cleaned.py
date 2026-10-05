import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
def find_min_distance_index(distance_matrix):
    min_distance = float('inf')
    min_i, min_j = -1, -1
    for i in range(len(distance_matrix)):
        for j in range(i + 1, len(distance_matrix)):
            if distance_matrix[i][j] < min_distance:
                min_distance = distance_matrix[i][j]
                min_i, min_j = i, j
    return min_i, min_j
def update_linkage_matrix(linkage_matrix, k, i, j, min_distance, new_clusters, size):
    linkage_matrix[k][0], linkage_matrix[k][1] = i, j
    new_clusters[size + k] = k
    if new_clusters[i] == -1 and new_clusters[j] == -1:
        linkage_matrix[k][3] = 2
    elif new_clusters[i] != -1 and new_clusters[j] != -1:
        linkage_matrix[k][3] = linkage_matrix[new_clusters[i]][3] + 1
    else:
        linkage_matrix[k][3] = linkage_matrix[max(new_clusters[i], new_clusters[j])][3] + 1
    linkage_matrix[k][2] = min_distance
def merge_clusters(distance_matrix, i, j):
    for k in range(len(distance_matrix)):
        if k != j:
            distance_matrix[i][k] = min(distance_matrix[i][k], distance_matrix[j][k])
            distance_matrix[k][i] = distance_matrix[i][k]
    distance_matrix[j] = [float('inf')] * len(distance_matrix)
    distance_matrix[:, j] = float('inf')
def agglomerative_clustering(distance_matrix):
    size = len(distance_matrix)
    linkage_matrix = np.zeros(shape=(size - 1, 4))
    new_clusters = {i: -1 for i in range(size)}
    for k in range(size - 1):
        i, j = find_min_distance_index(distance_matrix)
        min_distance = distance_matrix[i][j]
        update_linkage_matrix(linkage_matrix, k, i, j, min_distance, new_clusters, size)
        merge_clusters(distance_matrix, i, j)
    return linkage_matrix
def plot_dendrogram(linkage_matrix, labels):
    plt.figure(figsize=(25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    sch.dendrogram(linkage_matrix, labels=labels, show_leaf_counts=True, p=25, truncate_mode='lastp')
    plt.show()
if __name__ == "__main__":
    distance_matrix = np.load('distance_matrix.npy')
    linkage_matrix = agglomerative_clustering(distance_matrix)
    labels = list(range(len(distance_matrix)))
    plot_dendrogram(linkage_matrix, labels)