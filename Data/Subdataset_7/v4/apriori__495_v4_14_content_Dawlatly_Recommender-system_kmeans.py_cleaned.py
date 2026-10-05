
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
b1 = pd.read_csv('FYP.csv')
b2 = b1.iloc[:, [10]].values
b3 = b1.iloc[:, [9]].values
b4 = LabelEncoder()
b5 = b4.fit_transform(b2[:, 0])
b6 = LabelEncoder()
b7 = b6.fit_transform(b3[:, 0])
b8 = np.vstack((b7, b5)).T
b9 = OneHotEncoder(b2="auto")
b8 = b9.fit_transform(b8).toarray()
b10 = PCA(n_components=2)
b11 = b10.fit_transform(b8)
b12 = b10.explained_variance_ratio_
b13 = []
for i in range(1, 11):
    b14 = KMeans(n_clusters=i, init='k-means++', max_iter=1000, n_init=10)
    b14.fit(b11)
    b13.append(b14.inertia_)
plt.plot(range(1, 11), b13)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
b14 = KMeans(n_clusters=3, init='k-means++', max_iter=1000, n_init=10)
b15 = b14.fit_predict(b11)
plt.scatter(b11[b15 = = 0, 0], b11[b15 == 0, 1], b16=100, c='red', label='Cluster 1')
plt.scatter(b11[b15 = = 1, 0], b11[b15 == 1, 1], b16=100, c='blue', label='Cluster 2')
plt.scatter(b11[b15 = = 2, 0], b11[b15 == 2, 1], b16=100, c='green', label='Cluster 3')
plt.scatter(b14.cluster_centers_[:, 0], b14.cluster_centers_[:, 1], b16 = 300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel("Category")
plt.ylabel("Subcategory")
plt.legend()
plt.show()