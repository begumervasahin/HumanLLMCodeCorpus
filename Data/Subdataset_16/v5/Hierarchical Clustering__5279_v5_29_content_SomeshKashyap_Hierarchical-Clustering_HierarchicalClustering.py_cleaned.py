import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filename):
    return pd.read_csv(filename)
def fonk2(data):
    plt.figure(b1 = (10, 7))
    sch.dendrogram(sch.linkage(data, b2 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(data, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(data)
def fonk4(data, b7):
    plt.figure(b1 = (10, 7))
    b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(b5):
        plt.scatter(data[b7 = = i, 0], data[b7 == i, 1], s=100, c=color, label=b6[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = fonk1('Mall_Customers.csv')
    b9 = b8.iloc[:, [3, 4]].values
    fonk2(b9)
    b10 = fonk3(b9, b3=5)
    fonk4(b9, b10)
if b11 = = "__main__":
    fonk5()