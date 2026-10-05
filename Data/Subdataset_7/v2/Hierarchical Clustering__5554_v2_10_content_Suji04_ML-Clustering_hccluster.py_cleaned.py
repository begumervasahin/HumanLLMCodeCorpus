import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
b3 = sch.b3(sch.linkage(b2, method="ward"))
plt.title("Dendrogram")
plt.xlabel("Clusters")
plt.ylabel("Euclidean Distance")
plt.show()
b4 = AgglomerativeClustering(n_clusters=5, affinity="euclidean", linkage="ward")
b5 = b4.fit_predict(b2)
b6 = ['red', 'blue', 'green', 'gold', 'magenta']
b7 = [f'Cluster {i+1}' for i in range(5)]
for i, color, label in zip(range(5), b6, b7):
    plt.scatter(b2[b5 = = i, 0], b2[b5 == i, 1], s=50, c=color, label=label)
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()