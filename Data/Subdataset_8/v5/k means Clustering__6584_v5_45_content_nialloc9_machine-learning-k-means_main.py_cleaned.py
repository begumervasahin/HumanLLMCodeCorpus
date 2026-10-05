import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
plt.style.use('ggplot')
def get_random_int(min_value=1, max_value=20):
    return random.randint(min_value, max_value)
def plot_data(features, labels, centroids):
    colors = ["g.", "r.", "c.", "y."]
    for i, feature in enumerate(features):
        plt.plot(feature[0], feature[1], colors[labels[i]], markersize=10)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    plt.show()
features = np.array([[get_random_int(), get_random_int()] for _ in range(6)])
classifier = KMeans(n_clusters=2)
classifier.fit(features)
centroids = classifier.cluster_centers_
labels = classifier.labels_
plot_data(features, labels, centroids)