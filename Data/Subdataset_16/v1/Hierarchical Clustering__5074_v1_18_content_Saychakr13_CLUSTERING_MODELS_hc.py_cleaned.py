import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b7):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b7, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(b7, n_clusters):
    b3 = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return b3.fit_predict(b7)
def fonk4(b7, b5):
    plt.figure(b1 = (10, 7))
    b4 = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i in range(len(b4)):
        plt.scatter(b7[b5 = = i, 0], b7[b5 == i, 1], s=100, c=b4[i], label=f'Cluster {i+1}')
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b6 = fonk1('Mall_Customers.csv')
    b7 = b6.iloc[:, [3, 4]].values
    fonk2(b7)
    b5 = fonk3(b7, n_clusters=5)
    fonk4(b7, b5)
if b8 = = "__main__":
    fonk5()