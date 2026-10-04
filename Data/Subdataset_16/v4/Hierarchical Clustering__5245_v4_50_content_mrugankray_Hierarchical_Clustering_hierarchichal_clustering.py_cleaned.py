import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
plt.figure(b3 = (10, 7))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Distance Between Clusters / Dissimilarities')
sch.dendrogram(sch.linkage(b2, b4 = 'ward'))
plt.show()
b5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
plt.figure(b3 = (10, 7))
b7 = ['red', 'blue', 'magenta', 'cyan', 'green']
b8 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i in range(5):
    plt.scatter(b2[b6 = = i, 0], b2[b6 == i, 1], c=b7[i], label=b8[i])
plt.title('Hierarchical Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (0-100)')
plt.legend()
plt.show()