import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(filename):
    dataset = pd.read_csv(filename)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Distance Between Clusters / Dissimilarities')
    sch.dendrogram(sch.linkage(X, method='ward'))
    plt.show()
def apply_clustering(X, n_clusters=5):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return hc.fit_predict(X)
def plot_clusters(X, y_hc, colors, labels):
    plt.figure(figsize=(10, 7))
    for i, color, label in zip(range(len(labels)), colors, labels):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], c=color, label=label)
    plt.title('Hierarchical Clustering')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (0-100)')
    plt.legend()
    plt.show()
def main():
    X = load_data('Mall_Customers.csv')
    plot_dendrogram(X)
    y_hc = apply_clustering(X)
    colors = ['red', 'blue', 'magenta', 'cyan', 'green']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    plot_clusters(X, y_hc, colors, labels)
if __name__ == "__main__":
    main()