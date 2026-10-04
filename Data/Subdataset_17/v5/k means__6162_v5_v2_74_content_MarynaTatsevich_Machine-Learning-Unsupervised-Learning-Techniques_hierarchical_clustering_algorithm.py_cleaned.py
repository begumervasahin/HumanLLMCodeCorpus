
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
dataset = pd.read_csv('Mall_Customers.csv')
features = dataset[['Annual Income (k$)', 'Spending Score (1-100)']]
def plot_dendrogram(data):
    plt.figure(figsize=(10, 7))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    sch.dendrogram(sch.linkage(data, method='ward'))
    plt.show()
plot_dendrogram(features)
def apply_hierarchical_clustering(data, n_clusters=5):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return hc.fit_predict(data)
cluster_labels = apply_hierarchical_clustering(features)
def plot_clusters(data, labels):
    plt.figure(figsize=(10, 7))
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    cluster_colors = ['red', 'blue', 'green', 'black', 'magenta']
    cluster_names = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for cluster in range(len(cluster_colors)):
        plt.scatter(data[labels == cluster]['Annual Income (k$)'],
                    data[labels == cluster]['Spending Score (1-100)'],
                    s=100, c=cluster_colors[cluster], label=cluster_names[cluster])
    plt.legend()
    plt.show()
plot_clusters(features, cluster_labels)