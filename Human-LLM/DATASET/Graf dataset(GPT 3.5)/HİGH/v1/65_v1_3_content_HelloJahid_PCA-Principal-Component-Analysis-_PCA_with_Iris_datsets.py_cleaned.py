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
b3 = b5[:, 1]
b7 = b6[:50]
b8 = b3[:50]
b9 = b6[50:100]
b10 = b3[50:100]
b11 = b6[100:150]
b12 = b3[100:150]
b13 = plt.figure(figsize=(8, 8))
b14 = b13.add_subplot(1, 1, 1)
b14.set_xlabel('Principal Component 1', b15 = 15)
b14.set_ylabel('Principal Component 2', b15 = 15)
b14.set_title('2 Component PCA', b15 = 20)
b16 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b14.scatter(b7, b8, b17 = 'r', label=b16[0])
b14.scatter(b9, b10, b17 = 'g', label=b16[1])
b14.scatter(b11, b12, b17 = 'b', label=b16[2])
b14.legend()
b14.grid()
plt.show()