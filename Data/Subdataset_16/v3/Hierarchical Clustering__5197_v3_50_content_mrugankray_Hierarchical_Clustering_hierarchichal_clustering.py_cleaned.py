import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filename):
    b1 = pd.read_csv(filename)
    return b1.iloc[:, [3, 4]].values
def fonk2(b8):
    plt.figure(b2 = (10, 7))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    sch.dendrogram(sch.linkage(b8, b3 = 'ward'))
    plt.show()
def fonk3(b8, a1):
    b4 = AgglomerativeClustering(a1=a1, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b8)
def fonk4(b8, b7, a1):
    plt.figure(b2 = (10, 7))
    b5 = ['red', 'blue', 'magenta', 'cyan', 'green']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(a1):
        plt.scatter(b8[b7 = = i, 0], b8[b7 == i, 1], s=100, c=b5[i], label=b6[i])
    plt.title('Hierarchical Clustering of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = fonk1('Mall_Customers.csv')
    fonk2(b8)
    a1 = 5
    b7 = fonk3(b8, a1)
    fonk4(b8, b7, a1)
if b9 = = "__main__":
    fonk5()