
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import kmeans
def main():
    iris = datasets.load_iris()
    data = iris.data
    y_truth = iris.target
    num_clusters = 3
    max_iterations = 100
    init_method = 'kmeans++'
    y_pred = kmeans.KMeans(data, num_clusters, max_iterations, init_method)
    y_sklearn_pred = perform_sklearn_kmeans(data, num_clusters, max_iterations)
    plot_results(data, y_truth, 'Truth')
    plot_results(data, y_pred, 'Manual Output')
    plot_results(data, y_sklearn_pred, 'SKLearn Output')
    print_confusion_matrices(y_truth, y_pred, y_sklearn_pred)
def perform_sklearn_kmeans(data, num_clusters, max_iterations):
    kmeans_sklearn = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=max_iterations).fit(data)
    return kmeans_sklearn.labels_
def plot_results(data, labels, title):
    plt.figure()
    scatter = plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.title(title)
    plt.colorbar(scatter)
    plt.show()
def print_confusion_matrices(y_truth, y_pred, y_sklearn_pred):
    print('Confusion Matrix of True Labels vs Predicted Labels:')
    print(confusion_matrix(y_truth, y_pred))
    print('Confusion Matrix of True Labels vs SKLearn Predicted Labels:')
    print(confusion_matrix(y_truth, y_sklearn_pred))
    print('Confusion Matrix of SKLearn Predicted Labels vs Manual Predicted Labels:')
    print(confusion_matrix(y_sklearn_pred, y_pred))
if __name__ == "__main__":
    main()