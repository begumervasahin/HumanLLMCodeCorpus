import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(data):
    return data.iloc[:, [8, 12]].values
def fonk3(b9, b1 = 15):
    b2 = []
    for num_clusters in range(1, b1 + 1):
        b3 = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
        b3.fit(b9)
        b2.append(b3.inertia_)
    return b2
def fonk4(b2):
    plt.plot(range(1, len(b2) + 1), b2)
    plt.title('Elbow Method')
    plt.xlabel('Number Of Clusters')
    plt.ylabel('WCSS')
    plt.show()
def fonk5(b9, num_clusters):
    b3 = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    return b3.fit_predict(b9), b3.cluster_centers_
def fonk6(b9, b5, b10):
    b4 = ['red', 'blue', 'green', 'pink']
    for i in range(len(b4)):
        plt.scatter(b9[b5 = = i, 0], b9[b5 == i, 1],
                    b6 = 25, c=b4[i], label=f'Cluster {i+1}')
    plt.scatter(b10[:, 0], b10[:, 1], b6 = 25, c='yellow', label='Centroids')
    plt.title('K-Means Clustering')
    plt.xlabel('Balance')
    plt.ylabel('Estimated Salary in $')
    plt.legend()
    plt.show()
if b7 = = "__main__":
    b8 = fonk1("Churn_Modelling.csv")
    b9 = fonk2(b8)
    b2 = fonk3(b9)
    fonk4(b2)
    a1 = 4
    b5, b10 = fonk5(b9, a1)
    fonk6(b9, b5, b10)