import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(file_path):
    dataset = pd.read_csv(file_path)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def perform_clustering(X, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(X)
def plot_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    cluster_labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i in range(5):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=colors[i], label=cluster_labels[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    file_path = 'Mall_Customers.csv'
    X = load_data(file_path)
    plot_dendrogram(X)
    y_hc = perform_clustering(X, n_clusters=5)
    plot_clusters(X, y_hc)
if __name__ == "__main__":
    main()