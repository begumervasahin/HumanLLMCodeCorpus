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
plt.ylabel('Distance Between Clusters / Dissimilarities')
sch.dendrogram(sch.linkage(X, method='ward'))
plt.show()
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)
plt.figure(figsize=(10, 7))
colors = ['red', 'blue', 'magenta', 'cyan', 'green']
labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i in range(5):
    plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], c=colors[i], label=labels[i])
plt.title('Hierarchical Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (0-100)')
plt.legend()
plt.show()