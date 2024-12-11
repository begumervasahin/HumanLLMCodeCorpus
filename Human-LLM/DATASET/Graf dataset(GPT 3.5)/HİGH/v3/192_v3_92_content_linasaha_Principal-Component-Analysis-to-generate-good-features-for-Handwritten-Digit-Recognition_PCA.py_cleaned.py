import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import eig
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
def fonk1():
    b1 = pd.read_csv('./usps.test', header=None)
    b2 = pd.read_csv('./usps.train', header=None)
    b3 = pd.read_csv('./usps.valid', header=None)
    return b1, b2, b3
def fonk2(b1, b2, b3):
    X_testing, b4 = b1.iloc[:, 1:], b1.iloc[:, 0]
    X_training, b5 = b2.iloc[:, 1:], b2.iloc[:, 0]
    X_validate, b6 = b3.iloc[:, 1:], b3.iloc[:, 0]
    return X_testing, b4, X_training, b5, X_validate, b6
def fonk3(X_testing, b4, X_training, b5, X_validate, b6):
    X_test, X_train, b7 = np.array(X_testing), np.array(X_training), np.array(X_validate)
    y_test, y_train, b8 = np.array(b4), np.array(b5), np.array(b6)
    return X_test, X_train, b7, y_test, y_train, b8
def fonk4(X_train):
    b9 = np.matmul(X_train.transpose(), X_train)
    return b9
def fonk5(b9):
    eigen_values, b10 = eig(b9)
    b11 = [(np.abs(eigen_values[i]), b10[:, i]) for i in range(len(eigen_values))]
    b11.sort(b12 = lambda x: x[0], reverse=True)
    return b11
def fonk6(b11):
    plt.figure(b13 = (10, 10))
    for i in range(16):
        b14 = b11[i][1].reshape(16, 16)
        plt.subplot(4, 4, i+1)
        plt.imshow(b14)
    plt.show()
def fonk7(X_train, variance_ratio):
    b15 = PCA(variance_ratio)
    b16 = b15.fit_transform(X_train)
    return b15, b16
def fonk8(b15, variance_threshold):
    b17 = np.argmax(np.cumsum(b15.explained_variance_ratio_) >= variance_threshold)
    return b17
def fonk9(alpha, X_train_transformed, X, y_true):
    b18 = SGDClassifier(alpha=alpha, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_train_transformed, y_train)
    b19 = b18.predict(X)
    b20 = np.mean(b19 != y_true)
    return b20
def fonk10():
    b1, b2, b3 = fonk1()
    X_testing, b4, X_training, b5, X_validate, b6 = fonk2(b1, b2, b3)
    X_test, X_train, b7, y_test, y_train, b8 = fonk3(X_testing, b4, X_training, b5, X_validate, b6)
    b9 = fonk4(X_train)
    b11 = fonk5(b9)
    fonk6(b11)
    b15, b21 = fonk7(X_train, None)
    b22 = np.cumsum(np.round(b15.explained_variance_ratio_, decimals=3) * 100)
    plt.grid()
    plt.title('PCA Analysis')
    plt.ylabel('% Variance Explained')
    plt.xlabel('Number of Principal Components')
    plt.plot(b22, b23 = 'k')
    plt.show()
    pca_70, b24 = fonk7(X_train, 0.7)
    pca_80, b25 = fonk7(X_train, 0.8)
    pca_90, b26 = fonk7(X_train, 0.9)
    b27 = fonk8(pca_70, 0.7)
    b28 = fonk8(pca_80, 0.8)
    b29 = fonk8(pca_90, 0.9)
    b30 = [0.0001, 0.001, 0.01, 0.1]
    b31 = {}
    for alpha in b30:
        b31[f'k70_{alpha}'] = fonk9(alpha, b24[:, :b27], b7, b8)
        b31[f'k80_{alpha}'] = fonk9(alpha, b25[:, :b28], b7, b8)
        b31[f'k90_{alpha}'] = fonk9(alpha, b26[:, :b29], b7, b8)
    print('Validation Error:')
    print(b31)
    b32 = {}
    for alpha in b30:
        b32[f'k70_{alpha}'] = fonk9(alpha, b24[:, :b27], X_test, y_test)
        b32[f'k80_{alpha}'] = fonk9(alpha, b25[:, :b28], X_test, y_test)
        b32[f'k90_{alpha}'] = fonk9(alpha, b26[:, :b29], X_test, y_test)
    print('Test Error:')
    print(b32)
if b33 = = "__main__":
    fonk10()