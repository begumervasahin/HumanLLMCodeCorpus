import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def fonk1():
    b1 = datasets.load_digits()
    b2 = b1.data
    b3 = b1.target
    b2, b3 = shuffle(b2, b3)
    b2 = b2[:500]
    b3 = b3[:500]
    b4 = MinMaxScaler(feature_range=(-1, 1))
    b5 = b4.fit_transform(b2)
    b6 = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    plt.subplot(2, 1, 1)
    fonk2(b5, b3)
    b7 = Ktsne(b5, f_opts=b6)
    b8 = b7.get_solution(3000)
    b8 = b4.fit_transform(b8)
    plt.subplot(2, 1, 2)
    fonk3(b8, b3, b6)
    plt.subplots_adjust(b9 = 0.5)
    plt.show()
def fonk2(b5, b3):
    b10 = PCA(n_components=2).fit_transform(b5)
    plt.scatter(b10[:, 0], b10[:, 1], b11 = b3, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title('PCA without t-SNE')
def fonk3(b8, b3, b6):
    plt.scatter(b8[:, 0], b8[:, 1], b11 = b3, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.title('t-SNE with %s kernel' % b6["ker"])
if b12 = = "__main__":
    fonk1()