
from __future__ import print_function
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from scipy.stats import mode
digits = load_digits()
data = digits.data
targets = digits.target
print("Shape of the digits data:", data.shape)
kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(data)
print("Shape of the cluster centers:", kmeans.cluster_centers_.shape)
def visualize_cluster_centers(cluster_centers):
    fig, axes = plt.subplots(2, 5, figsize=(8, 3))
    cluster_centers_reshaped = cluster_centers.reshape(10, 8, 8)
    for ax, center in zip(axes.flat, cluster_centers_reshaped):
        ax.set(xticks=[], yticks=[])
        ax.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
    plt.show()
visualize_cluster_centers(kmeans.cluster_centers_)
def assign_labels_to_clusters(clusters, true_labels, n_clusters):
    assigned_labels = np.zeros_like(clusters)
    for i in range(n_clusters):
        mask = (clusters == i)
        assigned_labels[mask] = mode(true_labels[mask])[0]
    return assigned_labels
assigned_labels = assign_labels_to_clusters(clusters, targets, 10)
accuracy = accuracy_score(targets, assigned_labels)
print("Accuracy of clustering:", accuracy)