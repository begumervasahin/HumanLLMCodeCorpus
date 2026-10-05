import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def fonk1():
    b4, b1 = fonk2()
    fonk3(b4, b1)
    fonk4(b4)
    plt.subplots_adjust(b2 = 0.5)
    plt.show()
def fonk2():
    b3 = datasets.load_digits()
    b4 = b3.data
    b1 = b3.target
    b4, b1 = shuffle(b4, b1)
    b4 = b4[:500]
    b1 = b1[:500]
    b5 = MinMaxScaler(feature_range=(-1, 1))
    b6 = b5.fit_transform(b4)
    return b6, b1
def fonk3(b6, b1):
    b7 = PCA(n_components=2).fit_transform(b6)
    plt.subplot(2, 1, 1)
    plt.scatter(b7[:, 0], b7[:, 1], b8 = b1, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title('PCA without t-SNE')
def fonk4(b4):
    b9 = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    b10 = Ktsne(b4, f_opts=b9)
    b11 = b10.get_solution(3000)
    b5 = MinMaxScaler(feature_range=(-1, 1))
    b11 = b5.fit_transform(b11)
    plt.subplot(2, 1, 2)
    plt.scatter(b11[:, 0], b11[:, 1], b8 = b1, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.title('t-SNE with PCA kernel')
if b12 = = "__main__":
    fonk1()