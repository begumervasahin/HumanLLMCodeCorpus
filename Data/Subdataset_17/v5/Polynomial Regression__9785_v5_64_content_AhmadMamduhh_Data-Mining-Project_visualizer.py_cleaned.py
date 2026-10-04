import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
class Visualizer:
    def plot_classifier_regressor(self, y_test, y_result, method_identifier):
        if method_identifier == 2:
            self._plot_regression_results(y_test, y_result)
        elif method_identifier == 1:
            self._plot_classification_results(y_test, y_result)
    def _plot_regression_results(self, y_test, y_result):
        plt.scatter(y_test, y_result, c='blue')
        plt.title('Actual Price vs. Predicted Price')
        plt.xlabel('y_test (Actual Price)')
        plt.ylabel('y_result (Predicted Price)')
        plt.show()
    def _plot_classification_results(self, y_test, y_result):
        plt.hist(y_test, bins=2, edgecolor='black')
        plt.title('Malignant vs. Benign (Actual Data)')
        plt.xlabel('0 = Benign   1 = Malignant')
        plt.ylabel('Number of Patients')
        plt.grid(True)
        plt.show()
        plt.hist(y_result, bins=2, edgecolor='black')
        plt.title('Malignant vs. Benign (Predicted Classification Results)')
        plt.xlabel('0 = Benign   1 = Malignant')
        plt.ylabel('Number of Patients')
        plt.grid(True)
        plt.show()
    def plot_clustering(self, iris, clusters):
        pca_2d = self._apply_pca(iris.data)
        self._plot_reference_plot(pca_2d)
        self._plot_clustered_data(pca_2d, clusters)
    def _apply_pca(self, data, n_components=2):
        pca = PCA(n_components=n_components)
        return pca.fit_transform(data)
    def _plot_reference_plot(self, pca_2d):
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.scatter(pca_2d[:, 0], pca_2d[:, 1])
        plt.show()
    def _plot_clustered_data(self, pca_2d, clusters):
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        cluster_colors = ['r', 'g', 'b', 'y']
        cluster_markers = ['+', 'o', '*', 'X']
        list_clusters = []
        cluster_names = []
        for i in range(pca_2d.shape[0]):
            cluster_id = clusters[i]
            color = cluster_colors[cluster_id]
            marker = cluster_markers[cluster_id]
            scatter = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c=color, marker=marker)
            cluster_name = f'Cluster {cluster_id + 1}'
            if cluster_name not in cluster_names:
                cluster_names.append(cluster_name)
                list_clusters.append(scatter)
        plt.legend(list_clusters, cluster_names)
        plt.show()