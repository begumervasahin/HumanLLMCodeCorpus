
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
b6 = b4.fit_transform(b3[:, 0])
b7 = np.vstack((b6, b5)).T
b8 = OneHotEncoder(b2="auto")
b7 = b8.fit_transform(b7).toarray()
b9 = PCA(n_components=2)
b10 = b9.fit_transform(b7)
b11 = b9.explained_variance_ratio_
b12 = []
for num_clusters in range(1, 11):
    b13 = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=1000, n_init=10)
    b13.fit(b10)
    b12.append(b13.inertia_)
plt.plot(range(1, 11), b12)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
b13 = KMeans(n_clusters=3, init='k-means++', max_iter=1000, n_init=10)
b14 = b13.fit_predict(b10)
for cluster_num in range(3):
    plt.scatter(b10[b14 = = cluster_num, 0], b10[b14 == cluster_num, 1],
                b15 = 100, label=f'Cluster {cluster_num + 1}')
plt.scatter(b13.cluster_centers_[:, 0], b13.cluster_centers_[:, 1], b15 = 300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel("Category")
plt.ylabel("Subcategory")
plt.legend()
plt.show()