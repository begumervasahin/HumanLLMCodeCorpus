import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    return pd.read_csv(file_path)
def select_features(dataset, feature_columns):
    return dataset[feature_columns]
def plot_dendrogram(data):
    plt.figure(figsize=(10, 6))
    dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def perform_hierarchical_clustering(data, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(data)
def plot_clusters(data, cluster_labels):
    plt.figure(figsize=(10, 6))
    colors = ['red', 'blue', 'green', 'black', 'magenta']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for cluster_id in range(len(np.unique(cluster_labels))):
        plt.scatter(data[cluster_labels == cluster_id, 0], data[cluster_labels == cluster_id, 1],
                    s=100, c=colors[cluster_id], label=labels[cluster_id])
    plt.title('Clusters of clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    file_path = 'Mall_Customers.csv'
    feature_columns = ['Annual Income (k$)', 'Spending Score (1-100)']
    dataset = load_dataset(file_path)
    features = select_features(dataset, feature_columns)
    plot_dendrogram(features)
    cluster_labels = perform_hierarchical_clustering(features)
    plot_clusters(features.values, cluster_labels)
if __name__ == "__main__":
    main()