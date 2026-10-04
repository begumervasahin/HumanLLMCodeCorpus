
import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
def fonk1():
    b1 = datasets.load_iris()
    data, b2 = b1.data, b1.target
    a1 = 3
    a2 = 100
    b3 = 'kmeans++'
    b4 = kmeans.KMeans(data, a1, a2, b3)
    b5 = KMeans(n_clusters=a1, init=b3, max_iter=a2)
    b6 = b5.fit_predict(data)
    fonk2(data, b2, 'True Labels')
    fonk2(data, b4, 'Custom KMeans Output')
    fonk2(data, b6, 'SKLearn KMeans Output')
    fonk3(b2, b4, b6)
def fonk2(data, labels, title):
    kmeans.drawPlot(data, labels, title)
def fonk3(b2, b4, b6):
    print('Confusion Matrix of True Labels vs Custom KMeans Predicted Labels:')
    print(confusion_matrix(b2, b4))
    print('Confusion Matrix of True Labels vs SKLearn KMeans Predicted Labels:')
    print(confusion_matrix(b2, b6))
    print('Confusion Matrix of Custom KMeans Predicted Labels vs SKLearn KMeans Predicted Labels:')
    print(confusion_matrix(b4, b6))
if b7 = = "__main__":
    fonk1()