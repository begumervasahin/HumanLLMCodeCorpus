import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
X_train, y_train = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
X_test, y_test = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
y_train = [label - 1 for label in y_train if label in [1, 2]]
y_test = [label - 1 for label in y_test if label in [1, 2]]
with open('./bintrain.pkl', 'rb') as f:
    x_train = pickle.load(f)
with open('./bintest.pkl', 'rb') as f:
    x_test = pickle.load(f)
counttrain0 = np.load('./counttrain0.mat')
counttrain1 = np.load('./counttrain1.mat')
a = y_train.count(0)
b = y_train.count(1)
prior_trouser = a / (a + b)
prior_pullover = b / (a + b)
counttrain0[:, 0] /= a
counttrain1[:, 0] /= a
counttrain0[:, 1] /= b
counttrain1[:, 1] /= b
print(f"The prior for trouser is: {prior_trouser}")
print(f"The prior for pullover is: {prior_pullover}")
thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
y_pred = np.zeros((len(thresholds), len(x_test)))
def calculate_log_probabilities(x, count0, count1):
    log_prob_trouser = 0
    log_prob_pullover = 0
    for j in range(len(x)):
        if x[j] == 1:
            log_prob_trouser += math.log(count1[j][0])
            log_prob_pullover += math.log(count1[j][1])
        else:
            log_prob_trouser += math.log(count0[j][0])
            log_prob_pullover += math.log(count0[j][1])
    return log_prob_trouser, log_prob_pullover
for k, threshold in enumerate(thresholds):
    for i in range(len(x_test)):
        log_prob_trouser, log_prob_pullover = calculate_log_probabilities(x_test[i], counttrain0, counttrain1)
        prob_trouser = (log_prob_trouser * prior_trouser) / (log_prob_trouser * prior_trouser + log_prob_pullover * prior_pullover)
        y_pred[k][i] = 0 if prob_trouser <= threshold else 1
print(f"Prediction lengths: {len(y_pred)}, {len(y_test)}")
print(y_pred[:, 0], y_pred[:, 1])
tp_array = []
fp_array = []
def calculate_confusion_matrix(y_true, y_pred):
    tp = fp = fn = tn = 0
    for i in range(len(y_true)):
        if y_pred[i] == 0 and y_true[i] == 0:
            tp += 1
        elif y_pred[i] == 1 and y_true[i] == 1:
            tn += 1
        elif y_pred[i] == 0 and y_true[i] == 1:
            fp += 1
        elif y_pred[i] == 1 and y_true[i] == 0:
            fn += 1
    return np.array([[tp, fp], [fn, tn]])
for i, threshold in enumerate(thresholds):
    conf_matrix = calculate_confusion_matrix(y_test, y_pred[i])
    tp, fp, fn, tn = conf_matrix.flatten()
    tp_rate = tp / (tp + fn)
    fp_rate = fp / (fp + tn)
    tp_array.append(tp_rate)
    fp_array.append(fp_rate)
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0
    recall = tp_rate
    print(f"CASE {i + 1} (Threshold = {threshold}):")
    print(conf_matrix)
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
plt.plot(fp_array, tp_array)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()