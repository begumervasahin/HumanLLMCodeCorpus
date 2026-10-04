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
def apply_agglomerative_clustering(X, n_clusters=5):
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return model.fit_predict(X)
def plot_clusters(X, y_hc, cluster_labels, colors):
    plt.figure(figsize=(10, 7))
    for i, color in enumerate(colors):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=color, label=cluster_labels[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    filepath = 'Mall_Customers.csv'
    X = load_data(filepath)
    plot_dendrogram(X)
    y_hc = apply_agglomerative_clustering(X)
    cluster_labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    plot_clusters(X, y_hc, cluster_labels, colors)
if __name__ == "__main__":
    main()