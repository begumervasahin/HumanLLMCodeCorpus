import os
import struct
import numpy as np
from sklearn.decomposition import PCA
from KNN import KNN
class PCA_SVD:
    def __init__(self):
        self.img_shape = None
        self.img_size = (128, 128)
    def load_mnist(self, path, kind='train'):
        labels_path = os.path.join(path, f'{kind}-labels-idx1-ubyte')
        images_path = os.path.join(path, f'{kind}-images-idx3-ubyte')
        with open(labels_path, 'rb') as lbpath:
            magic, n = struct.unpack('>II', lbpath.read(8))
            labels = np.fromfile(lbpath, dtype=np.uint8)
        with open(images_path, 'rb') as imgpath:
            magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))
            images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)
        return images, labels
    def compute_mean(self, x, axis=0):
        return np.mean(x, axis=axis)
    def decompose_matrix(self, matrix):
        eigenvalues, featurevector = np.linalg.eig(matrix)
        return eigenvalues, featurevector
    def select_top_eigenvalues(self, eigenvalues, n_components):
        sorted_indices = np.argsort(eigenvalues)[::-1]
        return sorted_indices[:n_components]
    def extract_feature_vectors(self, indices, featurevector, n_components):
        return featurevector[:, indices[:n_components]]
    def compute_covariance_matrix(self, x, mean):
        return np.cov((x - mean).T)
    def map_features(self, samples, components_mat):
        return np.dot(samples, components_mat)
    def make_matrix_symmetric(self, x):
        return (x + x.T) / 2
    def perform_pca(self, samples, n_components=1):
        print("PCA decomposition start!")
        all_samples_mean = self.compute_mean(samples)
        cov_mat = self.compute_covariance_matrix(samples, all_samples_mean)
        cov_mat = self.make_matrix_symmetric(cov_mat)
        eigenvalues, featurevector = self.decompose_matrix(cov_mat)
        selected_indices = self.select_top_eigenvalues(eigenvalues, n_components)
        components_mat = self.extract_feature_vectors(selected_indices, featurevector, n_components)
        print("Number of components:", n_components)
        compress_data = self.map_features(samples, components_mat)
        return compress_data, components_mat
    def perform_pca_sklearn(self, data, n_components="mle", svd_solver="full"):
        print("PCA decomposition start!")
        pca = PCA(n_components=n_components, svd_solver=svd_solver)
        compress_data = pca.fit_transform(data)
        print("Number of components:", pca.n_components)
        print("Explained variance ratio:\n", pca.explained_variance_ratio_)
        return compress_data, pca
if __name__ == "__main__":
    root_dir = r'D:/Pattern_Recognition/Exp5-10'
    datasets_dir = os.path.join(root_dir, "datasets")
    os.chdir(root_dir)
    dataset_path = os.path.join(datasets_dir, "mnist")
    ps = PCA_SVD()
    dataset_type = "mnist"
    if dataset_type == "mnist":
        x_train, y_train = ps.load_mnist(dataset_path, "train")
        x_train, y_train = x_train[:10000], y_train[:10000]
        x_test, y_test = ps.load_mnist(dataset_path, "t10k")
        x_test, y_test = x_test[:2000], y_test[:2000]
        print("Data loaded!")
    elif dataset_type == "normal":
        print("Data loaded!")
    x_train, components_mat = ps.perform_pca(x_train, n_components=50)
    x_test = ps.map_features(x_test, components_mat)
    knn_classifier = KNN(kN=5, method="K_Nearest")
    knn_classifier.train(x_train, y_train)
    y_pred = knn_classifier.predict(x_test)
    accuracy, precision = knn_classifier.evaluate(y_pred, y_test)
    print(f"Accuracy: {accuracy} Precision: {precision}")