import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
b1 = 'word2vec/word2vec_wx'
b2 = Word2Vec.load(b1)
b2 = b2.wv
b3 = np.load('img2vec.npy')
def fonk1(matrix):
    b4 = np.reshape(matrix, (16, 16))
    plt.imshow(b4)
def fonk2(filename):
    b5 = Image.open(filename)
    width, b6 = b5.size
    b5 = b5.convert("L")
    b7 = b5.getdata()
    b7 = np.matrix(b7, dtype='float') / 255.0
    b8 = np.reshape(b7, (b6, width))
    return b8
b9 = []
for i in range(8984):
    b9.append(fonk2('G:\\Yeah!!!\\img2vec/b9/{}.jpg'.format(i + 1)))
b9 = np.array(b9)
b9 = np.reshape(b9, (8984, -1))
b10 = PCA(10)
b11 = b10.fit_transform(b9)
np.set_printoptions(b12 = 9)
print(b11[178])