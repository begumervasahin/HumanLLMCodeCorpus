import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
b1 = datasets.load_digits()
b2 = b1.data
b3 = b1.target
b2, b3 = shuffle(b2, b3)
b2 = b2[:500]
b3 = b3[:500]
b4 = MinMaxScaler(feature_range=(-1, 1))
b5 = b4.fit_transform(b2)
b6 = {'p_degree': 2.0, 'p_dims': 12, 'eta': 25.0,
          'perplexity': 50.0, 'n_dims': 2, 'ker': 'pca', 'gamma': 1.0}
plt.subplot(2, 1, 1)
b7 = PCA(n_components=2).fit_transform(b5)
plt.scatter(b7[:, 0], b7[:, 1], b8 = b3, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('PCA without ktsne')
b9 = Ktsne(b5, b6=b6)
b10 = b9.get_solution(3000)
b10 = b4.fit_transform(b10)
plt.subplot(2, 1, 2)
plt.scatter(b10[:, 0], b10[:, 1], b8 = b3, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('t-SNE with %s kernel' % b6["ker"])
plt.subplots_adjust(b11 = 0.5)
plt.show()