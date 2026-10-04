import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
class Visualizer:
    def plot_classifier_regressor(self, y_test, y_result, method_identifier):
        if method_identifier == 2:
            plt.scatter(y_test, y_result, c='blue')
            plt.title('Actual price vs. Predicted price')
            plt.xlabel('y_test (Actual Price)')
            plt.ylabel('y_predicted (Predicted Price)')
            plt.show()
        elif method_identifier == 1:
            plt.hist(y_test, bins=2, alpha=0.7, label='Actual')
            plt.hist(y_result, bins=2, alpha=0.7, label='Predicted')
            plt.title('Malignant vs. Benign (Classification Results)')
            plt.xlabel('0 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.legend()
            plt.grid()
            plt.show()
    def plot_clustering(self, iris_data, clusters):
        pca = PCA(n_components=2).fit(iris_data.data)
        pca_2d = pca.transform(iris_data.data)
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.scatter(pca_2d[:, 0], pca_2d[:, 1])
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        list_clusters = []
        cluster_names = []
        colors = ['r', 'g', 'b', 'y']
        markers = ['+', 'o', '*', 'X']
        for i in range(0, pca_2d.shape[0]):
            cluster_idx = clusters[i]
            scatter = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c=colors[cluster_idx], marker=markers[cluster_idx])
            if f'Cluster {cluster_idx + 1}' not in cluster_names:
                cluster_names.append(f'Cluster {cluster_idx + 1}')
                list_clusters.append(scatter)
        plt.legend(list_clusters, cluster_names)
        plt.show()
if __name__ == "__main__":
    visualizer = Visualizer()
    y_test = [0, 0, 1, 1, 0, 1, 0, 1]
    y_result = [0, 1, 1, 1, 0, 0, 0, 1]
    visualizer.plot_classifier_regressor(y_test, y_result, method_identifier = 1)
    iris = load_iris()
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(iris.data)
    clusters = kmeans.predict(iris.data)
    visualizer.plot_clustering(iris, clusters)