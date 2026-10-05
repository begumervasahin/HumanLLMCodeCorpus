
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']].values
b3 = []
for num_clusters in range(1, 11):
    b4 = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    b4.fit(b2)
    b3.append(b4.inertia_)
b4 = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
b5 = b4.fit_predict(b2)
b6 = ['red', 'blue', 'black', 'green', 'yellow']
for cluster_num, color in zip(range(5), b6):
    plt.scatter(b2[b5 = = cluster_num, 0], b2[b5 == cluster_num, 1], s=100, c=color, label=f'Cluster {cluster_num + 1}')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Clusters of Customers')
plt.legend()
plt.show()