import numpy as np
import sys
import os
from sklearn.decomposition import PCA
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict
def divide_train_and_test(dict, n):
    data = dict['data']
    data_test = data[:n].reshape(n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    data_train = data[n:1000].reshape(1000 - n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    labels = dict['labels']
    labels_test = np.array(labels[:n])
    labels_train = np.array(labels[n:1000])
    return data_test, data_train, labels_test, labels_train
def RGB_to_gray(data):
    coefficients = [0.299, 0.587, 0.114]
    num, height, width, _ = data.shape
    new_data = np.zeros((num, height, width), dtype=float)
    for n in range(num):
        for row in range(height):
            for col in range(width):
                new_data[n, row, col] = np.dot(data[n, row, col, :], coefficients)
    return new_data
def knn(test, data_train, data_labels, k):
    if k <= 0:
        return None
    predictions = np.zeros(test.shape[0], dtype=int)
    for i in range(test.shape[0]):
        diff = np.tile(test[i], (data_train.shape[0], 1)) - data_train
        sq_diff = diff ** 2
        sq_distance = sq_diff.sum(axis=1)
        sort_distance = sq_distance.argsort()
        count = {}
        for j in range(k):
            label = data_labels[sort_distance[j]]
            count[label] = count.get(label, 0) + 1
        max_count = 0
        max_label = -1
        for key, value in count.items():
            if value > max_count:
                max_count = value
                max_label = key
        predictions[i] = max_label
    return predictions
def write(predictions, labels):
    with open('4251258720.txt', 'w') as f:
        for i in range(predictions.shape[0]):
            f.write(str(predictions[i]) + " " + str(labels[i]) + "\n")
if __name__ == "__main__":
    K = int(sys.argv[1])
    D = int(sys.argv[2])
    N = int(sys.argv[3])
    file = sys.argv[4]
    dict = unpickle(file)
    data_test, data_train, labels_test, labels_train = divide_train_and_test(dict, N)
    data_gray_test = RGB_to_gray(data_test)
    data_gray_train = RGB_to_gray(data_train)
    data_pca_train = data_gray_train.reshape(1000 - N, 1024)
    data_pca_test = data_gray_test.reshape(N, 1024)
    pca = PCA(n_components=D, svd_solver='full')
    data_pca_train = pca.fit_transform(data_pca_train)
    data_pca_test = pca.transform(data_pca_test)
    predict = knn(data_pca_test, data_pca_train, labels_train, K)
    write(predict, labels_test)
    for i in range(predict.shape[0]):
        print(predict[i], labels_test[i])