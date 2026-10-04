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
    dendrogram(linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def perform_agglomerative_clustering(X, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(X)
def plot_clusters(X, cluster_labels):
    plt.figure(figsize=(10, 7))
    cluster_colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    cluster_names = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(cluster_colors):
        plt.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1],
                    s=100, c=color, label=cluster_names[i])
    plt.title('Clusters of Clients (Hierarchical Clustering)')
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