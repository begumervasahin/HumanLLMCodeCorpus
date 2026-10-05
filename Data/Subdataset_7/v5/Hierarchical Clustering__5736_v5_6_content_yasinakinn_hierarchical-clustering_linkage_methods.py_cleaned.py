import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('customers_dataset.csv')
b2 = b1.iloc[:, 2:8].values
b3 = ['ward', 'complete', 'average', 'single']
a1 = 4
b4 = [
    AgglomerativeClustering(a1 = a1, affinity='euclidean', linkage=method)
    for method in b3
]
b5 = [algorithm.fit_predict(b2) for algorithm in b4]
def fonk1(b2, b7, title):
    b6 = ['red', 'blue', 'green', 'yellow']
    for i, color in enumerate(b6):
        plt.scatter(b2[b7 = = i, 0], b2[b7 == i, 1], s=100, c=color)
    plt.title(title)
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
for method, b7 in zip(b3, b5):
    fonk1(b2, b7, method.capitalize())
def fonk2(b2, method, title):
    b8 = sch.b8(sch.linkage(b2, method=method))
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Euclidean")
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
for method in b3:
    fonk2(b2, method, method.capitalize())