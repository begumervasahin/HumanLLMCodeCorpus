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
        'kernel': 'pca',
        'gamma': 1.0
    }
    fonk2(b5, b3)
    fonk3(b5, b6)
    plt.subplots_adjust(b7 = 0.5)
    plt.show()
def fonk2(b5, b3):
    b8 = PCA(n_components=2).fit_transform(b5)
    plt.subplot(2, 1, 1)
    plt.scatter(b8[:, 0], b8[:, 1], b9 = b3, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('PCA Bileþeni 1')
    plt.ylabel('PCA Bileþeni 2')
    plt.title('t-SNE olmadan PCA')
def fonk3(b5, b6):
    b10 = Ktsne(b5, f_opts=b6)
    b11 = b10.get_solution(3000)
    b4 = MinMaxScaler(feature_range=(-1, 1))
    b11 = b4.fit_transform(b11)
    plt.subplot(2, 1, 2)
    plt.scatter(b11[:, 0], b11[:, 1], b9 = b3, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('t-SNE Bileþeni 1')
    plt.ylabel('t-SNE Bileþeni 2')
    plt.title('PCA çekirdeði ile t-SNE')
if b12 = = "__main__":
    fonk1()