import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
word2vec_file = 'word2vec/word2vec_wx'
word2vec_model = Word2Vec.load(word2vec_file)
word2vec_embeddings = word2vec_model.wv
image_embeddings = np.load('img2vec.npy')
def display_image(matrix):
    image = np.reshape(matrix, (16, 16))
    plt.imshow(image)
def image_to_matrix(filename):
    image = Image.open(filename)
    width, height = image.size
    grayscale_image = image.convert("L")
    pixel_data = grayscale_image.getdata()
    pixel_data = np.matrix(pixel_data, dtype='float') / 255.0
    matrix_data = np.reshape(pixel_data, (height, width))
    return matrix_data
image_matrices = []
for i in range(8984):
    image_matrix = image_to_matrix('G:\\Yeah!!!\\img2vec/img/{}.jpg'.format(i + 1))
    image_matrices.append(image_matrix)
image_matrices = np.array(image_matrices)
image_matrices_flattened = np.reshape(image_matrices, (8984, -1))
pca_model = PCA(n_components=10)
pca_transformed_data = pca_model.fit_transform(image_matrices_flattened)
np.set_printoptions(precision=9)
print("PCA transformation of image at index 178:")
print(pca_transformed_data[178])