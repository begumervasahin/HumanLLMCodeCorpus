
import numpy as np
import pandas as pd
from numpy.linalg import eig
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
b1 = pd.read_csv('./usps.test',header=None)
X_testing,  b2 = b1.loc[:,1:],  b1.loc[:,0]
b3 = pd.read_csv('./usps.train',header=None)
X_training, b4 = b3.loc[:,1:], b3.loc[:,0]
b5 = pd.read_csv('./usps.valid',header=None)
X_validate, b6 = b5.loc[:,1:], b5.loc[:,0]
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
for i in range(0,16):
    b17 = b15[i][1].reshape(16, 16)
    plt.subplot(4, 4, i+1)
    plt.imshow(b17)
plt.show()
b18 = PCA(n_components=None)
b19 = b18.fit(b7)
b20 = b19.explained_variance_ratio_
b21 = np.cumsum(np.round(-np.sort(-b20), decimals=3) * 100)
plt.grid()
plt.title('PCA Analysis')
plt.ylabel('% Variance')
plt.xlabel('Principal Components')
plt.plot(b21, b22 = 'k')
plt.show()
b23 = PCA(0.7)
b24 = b23.fit(b7)
b25 = b24.transform(b7)
b26 = b23.inverse_transform(b25)
b23 = PCA(0.8)
b24 = b23.fit(b7)
b25 = b24.transform(b7)
b27 = b23.inverse_transform(b25)
b23 = PCA(0.9)
b24 = b23.fit(b7)
b25 = b24.transform(b7)
b28 = b23.inverse_transform(b25)
a1 = 0
a2 = 0
a3 = 0
for i in range (b19.n_components_):
    if b21[i] > 70 and a1 = =0:
        b29 = i
        print('b29 is:', b29)
        a1 = a1+1
    if b21[i] > 80 and a2 = =0:
        b30 = i
        print('b30 is:', b30)
        a2 = a2+1
    if b21[i] > 90 and a3 = =0:
        b31 = i
        print('b31 is:', b31)
        a3 = a3+1
b32 = [0.0001, 0.001, 0.01, 0.1]
def fonk1(alpha_i, X_newTrain, X, b14, features):
    b33 = SGDClassifier(b32=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, b10)
    b34 = b33.predict(X)
    return b34
def fonk2(alpha_i, X_newTrain, X, b14):
    b33 = SGDClassifier(b32=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, b10)
    b34 = b33.predict(X)
    return b34
def fonk3(y_true, b34):
    a4 = 0
    b35 = len(y_true)
    for i in range(0, b35):
        if y_true[i] != b34[i]:
            a4 = a4 + 1
    return (a4/b35)
b36 = dict()
for i in b32:
    b34 = fonk1(i, b26, X_validate, b14, b29)
    b36['b29', i] = fonk3(b11, b34)
for i in b32:
    b34 = fonk1(i, b27, X_validate, b14, b30)
    b36['b30', i] = fonk3(b11, b34)
for i in b32:
    b34 = fonk1(i, b28, X_validate, b14, b31)
    b36['b31', i] = fonk3(b11, b34)
for i in b32:
    b34 = fonk2(i, b7, X_validate, b14)
    b36['k100', i] = fonk3(b11, b34)
print('validation Error\n',b36)
b37 = dict()
for i in b32:
    b34 = fonk1(i, b26, b9, b14, b29)
    b37['b29', i] = fonk3(b12, b34)
for i in b32:
    b34 = fonk1(i, b27, b9, b14, b30)
    b37['b30', i] = fonk3(b12, b34)
for i in b32:
    b34 = fonk1(i, b28, b9, b14, b31)
    b37['b31', i] = fonk3(b12, b34)
for i in b32:
    b34 = fonk2(i, b7, b9, b14)
    b37['b31', i] = fonk3(b12, b34)
print('test Error\n',b37)