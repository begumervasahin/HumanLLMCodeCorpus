import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(filename):
    dataset = pd.read_csv(filename)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    sch.dendrogram(sch.linkage(X, method='ward'))
    plt.show()
def apply_agglomerative_clustering(X, n_clusters):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return hc.fit_predict(X)
def plot_clusters(X, y_hc, n_clusters):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'magenta', 'cyan', 'green']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(n_clusters):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=colors[i], label=labels[i])
    plt.title('Hierarchical Clustering of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    X = load_dataset('Mall_Customers.csv')
    plot_dendrogram(X)
    n_clusters = 5
    y_hc = apply_agglomerative_clustering(X, n_clusters)
    plot_clusters(X, y_hc, n_clusters)
if __name__ == "__main__":
    main()