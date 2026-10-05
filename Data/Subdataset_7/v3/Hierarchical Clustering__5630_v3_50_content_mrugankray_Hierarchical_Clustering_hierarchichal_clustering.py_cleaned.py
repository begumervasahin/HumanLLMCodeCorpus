import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']].values
b3 = sch.linkage(b2, method='ward')
b4 = sch.b4(b3)
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance between Clusters / Dissimilarities')
plt.show()
b5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
b7 = ['red', 'blue', 'magenta', 'cyan', 'green']
b8 = np.unique(b6)
for cluster_label in b8:
    plt.scatter(b2[b6 = = cluster_label, 0], b2[b6 == cluster_label, 1],
                b9 = b7[cluster_label], label=f'Cluster {cluster_label}')
plt.title('Hierarchical Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()