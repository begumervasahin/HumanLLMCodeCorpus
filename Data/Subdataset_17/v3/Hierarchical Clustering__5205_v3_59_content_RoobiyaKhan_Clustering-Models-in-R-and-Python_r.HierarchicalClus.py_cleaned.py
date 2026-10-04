import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(filepath):
    dataset = pd.read_csv(filepath)
    X = dataset.iloc[:, [3, 4]].values
    return X
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def perform_agglomerative_clustering(X, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    y_hc = clustering_model.fit_predict(X)
    return y_hc
def plot_clusters(X, cluster_labels):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(colors):
        plt.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1],
                    s=100, c=color, label=labels[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    filepath = 'Mall_Customers.csv'
    X = load_data(filepath)
    plot_dendrogram(X)
    cluster_labels = perform_agglomerative_clustering(X)
    plot_clusters(X, cluster_labels)
if __name__ == "__main__":
    main()