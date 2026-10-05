
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
dataset = pd.read_csv("Churn_Modelling.csv")
features_to_extract = [8, 12]
X = dataset.iloc[:, features_to_extract].values
wcss = []
for num_clusters in range(1, 16):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 16), wcss)
plt.title('Elbow Method')
plt.xlabel('Number Of Clusters')
plt.ylabel('WCSS')
plt.show()
optimal_num_clusters = 4
kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', random_state=0)
cluster_labels = kmeans.fit_predict(X)
colors = ['red', 'blue', 'green', 'pink']
for cluster_num, color in zip(range(optimal_num_clusters), colors):
    plt.scatter(X[cluster_labels == cluster_num, 0], X[cluster_labels == cluster_num, 1], s=25, c=color, label=f'Cluster {cluster_num+1}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=25, c='yellow', label='Centroid')
plt.title('KMeans Clustering')
plt.xlabel('Balance')
plt.ylabel('Estimated Salary in $')
plt.legend()
plt.show()