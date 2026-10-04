import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
b1 = pd.read_csv("Wine.csv", header=1)
b1.b2 = ["Alkohol", "Kwas jabÅkowy", "PopiÃ³Å", "ZasadowoÅÄ popioÅu", "Magnez",
                "CaÅkowita zawartoÅÄ fenoli", "Flawonoidy", "Fenole nieflawonoidowe",
                "Proantocyjaniny", "IntensywnoÅÄ koloru", "OdcieÅ", "Transmitacja",
                "Prolina", "Etykieta"]
print(b1.head())
b3 = b1.iloc[:, :-1].values
b4 = b1.iloc[:, -1].values
X_train, X_test, b21, b5 = train_test_split(b3, b4, test_size=0.3, random_state=0)
b6 = StandardScaler()
b7 = b6.fit_transform(X_train)
b8 = b6.transform(X_test)
b9 = np.cov(b7.T)
eigen_val, b10 = np.linalg.eig(b9)
b11 = sum(eigen_val)
b12 = [(i / b11) for i in sorted(eigen_val, reverse=True)]
b13 = np.cumsum(b12)
b14 = [(np.abs(eigen_val[i]), b10[:, i]) for i in range(len(eigen_val))]
b14.sort(b15 = lambda k: k[0], reverse=True)
b16 = np.hstack((b14[0][1][:, np.newaxis], b14[1][1][:, np.newaxis]))
b17 = b7.dot(b16)
b18 = np.unique(b21)
b19 = ["r", "g", "b"]
b20 = ["s", "x", "o"]
for t, c, m in zip(b18, b19, b20):
    plt.scatter(b17[b21 = = t, 0], b17[b21 == t, 1], c=c, label=t, marker=m)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(b22 = "lower right")
plt.show()