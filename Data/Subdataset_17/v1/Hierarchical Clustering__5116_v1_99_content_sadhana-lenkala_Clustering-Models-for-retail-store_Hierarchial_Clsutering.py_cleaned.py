import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    X = dataset.iloc[:, [3, 4]].values
    return X
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method='ward', metric='euclidean'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distance using Ward method')
    plt.show()
def perform_agglomerative_clustering(X, n_clusters=5):
    ahc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return ahc.fit_predict(X)
def plot_clusters(X, cluster_labels):
    plt.figure(figsize=(10, 7))
    plt.scatter(X[cluster_labels == 0, 0], X[cluster_labels == 0, 1], color='red', label='Low spenders', s=100)
    plt.scatter(X[cluster_labels == 1, 0], X[cluster_labels == 1, 1], color='blue', label='Standard', s=100)
    plt.scatter(X[cluster_labels == 2, 0], X[cluster_labels == 2, 1], color='green', label='Target', s=100)
    plt.scatter(X[cluster_labels == 3, 0], X[cluster_labels == 3, 1], color='magenta', label='Low earners', s=100)
    plt.scatter(X[cluster_labels == 4, 0], X[cluster_labels == 4, 1], color='cyan', label='Out of target', s=100)
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    X = load_dataset('Mall_Customers.csv')
    plot_dendrogram(X)
    cluster_labels = perform_agglomerative_clustering(X)
    plot_clusters(X, cluster_labels)
if __name__ == "__main__":
    main()