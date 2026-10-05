import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
iris = datasets.load_iris()
data = iris.data
y_truth = iris.target
k = 3
max_iterations = 100
init_method = 'kmeans++'
y_pred_custom = kmeans.KMeans(data, k, max_iterations, init_method)
kmeans_sklearn = KMeans(n_clusters=3, init='k-means++').fit(data)
y_pred_sklearn = kmeans_sklearn.labels_
kmeans.drawPlot(data, y_truth, 'Ground Truth')
kmeans.drawPlot(data, y_pred_custom, 'Custom KMeans Output')
kmeans.drawPlot(data, y_pred_sklearn, 'SKLearn KMeans Output')
print('Confusion Matrix of True Labels v/s Custom KMeans Predicted Labels:')
print(confusion_matrix(y_truth, y_pred_custom))
print('Confusion Matrix of True Labels v/s SKLearn KMeans Predicted Labels:')
print(confusion_matrix(y_truth, y_pred_sklearn))
print('Confusion Matrix of SKLearn KMeans Predicted Labels v/s Custom KMeans Predicted Labels:')
print(confusion_matrix(y_pred_sklearn, y_pred_custom))
'''
'''