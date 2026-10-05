import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b8, b1 = 4, affinity='euclidean', linkage='ward'):
    b2 = AgglomerativeClustering(b1=b1, affinity=affinity, linkage=linkage)
    return b2.fit_predict(b8)
def fonk3(b8, b4, title):
    b3 = ['red', 'blue', 'green', 'yellow']
    for i, color in enumerate(b3):
        plt.scatter(b8[b4 = = i, 0], b8[b4 == i, 1], s=100, c=color)
    plt.title(title)
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
def fonk4(b8, method, title):
    b5 = sch.b5(sch.linkage(b8, method=method))
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Euclidean")
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
if b6 = = "__main__":
    b7 = fonk1('customers_dataset.csv')
    b8 = b7.iloc[:, 2:8].values
    b9 = fonk2(b8, linkage='ward')
    b10 = fonk2(b8, linkage='complete')
    b11 = fonk2(b8, linkage='average')
    b12 = fonk2(b8, linkage='single')
    fonk3(b8, b9, 'Ward')
    fonk3(b8, b10, 'Complete')
    fonk3(b8, b11, 'Average')
    fonk3(b8, b12, 'Single')
    fonk4(b8, 'ward', 'Ward')
    fonk4(b8, 'complete', 'Complete')
    fonk4(b8, 'average', 'Average')
    fonk4(b8, 'single', 'Single')