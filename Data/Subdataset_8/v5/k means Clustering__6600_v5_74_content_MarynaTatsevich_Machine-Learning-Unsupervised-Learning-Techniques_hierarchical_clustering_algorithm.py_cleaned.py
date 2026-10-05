
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
dataset = pd.read_csv('Mall_Customers.csv')
features = dataset[['Annual Income (k$)', 'Spending Score (1-100)']]
def visualize_dendrogram(data):
    dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def hierarchical_clustering(data, n_clusters=5):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    cluster_labels = hc.fit_predict(data)
    return cluster_labels
def visualize_clusters(data, cluster_labels):
    plt.figure(figsize=(10, 6))
    colors = ['red', 'blue', 'green', 'black', 'magenta']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(len(np.unique(cluster_labels))):
        plt.scatter(data[cluster_labels == i, 0], data[cluster_labels == i, 1], s=100, c=colors[i], label=labels[i])
    plt.title('Clusters of clients')
    plt.xlabel('Annual income (K$)')
    plt.ylabel('Spending score (1-100)')
    plt.legend()
    plt.show()
def main():
    visualize_dendrogram(features)
    cluster_labels = hierarchical_clustering(features)
    visualize_clusters(features.values, cluster_labels)
if __name__ == "__main__":
    main()