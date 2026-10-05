import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    return pd.read_csv(file_path)
def generate_dendrogram(X):
    dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
    plt.title("Dendrogram")
    plt.xlabel("Clusters")
    plt.ylabel("Euclidean Distance")
    plt.show()
def perform_hierarchical_clustering(X, n_clusters=5):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity="euclidean", linkage="ward")
    return hc.fit_predict(X)
def visualize_clusters(X, cluster_labels, colors, labels):
    for i, color, label in zip(range(len(colors)), colors, labels):
        plt.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1], s=50, c=color, label=label)
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
file_path = 'Mall_Customers.csv'
dataset = load_dataset(file_path)
X = dataset.iloc[:, [3, 4]].values
generate_dendrogram(X)
cluster_labels = perform_hierarchical_clustering(X)
colors = ['red', 'blue', 'green', 'gold', 'magenta']
labels = [f'Cluster {i+1}' for i in range(len(colors))]
visualize_clusters(X, cluster_labels, colors, labels)