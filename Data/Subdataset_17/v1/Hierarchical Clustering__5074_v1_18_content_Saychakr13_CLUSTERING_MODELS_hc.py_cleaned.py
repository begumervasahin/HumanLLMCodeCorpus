import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def load_dataset(file_path):
    return pd.read_csv(file_path)
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def perform_agglomerative_clustering(X, n_clusters):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return hc.fit_predict(X)
def plot_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i in range(len(colors)):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=colors[i], label=f'Cluster {i+1}')
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
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