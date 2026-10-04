import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filename):
    b1 = pd.read_csv(filename)
    return b1.iloc[:, [3, 4]].values
def fonk2(b7):
    plt.figure(b2 = (10, 7))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Distance Between Clusters / Dissimilarities')
    sch.dendrogram(sch.linkage(b7, b3 = 'ward'))
    plt.show()
def fonk3(b7, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b7)
def fonk4(b7, b6, b8, b9):
    plt.figure(b2 = (10, 7))
    for i, color, label in zip(range(len(b9)), b8, b9):
        plt.scatter(b7[b6 = = i, 0], b7[b6 == i, 1], c=color, label=label)
    plt.title('Hierarchical Clustering')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (0-100)')
    plt.legend()
    plt.show()
def fonk5():
    b7 = fonk1('Mall_Customers.csv')
    fonk2(b7)
    b6 = fonk3(b7)
    b8 = ['red', 'blue', 'magenta', 'cyan', 'green']
    b9 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    fonk4(b7, b6, b8, b9)
if b10 = = "__main__":
    fonk5()