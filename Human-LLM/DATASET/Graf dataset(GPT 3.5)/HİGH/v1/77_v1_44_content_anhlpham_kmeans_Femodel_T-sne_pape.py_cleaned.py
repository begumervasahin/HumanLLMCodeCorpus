
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
b1 = loadmat('Parekh_all2.mat')
b2 = b1['b2']
b3 = b1['b3']
b4 = np.reshape(b3, (35885))
b5 = np.array([1, 2, 3, 4])
b6 = [5, 30, 50, 100]
b7 = manifold.TSNE(n_components=2, init='random', random_state=0)
b8 = b7.fit_transform(b2)
sns.set(b9 = 'white', context='notebook', rc={'figure.figsize':(14,10)})
plt.scatter(b8[:, 0], b8[:, 1], b10 = [sns.color_palette()[x] for x in b4])
plt.gca().set_aspect('equal', 'datalim')
plt.title('b7 projection of sFe-all model', b11 = 24)
plt.savefig('b7-sFe-all.pdf')
plt.show()