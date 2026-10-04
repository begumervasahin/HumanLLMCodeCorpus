import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
b1 = pd.read_csv("Churn_Modelling.csv")
b2 = b1.iloc[:, [8, 12]].values
b3 = []
for num_clusters in range(1, 16):
    b4 = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    b4.fit(b2)
    b3.append(b4.inertia_)
plt.figure(b5 = (10, 6))
plt.plot(range(1, 16), b3, b6 = 'o', linestyle='--', color='b')
plt.title('Elbow Method to Determine Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.grid(True)
plt.show()
a1 = 4
b4 = KMeans(n_clusters=a1, init='k-means++', random_state=0)
b7 = b4.fit_predict(b2)
plt.figure(b5 = (10, 6))
plt.scatter(b2[b7 = = 0, 0], b2[b7 == 0, 1], b8=50, c='red', label='Cluster 1')
plt.scatter(b2[b7 = = 1, 0], b2[b7 == 1, 1], b8=50, c='blue', label='Cluster 2')
plt.scatter(b2[b7 = = 2, 0], b2[b7 == 2, 1], b8=50, c='green', label='Cluster 3')
plt.scatter(b2[b7 = = 3, 0], b2[b7 == 3, 1], b8=50, c='purple', label='Cluster 4')
plt.scatter(b4.cluster_centers_[:, 0], b4.cluster_centers_[:, 1], b8 = 200, c='yellow', b6='X', label='Centroids')
plt.title('K-Means Clustering of Customers')
plt.xlabel('Balance ($)')
plt.ylabel('Estimated Salary ($)')
plt.legend()
plt.grid(True)
plt.show()