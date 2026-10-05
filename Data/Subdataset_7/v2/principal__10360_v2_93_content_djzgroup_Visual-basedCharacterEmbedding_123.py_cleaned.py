import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
b1 = 'word2vec/word2vec_wx'
b2 = Word2Vec.load(b1)
b3 = b2.wv
b4 = np.load('img2vec.npy')
def fonk1(matrix):
    b5 = np.reshape(matrix, (16, 16))
    plt.imshow(b5)
def fonk2(filename):
    b5 = Image.open(filename)
    width, b6 = b5.size
    b7 = b5.convert("L")
    b8 = b7.getdata()
    b8 = np.matrix(b8, dtype='float') / 255.0
    b9 = np.reshape(b8, (b6, width))
    return b9
b10 = []
for i in range(8984):
    b11 = fonk2('G:\\Yeah!!!\\img2vec/img/{}.jpg'.format(i + 1))
    b10.append(b11)
b10 = np.array(b10)
b12 = np.reshape(b10, (8984, -1))
b13 = PCA(n_components=10)
b14 = b13.fit_transform(b12)
np.set_printoptions(b15 = 9)
print("PCA transformation of b5 at index 178:")
print(b14[178])