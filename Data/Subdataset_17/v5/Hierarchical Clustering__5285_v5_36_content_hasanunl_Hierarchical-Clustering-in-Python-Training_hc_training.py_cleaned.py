import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def load_data(file_path):
    dataset = pd.read_csv(file_path)
    return dataset.iloc[:, [3, 4]].values
def plot_dendrogram(X):
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def perform_clustering(X, n_clusters=5):
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return model.fit_predict(X)
def visualize_clusters(X, y_hc):
    plt.figure(figsize=(10, 7))
    colors = ['red', 'blue', 'green', 'cyan', 'magenta']
    labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(colors):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=color, label=labels[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def main():
    file_path = 'Mall_Customers.csv'
    X = load_data(file_path)
    plot_dendrogram(X)
    y_hc = perform_clustering(X, n_clusters=5)
    visualize_clusters(X, y_hc)
if __name__ == "__main__":
    main()