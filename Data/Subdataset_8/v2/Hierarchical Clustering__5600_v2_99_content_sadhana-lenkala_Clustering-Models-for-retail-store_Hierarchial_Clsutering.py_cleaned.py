import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values
dendrogram = sch.dendrogram(sch.linkage(X, method='ward', metric='euclidean'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance using ward method')
plt.show()
agglomerative = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
Y_ahc = agglomerative.fit_predict(X)
plt.scatter(X[Y_ahc == 0, 0], X[Y_ahc == 0, 1], color='red', label='Low spenders', s=100)
plt.scatter(X[Y_ahc == 1, 0], X[Y_ahc == 1, 1], color='blue', label='Standard', s=100)
plt.scatter(X[Y_ahc == 2, 0], X[Y_ahc == 2, 1], color='green', label='Target', s=100)
plt.scatter(X[Y_ahc == 3, 0], X[Y_ahc == 3, 1], color='magenta', label='Low earners', s=100)
plt.scatter(X[Y_ahc == 4, 0], X[Y_ahc == 4, 1], color='cyan', label='Out of target', s=100)
plt.title('Cluster of clients')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()