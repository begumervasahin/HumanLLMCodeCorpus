import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
Dataset = pd.read_csv('Mall_Customers.csv')
X = Dataset.iloc[:, [3, 4]].values
dendrogram = sch.dendrogram(sch.linkage(X, method='ward', metric='euclidean'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance using ward method')
plt.show()
ahc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
Y_ahc = ahc.fit_predict(X)
cluster_labels = ['Low spenders', 'Standard', 'Target', 'Low earners', 'Out of target']
cluster_colors = ['red', 'blue', 'green', 'magenta', 'cyan']
for i, label in enumerate(cluster_labels):
    plt.scatter(X[Y_ahc == i, 0], X[Y_ahc == i, 1], color=cluster_colors[i], label=label, s=100)
plt.title('Cluster of clients')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()