
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
dataset = pd.read_csv('FYP.csv')
categories = dataset.iloc[:, [10]].values
subcategories = dataset.iloc[:, [9]].values
label_encoder_X = LabelEncoder()
X = label_encoder_X.fit_transform(categories[:, 0])
label_encoder_Y = LabelEncoder()
Y = label_encoder_Y.fit_transform(subcategories[:, 0])
encoded_data = np.vstack((Y, X)).T
onehot_encoder = OneHotEncoder(categories="auto")
encoded_data = onehot_encoder.fit_transform(encoded_data).toarray()
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(encoded_data)
explained_variance = pca.explained_variance_ratio_
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=1000, n_init=10)
    kmeans.fit(reduced_data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=1000, n_init=10)
y_kmeans = kmeans.fit_predict(reduced_data)
plt.scatter(reduced_data[y_kmeans == 0, 0], reduced_data[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(reduced_data[y_kmeans == 1, 0], reduced_data[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(reduced_data[y_kmeans == 2, 0], reduced_data[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel("Category")
plt.ylabel("Subcategory")
plt.legend()
plt.show()