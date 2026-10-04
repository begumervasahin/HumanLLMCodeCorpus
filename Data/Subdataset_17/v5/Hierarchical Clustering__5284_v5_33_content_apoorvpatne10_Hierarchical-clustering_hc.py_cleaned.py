import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    features = dataset.iloc[:, [3, 4]].values
    return features
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def perform_clustering(X, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    cluster_labels = clustering_model.fit_predict(X)
    return cluster_labels
def visualize_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    cluster_colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    cluster_labels = ['Careful', 'Standard', 'Targets', 'Careless', 'Sensible']
    for i, color in enumerate(cluster_colors):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=color, label=cluster_labels[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    file_path = 'Mall_Customers.csv'
    features = load_dataset(file_path)
    plot_dendrogram(features)
    cluster_labels = perform_clustering(features, n_clusters=5)
    visualize_clusters(features, cluster_labels)
if __name__ == "__main__":
    main()