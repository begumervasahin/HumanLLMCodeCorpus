import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b8):
    return pd.read_csv(b8)
def fonk2(b10, b9):
    return b10[b9]
def fonk3(data):
    plt.figure(b1 = (10, 6))
    b2 = sch.b2(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk4(data, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(data)
def fonk5(data, b7):
    plt.figure(b1 = (10, 6))
    b5 = ['red', 'blue', 'green', 'black', 'magenta']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(len(np.unique(b7))):
        plt.scatter(data[b7 = = i, 0], data[b7 == i, 1], s=100, c=b5[i], label=b6[i])
    plt.title('Clusters of clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk6():
    b8 = 'Mall_Customers.csv'
    b9 = ['Annual Income (k$)', 'Spending Score (1-100)']
    b10 = fonk1(b8)
    b11 = fonk2(b10, b9)
    fonk3(b11)
    b7 = fonk4(b11)
    fonk5(b11.values, b7)
if b12 = = "__main__":
    fonk6()