import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values
plt.figure(figsize=(10, 7))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.show()
n_clusters = 5
hc = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)
plt.figure(figsize=(10, 7))
colors = ['red', 'blue', 'magenta', 'cyan', 'green']
labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i in range(n_clusters):
    plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=colors[i], label=labels[i])
plt.title('Hierarchical Clustering of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()