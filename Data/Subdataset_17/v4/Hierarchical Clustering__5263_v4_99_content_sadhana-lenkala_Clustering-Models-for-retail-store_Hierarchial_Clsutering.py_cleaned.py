import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method='ward', metric='euclidean'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance (Ward Method)')
    plt.show()
def perform_clustering(X, n_clusters=5):
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return model.fit_predict(X)
def plot_clusters(X, labels):
    plt.figure(figsize=(10, 7))
    cluster_colors = ['red', 'blue', 'green', 'magenta', 'cyan']
    cluster_names = ['Low Spenders', 'Standard', 'Target', 'Low Earners', 'Out of Target']
    for i, color in enumerate(cluster_colors):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], s=100, color=color, label=cluster_names[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    X = load_dataset('Mall_Customers.csv')
    plot_dendrogram(X)
    cluster_labels = perform_clustering(X)
    plot_clusters(X, cluster_labels)
if __name__ == "__main__":
    main()