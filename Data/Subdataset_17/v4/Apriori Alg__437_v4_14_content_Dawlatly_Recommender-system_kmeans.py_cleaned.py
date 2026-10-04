
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
np.set_printoptions(threshold=np.inf)
dataset = pd.read_csv('FYP.csv')
X = dataset.iloc[:, [10]].values
Y = dataset.iloc[:, [9]].values
labelencoder_X = LabelEncoder()
X = labelencoder_X.fit_transform(X[:, 0])
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y[:, 0])
encoded_data = np.vstack((Y, X)).T
onehotencoder = OneHotEncoder()
one_hot_encoded_data = onehotencoder.fit_transform(encoded_data).toarray()
pca = PCA(n_components=2)
pca_data = pca.fit_transform(one_hot_encoded_data)
explained_variance = pca.explained_variance_ratio_
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=1000, n_init=10)
    kmeans.fit(pca_data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=1000, n_init=10)
y_kmeans = kmeans.fit_predict(pca_data)
colors = ['red', 'blue', 'green']
for cluster in range(optimal_clusters):
    plt.scatter(pca_data[y_kmeans == cluster, 0], pca_data[y_kmeans == cluster, 1],
                s=100, c=colors[cluster], label=f'Cluster {cluster + 1}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel("Category")
plt.ylabel("Subcategory")
plt.legend()
plt.show()