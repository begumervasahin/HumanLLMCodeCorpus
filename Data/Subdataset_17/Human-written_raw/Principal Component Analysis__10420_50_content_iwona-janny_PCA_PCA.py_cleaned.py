ï»¿import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = pd.read_csv("Wine.csv", header = 1)
data.columns = ["Alkohol", "Kwas jabÅkowy", "PopiÃ³Å", "ZasadowoÅÄ popioÅu", "Magnez", "CaÅkowita zawartoÅÄ fenoli", "Flawonoidy", "Fenole nieflawonoidowe", "Proantocyjaniny","IntensywnoÅÄ koloru", "OdcieÅ", "Transmitacja", "Prolina","Etykieta"]
print(data)
X, y = data.iloc[:,:-1].values, data.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
sc = StandardScaler()
X_train_stand = sc.fit_transform(X_train)
X_test_stand = sc.transform(X_test)
cov_mat = np.cov(X_train_stand.T)
eigen_val, eigen_vec = np.linalg.eig(cov_mat)
total = sum(eigen_val)
variance_explained = [(j/total) for j in sorted(eigen_val, reverse = True)]
cumulated_variance_explained = np.cumsum(variance_explained)
eigen_pairs = [(np.abs(eigen_val[i]), eigen_vec[:,i])for i in range(len(eigen_val))]
eigen_pairs.sort(key = lambda k: k[0], reverse = True)
projection_matrix = np.hstack((eigen_pairs[0][1][:,np.newaxis],eigen_pairs[1][1][:,np.newaxis]))
Pca = X_train_stand.dot(projection_matrix)
targets = np.unique(y_train)
colors = ["r","g", "b"]
markers = ["s", "x", "o"]
for t, c, m in zip(targets, colors, markers):
    plt.scatter(Pca[y_train==t, 0], Pca[y_train==t,1], c = c, label = t, marker = m)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(loc="lower right")
plt.show()