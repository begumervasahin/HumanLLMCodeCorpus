import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv("Mall_Customers.csv")
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']].values
b3 = sch.b3(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()
b4 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b5 = b4.fit_predict(b2)
plt.scatter(b2[b5 = = 0, 0], b2[b5 == 0, 1], s=100, c='red', label='Careful')
plt.scatter(b2[b5 = = 1, 0], b2[b5 == 1, 1], s=100, c='blue', label='Standard')
plt.scatter(b2[b5 = = 2, 0], b2[b5 == 2, 1], s=100, c='green', label='Target')
plt.scatter(b2[b5 = = 3, 0], b2[b5 == 3, 1], s=100, c='cyan', label='Careless')
plt.scatter(b2[b5 = = 4, 0], b2[b5 == 4, 1], s=100, c='magenta', label='Sensible')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (K$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()