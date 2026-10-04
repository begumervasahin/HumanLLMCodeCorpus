import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
dataset = pd.read_csv("Churn_Modelling.csv")
features = dataset.iloc[:, [8, 12]].values
wcss = []
for num_clusters in range(1, 16):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 16), wcss)
plt.title('Elbow Method')
plt.xlabel('Number Of Clusters')
plt.ylabel('WCSS')
plt.show()
optimal_num_clusters = 4
kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', random_state=0)
cluster_labels = kmeans.fit_predict(features)
plt.scatter(features[cluster_labels == 0, 0], features[cluster_labels == 0, 1], s=25, c='red', label='Cluster 1')
plt.scatter(features[cluster_labels == 1, 0], features[cluster_labels == 1, 1], s=25, c='blue', label='Cluster 2')
plt.scatter(features[cluster_labels == 2, 0], features[cluster_labels == 2, 1], s=25, c='green', label='Cluster 3')
plt.scatter(features[cluster_labels == 3, 0], features[cluster_labels == 3, 1], s=25, c='pink', label='Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=25, c='yellow', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Balance')
plt.ylabel('Estimated Salary in $')
plt.legend()
plt.show()