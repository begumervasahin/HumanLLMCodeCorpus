
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
iris_data = load_iris()
X = iris_data.data
y = iris_data.target
X_standardized = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_standardized)
pc1, pc2 = principal_components[:, 0], principal_components[:, 1]
pc1_class0, pc2_class0 = pc1[:50], pc2[:50]
pc1_class1, pc2_class1 = pc1[50:100], pc2[50:100]
pc1_class2, pc2_class2 = pc1[100:150], pc2[100:150]
plt.figure(figsize=(8, 8))
plt.xlabel('Principal Component 1', fontsize=15)
plt.ylabel('Principal Component 2', fontsize=15)
plt.title('2 Component PCA', fontsize=20)
plt.scatter(pc1_class0, pc2_class0, c='r', label='Iris-setosa')
plt.scatter(pc1_class1, pc2_class1, c='g', label='Iris-versicolor')
plt.scatter(pc1_class2, pc2_class2, c='b', label='Iris-virginica')
plt.legend()
plt.grid()
plt.show()