import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def fonk1(b2, b1 = 150):
    b2 = b2.transpose()
    b3 = b2.iloc[:, -1].values
    b4 = StandardScaler().fit_transform(b2.iloc[:, :-1])
    b5 = np.cov(b4.T)
    eigenvalues, b6 = np.linalg.eig(b5)
    b7 = sorted([(np.abs(eigenvalues[i]), b6[:, i]) for i in range(len(eigenvalues))], key=lambda x: x[0], reverse=True)
    b8 = sum(eigenvalues)
    b9 = np.cumsum([eigen[0] for eigen in b7]) / b8
    plt.plot(b9, b10 = 'o')
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Sum of Eigenvalues / Total Eigenvalue")
    plt.title("PCA Cumulative Sum of Eigenvalues")
    plt.show()
    b11 = np.array([b7[i][1] for i in range(b1)]).T
    b12 = b4.dot(b11)
    b12 = np.real(b12)
    b13 = [f"PC{i+1}" for i in range(b1)]
    b14 = pd.DataFrame(b12, columns=b13)
    b14['label'] = b3
    return b14, b11, b13
def fonk2(b2, model, b13):
    b2 = b2.transpose()
    b3 = b2.iloc[:, -1].values
    b4 = StandardScaler().fit_transform(b2.iloc[:, :-1])
    b12 = b4.dot(model)
    b12 = np.real(b12)
    b14 = pd.DataFrame(b12, columns=b13)
    b14['label'] = b3
    return b14
if b15 = = '__main__':
    b16 = pd.read_csv('train.csv')
    pca_train_df, pca_model, b17 = fonk1(b16)
    pca_train_df.to_csv("pca_out.csv", b18 = False)
    b19 = pd.read_csv('test.csv')
    b20 = fonk2(b19, pca_model, b17)
    b20.to_csv("pca_test_out.csv", b18 = False)