import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
def fonk1(b9):
    b1 = pd.read_csv(b9)
    return b1.iloc[:, [3, 4]].values
def fonk2(b10):
    plt.figure(b2 = (10, 7))
    sch.dendrogram(sch.linkage(b10, b3 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance')
    plt.show()
def fonk3(b10, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b10)
def fonk4(b10, b7):
    plt.figure(b2 = (10, 7))
    b6 = {
        0: ('red', 'Careful'),
        1: ('blue', 'Standard'),
        2: ('green', 'Target'),
        3: ('cyan', 'Careless'),
        4: ('magenta', 'Sensible')
    }
    for cluster_id, (color, label) in b6.items():
        plt.scatter(b10[b7 = = cluster_id, 0], b10[b7 == cluster_id, 1],
                    b8 = 100, c=color, label=label)
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b9 = 'Mall_Customers.csv'
    b10 = fonk1(b9)
    fonk2(b10)
    b7 = fonk3(b10, b4=5)
    fonk4(b10, b7)
if b11 = = "__main__":
    fonk5()