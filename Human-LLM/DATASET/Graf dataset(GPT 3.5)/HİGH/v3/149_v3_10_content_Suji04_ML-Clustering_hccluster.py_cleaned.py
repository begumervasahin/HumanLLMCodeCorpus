import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b5):
    return pd.read_csv(b5)
def fonk2(b7):
    b1 = sch.b1(sch.linkage(b7, method="ward"))
    plt.title("Dendrogram")
    plt.xlabel("Clusters")
    plt.ylabel("Euclidean Distance")
    plt.show()
def fonk3(b7, b2 = 5):
    b3 = AgglomerativeClustering(b2=b2, affinity="euclidean", linkage="ward")
    return b3.fit_predict(b7)
def fonk4(b7, b4, b8, b9):
    for i, color, label in zip(range(len(b8)), b8, b9):
        plt.scatter(b7[b4 = = i, 0], b7[b4 == i, 1], s=50, c=color, label=label)
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
b5 = 'Mall_Customers.csv'
b6 = fonk1(b5)
b7 = b6.iloc[:, [3, 4]].values
fonk2(b7)
b4 = fonk3(b7)
b8 = ['red', 'blue', 'green', 'gold', 'magenta']
b9 = [f'Cluster {i+1}' for i in range(len(b8))]
fonk4(b7, b4, b8, b9)