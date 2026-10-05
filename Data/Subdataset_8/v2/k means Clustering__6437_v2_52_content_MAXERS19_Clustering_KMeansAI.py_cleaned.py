import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
dataset = pd.read_csv('Mall_Customers.csv')
features = dataset[['Annual Income (k$)', 'Spending Score (1-100)']]
inertia_values = []
for num_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(features)
    inertia_values.append(kmeans.inertia_)
optimal_num_clusters = 5
kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(features)
plt.figure(figsize=(8, 6))
for cluster_id in range(optimal_num_clusters):
    plt.scatter(features.iloc[cluster_labels == cluster_id, 0],
                features.iloc[cluster_labels == cluster_id, 1],
                s=100, label=f'Cluster {cluster_id + 1}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, c='orange', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()