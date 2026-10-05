
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
b1 = pd.read_csv('./usps.test', header=None)
X_testing, b2 = b1.loc[:, 1:], b1.loc[:, 0]
b3 = pd.read_csv('./usps.train', header=None)
X_training, b4 = b3.loc[:, 1:], b3.loc[:, 0]
b5 = pd.read_csv('./usps.valid', header=None)
X_validate, b6 = b5.loc[:, 1:], b5.loc[:, 0]
X_train, X_valid, b7 = np.array(X_training), np.array(X_validate), np.array(X_testing)
y_train, y_valid, b8 = np.array(b4), np.array(b6), np.array(b2)
b9 = np.matmul(X_train.transpose(), X_train)
eigenValues, b10 = np.linalg.eig(b9)
b11 = [(np.abs(eigenValues[i]), b10[:, i]) for i in range(len(eigenValues))]
b11.sort(b12 = lambda x: x[0], reverse=True)
for i in range(0, 16):
    b13 = b11[i][1].reshape(16, 16)
    plt.subplot(4, 4, i + 1)
    plt.imshow(b13)
plt.show()
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
b19 = PCA(0.7)
b20 = PCA(0.8)
b21 = PCA(0.9)
k70, k80, b22 = b19.fit(X_train).n_components_, b20.fit(X_train).n_components_, b21.fit(X_train).n_components_
b23 = b19.fit(X_train)
b24 = b23.inverse_transform(b23.transform(X_train))
b25 = b20.fit(X_train)
b26 = b25.inverse_transform(b25.transform(X_train))
b27 = b21.fit(X_train)
b28 = b27.inverse_transform(b27.transform(X_train))
b29 = [0.0001, 0.001, 0.01, 0.1]
def fonk1(alpha_i, X_newTrain, X, b10, features):
    b30 = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, y_train)
    b31 = b30.predict(X)
    return b31
def fonk2(alpha_i, X_newTrain, X, b10):
    b30 = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, y_train)
    b31 = b30.predict(X)
    return b31
def fonk3(y_true, b31):
    a1 = 0
    b32 = len(y_true)
    for i in range(0, b32):
        if y_true[i] != b31[i]:
            a1 += 1
    return (a1 / b32)
b33 = dict()
for alpha in b29:
    b31 = fonk1(alpha, b24, X_validate, b10, k70)
    b33['k70', alpha] = fonk3(y_valid, b31)
for alpha in b29:
    b31 = fonk1(alpha, b26, X_validate, b10, k80)
    b33['k80', alpha] = fonk3(y_valid, b31)
for alpha in b29:
    b31 = fonk1(alpha, b28, X_validate, b10, b22)
    b33['b22', alpha] = fonk3(y_valid, b31)
for alpha in b29:
    b31 = fonk2(alpha, X_train, X_validate, b10)
    b33['k100', alpha] = fonk3(y_valid, b31)
print('Validation Error:', b33)
b34 = dict()
for alpha in b29:
    b31 = fonk1(alpha, b24, b7, b10, k70)
    b34['k70', alpha] = fonk3(b8, b31)
for alpha in b29:
    b31 = fonk1(alpha, b26, b7, b10, k80)
    b34['k80', alpha] = fonk3(b8, b31)
for alpha in b29:
    b31 = fonk1(alpha, b28, b7, b10, b22)
    b34['b22', alpha] = fonk3(b8, b31)
for alpha in b29:
    b31 = fonk2(alpha, X_train, b7, b10)
    b34['k100', alpha] = fonk3(b8, b31)
print('Test Error:', b34)