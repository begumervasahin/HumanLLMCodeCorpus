import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b10):
    b1 = pd.read_csv(b10)
    b2 = b1.iloc[:, [3, 4]].values
    return b2
def fonk2(X):
    plt.figure(b3 = (10, 7))
    b4 = sch.b4(sch.linkage(X, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(X, b5 = 5):
    b6 = AgglomerativeClustering(b5=b5, affinity='euclidean', linkage='ward')
    b7 = b6.fit_predict(X)
    return b7
def fonk4(X, b9):
    plt.figure(b3 = (10, 7))
    b8 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b7 = ['Careful', 'Standard', 'Targets', 'Careless', 'Sensible']
    for i, color in enumerate(b8):
        plt.scatter(X[b9 = = i, 0], X[b9 == i, 1], s=100, c=color, label=b7[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b10 = 'Mall_Customers.csv'
    b2 = fonk1(b10)
    fonk2(b2)
    b7 = fonk3(b2, b5=5)
    fonk4(b2, b7)
if b11 = = "__main__":
    fonk5()