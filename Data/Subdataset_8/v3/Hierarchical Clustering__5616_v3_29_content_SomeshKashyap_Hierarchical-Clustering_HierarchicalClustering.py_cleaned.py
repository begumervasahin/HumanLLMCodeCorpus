import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset[['Annual Income (k$)', 'Spending Score (1-100)']].values
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster_labels = hc.fit_predict(X)
plt.scatter(X[cluster_labels == 0, 0], X[cluster_labels == 0, 1], s=100, c='red', label='Careful')
plt.scatter(X[cluster_labels == 1, 0], X[cluster_labels == 1, 1], s=100, c='blue', label='Standard')
plt.scatter(X[cluster_labels == 2, 0], X[cluster_labels == 2, 1], s=100, c='green', label='Target')
plt.scatter(X[cluster_labels == 3, 0], X[cluster_labels == 3, 1], s=100, c='cyan', label='Careless')
plt.scatter(X[cluster_labels == 4, 0], X[cluster_labels == 4, 1], s=100, c='magenta', label='Sensible')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()