import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(file_path):
    return pd.read_csv(file_path)
def extract_features(data, columns):
    return data.iloc[:, columns].values
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
def plot_clusters(X, cluster_labels, cluster_colors=None):
    plt.figure(figsize=(10, 7))
    if cluster_colors is None:
        cluster_colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i, color in enumerate(cluster_colors):
        plt.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1],
                    s=100, c=color, label=f'Cluster {i+1}')
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main(file_path='Mall_Customers.csv', feature_columns=[3, 4], n_clusters=5):
    data = load_data(file_path)
    X = extract_features(data, feature_columns)
    plot_dendrogram(X)
    cluster_labels = apply_agglomerative_clustering(X, n_clusters)
    plot_clusters(X, cluster_labels)
if __name__ == "__main__":
    main()