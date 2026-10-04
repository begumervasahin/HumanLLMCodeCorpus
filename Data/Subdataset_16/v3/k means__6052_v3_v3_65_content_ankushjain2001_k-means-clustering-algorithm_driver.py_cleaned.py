import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
def fonk1():
    b1 = datasets.load_iris()
    return b1.data, b1.target
def fonk2(data, num_clusters, max_iterations, init_method):
    return kmeans.KMeans(data, num_clusters, max_iterations, init_method)
def fonk3(data, num_clusters):
    b2 = KMeans(n_clusters=num_clusters, init='k-means++').fit(data)
    return b2.labels_
def fonk4(data, labels, title):
    plt.scatter(data[:, 0], data[:, 1], b3 = labels, cmap='viridis')
    plt.title(title)
    plt.show()
def fonk5(y_true, y_pred, title):
    b4 = confusion_matrix(y_true, y_pred)
    print(f'{title}:\n{b4}\n')
a1 = 3
a2 = 100
b5 = 'kmeans++'
def fonk6():
    data, b6 = fonk1()
    b7 = fonk2(data, a1, a2, b5)
    b8 = fonk3(data, a1)
    fonk4(data, b6, 'Ground Truth')
    fonk4(data, b7, 'Custom KMeans Output')
    fonk4(data, b8, 'SKLearn KMeans Output')
    fonk5(b6, b7, 'Confusion Matrix: True Labels vs Custom KMeans Predicted Labels')
    fonk5(b6, b8, 'Confusion Matrix: True Labels vs SKLearn KMeans Predicted Labels')
    fonk5(b8, b7, 'Confusion Matrix: SKLearn KMeans vs Custom KMeans Predicted Labels')
if b9 = = '__main__':
    fonk6()