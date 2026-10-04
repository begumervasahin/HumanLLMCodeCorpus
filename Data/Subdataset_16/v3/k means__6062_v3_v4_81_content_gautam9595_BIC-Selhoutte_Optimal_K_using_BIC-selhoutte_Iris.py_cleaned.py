import numpy as np
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
    b7 = b12.cluster_centers_
    b8 = (1.0 / (num_samples - b4) / b5) * \
                       sum(sum(distance.cdist(b2[b3 = = i], [b7[i]], 'euclidean')**2) for i in range(b4))
    b9 = 0.5 * b4 * np.log(num_samples) * (b5 + 1)
    b10 = np.sum([
        b6[i] * np.log(b6[i]) - b6[i] * np.log(num_samples) -
        ((b6[i] * b5) / 2) * np.log(2 * np.pi * b8) -
        ((b6[i] - 1) * b5 / 2)
        for i in range(b4)
    ]) - b9
    return b10
def fonk2(b2, b15):
    b11 = []
    for n_clusters in range(2, b15 + 1):
        b12 = KMeans(n_clusters=n_clusters, random_state=42)
        b12.fit(b2)
        b10 = fonk1(b12, b2)
        b13 = silhouette_score(b2, b12.labels_)
        b14 = b10 / b13
        b11.append(b14)
    return b11
b15 = int(math.sqrt(len(b2)))
b11 = fonk2(b2, b15)
plt.figure(b16 = (10, 6))
plt.plot(range(2, b15 + 1), b11, b17 = 'o')
plt.xlabel('Number of Clusters')
plt.ylabel('Normalized BIC')
plt.title('Normalized BIC vs Number of Clusters')
plt.grid(True)
plt.show()