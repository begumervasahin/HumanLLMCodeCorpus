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
        labels_path = os.path.join(path, '%s-labels-idx1-ubyte' % kind)
        images_path = os.path.join(path, '%s-images-idx3-ubyte' % kind)
        with open(labels_path, 'rb') as lbpath:
            magic, n = struct.unpack('>II', lbpath.read(8))
            labels = np.fromfile(lbpath, dtype=np.uint8)
        with open(images_path, 'rb') as imgpath:
            magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))
            images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)
        return images, labels
    def cal_means(self, x, axis=0):
        return x.mean(axis=axis)
    def matrix_decompose(self, matrix):
        eigenvalues, featurevector = np.linalg.eig(matrix)
        return eigenvalues, featurevector
    def find_max_eigenvalues(self, eigenvalues, n_components):
        eigenvalues_index = np.argsort(eigenvalues, kind='quicksort')[::-1]
        return eigenvalues_index[:n_components]
    def draw_featurevector(self, eigenvalues_index, featurevector, n_components):
        return featurevector[:, eigenvalues_index[:n_components]]
    def cov_variance_matrix(self, x, mean):
        return (x - mean).T.dot((x - mean))
    def feature_mapping(self, samples, components_mat):
        return np.dot(samples, components_mat)
    def matrix_symmetric(self, x):
        return (x + x.T) * 1.0 / 2
    def PCA_decomposition(self, samples, n_components=1):
        print("PCA decomposition start!")
        all_samples_mean = self.cal_means(samples)
        cov_mat = self.cov_variance_matrix(samples, all_samples_mean)
        cov_mat = cov_mat * 1.0 / samples.shape[0]
        cov_mat = self.matrix_symmetric(cov_mat)
        eigenvalues, featurevector = self.matrix_decompose(cov_mat)
        eigenvalues_index = self.find_max_eigenvalues(eigenvalues, n_components)
        components_mat = self.draw_featurevector(eigenvalues_index, featurevector, n_components)
        print("number of components: ", n_components)
        compress_data = self.feature_mapping(samples, components_mat)
        return compress_data, components_mat
    def PCA_decomposition_sklearn(self, data, n_components="mle", svd_solver="full"):
        print("PCA decomposition start!")
        pca = PCA(n_components=n_components, svd_solver="full")
        compress_data = pca.fit_transform(data)
        print("number of components: ", pca.n_components)
        print("explained variance ratio:\n", pca.explained_variance_ratio_)
        return compress_data, pca
if __name__ == "__main__":
    Root_dir = r'D:/Pattern_Recognion/Exp5-10'
    datasets_dir = os.path.join(Root_dir, "datasets")
    os.chdir(Root_dir)
    dataset_path = os.path.join(datasets_dir, "mnist")
    PS = PCA_SVD()
    datasets = "mnist"
    if datasets == "mnist":
        x_train, y_train = PS.load_mnist(dataset_path, "train")
        x_train, y_train = x_train[:10000], y_train[:10000]
        x_test, y_test = PS.load_mnist(dataset_path, "t10k")
        x_test, y_test = x_test[:2000], y_test[:2000]
        print("data loaded!")
    elif datasets == "normal":
        print("data loaded!")
    x_train, components_mat = PS.PCA_decomposition(x_train, n_components=50)
    x_test = PS.feature_mapping(x_test, components_mat)
    K_Nearest = KNN(kN=5, method="K_Nearest")
    K_Nearest.train(x_train, y_train)
    y_pred = K_Nearest.predict(x_test)
    acc, prec = K_Nearest.evaluate(y_pred, y_test)
    print("acc: {} prec:{}".format(acc, prec))