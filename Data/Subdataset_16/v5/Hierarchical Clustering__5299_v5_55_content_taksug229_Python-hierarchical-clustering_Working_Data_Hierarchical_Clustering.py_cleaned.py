import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b7):
    b1 = pd.read_csv(b7)
    return b1.iloc[:, [3, 4]].values
def fonk2(b8):
    plt.figure(b2 = (10, 7))
    sch.dendrogram(sch.linkage(b8, b3 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(b8, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b8)
def fonk4(b8, b6, b9, b10):
    plt.figure(b2 = (10, 7))
    for i, color in enumerate(b10):
        plt.scatter(b8[b6 = = i, 0], b8[b6 == i, 1], s=100, c=color, label=b9[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b7 = 'Mall_Customers.csv'
    b8 = fonk1(b7)
    fonk2(b8)
    b6 = fonk3(b8)
    b9 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    b10 = ['red', 'blue', 'green', 'cyan', 'magenta']
    fonk4(b8, b6, b9, b10)
if b11 = = "__main__":
    fonk5()