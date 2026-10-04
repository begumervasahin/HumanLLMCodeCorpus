import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filename):
    return pd.read_csv(filename)
def fonk2(b7):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b7, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b7, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b7)
def fonk4(b7, b5):
    plt.figure(b1 = (10, 7))
    plt.scatter(b7[b5 = = 0, 0], b7[b5 == 0, 1], s=100, c='red', label='Careful')
    plt.scatter(b7[b5 = = 1, 0], b7[b5 == 1, 1], s=100, c='blue', label='Standard')
    plt.scatter(b7[b5 = = 2, 0], b7[b5 == 2, 1], s=100, c='green', label='Target')
    plt.scatter(b7[b5 = = 3, 0], b7[b5 == 3, 1], s=100, c='cyan', label='Careless')
    plt.scatter(b7[b5 = = 4, 0], b7[b5 == 4, 1], s=100, c='magenta', label='Sensible')
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b6 = fonk1('Mall_Customers.csv')
    b7 = b6.iloc[:, [3, 4]].values
    fonk2(b7)
    b5 = fonk3(b7, b3=5)
    fonk4(b7, b5)
if b8 = = "__main__":
    fonk5()