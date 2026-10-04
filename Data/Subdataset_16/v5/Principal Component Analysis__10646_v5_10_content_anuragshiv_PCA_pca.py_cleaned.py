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
    b7 = [(np.abs(eigenvalues[i]), b6[:, i]) for i in range(len(eigenvalues))]
    b7.sort(b8 = lambda x: x[0], reverse=True)
    b9 = sum(eigenvalues)
    b10 = np.cumsum([pair[0] for pair in b7]) / b9
    plt.plot(b10, b11 = 'o')
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative sum of eigenvalues / total eigenvalues")
    plt.title("Cumulative Sum of Eigenvalues")
    plt.grid(True)
    plt.show()
    b12 = np.array([pair[1] for pair in b7[:b1]]).T
    b13 = b4.dot(b12)
    b13 = np.real(b13)
    b14 = [f"PC{i+1}" for i in range(b1)] + ['label']
    b15 = pd.DataFrame(b13, columns=b14[:-1])
    b15['label'] = b3
    return b15, b12, b14
def fonk2(b2, model, b14):
    b2 = b2.transpose()
    b3 = b2.iloc[:, -1].values
    b4 = StandardScaler().fit_transform(b2.iloc[:, :-1])
    b13 = b4.dot(model)
    b13 = np.real(b13)
    b15 = pd.DataFrame(b13, columns=b14[:-1])
    b15['label'] = b3
    return b15
if b16 = = '__main__':
    b17 = pd.read_csv('train.csv')
    pca_train_df, pca_model, b14 = fonk1(b17)
    pca_train_df.to_csv("pca_out.csv", b18 = False)
    b19 = pd.read_csv('test.csv')
    b20 = fonk2(b19, pca_model, b14)
    b20.to_csv("pca_test_out.csv", b18 = False)