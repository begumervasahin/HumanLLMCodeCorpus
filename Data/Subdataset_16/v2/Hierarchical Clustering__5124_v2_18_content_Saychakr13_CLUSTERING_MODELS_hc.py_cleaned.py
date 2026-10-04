import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(data):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(data, n_clusters):
    b3 = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return b3.fit_predict(data)
def fonk4(data, b5):
    plt.figure(b1 = (10, 7))
    b4 = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i, color in enumerate(b4):
        plt.scatter(data[b5 = = i, 0], data[b5 == i, 1],
                    b6 = 100, c=color, label=f'Cluster {i+1}')
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b7 = fonk1('Mall_Customers.csv')
    b8 = b7.iloc[:, [3, 4]].values
    fonk2(b8)
    b5 = fonk3(b8, n_clusters=5)
    fonk4(b8, b5)
if b9 = = "__main__":
    fonk5()