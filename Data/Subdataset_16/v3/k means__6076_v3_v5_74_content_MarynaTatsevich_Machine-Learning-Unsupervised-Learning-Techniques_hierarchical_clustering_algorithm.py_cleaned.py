import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filepath):
    return pd.read_csv(filepath)
def fonk2(b9, b10):
    return b9[b10]
def fonk3(data):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(data, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk4(data, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    b5 = b4.fit_predict(data)
    return b5
def fonk5(data, b5):
    plt.figure(b1 = (10, 6))
    b6 = ['red', 'blue', 'green', 'black', 'magenta']
    b7 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for cluster in np.unique(b5):
        plt.scatter(data[b5 = = cluster, 0], data[b5 == cluster, 1],
                    b8 = 100, c=b6[cluster], label=b7[cluster])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk6():
    b9 = fonk1('Mall_Customers.csv')
    b10 = ['Annual Income (k$)', 'Spending Score (1-100)']
    b11 = fonk2(b9, b10)
    fonk3(b11)
    b5 = fonk4(b11)
    fonk5(b11.values, b5)
if b12 = = "__main__":
    fonk6()