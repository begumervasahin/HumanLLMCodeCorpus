
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
dataset = pd.read_csv('Mall_Customers.csv')
features = dataset[['Annual Income (k$)', 'Spending Score (1-100)']].values
wcss = []
for num_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(features)
colors = ['red', 'blue', 'black', 'green', 'yellow']
for cluster_num, color in zip(range(5), colors):
    plt.scatter(features[cluster_labels == cluster_num, 0], features[cluster_labels == cluster_num, 1], s=100, c=color, label=f'Cluster {cluster_num + 1}')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Clusters of Customers')
plt.legend()
plt.show()