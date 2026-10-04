import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b8, feature_columns):
    return b8.iloc[:, feature_columns].values
def fonk3(b9):
    plt.figure(b1 = (10, 7))
    b2 = sch.b2(sch.linkage(b9, method='ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distances')
    plt.show()
def fonk4(b9, b3 = 5):
    b4 = AgglomerativeClustering(b3=b3, affinity='euclidean', linkage='ward')
    return b4.fit_predict(b9)
def fonk5(b9, b7):
    plt.figure(b1 = (10, 7))
    b5 = ['red', 'blue', 'green', 'cyan', 'magenta']
    b6 = [f'Cluster {i+1}' for i in range(len(b5))]
    for i in range(len(b5)):
        plt.scatter(b9[b7 = = i, 0], b9[b7 == i, 1], s=100, c=b5[i], label=b6[i])
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk6():
    b8 = fonk1('Mall_Customers.csv')
    b9 = fonk2(b8, [3, 4])
    fonk3(b9)
    b7 = fonk4(b9)
    fonk5(b9, b7)
if b10 = = "__main__":
    fonk6()