from __future__ import print_function
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from scipy.stats import mode
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
fig, axes = plt.subplots(2, 5, figsize=(8, 3))
cluster_centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for ax, center in zip(axes.flat, cluster_centers):
    ax.set(xticks=[], yticks=[])
    ax.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
plt.show()
assigned_labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    assigned_labels[mask] = mode(y[mask])[0]
accuracy = accuracy_score(y, assigned_labels)
print("Accuracy of clustering:", accuracy)