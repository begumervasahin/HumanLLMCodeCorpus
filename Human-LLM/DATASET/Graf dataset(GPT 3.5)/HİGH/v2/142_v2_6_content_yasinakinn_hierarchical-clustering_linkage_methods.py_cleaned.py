import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('customers_dataset.csv')
b2 = b1.iloc[:, 2:8].values
b3 = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='b3')
b4 = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='b4')
b5 = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='b5')
b6 = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='b6')
b7 = b3.fit_predict(b2)
b8 = b4.fit_predict(b2)
b9 = b5.fit_predict(b2)
b10 = b6.fit_predict(b2)
def fonk1(b2, b12, title):
    b11 = ['red', 'blue', 'green', 'yellow']
    for i in range(len(b11)):
        plt.scatter(b2[b12 = =i, 0], b2[b12==i, 1], s=100, c=b11[i])
    plt.title(title)
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
fonk1(b2, b7, 'Ward')
fonk1(b2, b8, 'Complete')
fonk1(b2, b9, 'Average')
fonk1(b2, b10, 'Single')
def fonk2(b2, method, title):
    b13 = sch.b13(sch.linkage(b2, method=method))
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Euclidean")
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
    plt.show()
fonk2(b2, 'b3', 'Ward')
fonk2(b2, 'b4', 'Complete')
fonk2(b2, 'b5', 'Average')
fonk2(b2, 'b6', 'Single')