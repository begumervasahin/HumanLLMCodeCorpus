
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from scipy.io import loadmat
import seaborn as sns
def fonk1(b11):
    b1 = loadmat(b11)
    b2 = b1['b2']
    b3 = b1['b3']
    b4 = np.reshape(b3, (35885))
    return b2, b4
def fonk2(X, labels, b13, b5 = None):
    b6 = TSNE(n_components=2, init='random', random_state=0)
    b7 = b6.fit_transform(X)
    sns.set(b8 = 'white', context='notebook', rc={'figure.figsize': (14, 10)})
    plt.scatter(b7[:, 0], b7[:, 1], b9 = [sns.color_palette()[x] for x in labels])
    plt.gca().set_aspect('equal', 'datalim')
    plt.b13(b13, b10 = 24)
    if b5:
        plt.savefig(b5)
    plt.show()
def fonk3():
    b11 = 'Parekh_all2.mat'
    b2, b4 = fonk1(b11)
    b12 = np.array([1, 2, 3, 4])
    b13 = 't-SNE Projection of sFe-all Model'
    b5 = 'b6-sFe-all.pdf'
    fonk2(b2, b4, b13, b5)
if b14 = = "__main__":
    fonk3()