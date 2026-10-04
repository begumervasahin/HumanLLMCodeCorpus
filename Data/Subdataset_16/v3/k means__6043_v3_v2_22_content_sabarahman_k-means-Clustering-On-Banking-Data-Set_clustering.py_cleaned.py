import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
b1 = pd.read_csv("Churn_Modelling.csv")
b2 = b1.iloc[:, [8, 12]].values
def fonk1(data, a1):
    b3 = []
    for num_clusters in range(1, a1 + 1):
        b4 = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
        b4.fit(data)
        b3.append(b4.inertia_)
    return b3
a1 = 15
b3 = fonk1(b2, a1)
def fonk2(b3, a1):
    plt.figure(b5 = (10, 6))
    plt.plot(range(1, a1 + 1), b3, b6 = 'o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.show()
fonk2(b3, a1)
a2 = 4
b4 = KMeans(n_clusters=a2, init='k-means++', random_state=0)
b7 = b4.fit_predict(b2)
def fonk3(b2, b7, centroids):
    plt.figure(b5 = (10, 6))
    b8 = ['red', 'blue', 'green', 'pink']
    for i in range(len(np.unique(b7))):
        plt.scatter(b2[b7 = = i, 0], b2[b7 == i, 1],
                    b9 = 25, c=b8[i], label=f'Cluster {i + 1}')
    plt.scatter(centroids[:, 0], centroids[:, 1],
                b9 = 100, c='yellow', label='Centroids', edgecolor='black')
    plt.title('K-Means Clustering')
    plt.xlabel('Balance')
    plt.ylabel('Estimated Salary in $')
    plt.legend()
    plt.grid(True)
    plt.show()
fonk3(b2, b7, b4.cluster_centers_)