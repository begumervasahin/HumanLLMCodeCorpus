import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = pd.read_csv("Wine.csv", header=1)
data.columns = [
    "Alkohol", "Kwas jabÅkowy", "PopiÃ³Å", "ZasadowoÅÄ popioÅu", "Magnez",
    "CaÅkowita zawartoÅÄ fenoli", "Flawonoidy", "Fenole nieflawonoidowe",
    "Proantocyjaniny", "IntensywnoÅÄ koloru", "OdcieÅ", "Transmitacja",
    "Prolina", "Etykieta"
]
print(data.head())
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
cov_matrix = np.cov(X_train_scaled.T)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
total_variance = sum(eigenvalues)
variance_explained = [(i / total_variance) for i in sorted(eigenvalues, reverse=True)]
cumulative_variance_explained = np.cumsum(variance_explained)
eigen_pairs = [(np.abs(eigenvalues[i]), eigenvectors[:, i]) for i in range(len(eigenvalues))]
eigen_pairs.sort(key=lambda x: x[0], reverse=True)
projection_matrix = np.hstack((
    eigen_pairs[0][1][:, np.newaxis],
    eigen_pairs[1][1][:, np.newaxis]
))
X_train_pca = X_train_scaled.dot(projection_matrix)
targets = np.unique(y_train)
colors = ["r", "g", "b"]
markers = ["s", "x", "o"]
for target, color, marker in zip(targets, colors, markers):
    plt.scatter(
        X_train_pca[y_train == target, 0],
        X_train_pca[y_train == target, 1],
        c=color, label=target, marker=marker
    )
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(loc="lower right")
plt.show()