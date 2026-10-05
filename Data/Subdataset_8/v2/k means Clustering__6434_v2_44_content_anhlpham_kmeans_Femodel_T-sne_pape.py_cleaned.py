
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
from scipy.io import loadmat
import seaborn as sns
data = loadmat('Parekh_all2.mat')
Xn = data['Xn']
IDX_new = data['IDX_new']
IDX = np.reshape(IDX_new, (35885))
target = np.array([1, 2, 3, 4])
perplexities = [5, 30, 50, 100]
tsne = manifold.TSNE(n_components=2, init='random', random_state=0)
Y = tsne.fit_transform(Xn)
sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})
plt.scatter(Y[:, 0], Y[:, 1], c=[sns.color_palette()[x] for x in IDX])
plt.gca().set_aspect('equal', 'datalim')
plt.title('t-SNE Projection of sFe-all Model', fontsize=24)
plt.savefig('tsne-sFe-all.pdf')
plt.show()
