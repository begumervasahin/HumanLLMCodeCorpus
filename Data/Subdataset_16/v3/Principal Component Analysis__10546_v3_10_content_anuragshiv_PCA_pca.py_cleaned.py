import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def fonk1(df, b1 = 150):
    b2 = df.transpose()
    b3 = b2.iloc[:, -1].values
    b4 = StandardScaler().fit_transform(b2.iloc[:, :-1])
    b5 = np.cov(b4.T)
    eigenvalues, b6 = np.linalg.eig(b5)
    b7 = sorted([(np.abs(eigenvalues[i]), b6[:, i]) for i in range(len(eigenvalues))],
                    b8 = lambda x: x[0], reverse=True)
    b9 = sum(eigenvalues)
    b10 = np.cumsum([eigen[0] for eigen in b7]) / b9
    plt.plot(b10, b11 = 'o')
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Sum of Eigenvalues / Total Eigenvalue")
    plt.title("PCA Cumulative Sum of Eigenvalues")
    plt.show()
    b12 = np.array([b7[i][1] for i in range(b1)]).T
    b13 = b4.dot(b12)
    b13 = np.real(b13)
    b14 = [f"PC{i+1}" for i in range(b1)]
    b15 = pd.DataFrame(b13, columns=b14)
    b15['label'] = b3
    return b15, b12, b14
def fonk2(df, model, b14):
    b2 = df.transpose()
    b3 = b2.iloc[:, -1].values
    b4 = StandardScaler().fit_transform(b2.iloc[:, :-1])
    b13 = b4.dot(model)
    b13 = np.real(b13)
    b15 = pd.DataFrame(b13, columns=b14)
    b15['label'] = b3
    return b15
if b16 = = '__main__':
    b17 = pd.read_csv('train.csv')
    pca_train_df, pca_model, b18 = fonk1(b17)
    pca_train_df.to_csv("pca_out.csv", b19 = False)
    b20 = pd.read_csv('test.csv')
    b21 = fonk2(b20, pca_model, b18)
    b21.to_csv("pca_test_out.csv", b19 = False)