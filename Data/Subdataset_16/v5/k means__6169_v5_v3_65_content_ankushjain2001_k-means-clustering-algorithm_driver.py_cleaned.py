import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
def fonk1():
    b1 = datasets.load_iris()
    return b1.data, b1.target
def fonk2(data, k, max_iterations, init_method):
    b2 = kmeans.KMeans(data, k, max_iterations, init_method)
    return b2
def fonk3(data, k):
    b3 = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300).fit(data)
    return b3.labels_
def fonk4(data, labels, title):
    plt.scatter(data[:, 0], data[:, 1], b4 = labels, cmap='viridis', marker='o', edgecolor='k')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
def fonk5(y_true, y_pred, title):
    print(title)
    print(confusion_matrix(y_true, y_pred))
a1 = 3
a2 = 100
b5 = 'kmeans++'
data, b6 = fonk1()
b7 = fonk2(data, a1, a2, b5)
b8 = fonk3(data, a1)
fonk4(data, b6, 'Ground Truth')
fonk4(data, b7, 'Custom KMeans Output')
fonk4(data, b8, 'SKLearn KMeans Output')
fonk5(b6, b7, 'Confusion Matrix of True Labels vs Custom KMeans Predicted Labels:')
fonk5(b6, b8, 'Confusion Matrix of True Labels vs SKLearn KMeans Predicted Labels:')
fonk5(b8, b7, 'Confusion Matrix of SKLearn KMeans Predicted Labels vs Custom KMeans Predicted Labels:')