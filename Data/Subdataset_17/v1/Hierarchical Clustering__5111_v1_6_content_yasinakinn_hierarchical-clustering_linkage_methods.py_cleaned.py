import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def load_dataset(file_path):
    return pd.read_csv(file_path)
def perform_clustering(X, n_clusters=4):
    clustering_methods = {
        'Ward': AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward'),
        'Complete': AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='complete'),
        'Average': AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='average'),
        'Single': AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='single')
    }
    predictions = {method: model.fit_predict(X) for method, model in clustering_methods.items()}
    return predictions
def plot_clusters(X, predictions):
    colors = ['red', 'blue', 'green', 'yellow']
    for method, labels in predictions.items():
        plt.figure(figsize=(10, 7))
        for i in range(4):
            plt.scatter(X[labels == i, 0], X[labels == i, 1], s=100, c=colors[i], label=f'Cluster {i+1}')
        plt.title(f'{method} Method')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.show()
def plot_dendrograms(X):
    methods = ['ward', 'complete', 'average', 'single']
    for method in methods:
        plt.figure(figsize=(10, 7))
        sch.dendrogram(sch.linkage(X, method=method))
        plt.title(f'{method.capitalize()} Dendrogram')
        plt.xlabel("Data Points")
        plt.ylabel("Euclidean Distance")
        plt.show()
def main():
    dataset = load_dataset('customers_dataset.csv')
    X = dataset.iloc[:, 2:8].values
    predictions = perform_clustering(X)
    plot_clusters(X, predictions)
    plot_dendrograms(X)
if __name__ == "__main__":
    main()