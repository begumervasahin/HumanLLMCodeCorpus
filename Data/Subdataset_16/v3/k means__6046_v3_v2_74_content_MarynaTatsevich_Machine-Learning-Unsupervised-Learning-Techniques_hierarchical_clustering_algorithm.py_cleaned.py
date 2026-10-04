
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']]
plt.figure(b3 = (10, 7))
b4 = sch.b4(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()
b5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
def fonk1(b2, b6, num_clusters):
    b7 = ['red', 'blue', 'green', 'black', 'magenta']
    b8 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
    plt.figure(b3 = (10, 7))
    for i in range(num_clusters):
        plt.scatter(b2[b6 = = i]['Annual Income (k$)'],
                    b2[b6 = = i]['Spending Score (1-100)'],
                    b9 = 100, c=b7[i], label=b8[i])
    plt.title('Clusters of Clients')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()
fonk1(b2, b6, 5)