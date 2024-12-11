import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']]
b3 = []
for num_clusters in range(1, 11):
    b4 = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    b4.fit(b2)
    b3.append(b4.inertia_)
a1 = 5
b4 = KMeans(n_clusters=a1, init='k-means++', max_iter=300, n_init=10, random_state=0)
b5 = b4.fit_predict(b2)
plt.figure(b6 = (8, 6))
for cluster_id in range(a1):
    plt.scatter(b2.iloc[b5 = = cluster_id, 0],
                b2.iloc[b5 = = cluster_id, 1],
                b7 = 100, label=f'Cluster {cluster_id + 1}')
plt.scatter(b4.cluster_centers_[:, 0], b4.cluster_centers_[:, 1],
            b7 = 300, c='orange', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()