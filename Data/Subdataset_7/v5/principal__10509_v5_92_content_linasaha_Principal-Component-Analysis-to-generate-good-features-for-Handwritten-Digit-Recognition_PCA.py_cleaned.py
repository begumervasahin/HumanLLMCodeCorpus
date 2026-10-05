import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
def fonk1():
    b1 = pd.read_csv('./usps.test', header=None)
    b2 = pd.read_csv('./usps.train', header=None)
    b3 = pd.read_csv('./usps.valid', header=None)
    X_testing, b4 = b1.loc[:, 1:], b1.loc[:, 0]
    X_training, b5 = b2.loc[:, 1:], b2.loc[:, 0]
    X_validate, b6 = b3.loc[:, 1:], b3.loc[:, 0]
    X_train, X_valid, b7 = np.array(X_training), np.array(X_validate), np.array(X_testing)
    y_train, y_valid, b8 = np.array(b5), np.array(b6), np.array(b4)
    return X_train, y_train, X_valid, y_valid, b7, b8
def fonk2(X):
    b9 = np.matmul(X.transpose(), X)
    eigenValues, b10 = np.linalg.eig(b9)
    b11 = [(np.abs(eigenValues[i]), b10[:, i]) for i in range(len(eigenValues))]
    b11.sort(b12 = lambda x: x[0], reverse=True)
    return b11
def fonk3(b11):
    for i in range(0, 16):
        b13 = b11[i][1].reshape(16, 16)
        plt.subplot(4, 4, i + 1)
        plt.imshow(b13)
    plt.show()
def fonk4(X_train):
    b14 = PCA(n_components=None)
    b15 = b14.fit(X_train)
    b16 = b15.explained_variance_ratio_
    b17 = np.cumsum(np.round(-np.sort(-b16), decimals=3) * 100)
    plt.grid()
    plt.title('PCA Analysis')
    plt.ylabel('% Variance')
    plt.xlabel('Principal Components')
    plt.plot(b17, b18 = 'k')
    plt.show()
    return b14
def fonk5(b14):
    b19 = b14.explained_variance_ratio_[b14.explained_variance_ratio_.cumsum() < 0.7].shape[0]
    b20 = b14.explained_variance_ratio_[b14.explained_variance_ratio_.cumsum() < 0.8].shape[0]
    b21 = b14.explained_variance_ratio_[b14.explained_variance_ratio_.cumsum() < 0.9].shape[0]
    return b19, b20, b21
def fonk6(X, b14, k):
    b22 = b14.fit(X)
    b23 = b22.inverse_transform(b22.transform(X))
    return b23, b22
def fonk7(alpha, X_train, y_train):
    b24 = SGDClassifier(alpha=alpha, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty)
    b24.fit(X_train, y_train)
    return b24
def fonk8(b24, X):
    b25 = b24.predict(X)
    return b25
def fonk9(y_true, b25):
    b26 = np.sum(y_true != b25)
    return b26 / len(y_true)
def fonk10(X_validate, b6, b31, X_reduced, b22, b32, b11):
    b27 = {}
    for alpha in b31:
        for i, X_red in enumerate(X_reduced):
            b24 = fonk7(alpha, X_red, y_train)
            b25 = fonk8(b24, b22.inverse_transform(X_validate[:, :b32[i]]))
            b28 = fonk9(b6, b25)
            b27[f'k{b32[i]}', alpha] = b28
    print('Validation Error:', b27)
def fonk11(b7, b8, b31, X_reduced, b22, b32):
    b29 = {}
    for alpha in b31:
        for i, X_red in enumerate(X_reduced):
            b24 = fonk7(alpha, X_red, y_train)
            b25 = fonk8(b24, b22.inverse_transform(b7[:, :b32[i]]))
            b28 = fonk9(b8, b25)
            b29[f'k{b32[i]}', alpha] = b28
    print('Test Error:', b29)
if b30 = = "__main__":
    X_train, y_train, X_validate, b6, b7, b8 = fonk1()
    b11 = fonk2(X_train)
    fonk3(b11)
    b14 = fonk4(X_train)
    b19, b20, b21 = fonk5(b14)
    X_reduced, b22 = fonk6(X_train, b14, [b19, b20, b21])
    b31 = [0.0001, 0.001, 0.01, 0.1]
    b32 = [b19, b20, b21]
    fonk10(X_validate, b6, b31, X_reduced, b22, b32, b11)
    fonk11(b7, b8, b31, X_reduced, b22, b32)