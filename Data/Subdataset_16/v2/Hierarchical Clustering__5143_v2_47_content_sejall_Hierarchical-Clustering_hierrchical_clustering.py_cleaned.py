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
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b8, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b8)
def fonk4(b8, b6):
    plt.figure(b2 = (10, 7))
    plt.scatter(b8[b6 = = 0, 0], b8[b6 == 0, 1], s=100, c='red', label='Careful')
    plt.scatter(b8[b6 = = 1, 0], b8[b6 == 1, 1], s=100, c='blue', label='Standard')
    plt.scatter(b8[b6 = = 2, 0], b8[b6 == 2, 1], s=100, c='green', label='Target')
    plt.scatter(b8[b6 = = 3, 0], b8[b6 == 3, 1], s=100, c='cyan', label='Careless')
    plt.scatter(b8[b6 = = 4, 0], b8[b6 == 4, 1], s=100, c='magenta', label='Sensible')
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b7 = 'Mall_Customers.csv'
    b8 = fonk1(b7)
    fonk2(b8)
    b6 = fonk3(b8, b4=5)
    fonk4(b8, b6)
if b9 = = "__main__":
    fonk5()