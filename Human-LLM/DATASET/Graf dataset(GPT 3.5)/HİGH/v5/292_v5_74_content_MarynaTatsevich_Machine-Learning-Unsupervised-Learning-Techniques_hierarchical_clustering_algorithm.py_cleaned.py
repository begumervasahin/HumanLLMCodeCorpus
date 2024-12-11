
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']]
def fonk1(data):
    b3 = sch.b3(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk2(data, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    b6 = b5.fit_predict(data)
    return b6
def fonk3(data, b6):
    plt.figure(b7 = (10, 6))
    b8 = ['red', 'blue', 'green', 'black', 'magenta']
    b9 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(len(np.unique(b6))):
        plt.scatter(data[b6 = = i, 0], data[b6 == i, 1], s=100, c=b8[i], label=b9[i])
    plt.title('Clusters of clients')
    plt.xlabel('Annual income (K$)')
    plt.ylabel('Spending score (1-100)')
    plt.legend()
    plt.show()
def fonk4():
    fonk1(b2)
    b6 = fonk2(b2)
    fonk3(b2.values, b6)
if b10 = = "__main__":
    fonk4()