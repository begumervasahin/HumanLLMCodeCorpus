import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
def load_mnist_data(images_path, labels_path):
    X, y = loadlocal_mnist(images_path=images_path, labels_path=labels_path)
    return X, y
def preprocess_binary_classification(X_train, y_train, X_test, y_test, target_classes=[1, 2]):
    Y_train = [label - 1 for label in y_train if label in target_classes]
    Y_test = [label - 1 for label in y_test if label in target_classes]
    return Y_train, Y_test
def load_preprocessed_data(train_path, test_path):
    with open(train_path, 'rb') as f:
        x_train = pickle.load(f)
    with open(test_path, 'rb') as f:
        x_test = pickle.load(f)
    return x_train, x_test
def load_count_matrices(train0_path, train1_path):
    counttrain0 = np.load(train0_path)
    counttrain1 = np.load(train1_path)
    return counttrain0, counttrain1
def calculate_priors(Y_train):
    a = Y_train.count(0)
    b = Y_train.count(1)
    priortrouser = a / (a + b)
    priorpullover = b / (a + b)
    return priortrouser, priorpullover
def normalize_count_matrices(counttrain0, counttrain1, a, b):
    counttrain0_norm = counttrain0 / a
    counttrain1_norm = counttrain1 / b
    return counttrain0_norm, counttrain1_norm
def classify_threshold(x_test, counttrain0, counttrain1, priortrouser, priorpullover, thresholds):
    y_pred = np.zeros(shape=(len(thresholds), len(x_test)))
    for k, threshold in enumerate(thresholds):
        for i in range(len(x_test)):
            pdt1 = sum(math.log(counttrain1[j][0]) if x_test[i][j] == 1 else math.log(counttrain0[j][0]) for j in range(len(x_test[0])))
            pdt2 = sum(math.log(counttrain1[j][1]) if x_test[i][j] == 1 else math.log(counttrain0[j][1]) for j in range(len(x_test[0])))
            prob0 = (pdt1 * priortrouser) / (pdt1 * priortrouser + pdt2 * priorpullover)
            y_pred[k][i] = 0 if prob0 <= threshold else 1
    return y_pred
def calculate_tpr_fpr(y_pred, Y_test):
    tpr_array = []
    fpr_array = []
    for i in range(len(y_pred)):
        tp = sum(y_pred[i][j] == 0 and Y_test[j] == 0 for j in range(len(Y_test)))
        tn = sum(y_pred[i][j] == 1 and Y_test[j] == 1 for j in range(len(Y_test)))
        fp = sum(y_pred[i][j] == 0 and Y_test[j] == 1 for j in range(len(Y_test)))
        fn = sum(y_pred[i][j] == 1 and Y_test[j] == 0 for j in range(len(Y_test)))
        tpr_array.append(tp / (tp + fn))
        fpr_array.append(fp / (fp + tn))
        conf_matrix = np.array([[tp, fp], [fn, tn]])
        print("CASE", i + 1, ":-")
        print(conf_matrix)
        print("The precision is:", tp / (tp + fp))
        print("The recall is:", tp / (tp + fn))
    return tpr_array, fpr_array
def plot_roc_curve(fpr_array, tpr_array):
    plt.plot(fpr_array, tpr_array)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.title("ROC Curve")
    plt.show()
if __name__ == "__main__":
    X_train, y_train = load_mnist_data(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
    X_test, y_test = load_mnist_data(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
    Y_train, Y_test = preprocess_binary_classification(X_train, y_train, X_test, y_test, target_classes=[1, 2])
    x_train, x_test = load_preprocessed_data(train_path='./bintrain.pkl', test_path='./bintest.pkl')
    counttrain0, counttrain1 = load_count_matrices(train0_path='./counttrain0.mat', train1_path='./counttrain1.mat')
    priortrouser, priorpullover = calculate_priors(Y_train)
    counttrain0_norm, counttrain1_norm = normalize_count_matrices(counttrain0, counttrain1, len(Y_train), len(Y_test))
    thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
    y_pred = classify_threshold(x_test, counttrain0_norm, counttrain1_norm, priortrouser, priorpullover, thresholds)
    tpr_array, fpr_array = calculate_tpr_fpr(y_pred, Y_test)
    plot_roc_curve(fpr_array, tpr_array)