import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
b3 = sch.b3(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()
b4 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
b5 = b4.fit_predict(b2)
b6 = ['red', 'blue', 'green', 'cyan', 'magenta']
b7 = ['Careful', 'Standard', 'Targets', 'Careless', 'Sensible']
for i, color in enumerate(b6):
    plt.scatter(b2[b5 = = i, 0], b2[b5 == i, 1], s=100, c=color, label=b7[i])
plt.title('Clusters of Clients')
plt.xlabel('Annual Income of Customers')
plt.ylabel('Spending Score')
plt.legend()
plt.show()