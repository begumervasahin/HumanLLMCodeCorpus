
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from scipy.stats import mode
from sklearn.metrics import accuracy_score
import sklearn
if int((sklearn.__version__).split(".")[1]) < 18:
    from sklearn.cross_validation import train_test_split
else:
    from sklearn.model_selection import train_test_split
def check_sklearn_version():
    if int((sklearn.__version__).split(".")[1]) < 18:
        from sklearn.cross_validation import train_test_split
    else:
        from sklearn.model_selection import train_test_split
def load_digits_dataset():
    return load_digits()
def visualize_cluster_centers(kmeans):
    fig, ax = plt.subplots(2, 5, figsize=(8, 3))
    centers = kmeans.cluster_centers_.reshape(10, 8, 8)
    for axi, center in zip(ax.flat, centers):
        axi.set(xticks=[], yticks=[])
        axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
def assign_labels(clusters, target):
    labels = np.zeros_like(clusters)
    for i in range(10):
        mask = (clusters == i)
        labels[mask] = mode(target[mask])[0]
    return labels
def calculate_accuracy(true_labels, predicted_labels):
    return accuracy_score(true_labels, predicted_labels)
def main():
    data = load_digits_dataset()
    print("Shape of the dataset:", data.data.shape)
    kmeans = KMeans(n_clusters=10, random_state=0)
    clusters = kmeans.fit_predict(data.data)
    print("Shape of cluster centers:", kmeans.cluster_centers_.shape)
    visualize_cluster_centers(kmeans)
    labels = assign_labels(clusters, data.target)
    accuracy = calculate_accuracy(data.target, labels)
    print("Accuracy:", accuracy)
if __name__ == "__main__":
    main()