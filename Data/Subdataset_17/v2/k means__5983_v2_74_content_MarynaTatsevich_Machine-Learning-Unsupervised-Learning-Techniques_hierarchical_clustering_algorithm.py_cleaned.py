
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
dataset = pd.read_csv('Mall_Customers.csv')
features = dataset[['Annual Income (k$)', 'Spending Score (1-100)']]
dendrogram = sch.dendrogram(sch.linkage(features, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster_labels = hc.fit_predict(features)
plt.scatter(features[cluster_labels == 0]['Annual Income (k$)'],
            features[cluster_labels == 0]['Spending Score (1-100)'],
            s=100, c='red', label='Careful')
plt.scatter(features[cluster_labels == 1]['Annual Income (k$)'],
            features[cluster_labels == 1]['Spending Score (1-100)'],
            s=100, c='blue', label='Standard')
plt.scatter(features[cluster_labels == 2]['Annual Income (k$)'],
            features[cluster_labels == 2]['Spending Score (1-100)'],
            s=100, c='green', label='Target')
plt.scatter(features[cluster_labels == 3]['Annual Income (k$)'],
            features[cluster_labels == 3]['Spending Score (1-100)'],
            s=100, c='black', label='Careless')
plt.scatter(features[cluster_labels == 4]['Annual Income (k$)'],
            features[cluster_labels == 4]['Spending Score (1-100)'],
            s=100, c='magenta', label='Sensible')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()