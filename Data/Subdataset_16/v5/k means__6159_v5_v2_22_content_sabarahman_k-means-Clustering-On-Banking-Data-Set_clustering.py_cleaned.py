import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
def fonk1(b9):
    return pd.read_csv(b9)
def fonk2(b11, b10):
    return b11.iloc[:, b10].values
def fonk3(b12, b1 = 15):
    b2 = []
    for num_clusters in range(1, b1 + 1):
        b3 = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
        b3.fit(b12)
        b2.append(b3.inertia_)
    return b2
def fonk4(b2):
    plt.figure(b4 = (10, 6))
    plt.plot(range(1, len(b2) + 1), b2, b5 = 'o', linestyle='--', color='b')
    plt.title('Elbow Method to Determine Optimal Number of Clusters')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
    plt.grid(True)
    plt.show()
def fonk5(b12, num_clusters):
    b3 = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0)
    return b3.fit_predict(b12), b3.cluster_centers_
def fonk6(b12, b7, b13):
    plt.figure(b4 = (10, 6))
    b6 = ['red', 'blue', 'green', 'purple']
    for i in range(len(b6)):
        plt.scatter(b12[b7 = = i, 0], b12[b7 == i, 1],
                    b8 = 50, c=b6[i], label=f'Cluster {i + 1}')
    plt.scatter(b13[:, 0], b13[:, 1],
                b8 = 200, c='yellow', b5='X', label='Centroids')
    plt.title('K-Means Clustering of Customers')
    plt.xlabel('Balance ($)')
    plt.ylabel('Estimated Salary ($)')
    plt.legend()
    plt.grid(True)
    plt.show()
b9 = "Churn_Modelling.csv"
b10 = [8, 12]
a1 = 4
b11 = fonk1(b9)
b12 = fonk2(b11, b10)
b2 = fonk3(b12)
fonk4(b2)
b7, b13 = fonk5(b12, a1)
fonk6(b12, b7, b13)