import numpy as np
import pandas as pd
from numpy import genfromtxt
from numpy import linalg as LA
from matplotlib import pyplot as plt
b23 = genfromtxt("C:/Users/vyoms/Desktop/dataset_1.csv", delimiter=",")
b2 = b23[1:, :]
b3 = b23[1:, 0]
b4 = b23[1:, 1]
b5 = b23[1:, 2]
plt.scatter(b3[0:30], b4[0:30], b6 = 'o', b29='purple', alpha=0.5)
plt.scatter(b3[30:60], b4[30:60], b6 = 'o', b29='purple', alpha=0.5)
plt.xlabel('b18')
plt.ylabel('b19')
plt.title('b19 vs b18')
plt.show()
def fonk1(x):
    b7 = x.mean(axis=0)
    b8 = np.tile(b7, reps=(x.shape[0], 1))
    b9 = x - b8
    b10 = b9
    b11 = np.cov(b10, rowvar=False)
    b14, b12 = LA.eig(b11)
    b13 = b14.argsort()[::-1]
    b14 = b14[b13]
    b12 = b12[:, b13]
    b15 = np.matmul(b10, b12)
    b16 = {'b2': x,
                   'mean_centered_data': b9,
                   'PC_variance': b14,
                   'loadings': b12,
                   'scores': b15}
    return b16
b17 = fonk1(b2)
b18 = b3
b19 = b4
b20 = len(b18)
b21 = np.mean(b18)
b22 = np.mean(b19)
a1 = 0
a2 = 0
for i in range(b20):
    a1 += (b18[i] - b21) * (b19[i] - b22)
    a2 += (b18[i] - b21) ** 2
b23 = a1 / a2
b24 = b22 - (b23 * b21)
b25 = np.max(b18)
b26 = np.min(b18)
b27 = np.linspace(b26, b25, 1000)
b28 = b24 + b23 * b27
plt.title('Regression Plot')
plt.scatter(b3[0:30], b4[0:30], b6 = 'o', b29='purple', alpha=0.5)
plt.scatter(b3[30:60], b4[30:60], b6 = 'o', b29='purple', alpha=0.5)
plt.plot(b27, b28, b29 = 'orange', linewidth=3)
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.show()
b30 = pd.read_csv('C:/Users/vyoms/Desktop/dataset_1.csv', header=None)
b31 = b30.drop(b30.index[0])
b32 = b31.drop(b30.columns[2], axis=1)
b32 = b32.astype(float)
b33 = b32
b34 = b32.values[0:30, :]
b35 = b32.values[30:, :]
b34 = b34.astype(float)
b35 = b35.astype(float)
b36 = b34.mean(axis=0)
b37 = b35.mean(axis=0)
b38 = b32.mean(axis=0)
b39 = b36.reshape(1, 2)
b39 = np.repeat(b39, 30, axis=0)
b40 = b37.reshape(1, 2)
b40 = np.repeat(b40, 30, axis=0)
b41 = np.zeros((2, 2))
b42 = np.matmul((np.transpose(b34 - b39)), (b34 - b39))
b43 = np.matmul((np.transpose(b35 - b40)), (b35 - b40))
b41 = np.add(b42, b43)
b44 = np.multiply(len(b34), np.outer((b36 - b38), (b36 - b38)))
b45 = np.multiply(len(b35), np.outer((b37 - b38), (b37 - b38)))
b46 = np.add(b44, b45)
e_val, b47 = np.linalg.eig(np.dot(LA.inv(b41), b46))
for e in range(len(e_val)):
    b48 = b47[:, e].reshape(2, 1)
    print(e_val[e].real)
print(b46)
b49 = sum(e_val)
b50 = [(i / b49) * 100 for i in sorted(e_val, reverse=True)]
b50
b51 = np.cumsum(b50)
b51
b52 = [(np.abs(e_val[i]).real, b47[:, i].real) for i in range(len(e_val))]
b52 = sorted(b52, key=lambda k: k[0], reverse=True)
b53 = b52[0][1].reshape(2, 1)
b54 = np.dot(b32, b53)
plt.title('b53 plot')
plt.scatter(b3[0:30], b4[0:30], b6 = 'o', b29='purple', alpha=0.5)
plt.scatter(b3[30:60], b4[30:60], b6 = 'o', b29='purple', alpha=0.5)
plt.plot([0, 100 * b17['loadings'][0, 0]], [0, 100 * b17['loadings'][1, 0]],
         b29 = 'orange', linewidth=3)
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.plot(60 * b53)
plt.show()
b55 = plt.figure()
b56 = b55.add_subplot(1, 1, 1)
b56.set_title('LDA')
b56.plot(b54[0:30], np.zeros(30), b57 = 'None', b6='o', b29='olive')
b56.plot(b54[30:60], np.zeros(30), b57 = 'None', b6='o', b29='purple')
b56.scatter(b3[0:30], b4[0:30], b6 = 'o', b29='purple', alpha=0.5)
b56.scatter(b3[30:60], b4[30:60], b6 = 'o', b29='purple', alpha=0.5)
b55.show()
b58 = b17['scores'] * b17['scores']
b59 = np.sum(b58, axis=0) / b58.shape[0] - 1
print('PCA Variance is:', b59)
b60 = np.sum(b59)
print('The total PCA b59 is:', b60)
b61 = 100 * b17['PC_variance'][0] / sum(b17['PC_variance'])
print("PC1 explains: " + str(round(b61, 2)) + '% b59')
b62 = 100 * b17['PC_variance'][1] / sum(b17['PC_variance'])
print("PC2 explains: " + str(round(b62, 2)) + '% b59')
b63 = np.cov(b17['scores'][:, 0], b17['scores'][:, 1])
print(b63)
b64 = np.var(b17['scores'][:, 0])
print(b64)
b65 = np.var(b17['scores'][:, 1])
print(b65)
b55 = plt.figure()
b56 = b55.add_subplot(1, 1, 1)
b56.set_title('Scree Plot')
b56.scatter(b17['scores'][:, 0], b17['scores'][:, 1], b29 = 'blue')
b55.show()
b66 = b17['b2'].dot(b17['loadings'][0])
plt.title('Regression Plot using PCA axis')
plt.scatter(b66[0:30], b66[0:30], b6 = 'o', b29='purple', alpha=0.5)
plt.scatter(b66[30:60], b66[30:60], b6 = 'o', b29='purple', alpha=0.5)
plt.show()