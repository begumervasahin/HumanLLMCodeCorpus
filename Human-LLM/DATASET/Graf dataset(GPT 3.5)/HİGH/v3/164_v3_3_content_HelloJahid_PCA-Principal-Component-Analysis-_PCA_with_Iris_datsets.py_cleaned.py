import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
b1 = load_iris()
b2 = b1.data
b3 = b1.target
b4 = StandardScaler()
b5 = b4.fit_transform(b2)
b6 = PCA(n_components=2)
b7 = b6.fit_transform(b5)
pc1, b8 = b7[:, 0], b7[:, 1]
setosa_pc1, b9 = pc1[:50], b8[:50]
versicolor_pc1, b10 = pc1[50:100], b8[50:100]
virginica_pc1, b11 = pc1[100:150], b8[100:150]
plt.figure(b12 = (8, 8))
plt.xlabel('Principal Component 1', b13 = 15)
plt.ylabel('Principal Component 2', b13 = 15)
plt.title('2 Component PCA', b13 = 20)
plt.scatter(setosa_pc1, b9, b14 = 'r', label='Iris-setosa')
plt.scatter(versicolor_pc1, b10, b14 = 'g', label='Iris-versicolor')
plt.scatter(virginica_pc1, b11, b14 = 'b', label='Iris-virginica')
plt.legend()
plt.grid()
plt.show()