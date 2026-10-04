import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filename):
    return pd.read_csv(filename)
def fonk2(b10):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b10, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b10, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b10)
def fonk4(b10, b7):
    plt.figure(b1 = (10, 7))
    b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(len(b6)):
        plt.scatter(b10[b7 = = i, 0], b10[b7 == i, 1],
                    b8 = 100, c=b5[i], label=b6[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b9 = fonk1('Mall_Customers.csv')
    b10 = b9.iloc[:, [3, 4]].values
    fonk2(b10)
    b7 = fonk3(b10, b3=5)
    fonk4(b10, b7)
if b11 = = "__main__":
    fonk5()