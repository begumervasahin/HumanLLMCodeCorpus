
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
np.set_printoptions(b1 = np.inf)
b2 = pd.read_csv('FYP.csv')
b3 = b2.iloc[:, [10]].values
b4 = b2.iloc[:, [9]].values
b5 = LabelEncoder()
b3 = b5.fit_transform(b3[:, 0])
b6 = LabelEncoder()
b4 = b6.fit_transform(b4[:, 0])
b7 = np.vstack((b4, b3)).T
b8 = OneHotEncoder()
b9 = b8.fit_transform(b7).toarray()
b10 = PCA(n_components=2)
b11 = b10.fit_transform(b9)
b12 = b10.explained_variance_ratio_
b13 = []
for i in range(1, 11):
    b14 = KMeans(n_clusters=i, init='k-means++', max_iter=1000, n_init=10)
    b14.fit(b11)
    b13.append(b14.inertia_)
plt.figure(b15 = (10, 6))
plt.plot(range(1, 11), b13, b16 = 'o')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()
a1 = 3
b14 = KMeans(n_clusters=a1, init='k-means++', max_iter=1000, n_init=10)
b17 = b14.fit_predict(b11)
plt.figure(b15 = (10, 6))
b18 = ['red', 'blue', 'green']
for cluster in range(a1):
    plt.scatter(b11[b17 = = cluster, 0], b11[b17 == cluster, 1],
                b19 = 100, c=b18[cluster], label=f'Cluster {cluster + 1}')
plt.scatter(b14.cluster_centers_[:, 0], b14.cluster_centers_[:, 1],
            b19 = 300, c='yellow', label='Centroids', edgecolors='black')
plt.title('Clusters of customers')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.grid(True)
plt.show()