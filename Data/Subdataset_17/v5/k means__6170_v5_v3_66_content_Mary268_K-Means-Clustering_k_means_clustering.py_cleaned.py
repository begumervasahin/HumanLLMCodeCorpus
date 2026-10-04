from __future__ import print_function
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from scipy.stats import mode
import sklearn
sklearn_version = int((sklearn.__version__).split(".")[1])
if sklearn_version < 18:
    from sklearn.cross_validation import train_test_split
else:
    from sklearn.model_selection import train_test_split
digits = load_digits()
X = digits.data
y = digits.target
print("Shape of the digits data:", X.shape)
kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(X)
print("Shape of the cluster centers:", kmeans.cluster_centers_.shape)
def plot_cluster_centers(cluster_centers):
    fig, axes = plt.subplots(2, 5, figsize=(8, 3))
    for ax, center in zip(axes.flat, cluster_centers):
        ax.set(xticks=[], yticks=[])
        ax.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
    plt.show()
cluster_centers_reshaped = kmeans.cluster_centers_.reshape(10, 8, 8)
plot_cluster_centers(cluster_centers_reshaped)
def assign_cluster_labels(clusters, true_labels):
    assigned_labels = np.zeros_like(clusters)
    for i in range(10):
        mask = (clusters == i)
        assigned_labels[mask] = mode(true_labels[mask])[0]
    return assigned_labels
assigned_labels = assign_cluster_labels(clusters, y)
accuracy = accuracy_score(y, assigned_labels)
print("Accuracy of clustering:", accuracy)