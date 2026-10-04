import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b11):
    b1 = pd.read_csv(b11)
    b2 = b1.iloc[:, [3, 4]].values
    return b2
def fonk2(b12):
    plt.figure(b3 = (10, 7))
    sch.dendrogram(sch.linkage(b12, b4 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk3(b12, b5 = 5):
    b6 = AgglomerativeClustering(b5=b5, affinity='euclidean', linkage='ward')
    b7 = b6.fit_predict(b12)
    return b7
def fonk4(b12, b10):
    plt.figure(b3 = (10, 7))
    b8 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b9 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for cluster_id, color in enumerate(b8):
        plt.scatter(b12[b10 = = cluster_id, 0], b12[b10 == cluster_id, 1], s=100, c=color, label=b9[cluster_id])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b11 = 'Mall_Customers.csv'
    b12 = fonk1(b11)
    fonk2(b12)
    b10 = fonk3(b12, b5=5)
    fonk4(b12, b10)
if b13 = = "__main__":
    fonk5()