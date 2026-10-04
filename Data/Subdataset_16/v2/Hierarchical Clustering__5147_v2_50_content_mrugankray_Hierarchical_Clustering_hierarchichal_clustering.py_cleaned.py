import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
plt.figure(b3 = (10, 7))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
b4 = sch.b4(sch.linkage(b2, method='ward'))
plt.show()
a1 = 5
b5 = AgglomerativeClustering(a1=a1, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
plt.figure(b3 = (10, 7))
b7 = ['red', 'blue', 'magenta', 'cyan', 'green']
b8 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
for i in range(a1):
    plt.scatter(b2[b6 = = i, 0], b2[b6 == i, 1], s=100, c=b7[i], label=b8[i])
plt.title('Hierarchical Clustering of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()