import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b7):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b7, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b7, n_clusters):
    b3 = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    return b3.fit_predict(b7)
def fonk4(b7, b5):
    plt.figure(b1 = (10, 7))
    b4 = [
        ('Careful', 'red'),
        ('Standard', 'blue'),
        ('Target', 'green'),
        ('Careless', 'cyan'),
        ('Sensible', 'magenta')
    ]
    for i, (label, color) in enumerate(b4):
        plt.scatter(b7[b5 = = i, 0], b7[b5 == i, 1], s=100, c=color, label=label)
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b6 = fonk1("Mall_Customers.csv")
    b7 = b6.iloc[:, [3, 4]].values
    fonk2(b7)
    b5 = fonk3(b7, n_clusters=5)
    fonk4(b7, b5)
if b8 = = "__main__":
    fonk5()