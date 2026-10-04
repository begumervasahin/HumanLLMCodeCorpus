import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
b1 = pd.read_csv("Wine.csv", header=1)
b1.b2 = ["Alkohol", "Kwas jabÅkowy", "PopiÃ³Å", "ZasadowoÅÄ popioÅu", "Magnez", "CaÅkowita zawartoÅÄ fenoli", "Flawonoidy", "Fenole nieflawonoidowe", "Proantocyjaniny", "IntensywnoÅÄ koloru", "OdcieÅ", "Transmitacja", "Prolina", "Etykieta"]
print(b1)
X, b3 = b1.iloc[:, :-1].values, b1.iloc[:, -1].values
X_train, X_test, b20, b4 = train_test_split(X, b3, test_size=0.3)
b5 = StandardScaler()
b6 = b5.fit_transform(X_train)
b7 = b5.transform(X_test)
b8 = np.cov(b6.T)
eigen_val, b9 = np.linalg.eig(b8)
b10 = sum(eigen_val)
b11 = [(j / b10) for j in sorted(eigen_val, reverse=True)]
b12 = np.cumsum(b11)
b13 = [(np.abs(eigen_val[i]), b9[:, i]) for i in range(len(eigen_val))]
b13.sort(b14 = lambda k: k[0], reverse=True)
b15 = np.hstack((b13[0][1][:, np.newaxis], b13[1][1][:, np.newaxis]))
b16 = b6.dot(b15)
b17 = np.unique(b20)
b18 = ["r", "g", "b"]
b19 = ["s", "x", "o"]
for t, c, m in zip(b17, b18, b19):
    plt.scatter(b16[b20 = = t, 0], b16[b20 == t, 1], c=c, label=t, marker=m)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(b21 = "lower right")
plt.show()