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
def fonk2(b9):
    b5 = Image.open(b9)
    b6 = b5.convert("L")
    b7 = np.array(b6, dtype='float') / 255.0
    return b7
def fonk3(num_images):
    b8 = []
    for i in range(1, num_images + 1):
        b9 = 'G:\\Yeah!!!\\img2vec/img/{}.jpg'.format(i)
        b10 = fonk2(b9)
        b8.append(b10)
    return np.array(b8)
def fonk4(data, b11 = 10):
    b12 = PCA(b11=b11)
    b13 = b12.fit_transform(data)
    return b13
def fonk5():
    b8 = fonk3(8984)
    b14 = b8.reshape(len(b8), -1)
    b15 = fonk4(b14)
    np.set_printoptions(b16 = 9)
    print("PCA transformation of b5 at index 178:")
    print(b15[178])
if b17 = = "__main__":
    fonk5()