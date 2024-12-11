
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
b1 = load_iris()
b2 = b1.data
b3 = b1.target
b2 = StandardScaler().fit_transform(b2)
b4 = PCA(n_components=2)
b5 = b4.fit_transform(b2)
b6 = b5[:, 0]
b7 = b5[:, 1]
b8 = b6[:50]
b9 = b7[:50]
b10 = b6[50:100]
b11 = b7[50:100]
b12 = b6[100:150]
b13 = b7[100:150]
plt.figure(b14 = (8, 8))
plt.xlabel('Principal Component 1', b15 = 15)
plt.ylabel('Principal Component 2', b15 = 15)
plt.title('2 Component PCA', b15 = 20)
plt.scatter(b8, b9, b16 = 'r', label='Iris-setosa')
plt.scatter(b10, b11, b16 = 'g', label='Iris-versicolor')
plt.scatter(b12, b13, b16 = 'b', label='Iris-virginica')
plt.legend()
plt.grid()
plt.show()