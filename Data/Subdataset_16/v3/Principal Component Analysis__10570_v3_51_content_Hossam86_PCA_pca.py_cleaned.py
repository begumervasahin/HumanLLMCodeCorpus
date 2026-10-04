import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA as sklearnPCA
def fonk1(b15):
    b1 = pd.read_csv(b15, header=None, sep=',')
    b1.b2 = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
    b1.dropna(b3 = "all", inplace=True)
    return b1
def fonk2(b16):
    b4 = StandardScaler()
    b5 = b4.fit_transform(b16)
    return b5
def fonk3(b5):
    return np.cov(b5.T)
def fonk4(matrix):
    eig_vals, b6 = np.linalg.eig(matrix)
    return eig_vals, b6
def fonk5(b6):
    for ev in b6:
        np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
    print('Eigenvector validation: Everything is ok!')
def fonk6(eig_vals, b6):
    b7 = [(np.abs(eig_vals[i]), b6[:, i]) for i in range(len(eig_vals))]
    b7.sort(b8 = lambda x: x[0], reverse=True)
    return b7
def fonk7(eig_vals):
    b9 = sum(eig_vals)
    b10 = [(i / b9) * 100 for i in sorted(eig_vals, reverse=True)]
    b11 = np.cumsum(b10)
    return b10, b11
def fonk8(b7, b12 = 2):
    b13 = np.hstack([b7[i][1].reshape(4, 1) for i in range(b12)])
    return b13
def fonk9(b5, b13):
    return b5.dot(b13)
def fonk10(b5, b12 = 2):
    b14 = sklearnPCA(b12=b12)
    return b14.fit_transform(b5)
def fonk11():
    b15 = '/media/hossam/MyFiles/MachineLearning/PCA/PCA/IrisDataSet/iris.data'
    b1 = fonk1(b15)
    print("First 5 rows of the dataset:\n", b1.head())
    b16 = b1.iloc[:, 0:4].values
    b17 = b1.iloc[:, 4].values
    b5 = fonk2(b16)
    b18 = fonk3(b5)
    print('Covariance matrix:\n', b18)
    eig_vals, b6 = fonk4(b18)
    print('Eigenvectors:\n', b6)
    print('Eigenvalues:\n', eig_vals)
    fonk5(b6)
    b7 = fonk6(eig_vals, b6)
    print('Eigenvalues in descending order:')
    for eig_val, eig_vec in b7:
        print(eig_val)
    b10, b11 = fonk7(eig_vals)
    b13 = fonk8(b7)
    print('Projection matrix W:\n', b13)
    b19 = fonk9(b5, b13)
    print("Projection by manual PCA:\n", b19[:5])
    b20 = fonk10(b5)
    print("Projection by sklearn PCA:\n", b20[:5])
if b21 = = "__main__":
    fonk11()