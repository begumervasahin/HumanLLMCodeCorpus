import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def load_dataset(file_path):
    return pd.read_csv(file_path)
def perform_clustering(X, n_clusters=4, affinity='euclidean', linkage='ward'):
    clustering = AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage=linkage)
    return clustering.fit_predict(X)
def plot_clusters(X, predict, title):
    colors = ['red', 'blue', 'green', 'yellow']
    for i, color in enumerate(colors):
        plt.scatter(X[predict == i, 0], X[predict == i, 1], s=100, c=color)
    plt.title(title)
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
def plot_dendrogram(X, method, title):
    dendrogram = sch.dendrogram(sch.linkage(X, method=method))
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Euclidean")
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
if __name__ == "__main__":
    dataset = load_dataset('customers_dataset.csv')
    X = dataset.iloc[:, 2:8].values
    ward_predict = perform_clustering(X, linkage='ward')
    complete_predict = perform_clustering(X, linkage='complete')
    average_predict = perform_clustering(X, linkage='average')
    single_predict = perform_clustering(X, linkage='single')
    plot_clusters(X, ward_predict, 'Ward')
    plot_clusters(X, complete_predict, 'Complete')
    plot_clusters(X, average_predict, 'Average')
    plot_clusters(X, single_predict, 'Single')
    plot_dendrogram(X, 'ward', 'Ward')
    plot_dendrogram(X, 'complete', 'Complete')
    plot_dendrogram(X, 'average', 'Average')
    plot_dendrogram(X, 'single', 'Single')