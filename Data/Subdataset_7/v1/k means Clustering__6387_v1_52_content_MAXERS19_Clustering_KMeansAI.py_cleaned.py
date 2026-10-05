import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
b3 = []
for i in range(1, 11):
    b4 = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    b4.fit(b2)
    b3.append(b4.inertia_)
b4 = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
b5 = b4.fit_predict(b2)
plt.figure(b6 = (8, 6))
plt.scatter(b2[b5 = = 0, 0], b2[b5 == 0, 1], b7=100, c='red', label='Cluster 1')
plt.scatter(b2[b5 = = 1, 0], b2[b5 == 1, 1], b7=100, c='blue', label='Cluster 2')
plt.scatter(b2[b5 = = 2, 0], b2[b5 == 2, 1], b7=100, c='black', label='Cluster 3')
plt.scatter(b2[b5 = = 3, 0], b2[b5 == 3, 1], b7=100, c='green', label='Cluster 4')
plt.scatter(b2[b5 = = 4, 0], b2[b5 == 4, 1], b7=100, c='yellow', label='Cluster 5')
plt.scatter(b4.cluster_centers_[:, 0], b4.cluster_centers_[:, 1], b7 = 300, c='orange', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()