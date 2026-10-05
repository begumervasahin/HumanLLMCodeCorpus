import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendrogram")
plt.xlabel("Clusters")
plt.ylabel("Euclidean Distance")
plt.show()
hc = AgglomerativeClustering(n_clusters=5, affinity="euclidean", linkage="ward")
cluster_labels = hc.fit_predict(X)
colors = ['red', 'blue', 'green', 'gold', 'magenta']
labels = [f'Cluster {i+1}' for i in range(5)]
for i, color, label in zip(range(5), colors, labels):
    plt.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1], s=50, c=color, label=label)
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()