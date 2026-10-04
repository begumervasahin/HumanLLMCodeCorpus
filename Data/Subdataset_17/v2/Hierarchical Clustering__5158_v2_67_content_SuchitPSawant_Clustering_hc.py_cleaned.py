import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(file_path):
    return pd.read_csv(file_path)
def extract_features(data, feature_columns):
    return data.iloc[:, feature_columns].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def apply_agglomerative_clustering(X, n_clusters=5):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return hc.fit_predict(X)
def plot_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    labels = [f'Cluster {i+1}' for i in range(len(colors))]
    for i in range(len(colors)):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=colors[i], label=labels[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    data = load_data('Mall_Customers.csv')
    X = extract_features(data, [3, 4])
    plot_dendrogram(X)
    y_hc = apply_agglomerative_clustering(X)
    plot_clusters(X, y_hc)
if __name__ == "__main__":
    main()