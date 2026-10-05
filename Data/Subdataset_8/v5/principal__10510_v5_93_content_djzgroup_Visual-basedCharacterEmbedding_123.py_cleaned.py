import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
word2vec_model = Word2Vec.load('word2vec/word2vec_wx').wv
img_embedding = np.load('img2vec.npy')
def display_matrix(matrix):
    reshaped_matrix = np.reshape(matrix, (16, 16))
    plt.imshow(reshaped_matrix)
def image_to_matrix(filename):
    image = Image.open(filename).convert("L")
    width, height = image.size
    data = np.array(image.getdata(), dtype='float') / 255.0
    return np.reshape(data, (height, width))
image_matrices = []
for i in range(8984):
    image_matrices.append(image_to_matrix(f'G:/Yeah!!!/img2vec/img/{i + 1}.jpg'))
image_matrices = np.array(image_matrices).reshape(8984, -1)
pca_model = PCA(n_components=10)
pca_result = pca_model.fit_transform(image_matrices)
np.set_printoptions(precision=9)
print(pca_result[178])