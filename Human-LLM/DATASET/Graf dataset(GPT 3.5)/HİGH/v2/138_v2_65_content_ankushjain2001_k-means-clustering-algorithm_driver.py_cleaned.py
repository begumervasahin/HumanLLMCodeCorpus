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
kmeans.drawPlot(b2, b3, 'Ground Truth')
kmeans.drawPlot(b2, b5, 'Custom KMeans Output')
kmeans.drawPlot(b2, b7, 'SKLearn KMeans Output')
print('Confusion Matrix of True Labels v/s Custom KMeans Predicted Labels:')
print(confusion_matrix(b3, b5))
print('Confusion Matrix of True Labels v/s SKLearn KMeans Predicted Labels:')
print(confusion_matrix(b3, b7))
print('Confusion Matrix of SKLearn KMeans Predicted Labels v/s Custom KMeans Predicted Labels:')
print(confusion_matrix(b7, b5))
'''
'''