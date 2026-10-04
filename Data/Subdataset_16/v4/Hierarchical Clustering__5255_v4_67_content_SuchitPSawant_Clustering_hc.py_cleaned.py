import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b9, columns):
    return b9.iloc[:, columns].values
def fonk3(b10):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b10, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk4(b10, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b10)
def fonk5(b10, b7):
    plt.figure(b1 = (10, 7))
    b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b6 = [f'Cluster {i+1}' for i in range(len(b5))]
    for i, color in enumerate(b5):
        plt.scatter(b10[b7 = = i, 0], b10[b7 == i, 1],
                    b8 = 100, c=color, label=b6[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk6():
    b9 = fonk1('Mall_Customers.csv')
    b10 = fonk2(b9, [3, 4])
    fonk3(b10)
    b7 = fonk4(b10)
    fonk5(b10, b7)
if b11 = = "__main__":
    fonk6()