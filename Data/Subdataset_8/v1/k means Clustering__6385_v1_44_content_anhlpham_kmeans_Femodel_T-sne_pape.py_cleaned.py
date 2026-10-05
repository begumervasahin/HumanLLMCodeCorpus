
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from sklearn import manifold, datasets
from time import time
from scipy.io import loadmat
from numpy import linspace
from numpy import meshgrid
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
annots = loadmat('Parekh_all2.mat')
Xn = annots['Xn']
IDX_new = annots['IDX_new']
IDX = np.reshape(IDX_new, (35885))
target = np.array([1, 2, 3, 4])
perplexities = [5, 30, 50, 100]
tsne = manifold.TSNE(n_components=2, init='random', random_state=0)
Y = tsne.fit_transform(Xn)
sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})
plt.scatter(Y[:, 0], Y[:, 1], c=[sns.color_palette()[x] for x in IDX])
plt.gca().set_aspect('equal', 'datalim')
plt.title('tsne projection of sFe-all model', fontsize=24)
plt.savefig('tsne-sFe-all.pdf')
plt.show()