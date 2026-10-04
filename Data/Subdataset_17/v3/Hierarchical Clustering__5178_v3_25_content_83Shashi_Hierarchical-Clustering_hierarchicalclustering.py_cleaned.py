import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(file_path):
    return pd.read_csv(file_path)
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def apply_agglomerative_clustering(X, n_clusters):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return hc.fit_predict(X)
def plot_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    labels_colors = [
        ('Careful', 'red'),
        ('Standard', 'blue'),
        ('Target', 'green'),
        ('Careless', 'cyan'),
        ('Sensible', 'magenta')
    ]
    for i, (label, color) in enumerate(labels_colors):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=color, label=label)
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    dataset = load_data("Mall_Customers.csv")
    X = dataset.iloc[:, [3, 4]].values
    plot_dendrogram(X)
    y_hc = apply_agglomerative_clustering(X, n_clusters=5)
    plot_clusters(X, y_hc)
if __name__ == "__main__":
    main()