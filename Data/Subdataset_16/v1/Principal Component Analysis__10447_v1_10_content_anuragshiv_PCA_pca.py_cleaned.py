import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def fonk1(b2, b1 = 150):
    b2 = b2.transpose()
    b3 = b2.iloc[:, -1].values
    b4 = StandardScaler().fit_transform(b2.iloc[:, :-1])
    b5 = np.cov(b4.T)
    eigen_val, b6 = np.linalg.eig(b5)
    b7 = [(np.abs(eigen_val[i]), b6[:, i]) for i in range(len(eigen_val))]
    b7.sort(b8 = lambda x: x[0], reverse=True)
    b9 = sum(eigen_val)
    b10 = [sum(eigen_val[:i+1]) / b9 for i in range(len(eigen_val))]
    plt.plot(b10, b11 = 'o')
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Sum of Eigenvalues / Total Eigenvalue")
    plt.show()
    b12 = np.array([b7[i][1] for i in range(b1)]).T
    b13 = b4.dot(b12)
    b13 = np.real(b13)
    b14 = [f"PC{i+1}" for i in range(b1)]
    b15 = pd.DataFrame(b13, columns=b14)
    b15['b3'] = b3
    return b15, b12, b14
def fonk2(b2, model, b14):
    b2 = b2.transpose()
    b3 = b2.iloc[:, -1].values
    b4 = StandardScaler().fit_transform(b2.iloc[:, :-1])
    b13 = b4.dot(model)
    b13 = np.real(b13)
    b15 = pd.DataFrame(b13, columns=b14)
    b15['b3'] = b3
    return b15
if b16 = = '__main__':
    b17 = pd.read_csv('b17.csv')
    df_train, model, b14 = fonk1(b17)
    df_train.to_csv("pca_out.csv", b18 = False)
    b19 = pd.read_csv('b19.csv')
    b20 = fonk2(b19, model, b14)
    b20.to_csv("pca_test_out.csv", b18 = False)