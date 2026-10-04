import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
b1 = pd.read_csv("Wine.csv", header=1)
b1.b2 = ["Alkohol", "Kwas jabÅkowy", "PopiÃ³Å", "ZasadowoÅÄ popioÅu", "Magnez", "CaÅkowita zawartoÅÄ fenoli", "Flawonoidy", "Fenole nieflawonoidowe", "Proantocyjaniny", "IntensywnoÅÄ koloru", "OdcieÅ", "Transmitacja", "Prolina", "Etykieta"]
print(b1.head())
b3 = b1.iloc[:, :-1].values
b4 = b1.iloc[:, -1].values
X_train, X_test, b22, b5 = train_test_split(b3, b4, test_size=0.3, random_state=42)
b6 = StandardScaler()
b7 = b6.fit_transform(X_train)
b8 = b6.transform(X_test)
b9 = np.cov(b7.T)
eigenvalues, b10 = np.linalg.eig(b9)
b11 = sum(eigenvalues)
b12 = [(i / b11) for i in sorted(eigenvalues, reverse=True)]
b13 = np.cumsum(b12)
b14 = [(np.abs(eigenvalues[i]), b10[:, i]) for i in range(len(eigenvalues))]
b14.sort(b15 = lambda x: x[0], reverse=True)
b16 = np.hstack((b14[0][1][:, np.newaxis], b14[1][1][:, np.newaxis]))
b17 = b7.dot(b16)
b18 = np.unique(b22)
b19 = ["r", "g", "b"]
b20 = ["s", "x", "o"]
plt.figure(b21 = (10, 6))
for target, color, marker in zip(b18, b19, b20):
    plt.scatter(b17[b22 = = target, 0], b17[b22 == target, 1], color=color, label=target, marker=marker)
plt.xlabel("Principal Component 1 (PC1)")
plt.ylabel("Principal Component 2 (PC2)")
plt.legend(b23 = "lower right")
plt.title("PCA of Wine Dataset")
plt.show()