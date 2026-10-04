import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b10):
    b1 = pd.read_csv(b10)
    return b1.iloc[:, [3, 4]].values
def fonk2(b11):
    plt.figure(b2 = (10, 7))
    sch.dendrogram(sch.linkage(b11, b3 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk3(b11, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b11)
def fonk4(b11, b8):
    plt.figure(b2 = (10, 7))
    b6 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b7 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(b6):
        plt.scatter(b11[b8 = = i, 0], b11[b8 == i, 1],
                    b9 = 100, c=color, label=b7[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b10 = 'Mall_Customers.csv'
    b11 = fonk1(b10)
    fonk2(b11)
    b8 = fonk3(b11)
    fonk4(b11, b8)
if b12 = = "__main__":
    fonk5()