import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def fonk1(filepath):
    b1 = pd.read_csv(filepath, header=1)
    b1.b2 = [
        "Alkohol", "Kwas jabÅkowy", "PopiÃ³Å", "ZasadowoÅÄ popioÅu",
        "Magnez", "CaÅkowita zawartoÅÄ fenoli", "Flawonoidy",
        "Fenole nieflawonoidowe", "Proantocyjaniny", "IntensywnoÅÄ koloru",
        "OdcieÅ", "Transmitacja", "Prolina", "Etykieta"
    ]
    return b1
def fonk2(b1):
    b3 = b1.iloc[:, :-1].values
    b4 = b1.iloc[:, -1].values
    return train_test_split(b3, b4, b5 = 0.3, random_state=42)
def fonk3(X_train, X_test):
    b6 = StandardScaler()
    b7 = b6.fit_transform(X_train)
    b8 = b6.transform(X_test)
    return b7, b8
def fonk4(b7):
    b9 = np.cov(b7.T)
    eigenvalues, b10 = np.linalg.eig(b9)
    b11 = [(np.abs(eigenvalues[i]), b10[:, i]) for i in range(len(eigenvalues))]
    b11.sort(b12 = lambda x: x[0], reverse=True)
    b13 = np.hstack((b11[0][1][:, np.newaxis], b11[1][1][:, np.newaxis]))
    b14 = b7.dot(b13)
    b15 = sum(eigenvalues)
    b16 = [(i / b15) for i in sorted(eigenvalues, reverse=True)]
    b17 = np.cumsum(b16)
    return b14, b16, b17
def fonk5(b14, b22):
    b18 = np.unique(b22)
    b19 = ["r", "g", "b"]
    b20 = ["s", "x", "o"]
    plt.figure(b21 = (10, 6))
    for target, b23, b25 in zip(b18, b19, b20):
        plt.scatter(
            b14[b22 = = target, 0],
            b14[b22 = = target, 1],
            b23 = b23,
            b24 = target,
            b25 = b25
        )
    plt.xlabel("Principal Component 1 (PC1)")
    plt.ylabel("Principal Component 2 (PC2)")
    plt.legend(b26 = "lower right")
    plt.title("PCA of Wine Dataset")
    plt.show()
def fonk6():
    b1 = fonk1("Wine.csv")
    print(b1.head())
    X_train, X_test, b22, b27 = fonk2(b1)
    b7, b8 = fonk3(X_train, X_test)
    b14, b16, b17 = fonk4(b7)
    fonk5(b14, b22)
if b28 = = "__main__":
    fonk6()