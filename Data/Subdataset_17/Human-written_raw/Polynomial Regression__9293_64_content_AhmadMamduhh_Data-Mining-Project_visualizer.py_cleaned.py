import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
class Visualizer:
    def plot_classifier_regressor(self, y_test, y_result, method_identifier):
        if method_identifier == 2:
            plt.scatter(y_test, y_result, c='blue')
            plt.title('Actual price vs. Predicted price')
            plt.xlabel('y_test (Actual Price)')
            plt.ylabel('y_predicted (Predicted Price)')
            plt.show()
        elif method_identifier == 1:
            plt.hist(y_test)
            plt.title('Malginant vs. Benign (Actual Data)')
            plt.xlabel('0 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.grid()
            plt.show()
            plt.hist(y_result)
            plt.title('Malginant vs. Benign (Predicted Classification Results)')
            plt.xlabel('0 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.grid()
            plt.show()
    def plot_clustering(self, iris, clusters):
        pca = PCA(n_components=2).fit(iris.data)
        pca_2d = pca.transform(iris)
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.scatter(pca_2d[:, 0], pca_2d[:, 1])
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        list_clusters = []
        cluster_names = []
        for i in range(0, pca_2d.shape[0]):
            if clusters[i] == 0:
                c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
                if 'Cluster 1' not in cluster_names:
                    cluster_names.append('Cluster 1')
                    list_clusters.append(c1)
            elif clusters[i] == 1:
                c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
                if 'Cluster 2' not in cluster_names:
                    cluster_names.append('Cluster 2')
                    list_clusters.append(c2)
            elif clusters[i] == 2:
                c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')
                if 'Cluster 3' not in cluster_names:
                    cluster_names.append('Cluster 3')
                    list_clusters.append(c3)
            elif clusters[i] == 3:
                c4 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='y', marker='X')
                if 'Cluster 4' not in cluster_names:
                    cluster_names.append('Cluster 4')
                    list_clusters.append(c4)
        cluster_names.sort()
        plt.legend(list_clusters, cluster_names)
        plt.show()