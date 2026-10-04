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
    b7 = b6["ker"]
    plt.clf()
    plt.subplot(2, 1, 1)
    b8 = PCA(n_components=2).fit_transform(b5)
    x_min, b9 = b8[:, 0].min() - 0.5, b8[:, 0].max() + 0.5
    y_min, b10 = b8[:, 1].min() - 0.5, b8[:, 1].max() + 0.5
    plt.scatter(b8[:, 0], b8[:, 1], b11 = b3, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('p1')
    plt.ylabel('p2')
    plt.xlim(x_min, b9)
    plt.ylim(y_min, b10)
    plt.xticks(())
    plt.yticks(())
    plt.title("PCA without ktsne")
    b12 = Ktsne(b5, b6=b6)
    b13 = b12.get_solution(steps=3000)
    b14 = b4.fit_transform(b13)
    plt.subplot(2, 1, 2)
    plt.scatter(b14[:, 0], b14[:, 1], b11 = b3, cmap=plt.cm.Set1, edgecolor='k')
    x1_min, b15 = b14[:, 0].min() - 0.5, b14[:, 0].max() + 0.5
    y1_min, b16 = b14[:, 1].min() - 0.5, b14[:, 1].max() + 0.5
    plt.xlabel('V1')
    plt.ylabel('V2')
    plt.xlim(x1_min, b15)
    plt.ylim(y1_min, b16)
    plt.xticks(())
    plt.yticks(())
    plt.title(f"With ktsne ({b7} b7)")
    plt.subplots_adjust(b17 = 0.5)
    plt.show()
if b18 = = "__main__":
    fonk1()