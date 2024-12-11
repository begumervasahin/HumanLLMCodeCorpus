
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
b1 = load_iris()
b2 = b1.data
b3 = b1.target
b4 = StandardScaler().fit_transform(b2)
b5 = PCA(n_components=2)
b6 = b5.fit_transform(b4)
pc1, b7 = b6[:, 0], b6[:, 1]
pc1_class0, b8 = pc1[:50], b7[:50]
pc1_class1, b9 = pc1[50:100], b7[50:100]
pc1_class2, b10 = pc1[100:150], b7[100:150]
plt.figure(b11 = (8, 8))
plt.xlabel('Principal Component 1', b12 = 15)
plt.ylabel('Principal Component 2', b12 = 15)
plt.title('2 Component PCA', b12 = 20)
plt.scatter(pc1_class0, b8, b13 = 'r', label='Iris-setosa')
plt.scatter(pc1_class1, b9, b13 = 'g', label='Iris-versicolor')
plt.scatter(pc1_class2, b10, b13 = 'b', label='Iris-virginica')
plt.legend()
plt.grid()
plt.show()