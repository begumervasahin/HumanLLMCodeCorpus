
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
dataset = pd.read_csv('FYP.csv')
categories = dataset.iloc[:, [10]].values
subcategories = dataset.iloc[:, [9]].values
label_encoder = LabelEncoder()
categories_encoded = label_encoder.fit_transform(categories[:, 0])
subcategories_encoded = label_encoder.fit_transform(subcategories[:, 0])
encoded_data = np.vstack((subcategories_encoded, categories_encoded)).T
onehot_encoder = OneHotEncoder(categories='auto')
encoded_data = onehot_encoder.fit_transform(encoded_data).toarray()
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(encoded_data)
wcss = []
for num_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=1000, n_init=10)
    kmeans.fit(reduced_data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
optimal_num_clusters = 3
kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', max_iter=1000, n_init=10)
cluster_labels = kmeans.fit_predict(reduced_data)
for cluster_num in range(optimal_num_clusters):
    plt.scatter(reduced_data[cluster_labels == cluster_num, 0], reduced_data[cluster_labels == cluster_num, 1],
                s=100, label=f'Cluster {cluster_num + 1}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Category')
plt.ylabel('Subcategory')
plt.legend()
plt.show()