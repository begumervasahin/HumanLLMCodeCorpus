import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
bin_fname = 'word2vec/word2vec_wx'
model = Word2Vec.load(bin_fname)
model = model.wv
img_embedding = np.load('img2vec.npy')
def show(matrix):
    a = np.reshape(matrix, (16, 16))
    plt.imshow(a)
def ImageToMatrix(filename):
    im = Image.open(filename)
    width, height = im.size
    im = im.convert("L")
    data = im.getdata()
    data = np.matrix(data, dtype='float') / 255.0
    new_data = np.reshape(data, (height, width))
    return new_data
img = []
for i in range(8984):
    img.append(ImageToMatrix('G:\\Yeah!!!\\img2vec/img/{}.jpg'.format(i + 1)))
img = np.array(img)
img = np.reshape(img, (8984, -1))
pca_model = PCA(10)
y = pca_model.fit_transform(img)
np.set_printoptions(precision=9)
print(y[178])