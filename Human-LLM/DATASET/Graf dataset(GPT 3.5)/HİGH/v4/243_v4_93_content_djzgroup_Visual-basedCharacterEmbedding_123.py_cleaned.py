
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from PIL import Image
b1 = Word2Vec.load('word2vec/word2vec_wx')
b1 = b1.wv
b2 = np.load('img2vec.npy')
def fonk1(matrix):
    b3 = np.reshape(matrix, (16, 16))
    plt.imshow(b3)
def fonk2(filename):
    b4 = Image.open(filename)
    width, b5 = b4.size
    b4 = b4.convert("L")
    b6 = b4.getdata()
    b6 = np.matrix(b6, dtype='float') / 255.0
    b7 = np.reshape(b6, (b5, width))
    return b7
b8 = []
for i in range(8984):
    b8.append(fonk2('G:/Yeah!!!/img2vec/img/{}.jpg'.format(i + 1)))
b8 = np.array(b8)
b8 = np.reshape(b8, (8984, -1))
b9 = PCA(n_components=10)
b10 = b9.fit_transform(b8)
np.set_printoptions(b11 = 9)
print(b10[178])