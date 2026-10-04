
import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
def fonk1():
    b1 = datasets.load_iris()
    b2 = b1.b2
    b3 = b1.target
    a1 = 3
    a2 = 100
    b4 = 'kmeans++'
    b5 = kmeans.KMeans(b2, a1, a2, b4)
    b6 = KMeans(n_clusters=a1, init='k-means++').fit(b2)
    b7 = b6.labels_
    fonk2(b2, b3, 'Truth')
    fonk2(b2, b5, 'Manual Output')
    fonk2(b2, b7, 'SKLearn Output')
    fonk3(b3, b5, b7)
def fonk2(b2, labels, title):
    kmeans.drawPlot(b2, labels, title)
def fonk3(b3, b5, b7):
    print('Confusion Matrix of True Labels vs Predicted Labels:')
    print(confusion_matrix(b3, b5))
    print('Confusion Matrix of True Labels vs SKLearn Predicted Labels:')
    print(confusion_matrix(b3, b7))
    print('Confusion Matrix of SKLearn Predicted Labels vs Manual Predicted Labels:')
    print(confusion_matrix(b7, b5))
if b8 = = "__main__":
    fonk1()