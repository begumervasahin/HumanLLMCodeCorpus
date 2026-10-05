
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
b2 = b4.fit_transform(b2[:, 0])
b5 = LabelEncoder()
b3 = b5.fit_transform(b3[:, 0])
b6 = np.vstack((b3, b2)).T
b7 = OneHotEncoder(categories='auto')
b6 = b7.fit_transform(b6).toarray()
b8 = PCA(n_components=2)
b6 = b8.fit_transform(b6)
b9 = []
for i in range(1, 11):
    b10 = KMeans(n_clusters=i, init='k-means++', max_iter=1000, n_init=10)
    b10.fit(b6)
    b9.append(b10.inertia_)
plt.plot(range(1, 11), b9)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
b10 = KMeans(n_clusters=3, init='k-means++', max_iter=1000, n_init=10)
b11 = b10.fit_predict(b6)
plt.scatter(b6[b11 = = 0, 0], b6[b11 == 0, 1], b12=100, c='red', label='Cluster 1')
plt.scatter(b6[b11 = = 1, 0], b6[b11 == 1, 1], b12=100, c='blue', label='Cluster 2')
plt.scatter(b6[b11 = = 2, 0], b6[b11 == 2, 1], b12=100, c='green', label='Cluster 3')
plt.scatter(b10.cluster_centers_[:, 0], b10.cluster_centers_[:, 1], b12 = 300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel("Category")
plt.ylabel("Subcategory")
plt.legend()
plt.show()