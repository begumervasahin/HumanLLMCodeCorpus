import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b7):
    b1 = pd.read_csv(b7)
    return b1.iloc[:, [3, 4]].values
def fonk2(data):
    plt.figure(b2 = (10, 7))
    b3 = sch.b3(sch.linkage(data, method='ward'))
    plt.title("Dendrogram")
    plt.xlabel("Customers")
    plt.ylabel("Euclidean Distance")
    plt.show()
def fonk3(data, a1):
    b4 = AgglomerativeClustering(a1=a1, affinity='euclidean', linkage='ward')
    return b4.fit_predict(data)
def fonk4(data, b6, a1):
    plt.figure(b2 = (10, 7))
    b5 = ['red', 'blue', 'green', 'gold', 'magenta']
    for i in range(a1):
        plt.scatter(data[b6 = = i, 0], data[b6 == i, 1], s=50, c=b5[i], label=f'Cluster {i+1}')
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b7 = 'Mall_Customers.csv'
    b8 = fonk1(b7)
    fonk2(b8)
    a1 = 5
    b9 = fonk3(b8, a1)
    fonk4(b8, b9, a1)
if b10 = = "__main__":
    fonk5()