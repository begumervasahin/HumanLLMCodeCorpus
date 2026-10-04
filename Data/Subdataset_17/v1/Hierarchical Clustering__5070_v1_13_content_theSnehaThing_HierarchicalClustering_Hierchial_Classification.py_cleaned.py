import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(data):
    plt.figure(figsize=(10, 7))
    dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))
    plt.title("Dendrogram")
    plt.xlabel("Customers")
    plt.ylabel("Euclidean distances")
    plt.show()
def apply_clustering(data, n_clusters):
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return clustering_model.fit_predict(data)
def plot_clusters(data, labels, n_clusters):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    cluster_names = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(n_clusters):
        plt.scatter(data[labels == i, 0], data[labels == i, 1], s=100, c=colors[i], label=cluster_names[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    file_path = 'Mall_Customers.csv'
    data = load_dataset(file_path)
    plot_dendrogram(data)
    n_clusters = 5
    cluster_labels = apply_clustering(data, n_clusters)
    plot_clusters(data, cluster_labels, n_clusters)
if __name__ == "__main__":
    main()