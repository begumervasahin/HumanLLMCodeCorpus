import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
b1 = load_iris()
b2 = b1.b2
def fonk1(b12, X):
    b3 = b12.cluster_centers_
    b4 = b12.labels_
    b5 = b12.n_clusters
    num_samples, b6 = X.shape
    b7 = (1.0 / (num_samples - b5) / b6) * \
        sum([np.sum(distance.cdist(X[b4 = = i], [b3[i]], 'euclidean') ** 2) for i in range(b5)])
    b8 = 0.5 * b5 * np.log(num_samples) * (b6 + 1)
    b9 = np.sum([
        np.sum(b4 = = i) * np.log(np.sum(b4 == i)) - np.sum(b4 == i) * np.log(num_samples) -
        ((np.sum(b4 = = i) * b6) / 2) * np.log(2 * np.pi * b7) -
        ((np.sum(b4 = = i) - 1) * b6 / 2)
        for i in range(b5)
    ]) - b8
    return b9
b10 = []
b11 = range(2, int(math.sqrt(len(b2))) + 1)
for b5 in b11:
    b12 = KMeans(n_clusters=b5, random_state=42)
    b4 = b12.fit_predict(b2)
    b9 = fonk1(b12, b2)
    b13 = silhouette_score(b2, b4)
    b10.append(b9 / b13)
plt.plot(b11, b10, b14 = 'o')
plt.xlabel('Number of Clusters')
plt.ylabel('BIC/Silhouette Ratio')
plt.title('BIC/Silhouette Ratio vs Number of Clusters')
plt.grid(True)
plt.show()