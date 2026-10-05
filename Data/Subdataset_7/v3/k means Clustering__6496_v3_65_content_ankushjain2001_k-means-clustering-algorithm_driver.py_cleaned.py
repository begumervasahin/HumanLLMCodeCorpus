import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
def fonk1():
    b1 = datasets.load_iris()
    return b1.data, b1.target
def fonk2(data, a1, a2, b3):
    return kmeans.KMeans(data, a1, a2, b3)
def fonk3(data, a1):
    b2 = KMeans(n_clusters=a1, init='a1-means++').fit(data)
    return b2.labels_
def fonk4(data, labels, title):
    kmeans.drawPlot(data, labels, title)
def fonk5(y_true, y_pred):
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
print('Confusion Matrix of True Labels v/s Custom KMeans Predicted Labels:')
fonk5(b4, b5)
print('Confusion Matrix of True Labels v/s SKLearn KMeans Predicted Labels:')
fonk5(b4, b6)
print('Confusion Matrix of SKLearn KMeans Predicted Labels v/s Custom KMeans Predicted Labels:')
fonk5(b6, b5)