import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def load_dataset(file_path):
    return pd.read_csv(file_path)
def plot_dendrogram(X):
    dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def perform_clustering(X, n_clusters=5):
    hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return hc.fit_predict(X)
def visualize_clusters(X, labels):
    colors = ['red', 'blue', 'green', 'black', 'magenta']
    for i, color in enumerate(colors):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], s=100, c=color, label=f'Cluster {i+1}')
    plt.title('Clusters of clients')
    plt.xlabel('Annual income (K$)')
    plt.ylabel('Spending score (1-100)')
    plt.legend()
    plt.show()
def main():
    dataset = load_dataset('Mall_Customers.csv')
    X = dataset.iloc[:, [3, 4]].values
    plot_dendrogram(X)
    labels = perform_clustering(X, n_clusters=5)
    visualize_clusters(X, labels)
if __name__ == '__main__':
    main()