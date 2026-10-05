import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
plt.style.use('ggplot')
def get_random_int(min_val=1, max_val=20):
    return random.randint(min_val, max_val)
def plot_data_with_centroids(features, labels, centroids):
    colors = ["g.", "r.", "c.", "y."]
    for i in range(len(features)):
        plt.plot(features[i][0], features[i][1], colors[labels[i]], markersize=10)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    plt.show()
features = np.array([[get_random_int(), get_random_int()] for _ in range(6)])
kmeans = KMeans(n_clusters=2)
kmeans.fit(features)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
plot_data_with_centroids(features, labels, centroids)