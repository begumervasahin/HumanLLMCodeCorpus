import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
b3 = sch.b3(sch.linkage(b2, method='ward', metric='euclidean'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance using ward method')
plt.show()
b4 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b5 = b4.fit_predict(b2)
b6 = ['Low spenders', 'Standard', 'Target', 'Low earners', 'Out of target']
b7 = ['red', 'blue', 'green', 'magenta', 'cyan']
for i, label in enumerate(b6):
    plt.scatter(b2[b5 = = i, 0], b2[b5 == i, 1], color=b7[i], label=label, s=100)
plt.title('Cluster of clients')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()