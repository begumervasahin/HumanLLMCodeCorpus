import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b7):
    b1 = sch.b1(sch.linkage(b7, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(b7, b2 = 5):
    b3 = AgglomerativeClustering(b2=b2, affinity='euclidean', linkage='ward')
    return b3.fit_predict(b7)
def fonk4(b7, b5):
    b4 = ['red', 'blue', 'green', 'black', 'magenta']
    for i, color in enumerate(b4):
        plt.scatter(b7[b5 = = i, 0], b7[b5 == i, 1], s=100, c=color, label=f'Cluster {i+1}')
    plt.title('Clusters of clients')
    plt.xlabel('Annual income (K$)')
    plt.ylabel('Spending score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b6 = fonk1('Mall_Customers.csv')
    b7 = b6.iloc[:, [3, 4]].values
    fonk2(b7)
    b5 = fonk3(b7, b2=5)
    fonk4(b7, b5)
if b8 = = '__main__':
    fonk5()