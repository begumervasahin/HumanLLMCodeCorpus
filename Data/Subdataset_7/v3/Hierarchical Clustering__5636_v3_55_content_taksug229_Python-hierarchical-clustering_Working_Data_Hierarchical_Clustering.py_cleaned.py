import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']].values
plt.figure(b3 = (10, 5))
b4 = sch.b4(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()
b5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
plt.figure(b3 = (10, 6))
b7 = ['red', 'blue', 'green', 'cyan', 'magenta']
b8 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i, color, label in zip(range(5), b7, b8):
    plt.scatter(b2[b6 = = i, 0], b2[b6 == i, 1], s=100, c=color, label=label)
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()