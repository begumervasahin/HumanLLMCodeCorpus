import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs
X1, b1 = make_blobs(n_samples=50, centers=[[4, 4], [-2, -1], [1, 1], [10, 4]], cluster_std=0.9)
plt.scatter(X1[:, 0], X1[:, 1], b2 = 'o')
plt.title('Sample Data')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()
b3 = AgglomerativeClustering(n_clusters=4, linkage='average')
b3.fit(X1, b1)
plt.figure(b4 = (6, 4))
x_min, b5 = np.min(X1, axis=0), np.max(X1, axis=0)
b6 = (X1 - x_min) / (b5 - x_min)
for i in range(X1.shape[0]):
    plt.text(b6[i, 0], b6[i, 1], str(b1[i]),
             b7 = plt.cm.nipy_spectral(b3.labels_[i] / 10.),
             b8 = {'weight': 'bold', 'size': 9})
plt.xticks([])
plt.yticks([])
plt.scatter(b6[:, 0], b6[:, 1], b2 = '.')
plt.title('Clustered Data')
plt.show()
b9 = distance_matrix(b6, b6)
print("Distance Matrix:\n", b9)
b10 = hierarchy.linkage(b9, 'complete')
b11 = hierarchy.dendrogram(b10)
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()