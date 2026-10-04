import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
def load_iris_dataset():
    iris = datasets.load_iris()
    return iris.data, iris.target
def run_custom_kmeans(data, k, max_iterations, init_method):
    return kmeans.KMeans(data, k, max_iterations, init_method)
def run_sklearn_kmeans(data, k):
    kmeans_sklearn = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300).fit(data)
    return kmeans_sklearn.labels_
def plot_clusters(data, labels, title):
    kmeans.drawPlot(data, labels, title)
def print_confusion_matrix(y_true, y_pred, title):
    print(title)
    print(confusion_matrix(y_true, y_pred))
k = 3
max_iterations = 100
init_method = 'kmeans++'
data, y_truth = load_iris_dataset()
y_pred_custom = run_custom_kmeans(data, k, max_iterations, init_method)
y_pred_sklearn = run_sklearn_kmeans(data, k)
plot_clusters(data, y_truth, 'Ground Truth')
plot_clusters(data, y_pred_custom, 'Custom KMeans Output')
plot_clusters(data, y_pred_sklearn, 'SKLearn KMeans Output')
print_confusion_matrix(y_truth, y_pred_custom, 'Confusion Matrix of True Labels vs Custom KMeans Predicted Labels:')
print_confusion_matrix(y_truth, y_pred_sklearn, 'Confusion Matrix of True Labels vs SKLearn KMeans Predicted Labels:')
print_confusion_matrix(y_pred_sklearn, y_pred_custom, 'Confusion Matrix of SKLearn KMeans Predicted Labels vs Custom KMeans Predicted Labels:')