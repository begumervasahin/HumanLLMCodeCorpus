import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
np.random.seed(0)
X, b1 = make_blobs(n_samples=5000, centers=[[4,4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)
plt.scatter(X[:, 0], X[:, 1], b2 = '.')
b3 = KMeans(init="k-means++", n_clusters=4, n_init=12)
b3.fit(X)
b4 = b3.labels_
b5 = b3.cluster_centers_
b6 = plt.cm.Spectral(np.linspace(0, 1, len(set(b4))))
b7 = plt.figure(figsize=(6, 4))
b8 = b7.add_subplot(1, 1, 1)
for k, col in zip(range(len([[4, 4], [-2, -1], [2, -3], [1, 1]])), b6):
    b9 = (b4 == k)
    b10 = b5[k]
    b8.plot(X[b9, 0], X[b9, 1], 'w', b11 = col, b2='.')
    b8.plot(b10[0], b10[1], 'o', b11 = col, markeredgecolor='k', markersize=6)
b8.set_title('KMeans')
b8.set_xticks(())
b8.set_yticks(())
plt.show()