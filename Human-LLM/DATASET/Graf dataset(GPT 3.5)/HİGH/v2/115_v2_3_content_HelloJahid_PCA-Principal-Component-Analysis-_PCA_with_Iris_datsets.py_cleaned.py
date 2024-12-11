
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
b1 = load_iris()
b2 = b1.data
b3 = b1.target
b4 = StandardScaler()
b5 = b4.fit_transform(b2)
b6 = PCA(n_components=2)
b7 = b6.fit_transform(b5)
b8 = b7[:, 0]
b9 = b7[:, 1]
b10 = b8[:50]
b11 = b9[:50]
b12 = b8[50:100]
b13 = b9[50:100]
b14 = b8[100:150]
b15 = b9[100:150]
plt.figure(b16 = (8, 8))
plt.xlabel('Principal Component 1', b17 = 15)
plt.ylabel('Principal Component 2', b17 = 15)
plt.title('2 Component PCA', b17 = 20)
plt.scatter(b10, b11, b18 = 'r', label='Iris-setosa')
plt.scatter(b12, b13, b18 = 'g', label='Iris-versicolor')
plt.scatter(b14, b15, b18 = 'b', label='Iris-virginica')
plt.legend()
plt.grid()
plt.show()