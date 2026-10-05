import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset[['Annual Income (k$)', 'Spending Score (1-100)']].values
linkage_matrix = sch.linkage(X, method='ward')
dendrogram = sch.dendrogram(linkage_matrix)
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance between Clusters / Dissimilarities')
plt.show()
agglomerative_clustering = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster_labels = agglomerative_clustering.fit_predict(X)
cluster_colors = ['red', 'blue', 'magenta', 'cyan', 'green']
cluster_labels_unique = np.unique(cluster_labels)
for cluster_label in cluster_labels_unique:
    plt.scatter(X[cluster_labels == cluster_label, 0], X[cluster_labels == cluster_label, 1],
                c=cluster_colors[cluster_label], label=f'Cluster {cluster_label}')
plt.title('Hierarchical Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()