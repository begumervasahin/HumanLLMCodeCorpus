import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    b2 = b1.iloc[:, [3, 4]].values
    return b2
def fonk2(b2):
    plt.figure(b3 = (10, 7))
    b4 = sch.b4(sch.linkage(b2, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(b2, b5 = 5):
    b6 = AgglomerativeClustering(b5=b5, affinity='euclidean', linkage='ward')
    return b6.fit_predict(b2)
def fonk4(b2, b9):
    plt.figure(b3 = (10, 7))
    b7 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b8 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i in range(len(b7)):
        plt.scatter(b2[b9 = = i, 0], b2[b9 == i, 1], s=100, c=b7[i], label=b8[i])
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b2 = fonk1('Mall_Customers.csv')
    fonk2(b2)
    b9 = fonk3(b2)
    fonk4(b2, b9)
if b10 = = "__main__":
    fonk5()