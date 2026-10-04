import numpy as np
import sys
from sklearn.decomposition import PCA
import os
import pickle
def unpickle(file):
    with open(file, 'rb') as fo:
        data_dict = pickle.load(fo, encoding='latin1')
    return data_dict
def divide_train_and_test(data_dict, n):
    data = data_dict['data']
    labels = data_dict['labels']
    data_test = data[:n].reshape(n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    data_train = data[n:1000].reshape(1000 - n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    labels_test = np.array(labels[:n])
    labels_train = np.array(labels[n:1000])
    return data_test, data_train, labels_test, labels_train
def rgb_to_gray(data):
    num, height, width, _ = data.shape
    gray_data = np.zeros([num, height, width], float)
    for n in range(num):
        for row in range(height):
            for col in range(width):
                gray_data[n, row, col] = 0.299 * data[n, row, col, 0] + 0.587 * data[n, row, col, 1] + 0.114 * data[n, row, col, 2]
    return gray_data
def knn(test, data_train, data_labels, k):
    if k <= 0:
        return None
    predictions = np.zeros(test.shape[0], int)
    for i in range(test.shape[0]):
        diff = np.tile(test[i], (data_train.shape[0], 1)) - data_train
        sqdiff = diff ** 2
        sqdistance = sqdiff.sum(axis=1)
        sortdistance = sqdistance.argsort()
        count = {}
        for j in range(k):
            label = data_labels[sortdistance[j]]
            count[label] = count.get(label, 0) + 1
        predictions[i] = max(count, key=count.get)
    return predictions
def write_predictions(predictions, labels, filename='4251258720.txt'):
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'a') as f:
        for pred, label in zip(predictions, labels):
            f.write(f"{pred} {label}\n")
def main():
    K = int(sys.argv[1])
    D = int(sys.argv[2])
    N = int(sys.argv[3])
    file = sys.argv[4]
    data_dict = unpickle(file)
    data_test, data_train, labels_test, labels_train = divide_train_and_test(data_dict, N)
    data_gray_test = rgb_to_gray(data_test)
    data_gray_train = rgb_to_gray(data_train)
    data_pca_train = data_gray_train.reshape(1000 - N, 1024)
    data_pca_test = data_gray_test.reshape(N, 1024)
    pca = PCA(n_components=D, svd_solver='full')
    data_pca_train = pca.fit_transform(data_pca_train)
    data_pca_test = pca.transform(data_pca_test)
    predictions = knn(data_pca_test, data_pca_train, labels_train, K)
    write_predictions(predictions, labels_test)
    for pred, label in zip(predictions, labels_test):
        print(pred, label)
if __name__ == "__main__":
    main()