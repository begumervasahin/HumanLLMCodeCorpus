import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('Mall_Customers.csv')
b2 = b1.iloc[:, [3, 4]].values
b3 = sch.b3(sch.linkage(b2, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Points')
plt.ylabel('Distance between Clusters / Dissimilarities')
plt.show()
b4 = AgglomerativeClustering(
    b5 = 5, affinity='euclidean', linkage='ward'
)
b6 = b4.fit_predict(b2)
plt.scatter(b2[b6 = = 0, 0], b2[b6 == 0, 1], c='red', label='Careful')
plt.scatter(b2[b6 = = 1, 0], b2[b6 == 1, 1], c='blue', label='Standard')
plt.scatter(b2[b6 = = 2, 0], b2[b6 == 2, 1], c='magenta', label='Target')
plt.scatter(b2[b6 = = 3, 0], b2[b6 == 3, 1], c='cyan', label='Careless')
plt.scatter(b2[b6 = = 4, 0], b2[b6 == 4, 1], c='green', label='Sensible')
plt.title('Hierarchical Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (0 - 100)')
plt.legend()
plt.show()