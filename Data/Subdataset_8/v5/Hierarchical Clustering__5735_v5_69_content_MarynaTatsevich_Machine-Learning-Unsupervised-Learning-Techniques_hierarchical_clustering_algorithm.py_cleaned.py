import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset[['Annual Income (k$)', 'Spending Score (1-100)']].values
def plot_dendrogram(X):
    dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def hierarchical_clustering(X):
    hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    return hc.fit_predict(X)
def plot_clusters(X, labels):
    colors = ['red', 'blue', 'green', 'black', 'magenta']
    labels_unique = np.unique(labels)
    for label in labels_unique:
        plt.scatter(X[labels == label, 0], X[labels == label, 1], s=100, c=colors[label], label=f'Cluster {label+1}')
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    plot_dendrogram(X)
    labels = hierarchical_clustering(X)
    plot_clusters(X, labels)
if __name__ == '__main__':
    main()