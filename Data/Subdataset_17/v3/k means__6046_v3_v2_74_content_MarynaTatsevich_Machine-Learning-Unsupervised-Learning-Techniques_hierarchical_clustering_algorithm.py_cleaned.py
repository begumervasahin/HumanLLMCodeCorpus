
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
dataset = pd.read_csv('Mall_Customers.csv')
features = dataset[['Annual Income (k$)', 'Spending Score (1-100)']]
plt.figure(figsize=(10, 7))
dendrogram = sch.dendrogram(sch.linkage(features, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster_labels = hc.fit_predict(features)
def plot_clusters(features, cluster_labels, num_clusters):
    colors = ['red', 'blue', 'green', 'black', 'magenta']
    cluster_names = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    plt.figure(figsize=(10, 7))
    for i in range(num_clusters):
        plt.scatter(features[cluster_labels == i]['Annual Income (k$)'],
                    features[cluster_labels == i]['Spending Score (1-100)'],
                    s=100, c=colors[i], label=cluster_names[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
plot_clusters(features, cluster_labels, 5)