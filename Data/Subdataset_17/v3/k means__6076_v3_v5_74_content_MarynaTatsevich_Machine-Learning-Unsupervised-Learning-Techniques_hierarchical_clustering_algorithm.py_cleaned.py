import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(filepath):
    return pd.read_csv(filepath)
def select_features(dataset, feature_columns):
    return dataset[feature_columns]
def visualize_dendrogram(data):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def perform_hierarchical_clustering(data, n_clusters=5):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    cluster_labels = clustering_model.fit_predict(data)
    return cluster_labels
def visualize_clusters(data, cluster_labels):
    plt.figure(figsize=(10, 6))
    colors = ['red', 'blue', 'green', 'black', 'magenta']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for cluster in np.unique(cluster_labels):
        plt.scatter(data[cluster_labels == cluster, 0], data[cluster_labels == cluster, 1],
                    s=100, c=colors[cluster], label=labels[cluster])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    dataset = load_data('Mall_Customers.csv')
    feature_columns = ['Annual Income (k$)', 'Spending Score (1-100)']
    features = select_features(dataset, feature_columns)
    visualize_dendrogram(features)
    cluster_labels = perform_hierarchical_clustering(features)
    visualize_clusters(features.values, cluster_labels)
if __name__ == "__main__":
    main()