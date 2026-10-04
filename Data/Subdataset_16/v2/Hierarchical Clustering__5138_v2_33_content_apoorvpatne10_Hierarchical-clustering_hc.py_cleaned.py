import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b8):
    b1 = pd.read_csv(b8)
    b2 = b1.iloc[:, [3, 4]].values
    return b2
def fonk2(b2):
    plt.figure(b3 = (10, 7))
    b4 = sch.b4(sch.linkage(b2, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b2, b5 = 5):
    b6 = AgglomerativeClustering(b5=b5, affinity='euclidean', linkage='ward')
    b7 = b6.fit_predict(b2)
    return b7
def fonk4(b2, b7):
    plt.figure(b3 = (10, 7))
    plt.scatter(b2[b7 = = 0, 0], b2[b7 == 0, 1], s=100, c='red', label='Careful')
    plt.scatter(b2[b7 = = 1, 0], b2[b7 == 1, 1], s=100, c='blue', label='Standard')
    plt.scatter(b2[b7 = = 2, 0], b2[b7 == 2, 1], s=100, c='green', label='Targets')
    plt.scatter(b2[b7 = = 3, 0], b2[b7 == 3, 1], s=100, c='cyan', label='Careless')
    plt.scatter(b2[b7 = = 4, 0], b2[b7 == 4, 1], s=100, c='magenta', label='Sensible')
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = 'Mall_Customers.csv'
    b2 = fonk1(b8)
    fonk2(b2)
    b7 = fonk3(b2, b5=5)
    fonk4(b2, b7)
if b9 = = "__main__":
    fonk5()