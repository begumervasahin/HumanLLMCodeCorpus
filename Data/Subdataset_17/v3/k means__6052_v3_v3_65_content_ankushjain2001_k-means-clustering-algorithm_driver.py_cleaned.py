import kmeans
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
def load_iris_dataset():
    iris = datasets.load_iris()
    return iris.data, iris.target
def run_custom_kmeans(data, num_clusters, max_iterations, init_method):
    return kmeans.KMeans(data, num_clusters, max_iterations, init_method)
def run_sklearn_kmeans(data, num_clusters):
    kmeans_model = KMeans(n_clusters=num_clusters, init='k-means++').fit(data)
    return kmeans_model.labels_
def plot_clusters(data, labels, title):
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.title(title)
    plt.show()
def display_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    print(f'{title}:\n{cm}\n')
NUM_CLUSTERS = 3
MAX_ITERATIONS = 100
INIT_METHOD = 'kmeans++'
def main():
    data, true_labels = load_iris_dataset()
    predicted_labels_custom = run_custom_kmeans(data, NUM_CLUSTERS, MAX_ITERATIONS, INIT_METHOD)
    predicted_labels_sklearn = run_sklearn_kmeans(data, NUM_CLUSTERS)
    plot_clusters(data, true_labels, 'Ground Truth')
    plot_clusters(data, predicted_labels_custom, 'Custom KMeans Output')
    plot_clusters(data, predicted_labels_sklearn, 'SKLearn KMeans Output')
    display_confusion_matrix(true_labels, predicted_labels_custom, 'Confusion Matrix: True Labels vs Custom KMeans Predicted Labels')
    display_confusion_matrix(true_labels, predicted_labels_sklearn, 'Confusion Matrix: True Labels vs SKLearn KMeans Predicted Labels')
    display_confusion_matrix(predicted_labels_sklearn, predicted_labels_custom, 'Confusion Matrix: SKLearn KMeans vs Custom KMeans Predicted Labels')
if __name__ == '__main__':
    main()