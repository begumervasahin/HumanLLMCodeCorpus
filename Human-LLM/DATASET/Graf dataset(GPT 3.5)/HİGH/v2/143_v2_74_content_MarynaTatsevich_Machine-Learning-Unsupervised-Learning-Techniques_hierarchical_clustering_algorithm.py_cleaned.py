
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1[['Annual Income (k$)', 'Spending Score (1-100)']]
b3 = sch.b3(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()
b4 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b5 = b4.fit_predict(b2)
plt.scatter(b2[b5 = = 0]['Annual Income (k$)'],
            b2[b5 = = 0]['Spending Score (1-100)'],
            b6 = 100, c='red', label='Careful')
plt.scatter(b2[b5 = = 1]['Annual Income (k$)'],
            b2[b5 = = 1]['Spending Score (1-100)'],
            b6 = 100, c='blue', label='Standard')
plt.scatter(b2[b5 = = 2]['Annual Income (k$)'],
            b2[b5 = = 2]['Spending Score (1-100)'],
            b6 = 100, c='green', label='Target')
plt.scatter(b2[b5 = = 3]['Annual Income (k$)'],
            b2[b5 = = 3]['Spending Score (1-100)'],
            b6 = 100, c='black', label='Careless')
plt.scatter(b2[b5 = = 4]['Annual Income (k$)'],
            b2[b5 = = 4]['Spending Score (1-100)'],
            b6 = 100, c='magenta', label='Sensible')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()