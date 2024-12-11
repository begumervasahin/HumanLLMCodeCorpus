import os
import numpy as np
import matplotlib.pyplot as plt
import theano
import theano.tensor as T
import theano.tensor.nnet.neighbours as nbs
from PIL import Image
import matplotlib.image as mpimg
import numpy.linalg as linalg
a1 = 256
b1 = os.getcwd()
def fonk1(directory_path):
    os.chdir(directory_path)
    b2 = [f for f in os.listdir('.') if f.endswith('.jpg')]
    b3 = np.array([mpimg.imread(f) for f in b2])
    return b3
def fonk2(b3, patch_size):
    b4 = T.tensor4('Image')
    b5 = nbs.images2neibs(b4, neib_shape=(patch_size, patch_size))
    b6 = theano.function([b4], b5)
    b3 = b3.reshape((1, b3.shape[0], b3.shape[1], b3.shape[2]))
    b7 = b6(b3)
    return b7
def fonk3(D, coeffs, b18, b26, n_blocks, image_index):
    b8 = coeffs[:b18, n_blocks * n_blocks * image_index:n_blocks * n_blocks * (image_index + 1)]
    b9 = D[:, :b18]
    b10 = np.dot(b9.T, b26.T)
    b11 = b8 - np.repeat(b10.reshape(-1, 1), n_blocks ** 2, axis=1)
    b7 = np.dot(b9, b11) + np.repeat(b26.reshape(-1, 1), n_blocks ** 2, axis=1)
    b7 = b7.T
    b12 = int(b26.size ** 0.5)
    b4 = T.tensor4('image')
    b5 = nbs.images2neibs(b4, neib_shape=(b12, b12))
    b13 = nbs.neibs2images(b5, neib_shape=(b12, b12), original_shape=(1, 1, a1, a1))
    b14 = theano.function([b5], b13)
    b15 = b14(b7)
    return b15[0, 0]
def fonk4(D, coeffs, b25, b26, n_blocks, image_index, b16 = 'output'):
    f, b17 = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            b18 = b25[i * 3 + j]
            b19 = b17[i, j]
            b19.imshow(fonk3(D, coeffs, b18, b26, n_blocks, image_index), b20 = 'gray')
            b19.axis('off')
    plt.tight_layout()
    os.makedirs(b16, b21 = True)
    f.savefig(os.path.join(b16, f'reconstruction_{n_blocks}_im{image_index}.png'))
    plt.close(f)
def fonk5(D, component_size, b16 = 'output'):
    f, b17 = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            b22 = D[:, [i * 4 + j]].T
            b19 = b17[i, j]
            b19.imshow(b22.reshape((component_size, component_size)), b20 = 'gray')
            b19.axis('off')
    plt.tight_layout()
    os.makedirs(b16, b21 = True)
    f.savefig(os.path.join(b16, 'top_16_components.png'))
    plt.close(f)
def fonk6():
    b23 = os.path.join(b1, 'Fei_256')
    b3 = fonk1(b23)
    b24 = [8, 32, 64]
    b25 = [list(range(1, 10)), list(range(3, 30, 3)), list(range(5, 50, 5))]
    for patch_size, coeffs_range in zip(b24, b25):
        b7 = fonk2(b3, patch_size)
        b26 = np.mean(b7, axis=0)
        b27 = b7 - np.repeat(b26.reshape(1, -1), b7.shape[0], axis=0)
        b28 = np.dot(b27.T, b27) / b27.shape[0]
        eigenvalues, b29 = linalg.eigh(b28)
        b30 = b29[:, ::-1]
        b31 = np.dot(b30.T, b27.T)
        for image_index in range(0, 200, 10):
            fonk4(b30, b31, coeffs_range, b26, int(a1 / patch_size), image_index)
        fonk5(b30, patch_size)
if b32 = = '__main__':
    fonk6()