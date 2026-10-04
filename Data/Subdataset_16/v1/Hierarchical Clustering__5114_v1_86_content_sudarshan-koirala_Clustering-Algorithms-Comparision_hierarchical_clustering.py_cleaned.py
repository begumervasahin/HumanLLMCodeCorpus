import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    return b1.iloc[:, [3, 4]].values
def fonk2(b7):
    plt.figure(b2 = (10, 7))
    dendrogram(linkage(b7, b3 = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
def fonk3(b7, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b7)
def fonk4(b7, b6):
    plt.figure(b2 = (10, 7))
    plt.scatter(b7[b6 = = 0, 0], b7[b6 == 0, 1], s=100, c='red', label='Careful')
    plt.scatter(b7[b6 = = 1, 0], b7[b6 == 1, 1], s=100, c='blue', label='Standard')
    plt.scatter(b7[b6 = = 2, 0], b7[b6 == 2, 1], s=100, c='green', label='Target')
    plt.scatter(b7[b6 = = 3, 0], b7[b6 == 3, 1], s=100, c='cyan', label='Careless')
    plt.scatter(b7[b6 = = 4, 0], b7[b6 == 4, 1], s=100, c='magenta', label='Sensible')
    plt.title('Clusters of clients (Hierarchical clustering)')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b7 = fonk1('Mall_Customers.csv')
    fonk2(b7)
    b6 = fonk3(b7)
    fonk4(b7, b6)
if b8 = = "__main__":
    fonk5()