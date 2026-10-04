import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b9):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b9, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(b9, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b9)
def fonk4(b9, b7):
    plt.figure(b1 = (10, 7))
    b5 = ['red', 'blue', 'green', 'black', 'magenta']
    b6 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    for i, color in enumerate(b5):
        plt.scatter(b9[b7 = = i, 0], b9[b7 == i, 1], s=100, c=color, label=b6[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (K$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b8 = fonk1('Mall_Customers.csv')
    b9 = b8.iloc[:, [3, 4]].values
    fonk2(b9)
    b6 = fonk3(b9)
    fonk4(b9, b6)
if b10 = = "__main__":
    fonk5()