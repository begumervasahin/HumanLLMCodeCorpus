import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def perform_clustering(X, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(X)
def visualize_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=100, c='red', label='Careful')
    plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=100, c='blue', label='Standard')
    plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s=100, c='green', label='Target')
    plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s=100, c='cyan', label='Careless')
    plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s=100, c='magenta', label='Sensible')
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    file_path = 'Mall_Customers.csv'
    X = load_dataset(file_path)
    plot_dendrogram(X)
    y_hc = perform_clustering(X, n_clusters=5)
    visualize_clusters(X, y_hc)
if __name__ == "__main__":
    main()