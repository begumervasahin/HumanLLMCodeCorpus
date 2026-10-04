import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b2 = b1.iloc[:, [3, 4]].values
    return b2
def fonk2(b2):
    plt.figure(b3 = (10, 7))
    dendrogram(linkage(b2, b4 = 'ward', metric='euclidean'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distance using Ward b4')
    plt.show()
def fonk3(b2, b5 = 5):
    b6 = AgglomerativeClustering(b5=b5, affinity='euclidean', linkage='ward')
    return b6.fit_predict(b2)
def fonk4(b2, b7):
    plt.figure(b3 = (10, 7))
    plt.scatter(b2[b7 = = 0, 0], b2[b7 == 0, 1], color='red', label='Low spenders', s=100)
    plt.scatter(b2[b7 = = 1, 0], b2[b7 == 1, 1], color='blue', label='Standard', s=100)
    plt.scatter(b2[b7 = = 2, 0], b2[b7 == 2, 1], color='green', label='Target', s=100)
    plt.scatter(b2[b7 = = 3, 0], b2[b7 == 3, 1], color='magenta', label='Low earners', s=100)
    plt.scatter(b2[b7 = = 4, 0], b2[b7 == 4, 1], color='cyan', label='Out of target', s=100)
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b2 = fonk1('Mall_Customers.csv')
    fonk2(b2)
    b7 = fonk3(b2)
    fonk4(b2, b7)
if b8 = = "__main__":
    fonk5()