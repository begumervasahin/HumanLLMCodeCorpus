import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    return pd.read_csv(file_path)
def plot_dendrogram(X, method='ward'):
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(X, method=method))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def perform_agglomerative_clustering(X, n_clusters=5, affinity='euclidean', linkage='ward'):
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage=linkage)
    return model.fit_predict(X)
def plot_clusters(X, labels, cluster_colors=None, cluster_labels=None):
    if cluster_colors is None:
        cluster_colors = ['red', 'blue', 'green', 'black', 'magenta']
    if cluster_labels is None:
        cluster_labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    plt.figure(figsize=(10, 7))
    for i, color in enumerate(cluster_colors):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], s=100, c=color, label=cluster_labels[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    dataset = load_dataset('Mall_Customers.csv')
    X = dataset.iloc[:, [3, 4]].values
    plot_dendrogram(X)
    cluster_labels = perform_agglomerative_clustering(X)
    plot_clusters(X, cluster_labels)
if __name__ == "__main__":
    main()