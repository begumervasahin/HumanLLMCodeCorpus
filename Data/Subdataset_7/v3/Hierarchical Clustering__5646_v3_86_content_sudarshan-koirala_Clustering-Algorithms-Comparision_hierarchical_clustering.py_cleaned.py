import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']].values
b3 = sch.b3(sch.linkage(b2, method='ward'))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()
b4 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b5 = b4.fit_predict(b2)
b6 = ['red', 'blue', 'green', 'cyan', 'magenta']
b7 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i in range(5):
    plt.scatter(b2[b5 = = i, 0], b2[b5 == i, 1], s=100, c=b6[i], label=b7[i])
plt.title('Cluster of Clients (Hierarchical Clustering)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()