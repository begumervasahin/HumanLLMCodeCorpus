import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import theano
import theano.tensor as T
a1 = 256
a2 = 50
a3 = 0.0001
a4 = 0.00001
a5 = 16
b1 = os.getcwd()
def fonk1(b13, b14, num_coeffs, b34, im_num):
    b2 = b14[:num_coeffs, im_num]
    b3 = b13[:, :num_coeffs]
    b4 = np.dot(b3.T, b34.T)
    b5 = b2 - b4
    b6 = np.dot(b3, b5) + b34
    b7 = b6.reshape(a1, a1)
    return b7
def fonk2(b13, b14, num_coeff_array, b34, im_num):
    b19, b8 = plt.subplots(3, 3)
    for a6 in range(3):
        for j in range(3):
            plt.axes(b8[a6, j])
            plt.imshow(
                fonk1(
                    b13, b14, num_coeff_array[a6 * 3 + j], b34, im_num), b9 = 'gray')
    b19.savefig('hw1b_{0}.png'.format(im_num))
    plt.close(b19)
def fonk3(b13, sz, imname):
    b19, b8 = plt.subplots(4, 4)
    for a6 in range(4):
        for j in range(4):
            plt.axes(b8[a6, j])
            plt.imshow(b13[:, a6 * 4 + j].reshape(a1, a1), b9 = 'gray')
    b19.savefig(imname)
    plt.close(b19)
def fonk4():
    os.chdir(b1 + '/Fei_256')
    b10 = len([name for name in os.listdir('.') if os.path.isfile(name)])
    b6 = np.ndarray(shape=(b10 - 1, a1 * a1))
    a6 = 0
    for dirPath, dirNames, fileNames in os.walk(b1 + "/Fei_256"):
        for b19 in fileNames:
            if b19.endswith('.jpg'):
                b11 = mpimg.imread(b19, 0)
                b6[a6, :] = b11.flatten()
                a6 += 1
    return b6
def fonk5(b6, num_eig, iteration, step, epsilon):
    b12 = b6.shape[1]
    b13 = np.zeros((b12, num_eig), dtype=np.float32)
    b14 = np.zeros((num_eig, b6.shape[0]), dtype=np.float32)
    b15 = T.matrix('b15')
    b16 = T.vector('b16')
    b17 = T.vector('b17')
    b18 = T.scalar('b18')
    b19 = 2 * T.dot(T.dot(b16.T, b15.T), b15)
    b20 = b18 * 2 * T.dot(T.dot(b16.T, b17), b17.T)
    b21 = theano.function([b16, b15], b19)
    b22 = theano.function([b18, b16, b17], b20)
    for a6 in range(num_eig):
        b23 = np.random.normal(0, 10, b12)
        b24 = b23 / np.linalg.norm(b23)
        print("Getting {0}th eigen vector...".format(a6))
        b25 = time.time()
        for k in range(iteration):
            b26 = b21(b24, b6)
            b27 = np.zeros(b12)
            for j in range(a6):
                b27 += b22(b14[j], b24, b13[:, j])
            b28 = (b26 - b27)
            b29 = b24 + b28 * step
            b30 = b29 / np.linalg.norm(b29)
            print("Iteration {0}, Difference: {1}".format(
                k, np.sum(abs(b30 - b24))))
            if abs(np.sum(b30 - b24)) < epsilon:
                b24 = b30
                break
            b24 = b30
        print("Time spent getting eigen vector: {0}".format(time.time() - b25))
        b13[:, a6] = b24
        b14[a6] = np.dot(b21(b24, b6) / 2.0, b24)
        print("b14{0}: {1}".format(a6, b14[a6]))
        if a6 >= 1:
            print("Difference between eigen vectors:", np.sum(abs(b13[:, a6] - b13[:, (a6 - 1)])))
    return (b13, b14)
def fonk6():
    b31 = fonk4()
    b31 = b31.astype(np.float32)
    b32 = np.mean(b31, 0)
    b6 = b31 - np.repeat(b32.reshape(1, -1), b31.shape[0], 0)
    b13, b33 = fonk5(b6, a5, a2, a3, a4)
    b14 = np.dot(b13.T, b6.T)
    os.chdir(b1 + '/output')
    for a6 in range(0, 200, 10):
        fonk2(b13 = b13, b14=b14, num_coeff_array=[1, 2, 4, 6, 8, 10, 12, 14, 16],
                             b34 = b32, im_num=a6)
    fonk3(b13, 256, 'hw1b_top16_256.png')
if b35 = = '__main__':
    fonk6()