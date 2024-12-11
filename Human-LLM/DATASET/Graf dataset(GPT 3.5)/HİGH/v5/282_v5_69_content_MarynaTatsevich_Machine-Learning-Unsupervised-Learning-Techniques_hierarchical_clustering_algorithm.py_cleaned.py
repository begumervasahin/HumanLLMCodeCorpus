import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']].values
def fonk1(b2):
    b3 = sch.b3(sch.linkage(b2, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk2(b2):
    b4 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b2)
def fonk3(b2, b7):
    b5 = ['red', 'blue', 'green', 'black', 'magenta']
    b6 = np.unique(b7)
    for label in b6:
        plt.scatter(b2[b7 = = label, 0], b2[b7 == label, 1], s=100, c=b5[label], label=f'Cluster {label+1}')
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk4():
    fonk1(b2)
    b7 = fonk2(b2)
    fonk3(b2, b7)
if b8 = = '__main__':
    fonk4()