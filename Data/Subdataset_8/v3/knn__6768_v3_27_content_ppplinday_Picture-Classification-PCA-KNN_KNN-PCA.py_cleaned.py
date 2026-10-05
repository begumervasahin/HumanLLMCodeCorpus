import numpy as np
import sys
from sklearn.decomposition import PCA
import os
import pickle
def unpickle(file):
    with open(file, 'rb') as fo:
        return pickle.load(fo, encoding='latin1')
def divide_train_and_test(data, labels, n):
    data_test = data[:n].reshape(n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    data_train = data[n:1000].reshape(1000 - n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    labels_test = np.array(labels[:n])
    labels_train = np.array(labels[n:1000])
    return data_test, data_train, labels_test, labels_train
def RGB_to_gray(data):
    return np.dot(data[..., :3], [0.299, 0.587, 0.114])
def knn(test, data_train, data_labels, k):
    pre = np.zeros([test.shape[0]], int)
    for i in range(test.shape[0]):
        diff = np.tile(test[i], (data_train.shape[0], 1)) - data_train
        sqdiff = diff ** 2
        sqdistance = sqdiff.sum(axis=1)
        sortdistance = sqdistance.argsort()
        Count = {}
        for j in range(k):
            label = data_labels[sortdistance[j]]
            Count[label] = Count.get(label, 0) + 1
        maxx = 0
        index = -1
        for key in Count:
            if Count[key] > maxx:
                maxx = Count[key]
                index = key
        pre[i] = index
    return pre
def write_predictions(predictions, labels):
    with open('4251258720.txt', 'w') as f:
        for i in range(predictions.shape[0]):
            f.write(str(predictions[i]) + " " + str(labels[i]) + "\n")
if __name__ == "__main__":
    K, D, N, file = map(int, sys.argv[1:])
    data_dict = unpickle(file)
    data_test, data_train, labels_test, labels_train = divide_train_and_test(data_dict['data'], data_dict['labels'], N)
    data_gray_test = RGB_to_gray(data_test)
    data_gray_train = RGB_to_gray(data_train)
    data_pca_train = data_gray_train.reshape(1000 - N, 1024)
    data_pca_test = data_gray_test.reshape(N, 1024)
    pca = PCA(n_components=D, svd_solver='full')
    data_pca_train = pca.fit_transform(data_pca_train)
    data_pca_test = pca.transform(data_pca_test)
    predictions = knn(data_pca_test, data_pca_train, labels_train, K)
    write_predictions(predictions, labels_test)
    for i in range(predictions.shape[0]):
        print(predictions[i], labels_test[i])