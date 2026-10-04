import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(filepath):
    dataset = pd.read_csv(filepath)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def perform_clustering(X, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(X)
def plot_clusters(X, labels, cluster_labels):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i, color in enumerate(colors):
        plt.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1], s=100, c=color, label=labels[i])
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    cluster_labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    X = load_data('Mall_Customers.csv')
    plot_dendrogram(X)
    y_hc = perform_clustering(X)
    plot_clusters(X, cluster_labels, y_hc)
if __name__ == "__main__":
    main()