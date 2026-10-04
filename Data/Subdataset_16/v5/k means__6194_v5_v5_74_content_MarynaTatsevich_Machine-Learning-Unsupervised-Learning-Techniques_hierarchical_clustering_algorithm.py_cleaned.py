import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b9):
    return pd.read_csv(b9)
def fonk2(b11, b10):
    return b11[b10]
def fonk3(data):
    plt.figure(b1 = (10, 6))
    b2 = sch.b2(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk4(data, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(data)
def fonk5(data, b7):
    plt.figure(b1 = (10, 6))
    b5 = ['red', 'blue', 'green', 'black', 'magenta']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for cluster_id in range(len(np.unique(b7))):
        plt.scatter(data[b7 = = cluster_id, 0], data[b7 == cluster_id, 1],
                    b8 = 100, c=b5[cluster_id], label=b6[cluster_id])
    plt.title('Clusters of clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk6():
    b9 = 'Mall_Customers.csv'
    b10 = ['Annual Income (k$)', 'Spending Score (1-100)']
    b11 = fonk1(b9)
    b12 = fonk2(b11, b10)
    fonk3(b12)
    b7 = fonk4(b12)
    fonk5(b12.values, b7)
if b13 = = "__main__":
    fonk6()