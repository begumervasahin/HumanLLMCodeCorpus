import numpy as np
import pandas as pd
from scipy import ndimage
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt
from sklearn import mainfold, datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs
%matplotlib inline
b6, b1 = make_blobs(n_samples=50, centers=[[4,4], [-2,-1], [1,1], [10,4]], cluster_std=0.9)
plt.scatter(b6[:,0], b6[:,1], b2 = 'o')
b3 = AgglomerativeClustering(n_clusters = 4, linkage = 'average')
b3.fit(b6, b1)
plt.figure(b4 = (6,4))
x_min, b5 = np.min(b6, axis=0), np.max(b6, axis=0)
b6 = (b6-x_min) / (b5-x_min)
for i in range(b6.shape[0]):
	plt.text(b6[i,0], b6[i,1], str(b1[i]), b7 = plt.cm.nipy_spectral(b3.labels_[i]/10.), fontdict={'weight': 'blod', 'size': 9})
plt.xticks([])
plt.yticks([])
plt.scatter(b6[:, 0], b6[:, 1], b2 = '.')
plt.show()
b8 = distance_matrix(b6,b6)
print(b8)
b9 = hierarchy.linkage(b8, 'complete')
b10 = hierarchy.dendrogram(b9)