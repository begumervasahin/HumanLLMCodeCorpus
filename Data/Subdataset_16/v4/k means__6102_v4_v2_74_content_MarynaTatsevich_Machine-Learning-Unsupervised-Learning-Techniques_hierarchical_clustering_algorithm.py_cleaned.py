
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']]
plt.figure(b3 = (10, 7))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
b4 = sch.b4(sch.linkage(b2, method='ward'))
plt.show()
b5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
plt.figure(b3 = (10, 7))
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.scatter(b2[b6 = = 0]['Annual Income (k$)'],
            b2[b6 = = 0]['Spending Score (1-100)'],
            b7 = 100, c='red', label='Careful')
plt.scatter(b2[b6 = = 1]['Annual Income (k$)'],
            b2[b6 = = 1]['Spending Score (1-100)'],
            b7 = 100, c='blue', label='Standard')
plt.scatter(b2[b6 = = 2]['Annual Income (k$)'],
            b2[b6 = = 2]['Spending Score (1-100)'],
            b7 = 100, c='green', label='Target')
plt.scatter(b2[b6 = = 3]['Annual Income (k$)'],
            b2[b6 = = 3]['Spending Score (1-100)'],
            b7 = 100, c='black', label='Careless')
plt.scatter(b2[b6 = = 4]['Annual Income (k$)'],
            b2[b6 = = 4]['Spending Score (1-100)'],
            b7 = 100, c='magenta', label='Sensible')
plt.legend()
plt.show()