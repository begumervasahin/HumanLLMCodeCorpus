import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
def load_mnist_data():
    X_train, y_train = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
    X_test, y_test = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
    Y_train = [label - 1 for label in y_train if label in [1, 2]]
    Y_test = [label - 1 for label in y_test if label in [1, 2]]
    return X_train, Y_train, X_test, Y_test
def load_binary_data():
    with open('./bintrain.pkl', 'rb') as f:
        x_train = pickle.load(f)
    with open('./bintest.pkl', 'rb') as f:
        x_test = pickle.load(f)
    return x_train, x_test
def load_count_matrices():
    counttrain0 = np.load('./counttrain0.mat')
    counttrain1 = np.load('./counttrain1.mat')
    a = y_train.count(0)
    b = y_train.count(1)
    priortrouser = a / (a + b)
    priorpullover = b / (a + b)
    return counttrain0, counttrain1, priortrouser, priorpullover
def normalize_matrices(counttrain0, counttrain1, a, b):
    for i in range(len(counttrain0)):
        for j in range(2):
            counttrain0[i][j] /= a
            counttrain1[i][j] /= b
    return counttrain0, counttrain1
def predict_labels(x_test, counttrain0, counttrain1, priortrouser, priorpullover, thresholds):
    y_pred = np.zeros(shape=(len(thresholds), len(x_test)))
    for k, threshold in enumerate(thresholds):
        for i in range(len(x_test)):
            pdt1 = sum(math.log(counttrain1[j][0]) if x_test[i][j] == 1 else math.log(counttrain0[j][0]) for j in range(len(x_test[0])))
            pdt2 = sum(math.log(counttrain1[j][1]) if x_test[i][j] == 1 else math.log(counttrain0[j][1]) for j in range(len(x_test[0])))
            prob0 = (pdt1 * priortrouser) / (pdt1 * priortrouser + pdt2 * priorpullover)
            y_pred[k][i] = 0 if prob0 <= threshold else 1
    return y_pred
def calculate_rates(y_test, y_pred):
    tparray = []
    fparray = []
    for i in range(len(y_pred)):
        confmatrix = np.zeros(shape=(2, 2))
        tp = sum(1 for j in range(len(y_test)) if y_pred[i][j] == 0 and y_test[j] == 0)
        tn = sum(1 for j in range(len(y_test)) if y_pred[i][j] == 1 and y_test[j] == 1)
        fp = sum(1 for j in range(len(y_test)) if y_pred[i][j] == 0 and y_test[j] == 1)
        fn = sum(1 for j in range(len(y_test)) if y_pred[i][j] == 1 and y_test[j] == 0)
        confmatrix[0][0] = tp
        confmatrix[1][1] = tn
        confmatrix[0][1] = fp
        confmatrix[1][0] = fn
        tparray.append(tp / (tp + fn))
        fparray.append(fp / (fp + tn))
        print("CASE" + str(i + 1) + " :-")
        print(confmatrix)
        print("The precision is: " + str((tp / (tp + fp))))
        print("The recall is: " + str((tp / (tp + fn))))
    return tparray, fparray
def plot_roc_curve(fparray, tparray):
    plt.plot(fparray, tparray)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.title("ROC Curve")
    plt.show()
X_train, y_train, X_test, y_test = load_mnist_data()
x_train, x_test = load_binary_data()
counttrain0, counttrain1, priortrouser, priorpullover = load_count_matrices()
counttrain0, counttrain1 = normalize_matrices(counttrain0, counttrain1, len(y_train.count(0)), len(y_train.count(1)))
thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
y_pred = predict_labels(x_test, counttrain0, counttrain1, priortrouser, priorpullover, thresholds)
tparray, fparray = calculate_rates(y_test, y_pred)
plot_roc_curve(fparray, tparray)