import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv('customers_dataset.csv')
X = dataset.iloc[:, 2:8].values
clustering_methods = {
    'Ward': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward'),
    'Complete': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='complete'),
    'Average': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='average'),
    'Single': AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='single')
}
predictions = {method: model.fit_predict(X) for method, model in clustering_methods.items()}
colors = ['red', 'blue', 'green', 'yellow']
for method, labels in predictions.items():
    plt.figure(figsize=(10, 7))
    for i, color in enumerate(colors):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], s=100, c=color, label=f'Cluster {i + 1}')
    plt.title(f'{method} Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()
for method in clustering_methods.keys():
    plt.figure(figsize=(10, 7))
    sch.dendrogram(sch.linkage(X, method=method.lower()))
    plt.title(f'{method} Dendrogram')
    plt.xlabel("Data Points")
    plt.ylabel("Euclidean Distance")
    plt.show()