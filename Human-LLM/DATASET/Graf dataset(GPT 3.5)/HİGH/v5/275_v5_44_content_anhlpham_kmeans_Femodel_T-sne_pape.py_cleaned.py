
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
from scipy.io import loadmat
import seaborn as sns
sns.set(b1 = 'white', context='notebook', rc={'figure.figsize': (14, 10)})
b2 = loadmat('Parekh_all2.mat')
b3 = b2['b3']
b4 = b2['IDX_new'].flatten()
b5 = np.array([1, 2, 3, 4])
b6 = [5, 30, 50, 100]
b7 = manifold.TSNE(n_components=2, init='random', random_state=0, perplexity=30)
b8 = b7.fit_transform(b3)
plt.scatter(b8[:, 0], b8[:, 1], b9 = [sns.color_palette()[x] for x in b4])
plt.gca().set_aspect('equal', 'datalim')
plt.title('t-SNE projection of sFe-all model', b10 = 24)
plt.savefig('b7-sFe-all.pdf')
plt.show()