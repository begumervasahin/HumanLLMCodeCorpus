import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(filename):
    return pd.read_csv(filename)
def plot_dendrogram(data):
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def perform_agglomerative_clustering(data, n_clusters=5):
    clustering = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering.fit_predict(data)
def plot_clusters(data, labels):
    plt.figure(figsize=(10, 7))
    cluster_colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    cluster_labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(cluster_colors):
        plt.scatter(data[labels == i, 0], data[labels == i, 1], s=100, c=color, label=cluster_labels[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    dataset = load_dataset('Mall_Customers.csv')
    X = dataset.iloc[:, [3, 4]].values
    plot_dendrogram(X)
    y_hc = perform_agglomerative_clustering(X, n_clusters=5)
    plot_clusters(X, y_hc)
if __name__ == "__main__":
    main()