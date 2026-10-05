from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
iris = load_iris()
X = iris.data
y = iris.target
X = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X)
x = principal_components[:, 0]
y = principal_components[:, 1]
x0 = x[:50]
y0 = y[:50]
x1 = x[50:100]
y1 = y[50:100]
x2 = x[100:150]
y2 = y[100:150]
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
ax.scatter(x0, y0, c='r', label=targets[0])
ax.scatter(x1, y1, c='g', label=targets[1])
ax.scatter(x2, y2, c='b', label=targets[2])
ax.legend()
ax.grid()
plt.show()