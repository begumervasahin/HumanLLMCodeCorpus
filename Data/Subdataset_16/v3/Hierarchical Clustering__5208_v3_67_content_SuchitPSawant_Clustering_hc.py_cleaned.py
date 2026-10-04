import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b8):
    return pd.read_csv(b8)
def fonk2(b9, columns):
    return b9.iloc[:, columns].values
def fonk3(b10):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b10, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk4(b10, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b10)
def fonk5(b10, b6, b5 = None):
    plt.figure(b1 = (10, 7))
    if b5 is None:
        b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i, color in enumerate(b5):
        plt.scatter(b10[b6 = = i, 0], b10[b6 == i, 1],
                    b7 = 100, c=color, label=f'Cluster {i+1}')
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk6(b8 = 'Mall_Customers.csv', feature_columns=[3, 4], b3=5):
    b9 = fonk1(b8)
    b10 = fonk2(b9, feature_columns)
    fonk3(b10)
    b6 = fonk4(b10, b3)
    fonk5(b10, b6)
if b11 = = "__main__":
    fonk6()