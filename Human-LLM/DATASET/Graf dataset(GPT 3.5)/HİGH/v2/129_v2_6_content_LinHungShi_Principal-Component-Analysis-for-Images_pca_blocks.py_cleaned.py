import os
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as linalg
import copy
import theano
import theano.tensor as T
import theano.tensor.nnet.neighbours as nbs
import matplotlib.b8 as mpimg
a1 = 256
b1 = os.getcwd()
def fonk1(b27, b28, b23, b24, n_blocks, b29):
    b2 = b28[:b23, n_blocks * n_blocks * b29: n_blocks * n_blocks * (b29 + 1)]
    b3 = b27[:, :b23]
    b4 = np.dot(b3.T, b24.T)
    b5 = b2 - np.repeat(b4.reshape(-1, 1), n_blocks ** 2, 1)
    b6 = np.dot(b3, b5) + np.repeat(b24.reshape(-1, 1), n_blocks ** 2, 1)
    b6 = b6.T
    b7 = int(b24.size ** 0.5)
    b8 = T.tensor4('b8')
    b9 = nbs.images2neibs(b8, neib_shape=(b7, b7))
    b10 = nbs.neibs2images(b9, neib_shape=(b7, b7), original_shape=(1, 1, a1, a1))
    b11 = theano.function([b9], b10)
    b12 = b11(b6)
    return b12[0, 0]
def fonk2(b27, b28, num_coeff_array, b24, n_blocks, b29):
    f, b13 = plt.subplots(3, 3)
    for a2 in range(3):
        for j in range(3):
            plt.axes(b13[a2, j])
            plt.imshow(fonk1(b27, b28, num_coeff_array[a2 * 3 + j], b24, n_blocks, b29), b14 = 'gray')
    os.chdir(b1)
    f.savefig('output/hw1a_{0}_im{1}.png'.format(n_blocks, b29))
    plt.close(f)
def fonk3(b27, sz, b30):
    b8 = T.tensor4('b8')
    b9 = nbs.images2neibs(b8, neib_shape=(sz, sz))
    b10 = nbs.neibs2images(b9, neib_shape=(sz, sz), original_shape=(1, 1, sz, sz))
    b11 = theano.function([b9], b10)
    f, b13 = plt.subplots(4, 4)
    for a2 in range(4):
        for j in range(4):
            plt.axes(b13[a2, j])
            plt.imshow(b11(b27[:, [a2 * 4 + j]].T)[0, 0], b14 = 'gray')
    os.chdir(b1)
    f.savefig(b30)
    plt.close(f)
def fonk4():
    os.chdir(b1 + '/Fei_256')
    b15 = len([name for name in os.listdir('.') if os.path.isfile(name)])
    b16 = np.ndarray(b20=(b15 - 1, a1, a1))
    a2 = 0
    for dirPath, dirNames, fileNames in os.walk(b1 + "/Fei_256"):
        for f in fileNames:
            if f.endswith('.jpg'):
                b17 = mpimg.imread(f, 0)
                b16[a2, :, :] = b17
                a2 = a2 + 1
    return b16
def fonk5(b16, window):
    b8 = T.tensor4('Image')
    b9 = nbs.images2neibs(b8, neib_shape=(window, window))
    b18 = theano.function([b8], b9)
    b6 = None
    b19 = copy.copy(b16)
    b19.b20 = (1, b19.b20[0], b19.b20[1], b19.b20[2])
    b6 = b18(b19)
    return b6
def fonk6():
    b21 = fonk4()
    b22 = [8, 32, 64]
    b23 = [range(1, 10, 1), range(3, 30, 3), range(5, 50, 5)]
    for sz, nc in zip(b22, b23):
        b16 = fonk5(b21, sz)
        b24 = np.mean(b16, 0)
        b16 = b16 - np.repeat(b24.reshape(1, -1), b16.b20[0], 0)
        b25 = np.dot(b16.T, b16) / b16.b20[0]
        v, b26 = linalg.eigh(b25)
        b27 = b26[:, ::-1]
        b28 = np.dot(b27.T, b16.T)
        os.chdir(b1)
        for a2 in range(0, 200, 10):
            fonk2(b27 = b27, b28=b28, num_coeff_array=nc, b24=b24, n_blocks=int(a1 / sz),
                                 b29 = a2)
        fonk3(b27, sz, b30 = 'output/hw1a_top16_{0}.png'.format(sz))
if b31 = = '__main__':
    fonk6()