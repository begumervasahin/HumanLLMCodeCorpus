import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
dataset = pd.read_csv("Mall_Customers.csv")
X = dataset[['Annual Income (k$)', 'Spending Score (1-100)']].values
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster_labels = hc.fit_predict(X)
colors = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i in range(5):
    plt.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1], s=100, c=colors[i], label=labels[i])
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (K$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()