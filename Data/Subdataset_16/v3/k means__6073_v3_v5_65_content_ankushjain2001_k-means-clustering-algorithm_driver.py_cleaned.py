
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import kmeans
def fonk1():
    b1 = datasets.load_iris()
    b2 = b1.b2
    b3 = b1.target
    a1 = 3
    a2 = 100
    b4 = 'kmeans++'
    b5 = kmeans.KMeans(b2, a1, a2, b4)
    b6 = fonk2(b2, a1, a2)
    fonk3(b2, b3, 'Truth')
    fonk3(b2, b5, 'Manual Output')
    fonk3(b2, b6, 'SKLearn Output')
    fonk4(b3, b5, b6)
def fonk2(b2, a1, a2):
    b7 = KMeans(n_clusters=a1, init='k-means++', max_iter=a2).fit(b2)
    return b7.labels_
def fonk3(b2, labels, title):
    plt.figure()
    b8 = plt.b8(b2[:, 0], b2[:, 1], c=labels, cmap='viridis')
    plt.title(title)
    plt.colorbar(b8)
    plt.show()
def fonk4(b3, b5, b6):
    print('Confusion Matrix of True Labels vs Predicted Labels:')
    print(confusion_matrix(b3, b5))
    print('Confusion Matrix of True Labels vs SKLearn Predicted Labels:')
    print(confusion_matrix(b3, b6))
    print('Confusion Matrix of SKLearn Predicted Labels vs Manual Predicted Labels:')
    print(confusion_matrix(b6, b5))
if b9 = = "__main__":
    fonk1()