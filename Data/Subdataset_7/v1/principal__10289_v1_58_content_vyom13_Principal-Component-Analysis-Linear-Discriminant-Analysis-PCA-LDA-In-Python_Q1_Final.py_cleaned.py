import numpy as np
from numpy import genfromtxt
from numpy import linalg as lg
from numpy import linalg as LA
from matplotlib import pyplot as plt
import pandas as pd
b1 = genfromtxt("C:/Users/vyoms/Desktop/dataset_1.csv", delimiter=",")
b2 = b1[1:, :]
b3 = b1[1:, 0]
b4 = b1[1:, 1]
plt.scatter(b3[0:30], b4[0:30], b5 = 'o', b17='purple', alpha=0.5)
plt.scatter(b3[30:60], b4[30:60], b5 = 'o', b17='purple', alpha=0.5)
plt.xlabel('V1')
plt.ylabel('V2')
plt.title('V2 vs V1')
plt.show()
def fonk1(x):
    b6 = x.mean(axis=0)
    b7 = np.tile(b6, reps=(x.shape[0], 1))
    b8 = x - b7
    b9 = b8
    b10 = np.cov(b9, rowvar=False)
    b13, b11 = LA.eig(b10)
    b12 = b13.argsort()[::-1]
    b13 = b13[b12]
    b11 = b11[:, b12]
    b14 = np.matmul(b9, b11)
    b15 = {'b2': x,
                  'mean_centered_data': b8,
                  'PC_variance': b13,
                  'loadings': b11,
                  'scores': b14}
    return b15
b16 = fonk1(b2)
plt.title('Regression Plot')
plt.scatter(b3[0:30], b4[0:30], b5 = 'o', b17='purple', alpha=0.5)
plt.scatter(b3[30:60], b4[30:60], b5 = 'o', b17='purple', alpha=0.5)
plt.plot([0, 100 * b16['loadings'][0, 0]], [0, 100 * b16['loadings'][1, 0]],
         b17 = 'orange', linewidth=3)
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.show()
b18 = pd.read_csv('C:/Users/vyoms/Desktop/dataset_1.csv', header=None)
b19 = b18.drop(b18.index[0])
b20 = b19.drop(b18.columns[2], axis=1)
b20 = b20.astype(float)
b21 = b20
b22 = b20.values[0:30, :]
b23 = b20.values[30:, :]
b22 = b22.astype(float)
b23 = b23.astype(float)
b24 = b22.mean(axis=0)
b25 = b23.mean(axis=0)
b26 = b20.mean(axis=0)
b27 = b24.reshape(1, 2)
b27 = np.repeat(b27, 30, axis=0)
b28 = b25.reshape(1, 2)
b28 = np.repeat(b28, 30, axis=0)
b29 = np.zeros((2, 2))
b30 = np.zeros((2, 2))
b30 = np.matmul((np.transpose(b22 - b27)), (b22 - b27))
b31 = np.zeros((2, 2))
b31 = np.matmul((np.transpose(b23 - b28)), (b23 - b28))
b29 = np.add(b30, b31)
b32 = np.multiply(len(b22), np.outer((b24 - b26), (b24 - b26)))
b33 = np.multiply(len(b23), np.outer((b25 - b26), (b25 - b26)))
b34 = np.add(b32, b33)
e_val, b35 = np.linalg.eig(np.dot(lg.inv(b29), b34))
for e in range(len(e_val)):
    b36 = b35[:, e].reshape(2, 1)
    print(e_val[e].real)
print(b34)
b37 = sum(e_val)
b38 = [(i / b37) * 100 for i in sorted(e_val, reverse=True)]
b38
b39 = np.cumsum(b38)
b39
b40 = [(np.abs(e_val[i]).real, b35[:, i].real) for i in range(len(e_val))]
b40 = sorted(b40, key=lambda k: k[0], reverse=True)
b41 = b40[0][1].reshape(2, 1)
b42 = np.dot(b20, b41)
plt.title('b41 plot')
plt.scatter(b3[0:30], b4[0:30], b5 = 'o', b17='purple', alpha=0.5)
plt.scatter(b3[30:60], b4[30:60], b5 = 'o', b17='purple', alpha=0.5)
plt.plot([0, 100 * b16['loadings'][0, 0]], [0, 100 * b16['loadings'][1, 0]],
         b17 = 'orange', linewidth=3)
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.plot(60 * b41)
plt.show()
b43 = plt.figure()
b44 = b43.add_subplot(1, 1, 1)
b44.set_title('LDA')
b44.plot(b42[0:30], np.zeros(30), b45 = 'None', b5='o', b17='olive')
b44.plot(b42[30:60], np.zeros(30), b45 = 'None', b5='o', b17='purple')
b44.scatter(b3[0:30], b4[0:30], b5 = 'o', b17='purple', alpha=0.5)
b44.scatter(b3[30:60], b4[30:60], b5 = 'o', b17='purple', alpha=0.5)
b43.show()
b16 = fonk1(b2)
b46 = b16['scores'] * b16['scores']
b47 = np.sum(b46, axis=0) / b46.shape[0] - 1
print('PCA Variance is :', b47)
b48 = np.sum(b47)
print('The total PCA varinace is :', b48)
b49 = 100 * b16['PC_variance'][0] / sum(b16['PC_variance'])
print("PC1 explains: " + str(round(b49, 2)) + '% b47\n')
b50 = 100 * b16['PC_variance'][1] / sum(b16['PC_variance'])
print("PC2 explains: " + str(round(b50, 2)) + '% b47\n')
b51 = np.cov(b16['scores'][:, 0], b16['scores'][:, 1])
print(b51)
b52 = np.var(b16['scores'][:, 0])
print(b52)
b53 = np.var(b16['scores'][:, 1])
print(b53)
b43 = plt.figure()
b44 = b43.add_subplot(1, 1, 1)
b44.set_title('scree plot')
b44.scatter(b16['scores'][:, 0], b16['scores'][:, 1], b17 = 'blue')
b43.show()
b54 = b16['b2'].dot(b16['loadings'][0])
plt.title('Regression Plot')
plt.scatter(b54[0:30], b54[0:30], b5 = 'o', b17='purple', alpha=0.5)
plt.scatter(b54[30:60], b54[30:60], b5 = 'o', b17='purple', alpha=0.5)
plt.show()