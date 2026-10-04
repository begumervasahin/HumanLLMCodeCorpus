
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
def fonk1(b16):
    return pd.read_csv(b16)
def fonk2(b17):
    b1 = b17.iloc[:, [10]].values
    b2 = b17.iloc[:, [9]].values
    b3 = LabelEncoder()
    b1 = b3.fit_transform(b1[:, 0])
    b4 = LabelEncoder()
    b2 = b4.fit_transform(b2[:, 0])
    b5 = np.vstack((b2, b1)).T
    b6 = OneHotEncoder()
    b5 = b6.fit_transform(b5).toarray()
    return b5
def fonk3(data, b7 = 2):
    b8 = PCA(b7=b7)
    b9 = b8.fit_transform(data)
    b10 = b8.explained_variance_ratio_
    return b9, b10
def fonk4(data):
    b11 = []
    for i in range(1, 11):
        b12 = KMeans(b13=i, init='k-means++', max_iter=1000, n_init=10)
        b12.fit(data)
        b11.append(b12.inertia_)
    plt.plot(range(1, 11), b11)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
def fonk5(data, b13 = 3):
    b12 = KMeans(b13=b13, init='k-means++', max_iter=1000, n_init=10)
    b14 = b12.fit_predict(data)
    return b12, b14
def fonk6(data, b12, b14):
    plt.scatter(data[b14 = = 0, 0], data[b14 == 0, 1], b15=100, c='red', label='Cluster 1')
    plt.scatter(data[b14 = = 1, 0], data[b14 == 1, 1], b15=100, c='blue', label='Cluster 2')
    plt.scatter(data[b14 = = 2, 0], data[b14 == 2, 1], b15=100, c='green', label='Cluster 3')
    plt.scatter(b12.cluster_centers_[:, 0], b12.cluster_centers_[:, 1], b15 = 300, c='yellow', label='Centroids')
    plt.title('Clusters of customers')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()
def fonk7():
    b16 = 'FYP.csv'
    b17 = fonk1(b16)
    print(b17.head())
    b18 = fonk2(b17)
    b9, b10 = fonk3(b18)
    print("Explained Variance Ratio:", b10)
    fonk4(b9)
    b12, b14 = fonk5(b9)
    fonk6(b9, b12, b14)
if b19 = = "__main__":
    fonk7()