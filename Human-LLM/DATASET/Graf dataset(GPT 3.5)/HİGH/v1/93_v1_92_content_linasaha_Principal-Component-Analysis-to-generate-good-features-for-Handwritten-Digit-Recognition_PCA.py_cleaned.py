import numpy as np
import pandas as pd
from numpy.linalg import eig
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
b1 = pd.read_csv('./usps.test', header=None)
X_testing, b2 = b1.loc[:, 1:], b1.loc[:, 0]
b3 = pd.read_csv('./usps.train', header=None)
X_training, b4 = b3.loc[:, 1:], b3.loc[:, 0]
b5 = pd.read_csv('./usps.valid', header=None)
X_validate, b6 = b5.loc[:, 1:], b5.loc[:, 0]
b7 = np.array(X_training)
b8 = np.array(X_validate)
b9 = np.array(X_testing)
b10 = np.array(b4)
b11 = np.array(b6)
b12 = np.array(b2)
b13 = np.matmul(b7.transpose(), b7)
eigenValues, b14 = eig(b13)
b15 = [(np.abs(eigenValues[i]), b14[:, i]) for i in range(len(eigenValues))]
b15.sort(b16 = lambda x: x[0], reverse=True)
plt.figure(b17 = (10, 10))
for i in range(16):
    b18 = b15[i][1].reshape(16, 16)
    plt.subplot(4, 4, i+1)
    plt.imshow(b18)
plt.show()
b13 = PCA(n_components=None)
b19 = b13.fit(b7)
b20 = b19.explained_variance_ratio_
b21 = np.cumsum(np.round(-np.sort(-b20), decimals=3) * 100)
plt.grid()
plt.title('PCA Analysis')
plt.ylabel('% Variance')
plt.xlabel('Principal Components')
plt.plot(b21, b22 = 'k')
plt.show()
b23 = PCA(0.7)
b24 = b23.fit_transform(b7)
b25 = PCA(0.8)
b26 = b25.fit_transform(b7)
b27 = PCA(0.9)
b28 = b27.fit_transform(b7)
b29 = np.argmax(np.cumsum(b23.explained_variance_ratio_) >= 0.7)
b30 = np.argmax(np.cumsum(b25.explained_variance_ratio_) >= 0.8)
b31 = np.argmax(np.cumsum(b27.explained_variance_ratio_) >= 0.9)
b32 = [0.0001, 0.001, 0.01, 0.1]
def fonk1(alpha_i, X_newTrain, X, y_true):
    b33 = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, b10)
    b34 = b33.predict(X)
    b35 = np.mean(b34 != y_true)
    return b35
b36 = dict()
for alpha_i in b32:
    b36[f'k70_{alpha_i}'] = fonk1(alpha_i, b24[:, :b29], X_validate, b11)
    b36[f'k80_{alpha_i}'] = fonk1(alpha_i, b26[:, :b30], X_validate, b11)
    b36[f'k90_{alpha_i}'] = fonk1(alpha_i, b28[:, :b31], X_validate, b11)
print('Validation Error:')
print(b36)
b37 = dict()
for alpha_i in b32:
    b37[f'k70_{alpha_i}'] = fonk1(alpha_i, b24[:, :b29], b9, b12)
    b37[f'k80_{alpha_i}'] = fonk1(alpha_i, b26[:, :b30], b9, b12)
    b37[f'k90_{alpha_i}'] = fonk1(alpha_i, b28[:, :b31], b9, b12)
print('Test Error:')
print(b37)