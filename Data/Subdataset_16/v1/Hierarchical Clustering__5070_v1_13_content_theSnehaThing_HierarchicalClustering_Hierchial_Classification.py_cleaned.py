import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b8):
    b1 = pd.read_csv(b8)
    return b1.iloc[:, [3, 4]].values
def fonk2(b9):
    plt.figure(b2 = (10, 7))
    b3 = sch.b3(sch.linkage(b9, method='ward'))
    plt.title("Dendrogram")
    plt.xlabel("Customers")
    plt.ylabel("Euclidean distances")
    plt.show()
def fonk3(b9, a1):
    b4 = AgglomerativeClustering(a1=a1, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b9)
def fonk4(b9, b7, a1):
    plt.figure(b2 = (10, 7))
    b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(a1):
        plt.scatter(b9[b7 = = i, 0], b9[b7 == i, 1], s=100, c=b5[i], label=b6[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = 'Mall_Customers.csv'
    b9 = fonk1(b8)
    fonk2(b9)
    a1 = 5
    b10 = fonk3(b9, a1)
    fonk4(b9, b10, a1)
if b11 = = "__main__":
    fonk5()