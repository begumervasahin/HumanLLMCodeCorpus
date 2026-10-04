import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
plt.figure(b3 = (10, 7))
b4 = sch.b4(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()
b5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
plt.figure(b3 = (10, 7))
plt.scatter(b2[b6 = = 0, 0], b2[b6 == 0, 1], s=100, c='red', label='Careful')
plt.scatter(b2[b6 = = 1, 0], b2[b6 == 1, 1], s=100, c='blue', label='Standard')
plt.scatter(b2[b6 = = 2, 0], b2[b6 == 2, 1], s=100, c='green', label='Target')
plt.scatter(b2[b6 = = 3, 0], b2[b6 == 3, 1], s=100, c='cyan', label='Careless')
plt.scatter(b2[b6 = = 4, 0], b2[b6 == 4, 1], s=100, c='magenta', label='Sensible')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()