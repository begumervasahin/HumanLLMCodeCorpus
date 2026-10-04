import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b9, b1 = 'ward'):
    plt.figure(b2 = (10, 7))
    sch.dendrogram(sch.linkage(b9, b1 = b1))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk3(b9, b3 = 5, affinity='euclidean', linkage='ward'):
    b4 = AgglomerativeClustering(b3=b3, affinity=affinity, linkage=linkage)
    return b4.fit_predict(b9)
def fonk4(b9, b7, b5 = None, b6=None):
    if b5 is None:
        b5 = ['red', 'blue', 'green', 'black', 'magenta']
    if b6 is None:
        b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    plt.figure(b2 = (10, 7))
    for i, color in enumerate(b5):
        plt.scatter(b9[b7 = = i, 0], b9[b7 == i, 1], s=100, c=color, label=b6[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = fonk1('Mall_Customers.csv')
    b9 = b8.iloc[:, [3, 4]].values
    fonk2(b9)
    b10 = fonk3(b9)
    fonk4(b9, b10)
if b11 = = "__main__":
    fonk5()