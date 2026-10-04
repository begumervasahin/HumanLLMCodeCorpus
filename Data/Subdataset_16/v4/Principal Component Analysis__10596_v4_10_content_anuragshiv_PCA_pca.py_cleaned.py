import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def fonk1(b1):
    b1 = b1.transpose()
    b2 = list(b1.iloc[:, -1])
    b3 = StandardScaler().fit_transform(b1.iloc[:, :-1])
    b4 = np.cov(b3.T)
    eigen_values, b5 = np.linalg.eig(b4)
    b6 = [(np.abs(eigen_values[i]), b5[:, i]) for i in range(len(eigen_values))]
    b6.sort(b7 = lambda x: x[0], reverse=True)
    b8 = sum(eigen_values)
    b9 = np.cumsum([eigen[0] for eigen in b6]) / b8
    plt.plot(b9, b10 = 'o')
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative sum of eigenvalues / total eigenvalues")
    plt.show()
    b11 = np.array([eigen[1] for eigen in b6[:150]]).T
    b12 = b3.dot(b11)
    b12 = np.real(b12)
    b13 = pd.DataFrame(b12)
    b13['label'] = b2
    return b13, b11, [f"PC{i+1}" for i in range(150)] + ['label']
def fonk2(b1, model, b17):
    b1 = b1.transpose()
    b2 = list(b1.iloc[:, -1])
    b3 = StandardScaler().fit_transform(b1.iloc[:, :-1])
    b14 = b3.dot(model)
    b14 = np.real(b14)
    b13 = pd.DataFrame(b14, columns=b17[:-1])
    b13['label'] = b2
    return b13
if b15 = = '__main__':
    b16 = pd.read_csv('train.csv')
    pca_train_df, model, b17 = fonk1(b16)
    pca_train_df.to_csv("pca_out.csv", b18 = False)
    b19 = pd.read_csv('test.csv')
    b20 = fonk2(b19, model, b17)
    b20.to_csv("pca_test_out.csv", b18 = False)