import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def load_dataset(file_path):
    return pd.read_csv(file_path)
def plot_dendrogram(data):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def perform_agglomerative_clustering(data, n_clusters):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(data)
def plot_clusters(data, cluster_labels):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i, color in enumerate(colors):
        plt.scatter(data[cluster_labels == i, 0], data[cluster_labels == i, 1],
                    s=100, c=color, label=f'Cluster {i+1}')
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    dataset = load_dataset('Mall_Customers.csv')
    X = dataset.iloc[:, [3, 4]].values
    plot_dendrogram(X)
    cluster_labels = perform_agglomerative_clustering(X, n_clusters=5)
    plot_clusters(X, cluster_labels)
if __name__ == "__main__":
    main()