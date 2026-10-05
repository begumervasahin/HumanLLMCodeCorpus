import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
b1 = Word2Vec.load('word2vec/word2vec_wx').wv
b2 = np.load('img2vec.npy')
def fonk1(matrix):
    b3 = np.reshape(matrix, (16, 16))
    plt.imshow(b3)
def fonk2(filename):
    b4 = Image.open(filename).convert("L")
    width, b5 = b4.size
    b6 = np.array(b4.getdata(), dtype='float') / 255.0
    return np.reshape(b6, (b5, width))
b7 = []
for i in range(8984):
    b7.append(fonk2(f'G:/Yeah!!!/img2vec/img/{i + 1}.jpg'))
b7 = np.array(b7).reshape(8984, -1)
b8 = PCA(n_components=10)
b9 = b8.fit_transform(b7)
np.set_printoptions(b10 = 9)
print(b9[178])