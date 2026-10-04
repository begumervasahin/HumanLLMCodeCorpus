import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
b1 = load_iris()
b2 = b1.data
def fonk1(b12, b2):
    b3 = b12.labels_
    b4 = b12.n_clusters
    num_samples, b5 = b2.shape
    b6 = np.bincount(b3)
    b7 = (1.0 / (num_samples - b4) / b5) * \
                       sum([sum(distance.cdist(b2[b3 = = i], [b12.cluster_centers_[i]], 'euclidean') ** 2)
                            for i in range(b4)])
    b8 = 0.5 * b4 * np.log(num_samples) * (b5 + 1)
    b9 = np.sum([
        b6[i] * np.log(b6[i]) - b6[i] * np.log(num_samples) -
        (b6[i] * b5 / 2) * np.log(2 * np.pi * b7) -
        ((b6[i] - 1) * b5 / 2)
        for i in range(b4)
    ]) - b8
    return b9
b10 = []
b11 = range(2, int(math.sqrt(len(b2))) + 1)
for n_clusters in b11:
    b12 = KMeans(n_clusters=n_clusters)
    b3 = b12.fit_predict(b2)
    b9 = fonk1(b12, b2)
    b13 = silhouette_score(b2, b3)
    b14 = b9 / b13
    b10.append(b14)
plt.figure(b15 = (10, 6))
plt.plot(b11, b10, b16 = 'o')
plt.xlabel('Number of Clusters')
plt.ylabel('Normalized BIC Value')
plt.title('Normalized BIC Values vs. Number of Clusters')
plt.grid(True)
plt.show()