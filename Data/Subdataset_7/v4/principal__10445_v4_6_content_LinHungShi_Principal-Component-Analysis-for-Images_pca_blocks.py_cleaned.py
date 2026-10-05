import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.b8 as mpimg
import numpy.linalg as linalg
import theano
import theano.tensor as T
import theano.tensor.nnet.neighbours as nbs
from PIL import Image
import cv2
import copy
a1 = 256
b1 = os.getcwd()
def fonk1(b28, b29, b24, b25, n_blocks, im_num):
    b2 = b29[:b24, n_blocks * n_blocks * im_num:n_blocks * n_blocks * (im_num + 1)]
    b3 = b28[:, :b24]
    b4 = np.dot(b3.T, b25.T)
    b5 = b2 - np.repeat(b4.reshape(-1, 1), n_blocks ** 2, 1)
    b6 = np.dot(b3, b5) + np.repeat(b25.reshape(-1, 1), n_blocks ** 2, 1)
    b6 = b6.T
    b7 = int(b25.size ** 0.5)
    b8 = T.tensor4('b8')
    b9 = nbs.images2neibs(b8, neib_shape=(b7, b7))
    b10 = nbs.neibs2images(b9, neib_shape=(b7, b7), original_shape=(1, 1, a1, a1))
    b11 = theano.function([b9], b10)
    b12 = b11(b6)
    return b12[0, 0]
def fonk2(b28, b29, num_coeff_array, b25, n_blocks, im_num):
    f, b13 = plt.subplots(3, 3)
    for a2 in range(3):
        for j in range(3):
            plt.axes(b13[a2, j])
            plt.imshow(fonk1(b28, b29, num_coeff_array[a2 * 3 + j], b25, n_blocks, im_num), b14 = 'gray')
    os.chdir(b1)
    f.savefig('output/hw1a_{0}_im{1}.png'.format(n_blocks, im_num))
    plt.close(f)
def fonk3(b28, sz, b30):
    b8 = T.tensor4('b8')
    b9 = nbs.images2neibs(b8, neib_shape=(sz, sz))
    b10 = nbs.neibs2images(b9, neib_shape=(sz, sz), original_shape=(1, 1, sz, sz))
    b11 = theano.function([b9], b10)
    f, b13 = plt.subplots(4, 4)
    for a2 in range(4):
        for j in range(4):
            plt.axes(b13[a2, j])
            plt.imshow(b11(b28[:, [a2 * 4 + j]].T)[0, 0], b14 = 'gray')
    os.chdir(b1)
    f.savefig(b30)
    plt.close(f)
def fonk4():
    os.chdir(b1 + '/Fei_256')
    b15 = len([name for name in os.listdir('.') if os.path.isfile(name)])
    b16 = np.ndarray(b21=(b15 - 1, a1, a1))
    a2 = 0
    for dirPath, dirNames, fileNames in os.walk(b1 + "/Fei_256"):
        for f in fileNames:
            if f.endswith('.jpg'):
                b17 = mpimg.imread(f, 0)
                b16[a2, :, :] = b17
                a2 = a2 + 1
    return b16
def fonk5(b16, window):
    b18 = b16.b21[0]
    b8 = T.tensor4('Image')
    b9 = nbs.images2neibs(b8, neib_shape=(window, window))
    b19 = theano.function([b8], b9)
    b6 = None
    b20 = copy.copy(b16)
    b20.b21 = (1, b20.b21[0], b20.b21[1], b20.b21[2])
    b6 = b19(b20)
    return b6
def fonk6():
    b22 = fonk4()
    b23 = [8, 32, 64]
    b24 = [range(1, 10, 1), range(3, 30, 3), range(5, 50, 5)]
    for sz, nc in zip(b23, b24):
        b16 = fonk5(b22, sz)
        b25 = np.mean(b16, 0)
        b16 = b16 - np.repeat(b25.reshape(1, -1), b16.b21[0], 0)
        b26 = np.dot(b16.T, b16) / b16.b21[0]
        v, b27 = linalg.eigh(b26)
        b28 = b27[:, ::-1]
        b29 = np.dot(b28.T, b16.T)
        os.chdir(b1)
        for a2 in range(0, 200, 10):
            fonk2(b28 = b28, b29=b29, num_coeff_array=nc, b25=b25, n_blocks=int(a1 / sz), im_num=a2)
        fonk3(b28, sz, b30 = 'output/hw1a_top16_{0}.png'.format(sz))
if b31 = = '__main__':
    fonk6()