import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
iris = load_iris()
features = iris.data
targets = iris.target
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(standardized_features)
pc1, pc2 = principal_components[:, 0], principal_components[:, 1]
setosa_pc1, setosa_pc2 = pc1[:50], pc2[:50]
versicolor_pc1, versicolor_pc2 = pc1[50:100], pc2[50:100]
virginica_pc1, virginica_pc2 = pc1[100:150], pc2[100:150]
plt.figure(figsize=(8, 8))
plt.xlabel('Principal Component 1', fontsize=15)
plt.ylabel('Principal Component 2', fontsize=15)
plt.title('2 Component PCA', fontsize=20)
plt.scatter(setosa_pc1, setosa_pc2, c='r', label='Iris-setosa')
plt.scatter(versicolor_pc1, versicolor_pc2, c='g', label='Iris-versicolor')
plt.scatter(virginica_pc1, virginica_pc2, c='b', label='Iris-virginica')
plt.legend()
plt.grid()
plt.show()