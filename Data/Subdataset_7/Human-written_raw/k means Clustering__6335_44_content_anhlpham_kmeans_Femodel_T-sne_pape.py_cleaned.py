
print(__doc__)
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
sns.set(b1 = 'white', context='notebook', rc={'figure.figsize':(14,10)})
b2 = loadmat('Parekh_all2.mat')
b2.keys()
b3 = b2['b3'];
type(b2['b3']),b2['b3'].shape
b4 = b2['b4']
b5 = np.reshape(b4,(35885))
b6 = np.array([1, 2, 3, 4]);
b7 = [5, 30, 50, 100]
b8 = manifold.TSNE(n_components=2, init='random',
                         b9 = 0, perplexity=30)
b10 = b8.fit_transform(b3)
plt.scatter(b10[:, 0], b10[:, 1], b11 = [sns.color_palette()[x] for x in b5])
plt.gca().set_aspect('equal', 'datalim')
plt.title('b8 projection of sFe-all model', b12 = 24);
plt.savefig('b8-sFe-all.pdf')
plt.show()