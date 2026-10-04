
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']]
def fonk1(data):
    plt.figure(b3 = (10, 7))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    sch.dendrogram(sch.linkage(data, b4 = 'ward'))
    plt.show()
fonk1(b2)
def fonk2(data, b5 = 5):
    b6 = AgglomerativeClustering(b5=b5, affinity='euclidean', linkage='ward')
    return b6.fit_predict(data)
b7 = fonk2(b2)
def fonk3(data, b10):
    plt.figure(b3 = (10, 7))
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    b8 = ['red', 'blue', 'green', 'black', 'magenta']
    b9 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for cluster in range(len(b8)):
        plt.scatter(data[b10 = = cluster]['Annual Income (k$)'],
                    data[b10 = = cluster]['Spending Score (1-100)'],
                    b11 = 100, c=b8[cluster], label=b9[cluster])
    plt.legend()
    plt.show()
fonk3(b2, b7)