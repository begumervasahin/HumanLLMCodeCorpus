import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv('customers_dataset.csv')
X = dataset.iloc[:, 2:8].values
clustering_algorithms = {
    'Ward': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward'),
    'Complete': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='complete'),
    'Average': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='average'),
    'Single': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='single')
}
predictions = {name: algo.fit_predict(X) for name, algo in clustering_algorithms.items()}
colors = ['red', 'blue', 'green', 'yellow']
def plot_clusters(X, predictions, colors):
    for method_name, labels in predictions.items():
        plt.figure(figsize=(10, 7))
        for cluster_index, color in enumerate(colors):
            plt.scatter(X[labels == cluster_index, 0], X[labels == cluster_index, 1],
                        s=100, c=color, label=f'Cluster {cluster_index + 1}')
        plt.title(f'{method_name} Clustering')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.show()
def plot_dendrograms(X, methods):
    for method in methods:
        plt.figure(figsize=(10, 7))
        sch.dendrogram(sch.linkage(X, method=method.lower()))
        plt.title(f'{method} Dendrogram')
        plt.xlabel("Data Points")
        plt.ylabel("Euclidean Distance")
        plt.show()
plot_clusters(X, predictions, colors)
plot_dendrograms(X, clustering_algorithms.keys())