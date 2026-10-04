import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    return b1.iloc[:, [3, 4]].values
def fonk2(b8):
    plt.figure(b2 = (10, 7))
    sch.dendrogram(sch.linkage(b8, b3 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk3(b8, n_clusters):
    b4 = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b8)
def fonk4(b8, b6):
    plt.figure(b2 = (10, 7))
    b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    for cluster_index, color in enumerate(b5):
        plt.scatter(b8[b6 = = cluster_index, 0],
                    b8[b6 = = cluster_index, 1],
                    b7 = 100, c=color, label=f'Cluster {cluster_index + 1}')
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = fonk1('Mall_Customers.csv')
    fonk2(b8)
    b6 = fonk3(b8, n_clusters=5)
    fonk4(b8, b6)
if b9 = = "__main__":
    fonk5()