import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    return b1.iloc[:, [3, 4]].values
def fonk2(b8):
    plt.figure(b2 = (10, 7))
    sch.dendrogram(sch.linkage(b8, b3 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(b8, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b8)
def fonk4(b8, labels, b7):
    plt.figure(b2 = (10, 7))
    b6 = ['red', 'blue', 'green', 'cyan', 'magenta']
    for i, color in enumerate(b6):
        plt.scatter(b8[b7 = = i, 0], b8[b7 == i, 1], s=100, c=color, label=labels[i])
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b7 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    b8 = fonk1('Mall_Customers.csv')
    fonk2(b8)
    b9 = fonk3(b8)
    fonk4(b8, b7, b9)
if b10 = = "__main__":
    fonk5()