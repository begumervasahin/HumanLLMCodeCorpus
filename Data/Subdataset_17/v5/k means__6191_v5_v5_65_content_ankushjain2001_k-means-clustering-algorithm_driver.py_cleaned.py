
import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
def main():
    iris = datasets.load_iris()
    data, y_truth = iris.data, iris.target
    num_clusters = 3
    max_iterations = 100
    init_method = 'kmeans++'
    y_pred_custom = kmeans.KMeans(data, num_clusters, max_iterations, init_method)
    kmeans_sklearn = KMeans(n_clusters=num_clusters, init=init_method, max_iter=max_iterations)
    y_pred_sklearn = kmeans_sklearn.fit_predict(data)
    plot_results(data, y_truth, 'True Labels')
    plot_results(data, y_pred_custom, 'Custom KMeans Output')
    plot_results(data, y_pred_sklearn, 'SKLearn KMeans Output')
    print_confusion_matrices(y_truth, y_pred_custom, y_pred_sklearn)
def plot_results(data, labels, title):
    kmeans.drawPlot(data, labels, title)
def print_confusion_matrices(y_truth, y_pred_custom, y_pred_sklearn):
    print('Confusion Matrix of True Labels vs Custom KMeans Predicted Labels:')
    print(confusion_matrix(y_truth, y_pred_custom))
    print('Confusion Matrix of True Labels vs SKLearn KMeans Predicted Labels:')
    print(confusion_matrix(y_truth, y_pred_sklearn))
    print('Confusion Matrix of Custom KMeans Predicted Labels vs SKLearn KMeans Predicted Labels:')
    print(confusion_matrix(y_pred_custom, y_pred_sklearn))
if __name__ == "__main__":
    main()