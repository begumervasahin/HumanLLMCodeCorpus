
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b15):
    b1 = b15.iloc[:, [10]].values
    b2 = b15.iloc[:, [9]].values
    b3 = LabelEncoder()
    b4 = b3.fit_transform(b1[:, 0])
    b5 = b3.fit_transform(b2[:, 0])
    b6 = np.vstack((b5, b4)).T
    b7 = OneHotEncoder(b1='auto')
    b6 = b7.fit_transform(b6).toarray()
    return b6
def fonk3(data, b8 = 2):
    b9 = PCA(b8=b8)
    return b9.fit_transform(data)
def fonk4(data):
    b10 = []
    for num_clusters in range(1, 11):
        b11 = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=1000, n_init=10)
        b11.fit(data)
        b10.append(b11.inertia_)
    return b10
def fonk5(data, b12, centroids):
    for cluster_num in range(len(centroids)):
        plt.scatter(data[b12 = = cluster_num, 0], data[b12 == cluster_num, 1],
                    b13 = 100, label=f'Cluster {cluster_num + 1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], b13 = 300, c='yellow', label='Centroids')
    plt.title('Clusters of customers')
    plt.xlabel('Category')
    plt.ylabel('Subcategory')
    plt.legend()
    plt.show()
if b14 = = "__main__":
    b15 = fonk1('FYP.csv')
    b6 = fonk2(b15)
    b16 = fonk3(b6)
    b10 = fonk4(b16)
    plt.plot(range(1, 11), b10)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
    a1 = 3
    b11 = KMeans(n_clusters=a1, init='k-means++', max_iter=1000, n_init=10)
    b12 = b11.fit_predict(b16)
    fonk5(b16, b12, b11.cluster_centers_)