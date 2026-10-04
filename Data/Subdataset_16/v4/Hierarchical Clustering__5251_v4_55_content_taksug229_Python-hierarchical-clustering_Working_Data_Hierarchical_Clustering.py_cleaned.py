import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
plt.figure(b3 = (10, 7))
b4 = sch.b4(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()
b5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b6 = b5.fit_predict(b2)
b7 = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']
b8 = ['red', 'blue', 'green', 'cyan', 'magenta']
plt.figure(b3 = (10, 7))
for i, color in enumerate(b8):
    plt.scatter(b2[b6 = = i, 0], b2[b6 == i, 1], s=100, c=color, label=b7[i])
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()