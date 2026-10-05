import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import eig
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
b1 = pd.read_csv('./usps.test', header=None)
b2 = pd.read_csv('./usps.train', header=None)
b3 = pd.read_csv('./usps.valid', header=None)
X_testing, b4 = b1.iloc[:, 1:], b1.iloc[:, 0]
X_training, b5 = b2.iloc[:, 1:], b2.iloc[:, 0]
X_validate, b6 = b3.iloc[:, 1:], b3.iloc[:, 0]
X_train, X_valid, b7 = np.array(X_training), np.array(X_validate), np.array(X_testing)
y_train, y_valid, b8 = np.array(b5), np.array(b6), np.array(b4)
b9 = np.matmul(X_train.transpose(), X_train)
eigen_values, b10 = eig(b9)
b11 = [(np.abs(eigen_values[i]), b10[:, i]) for i in range(len(eigen_values))]
b11.sort(b12 = lambda x: x[0], reverse=True)
plt.figure(b13 = (10, 10))
for i in range(16):
    b14 = b11[i][1].reshape(16, 16)
    plt.subplot(4, 4, i+1)
    plt.imshow(b14)
plt.show()
b15 = PCA(n_components=None)
b16 = b15.fit(X_train)
b17 = b16.explained_variance_ratio_
b18 = np.cumsum(np.round(b17, decimals=3) * 100)
plt.grid()
plt.title('PCA Analysis')
plt.ylabel('% Variance Explained')
plt.xlabel('Number of Principal Components')
plt.plot(b18, b19 = 'k')
plt.show()
b20 = PCA(0.7)
b21 = b20.fit_transform(X_train)
b22 = PCA(0.8)
b23 = b22.fit_transform(X_train)
b24 = PCA(0.9)
b25 = b24.fit_transform(X_train)
b26 = np.argmax(np.cumsum(b20.explained_variance_ratio_) >= 0.7)
b27 = np.argmax(np.cumsum(b22.explained_variance_ratio_) >= 0.8)
b28 = np.argmax(np.cumsum(b24.explained_variance_ratio_) >= 0.9)
b29 = [0.0001, 0.001, 0.01, 0.1]
def fonk1(alpha_i, X_newTrain, X, y_true):
    b30 = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, y_train)
    b31 = b30.predict(X)
    b32 = np.mean(b31 != y_true)
    return b32
b33 = dict()
for alpha_i in b29:
    b33[f'k70_{alpha_i}'] = fonk1(alpha_i, b21[:, :b26], X_validate, y_valid)
    b33[f'k80_{alpha_i}'] = fonk1(alpha_i, b23[:, :b27], X_validate, y_valid)
    b33[f'k90_{alpha_i}'] = fonk1(alpha_i, b25[:, :b28], X_validate, y_valid)
print('Validation Error:')
print(b33)
b34 = dict()
for alpha_i in b29:
    b34[f'k70_{alpha_i}'] = fonk1(alpha_i, b21[:, :b26], b7, b8)
    b34[f'k80_{alpha_i}'] = fonk1(alpha_i, b23[:, :b27], b7, b8)
    b34[f'k90_{alpha_i}'] = fonk1(alpha_i, b25[:, :b28], b7, b8)
print('Test Error:')
print(b34)