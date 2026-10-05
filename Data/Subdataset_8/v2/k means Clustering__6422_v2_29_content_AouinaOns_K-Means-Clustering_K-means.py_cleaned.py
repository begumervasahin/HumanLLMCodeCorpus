import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
np.random.seed(0)
num_samples = 5000
centers = [[4, 4], [-2, -1], [2, -3], [1, 1]]
cluster_std = 0.9
X, y = make_blobs(n_samples=num_samples, centers=centers, cluster_std=cluster_std)
plt.scatter(X[:, 0], X[:, 1], marker='.')
plt.show()
k_means = KMeans(init="k-means++", n_clusters=4, n_init=12)
k_means.fit(X)
cluster_labels = k_means.labels_
cluster_centers = k_means.cluster_centers_
colors = plt.cm.Spectral(np.linspace(0, 1, len(set(cluster_labels))))
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(1, 1, 1)
for k, col in zip(range(len(cluster_centers)), colors):
    members_in_cluster = (cluster_labels == k)
    cluster_center = cluster_centers[k]
    ax.plot(X[members_in_cluster, 0], X[members_in_cluster, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)
ax.set_title('KMeans Clustering')
ax.set_xticks(())
ax.set_yticks(())
plt.show()