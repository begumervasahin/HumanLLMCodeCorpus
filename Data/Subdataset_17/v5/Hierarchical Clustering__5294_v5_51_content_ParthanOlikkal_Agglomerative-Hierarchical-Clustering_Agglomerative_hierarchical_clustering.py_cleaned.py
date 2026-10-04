import numpy as np
from scipy.spatial import distance_matrix
from scipy.cluster import hierarchy
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
def generate_synthetic_data(n_samples, centers, cluster_std):
    X, y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std)
    return X, y
def plot_data_points(X, title):
    plt.scatter(X[:, 0], X[:, 1], marker='o')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
def perform_agglomerative_clustering(X, n_clusters, linkage_method):
    agglom = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage_method)
    agglom.fit(X)
    return agglom
def plot_clusters(X, y, labels, title):
    plt.figure(figsize=(6, 4))
    x_min, x_max = np.min(X, axis=0), np.max(X, axis=0)
    X_normalized = (X - x_min) / (x_max - x_min)
    for i in range(X_normalized.shape[0]):
        plt.text(X_normalized[i, 0], X_normalized[i, 1], str(y[i]),
                 color=plt.cm.nipy_spectral(labels[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    plt.xticks([])
    plt.yticks([])
    plt.scatter(X_normalized[:, 0], X_normalized[:, 1], marker='.')
    plt.title(title)
    plt.show()
def compute_and_print_distance_matrix(X):
    dist_matrix = distance_matrix(X, X)
    print("Distance Matrix:\n", dist_matrix)
    return dist_matrix
def plot_hierarchical_dendrogram(Z, title):
    plt.figure(figsize=(10, 7))
    hierarchy.dendrogram(Z)
    plt.title(title)
    plt.xlabel('Sample Index')
    plt.ylabel('Distance')
    plt.show()
def main():
    X1, y1 = generate_synthetic_data(n_samples=50, centers=[[4, 4], [-2, -1], [1, 1], [10, 4]], cluster_std=0.9)
    plot_data_points(X1, title='Generated Data Points')
    agglom = perform_agglomerative_clustering(X1, n_clusters=4, linkage_method='average')
    plot_clusters(X1, y1, agglom.labels_, title='Agglomerative Clustering')
    dist_matrix = compute_and_print_distance_matrix(X1)
    Z = hierarchy.linkage(dist_matrix, 'complete')
    plot_hierarchical_dendrogram(Z, title='Dendrogram')
if __name__ == "__main__":
    main()