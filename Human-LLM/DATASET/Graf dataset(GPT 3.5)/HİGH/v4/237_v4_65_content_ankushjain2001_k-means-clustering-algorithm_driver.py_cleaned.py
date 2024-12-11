
import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
b1 = datasets.load_iris()
b2 = b1.b2
b3 = b1.target
a1 = 3
a2 = 100
b4 = 'kmeans++'
b5 = kmeans.KMeans(b2, a1, a2, b4)
b6 = KMeans(n_clusters=3, init='a1-means++').fit(b2)
b7 = b6.labels_
kmeans.drawPlot(b2, b3, 'Truth')
kmeans.drawPlot(b2, b5, 'Manual Output')
kmeans.drawPlot(b2, b7, 'SKLearn Output')
print('Confusion Matrix of True Labels vs Predicted Labels:')
print(confusion_matrix(b3, b5))
print('Confusion Matrix of True Labels vs SKLearn Predicted Labels:')
print(confusion_matrix(b3, b7))
print('Confusion Matrix of SKLearn Predicted Labels vs Manual Predicted Labels:')
print(confusion_matrix(b7, b5))
'''
for i in range(len(b5)):
    if b5[i] == 0:
        b5[i] = 2
    elif b5[i] == 1:
        b5[i] = 0
    elif b5[i] == 2:
        b5[i] = 1
'''