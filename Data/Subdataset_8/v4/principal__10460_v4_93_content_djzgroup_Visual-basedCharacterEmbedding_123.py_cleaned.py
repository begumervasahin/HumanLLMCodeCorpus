
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from PIL import Image
word2vec_model = Word2Vec.load('word2vec/word2vec_wx')
word2vec_model = word2vec_model.wv
img_embedding = np.load('img2vec.npy')
def display_matrix(matrix):
    reshaped_matrix = np.reshape(matrix, (16, 16))
    plt.imshow(reshaped_matrix)
def image_to_matrix(filename):
    image = Image.open(filename)
    width, height = image.size
    image = image.convert("L")
    data = image.getdata()
    data = np.matrix(data, dtype='float') / 255.0
    new_data = np.reshape(data, (height, width))
    return new_data
image_matrices = []
for i in range(8984):
    image_matrices.append(image_to_matrix('G:/Yeah!!!/img2vec/img/{}.jpg'.format(i + 1)))
image_matrices = np.array(image_matrices)
image_matrices = np.reshape(image_matrices, (8984, -1))
pca_model = PCA(n_components=10)
pca_result = pca_model.fit_transform(image_matrices)
np.set_printoptions(precision=9)
print(pca_result[178])