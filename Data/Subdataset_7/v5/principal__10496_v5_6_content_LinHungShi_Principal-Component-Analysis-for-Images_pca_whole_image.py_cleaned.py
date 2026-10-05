import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import theano
import theano.tensor as T
from PIL import Image
a1 = 256
a2 = 50
a3 = 0.0001
a4 = 0.00001
a5 = 16
b1 = os.getcwd()
def fonk1(b12, b13, num_coeffs, b31, im_num):
    b2 = b13[:num_coeffs, im_num]
    b3 = b12[:, :num_coeffs]
    b4 = np.dot(b3.T, b31.T)
    b5 = b2 - b4
    b6 = np.dot(b3, b5) + b31
    b7 = b6.reshape(a1, a1)
    return b7
def fonk2(b12, b13, num_coeff_array, b31, im_num):
    b18, b8 = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            plt.axes(b8[i, j])
            plt.imshow(fonk1(b12, b13, num_coeff_array[i * 3 + j], b31, im_num), b9 = 'gray')
    b18.savefig('hw1b_{0}.png'.format(im_num))
    plt.close(b18)
def fonk3(b12, sz, imname):
    b18, b8 = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            plt.axes(b8[i, j])
            plt.imshow(b12[:, i * 4 + j].reshape(a1, a1), b9 = 'gray')
    b18.savefig(imname)
    plt.close(b18)
def fonk4():
    os.chdir(b1 + '/Fei_256')
    b6 = []
    for filename in os.listdir('.'):
        if filename.endswith('.jpg'):
            b10 = mpimg.imread(filename, 0)
            b6.append(b10.flatten())
    return np.array(b6)
def fonk5(b6, num_eig, iteration, step, epsilon):
    b11 = b6.shape[1]
    b12 = np.zeros((b11, b11), dtype=np.float32)
    b13 = np.zeros(b11, dtype=np.float32)
    b14 = T.matrix('b14')
    b15 = T.vector('b15')
    b16 = T.vector('b16')
    b17 = T.scalar('b17')
    b18 = 2 * T.dot(T.dot(b15.T, b14.T), b14)
    b19 = b17 * 2 * T.dot(T.dot(b15.T, b16), b16.T)
    b20 = theano.function([b15, b14], b18)
    b21 = theano.function([b17, b15, b16], b19)
    for i in range(num_eig):
        b22 = np.random.normal(0, 10, b11)
        b23 = b22 / np.linalg.norm(b22)
        print("Obtaining {0}th eigen vector".format(i))
        b24 = time.time()
        for k in range(iteration):
            b25 = b20(b23, b6)
            b26 = np.zeros(b11)
            for j in range(i):
                b26 = b26 + b21(b13[j], b23, b12[:, j])
            b27 = (b25 - b26)
            b28 = b23 + b27 * step
            b29 = b28 / np.linalg.norm(b28)
            print("{0}th difference: {1}".format(k, np.sum(abs(b29 - b23))))
            if abs(np.sum(b29 - b23)) < epsilon:
                b23 = b29
                break
            b23 = b29
        print("Time spent: {0} to obtain eigen vector".format(time.time() - b24))
        b12[:, i] = b23
        b13[i] = np.dot(b20(b23, b6) / 2.0, b23)
        print("b13: ", np.dot(np.dot(np.dot(b23.T, b6.T), b6), b23))
        print("b13{0} = {1}".format(i, b13[i]))
        if i >= 1:
            print("Difference between eigen vectors:", np.sum(abs(b12[:, i] - b12[:, (i - 1)])))
    return (b12, b13)
def fonk6():
    b30 = fonk4()
    b30 = b30.astype(np.float32)
    b31 = np.mean(b30, 0)
    b6 = b30 - np.repeat(b31.reshape(1, -1), b30.shape[0], 0)
    b12, b32 = fonk5(b6, a5, a2, a3, a4)
    b13 = np.dot(b12.T, b6.T)
    os.chdir(b1 + '/output')
    for i in range(0, 200, 10):
        fonk2(b12 = b12, b13=b13, num_coeff_array=[1, 2, 4, 6, 8, 10, 12, 14, 16], b31=b31, im_num=i)
    fonk3(b12, 256, 'hw1b_top16_256.png')
if b33 = = '__main__':
    fonk6()