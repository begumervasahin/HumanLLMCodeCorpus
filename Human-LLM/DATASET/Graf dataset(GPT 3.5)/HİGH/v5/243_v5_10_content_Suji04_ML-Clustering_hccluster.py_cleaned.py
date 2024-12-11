import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
b3 = sch.b3(sch.linkage(b2, method="ward"))
plt.title("Dendrogram")
plt.xlabel("Clusters")
plt.ylabel("Euclidean Distance")
plt.show()
a1 = 5
b4 = "ward"
b5 = AgglomerativeClustering(a1=a1, affinity="euclidean", linkage=b4)
b6 = b5.fit_predict(b2)
b7 = ['red', 'blue', 'green', 'gold', 'magenta']
for i in range(a1):
    plt.scatter(b2[b6 = = i, 0], b2[b6 == i, 1], s=50, c=b7[i], label=f'Cluster {i+1}')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()