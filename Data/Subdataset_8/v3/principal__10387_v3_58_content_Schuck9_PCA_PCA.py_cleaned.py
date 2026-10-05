import os
import numpy as np
import struct
from sklearn.decomposition import PCA
from sklearn.metrics import precision_score, accuracy_score
from KNN import KNN
class PrincipalComponentAnalysis:
    def __init__(self):
        self.img_shape = None
        self.img_size = (128, 128)
    def load_mnist_data(self, path, kind='train'):
        labels_path = os.path.join(path, f'{kind}-labels-idx1-ubyte')
        images_path = os.path.join(path, f'{kind}-images-idx3-ubyte')
        with open(labels_path, 'rb') as lb_file:
            _, n = struct.unpack('>II', lb_file.read(8))
            labels = np.fromfile(lb_file, dtype=np.uint8)
        with open(images_path, 'rb') as img_file:
            _, num, rows, cols = struct.unpack('>IIII', img_file.read(16))
            images = np.fromfile(img_file, dtype=np.uint8).reshape(len(labels), 784)
        return images, labels
    def apply_pca(self, samples, n_components=1):
        pca = PCA(n_components=n_components)
        compressed_data = pca.fit_transform(samples)
        return compressed_data, pca
if __name__ == "__main__":
    root_dir = r'D:/Pattern_Recognion/Exp5-10'
    datasets_dir = os.path.join(root_dir, "datasets")
    os.chdir(root_dir)
    mnist_dataset_path = os.path.join(datasets_dir, "mnist")
    pca_instance = PrincipalComponentAnalysis()
    dataset_type = "mnist"
    if dataset_type == "mnist":
        x_train, y_train = pca_instance.load_mnist_data(mnist_dataset_path, "train")
        x_train, y_train = x_train[:10000], y_train[:10000]
        x_test, y_test = pca_instance.load_mnist_data(mnist_dataset_path, "t10k")
        x_test, y_test = x_test[:2000], y_test[:2000]
        print("MNIST dataset loaded!")
        x_train_compressed, pca_model = pca_instance.apply_pca(x_train, n_components=50)
        x_test_compressed = pca_model.transform(x_test)
        knn_classifier = KNN(kN=5, method="K_Nearest")
        knn_classifier.train(x_train_compressed, y_train)
        y_pred = knn_classifier.predict(x_test_compressed)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        print("Accuracy:", accuracy)
        print("Precision:", precision)
    elif dataset_type == "normal":
        pass