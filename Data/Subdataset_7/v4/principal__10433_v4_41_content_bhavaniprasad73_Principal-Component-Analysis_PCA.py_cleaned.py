import numpy.linalg as LA
from scipy import stats
import pandas as pd
import numpy as np
b1 = pd.read_csv('C:/Users/ebhavaniprasad/Desktop/magic04.txt', header=None)
print("Data structure:", type(b1))
print("Data with class1:")
print(b1.head(3))
b2 = b1[b1.columns[:-1]]
print("Data without class class1:")
print(b2.head(3))
b3 = b2.T
print("Transposed data:")
print(b3)
b3["sum"] = b3.sum(b4 = 1)
print("Sum of each row:")
print(b3["sum"])
b5 = len(b2.columns)
b6 = b3["sum"] / b5
print("Mean:", b6)
b7 = (b2 - b6) / b2.std()
b8 = np.cov(b7, bias=True, rowvar=False)
eigen_values, b9 = LA.eig(b8)
b10 = eigen_values.argsort()[::-1]
b11 = eigen_values[b10]
b12 = b9[:, b10]
b13 = b12[:, :2]
b14 = b7.dot(b13)
def fonk1(data, threshold):
    b15 = np.cov(data, bias=True, rowvar=False)
    eigenvalues, b16 = LA.eig(b15)
    b10 = eigenvalues.argsort()[::-1]
    b17 = eigenvalues[b10]
    b18 = b16[:, b10]
    b19 = eigenvalues.sum()
    b20 = np.cumsum((b17 / b19) * 100)
    b21 = np.argmax(b20 >= threshold) + 1
    b22 = b18[:, :b21]
    b23 = data.dot(b22)
    return b23, b17, b21
b23, eigenvalues, b21 = fonk1(b2, 95)
b24 = np.cov(b23, bias=True, rowvar=False)
b25 = np.trace(b24)
b26 = eigenvalues[:b21].sum()
print("Covariance of the projected data points:", b25)
print("Sum of the eigenvalues corresponding to the principal vectors:", b26)