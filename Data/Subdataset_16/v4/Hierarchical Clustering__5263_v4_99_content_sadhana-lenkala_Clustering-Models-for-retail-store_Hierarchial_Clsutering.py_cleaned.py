import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    return b1.iloc[:, [3, 4]].values
def fonk2(b9):
    plt.figure(b2 = (10, 7))
    dendrogram(linkage(b9, b3 = 'ward', metric='euclidean'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean Distance (Ward Method)')
    plt.show()
def fonk3(b9, b4 = 5):
    b5 = AgglomerativeClustering(b4=b4, affinity='euclidean', linkage='ward')
    return b5.fit_predict(b9)
def fonk4(b9, b8):
    plt.figure(b2 = (10, 7))
    b6 = ['red', 'blue', 'green', 'magenta', 'cyan']
    b7 = ['Low Spenders', 'Standard', 'Target', 'Low Earners', 'Out of Target']
    for i, color in enumerate(b6):
        plt.scatter(b9[b8 = = i, 0], b9[b8 == i, 1], s=100, color=color, label=b7[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
def fonk5():
    b9 = fonk1('Mall_Customers.csv')
    fonk2(b9)
    b10 = fonk3(b9)
    fonk4(b9, b10)
if b11 = = "__main__":
    fonk5()