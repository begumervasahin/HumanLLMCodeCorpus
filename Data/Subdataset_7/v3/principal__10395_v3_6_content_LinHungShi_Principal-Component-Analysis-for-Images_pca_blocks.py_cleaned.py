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
def fonk1(b29, b30, b25, b26, n_blocks, b31):
    b2 = b30[:b25, n_blocks * n_blocks * b31: n_blocks * n_blocks * (b31 + 1)]
    b3 = b29[:, :b25]
    b4 = np.dot(b3.T, b26.T)
    b5 = b2 - np.repeat(b4.reshape(-1, 1), n_blocks ** 2, 1)
    b6 = np.dot(b3, b5) + np.repeat(b26.reshape(-1, 1), n_blocks ** 2, 1)
    b6 = b6.T
    b7 = int(b26.size ** 0.5)
    b8 = T.tensor4('b8')
    b9 = nbs.images2neibs(b8, neib_shape=(b7, b7))
    b10 = nbs.neibs2images(b9, neib_shape=(b7, b7), original_shape=(1, 1, a1, a1))
    b11 = theano.function([b9], b10)
    b12 = b11(b6)
    return b12[0, 0]
def fonk2(b29, b30, num_coeff_array, b26, n_blocks, b31):
    fig, b13 = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            b14 = b13[i, j]
            b14.imshow(fonk1(b29, b30, num_coeff_array[i * 3 + j], b26, n_blocks, b31), b15 = 'gray')
    os.chdir(b1)
    fig.savefig('output/hw1a_{0}_im{1}.png'.format(n_blocks, b31))
    plt.close(fig)
def fonk3(b29, sz, b32):
    b8 = T.tensor4('b8')
    b9 = nbs.images2neibs(b8, neib_shape=(sz, sz))
    b10 = nbs.neibs2images(b9, neib_shape=(sz, sz), original_shape=(1, 1, sz, sz))
    b11 = theano.function([b9], b10)
    fig, b13 = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            b14 = b13[i, j]
            b14.imshow(b11(b29[:, [i * 4 + j]].T)[0, 0], b15 = 'gray')
    os.chdir(b1)
    fig.savefig(b32)
    plt.close(fig)
def fonk4():
    os.chdir(b1 + '/Fei_256')
    b16 = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.jpg')]
    b17 = len(b16)
    b18 = np.empty((b17 - 1, a1, a1))
    for i, f in enumerate(b16):
        b19 = mpimg.imread(f, 0)
        b18[i, :, :] = b19
    return b18
def fonk5(b18, window):
    b8 = T.tensor4('Image')
    b9 = nbs.images2neibs(b8, neib_shape=(window, window))
    b20 = theano.function([b8], b9)
    b6 = None
    b21 = copy.copy(b18)
    b21.b22 = (1, b21.b22[0], b21.b22[1], b21.b22[2])
    b6 = b20(b21)
    return b6
def fonk6():
    b23 = fonk4()
    b24 = [8, 32, 64]
    b25 = [range(1, 10, 1), range(3, 30, 3), range(5, 50, 5)]
    for sz, nc in zip(b24, b25):
        b18 = fonk5(b23, sz)
        b26 = np.mean(b18, 0)
        b18 = b18 - np.repeat(b26.reshape(1, -1), b18.b22[0], 0)
        b27 = np.dot(b18.T, b18) / b18.b22[0]
        v, b28 = linalg.eigh(b27)
        b29 = b28[:, ::-1]
        b30 = np.dot(b29.T, b18.T)
        os.chdir(b1)
        for i in range(0, 200, 10):
            fonk2(b29 = b29, b30=b30, num_coeff_array=nc, b26=b26, n_blocks=int(a1 / sz),
                                 b31 = i)
        fonk3(b29, sz, b32 = 'output/hw1a_top16_{0}.png'.format(sz))
if b33 = = '__main__':
    fonk6()