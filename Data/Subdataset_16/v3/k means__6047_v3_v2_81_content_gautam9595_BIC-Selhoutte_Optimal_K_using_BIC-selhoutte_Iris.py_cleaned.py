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
    b3 = b12.cluster_centers_
    b4 = b12.labels_
    b5 = b12.n_clusters
    b6 = np.bincount(b4)
    num_samples, b7 = b2.shape
    b8 = (1.0 / (num_samples - b5) / b7) * sum(
        [sum(distance.cdist(b2[b4 = = i], [b3[i]], 'euclidean') ** 2) for i in range(b5)]
    )
    b9 = 0.5 * b5 * np.log(num_samples) * (b7 + 1)
    b10 = np.sum(
        [
            b6[i] * np.log(b6[i]) - b6[i] * np.log(num_samples)
            - ((b6[i] * b7) / 2) * np.log(2 * np.pi * b8)
            - ((b6[i] - 1) * b7 / 2)
            for i in range(b5)
        ]
    ) - b9
    return b10
def fonk2(b2, b16):
    b11 = []
    for b5 in range(2, b16 + 1):
        b12 = KMeans(n_clusters=b5, random_state=42)
        b4 = b12.fit_predict(b2)
        b10 = fonk1(b12, b2)
        b13 = silhouette_score(b2, b4)
        b11.append(b10 / b13)
    return b11
def fonk3(ratios, b16):
    plt.figure(b14 = (10, 6))
    plt.plot(range(2, b16 + 1), ratios, b15 = 'o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('BIC/Silhouette Ratio')
    plt.title('BIC/Silhouette Ratio vs Number of Clusters')
    plt.grid(True)
    plt.show()
b16 = int(math.sqrt(len(b2)))
b11 = fonk2(b2, b16)
fonk3(b11, b16)