import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(filename):
    return pd.read_csv(filename)
def plot_dendrogram(data):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def perform_agglomerative_clustering(data, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(data)
def plot_clusters(data, cluster_labels):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(len(labels)):
        plt.scatter(data[cluster_labels == i, 0], data[cluster_labels == i, 1],
                    s=100, c=colors[i], label=labels[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    dataset = load_dataset('Mall_Customers.csv')
    data = dataset.iloc[:, [3, 4]].values
    plot_dendrogram(data)
    cluster_labels = perform_agglomerative_clustering(data, n_clusters=5)
    plot_clusters(data, cluster_labels)
if __name__ == "__main__":
    main()