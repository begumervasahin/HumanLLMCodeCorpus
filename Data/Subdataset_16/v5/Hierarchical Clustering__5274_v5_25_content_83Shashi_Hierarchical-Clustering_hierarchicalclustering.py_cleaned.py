import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    return b1.iloc[:, [3, 4]].values
def fonk2(b8):
    plt.figure(b2 = (10, 7))
    b3 = sch.b3(sch.linkage(b8, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b8, n_clusters):
    b4 = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b8)
def fonk4(b8, b7):
    plt.figure(b2 = (10, 7))
    b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(b5):
        plt.scatter(b8[b7 = = i, 0], b8[b7 == i, 1], s=100, c=color, label=b6[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = fonk1("Mall_Customers.csv")
    fonk2(b8)
    b7 = fonk3(b8, n_clusters=5)
    fonk4(b8, b7)
if b9 = = "__main__":
    fonk5()