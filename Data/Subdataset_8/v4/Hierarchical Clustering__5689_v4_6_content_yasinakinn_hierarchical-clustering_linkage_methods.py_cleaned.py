import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv('customers_dataset.csv')
X = dataset.iloc[:, 2:8].values
ward = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
complete = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='complete')
average = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='average')
single = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='single')
ward_predict = ward.fit_predict(X)
complete_predict = complete.fit_predict(X)
average_predict = average.fit_predict(X)
single_predict = single.fit_predict(X)
def plot_clusters(predict, title):
    colors = ['red', 'blue', 'green', 'yellow']
    for i, color in enumerate(colors):
        plt.scatter(X[predict == i, 0], X[predict == i, 1], s=100, c=color)
    plt.title(title)
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
plot_clusters(ward_predict, 'Ward')
plot_clusters(complete_predict, 'Complete')
plot_clusters(average_predict, 'Average')
plot_clusters(single_predict, 'Single')
def plot_dendrogram(method, title):
    dendrogram = sch.dendrogram(sch.linkage(X, method=method))
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Euclidean")
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
plot_dendrogram('ward', 'Ward')
plot_dendrogram('complete', 'Complete')
plot_dendrogram('average', 'Average')
plot_dendrogram('single', 'Single')