
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']].values
b3 = sch.b3(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()
b4 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b5 = b4.fit_predict(b2)
plt.figure(b6 = (10, 6))
b7 = ['red', 'blue', 'green', 'cyan', 'magenta']
b8 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i in range(5):
    plt.scatter(b2[b5 = = i, 0], b2[b5 == i, 1], b9=100, c=b7[i], label=b8[i])
plt.scatter(b4.cluster_centers_[:, 0], b4.cluster_centers_[:, 1], b9 = 300, c='yellow', label='Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()