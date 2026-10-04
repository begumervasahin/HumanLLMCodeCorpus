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
    plt.ylabel('Euclidean Distance')
    plt.show()
def perform_clustering(X, n_clusters=5):
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return model.fit_predict(X)
def plot_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    cluster_definitions = {
        0: ('red', 'Careful'),
        1: ('blue', 'Standard'),
        2: ('green', 'Target'),
        3: ('cyan', 'Careless'),
        4: ('magenta', 'Sensible')
    }
    for cluster_id, (color, label) in cluster_definitions.items():
        plt.scatter(X[y_hc == cluster_id, 0], X[y_hc == cluster_id, 1],
                    s=100, c=color, label=label)
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    file_path = 'Mall_Customers.csv'
    X = load_dataset(file_path)
    plot_dendrogram(X)
    y_hc = perform_clustering(X, n_clusters=5)
    plot_clusters(X, y_hc)
if __name__ == "__main__":
    main()