import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b6):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b6, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b6, n_clusters):
    b3 = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return b3.fit_predict(b6)
def fonk4(b6, b4):
    plt.figure(b1 = (10, 7))
    plt.scatter(b6[b4 = = 0, 0], b6[b4 == 0, 1], s=100, c='red', label='Careful')
    plt.scatter(b6[b4 = = 1, 0], b6[b4 == 1, 1], s=100, c='blue', label='Standard')
    plt.scatter(b6[b4 = = 2, 0], b6[b4 == 2, 1], s=100, c='green', label='Target')
    plt.scatter(b6[b4 = = 3, 0], b6[b4 == 3, 1], s=100, c='cyan', label='Careless')
    plt.scatter(b6[b4 = = 4, 0], b6[b4 == 4, 1], s=100, c='magenta', label='Sensible')
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b5 = fonk1("Mall_Customers.csv")
    b6 = b5.iloc[:, [3, 4]].values
    fonk2(b6)
    b4 = fonk3(b6, n_clusters=5)
    fonk4(b6, b4)
if b7 = = "__main__":
    fonk5()