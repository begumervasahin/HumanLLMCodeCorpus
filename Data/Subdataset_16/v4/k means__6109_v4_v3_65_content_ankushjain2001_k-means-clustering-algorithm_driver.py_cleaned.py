import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
def fonk1():
    b1 = datasets.load_iris()
    return b1.data, b1.target
def fonk2(data, a1, a2, b3):
    return kmeans.KMeans(data, a1, a2, b3)
def fonk3(data, a1):
    b2 = KMeans(n_clusters=a1, init='a1-means++', n_init=10, max_iter=300).fit(data)
    return b2.labels_
def fonk4(data, labels, title):
    kmeans.drawPlot(data, labels, title)
def fonk5(y_true, y_pred, title):
    print(title)
    print(confusion_matrix(y_true, y_pred))
a1 = 3
a2 = 100
b3 = 'kmeans++'
data, b4 = fonk1()
b5 = fonk2(data, a1, a2, b3)
b6 = fonk3(data, a1)
fonk4(data, b4, 'Ground Truth')
fonk4(data, b5, 'Custom KMeans Output')
fonk4(data, b6, 'SKLearn KMeans Output')
fonk5(b4, b5, 'Confusion Matrix of True Labels vs Custom KMeans Predicted Labels:')
fonk5(b4, b6, 'Confusion Matrix of True Labels vs SKLearn KMeans Predicted Labels:')
fonk5(b6, b5, 'Confusion Matrix of SKLearn KMeans Predicted Labels vs Custom KMeans Predicted Labels:')