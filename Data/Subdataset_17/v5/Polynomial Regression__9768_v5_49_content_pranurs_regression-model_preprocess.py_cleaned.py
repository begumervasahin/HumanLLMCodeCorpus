import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def normalize(x, norm_type='min_max_normalization'):
    if norm_type == 'standardization':
        return (x - np.mean(x)) / np.std(x)
    else:
        return (x - np.min(x)) / (np.max(x) - np.min(x))
def train_test_val_split(x1, x2, Y):
    x1 = x1.reshape(-1, 1)
    x2 = x2.reshape(-1, 1)
    X = np.concatenate((x1, x2), axis=1)
    Y = Y.reshape(-1, 1)
    X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.2, random_state=0)
    X_test, X_val, Y_test, Y_val = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=3)
    x1_train, x2_train = X_train[:, 0].reshape(-1, 1), X_train[:, 1].reshape(-1, 1)
    x1_test, x2_test = X_test[:, 0].reshape(-1, 1), X_test[:, 1].reshape(-1, 1)
    x1_val, x2_val = X_val[:, 0].reshape(-1, 1), X_val[:, 1].reshape(-1, 1)
    return x1_train, x1_test, x1_val, x2_train, x2_test, x2_val, Y_train, Y_test, Y_val
def generate_feature_matrix(x1, x2, degree):
    feature_matrix = np.ones((x1.shape[0], 1))
    for d in range(1, degree + 1):
        for i in range(d + 1):
            feature = (x1 ** (d - i)) * (x2 ** i)
            feature_matrix = np.concatenate((feature_matrix, feature.reshape(-1, 1)), axis=1)
    return feature_matrix