import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import theano
import theano.tensor as T
from PIL import Image
IMG_SIZE = 256
ITERATION = 50
STEP_SIZE = 0.0001
EPSILON = 0.00001
NUM_EIG = 16
CWD = os.getcwd()
def reconstructed_image(D, c, num_coeffs, X_mean, im_num):
    c_im = c[:num_coeffs, im_num]
    D_im = D[:, :num_coeffs]
    M_coef = np.dot(D_im.T, X_mean.T)
    tmp1 = c_im - M_coef
    X = np.dot(D_im, tmp1) + X_mean
    X_recon_img = X.reshape(IMG_SIZE, IMG_SIZE)
    return X_recon_img
def plot_reconstructions(D, c, num_coeff_array, X_mean, im_num):
    f, axarr = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            plt.axes(axarr[i, j])
            plt.imshow(reconstructed_image(D, c, num_coeff_array[i * 3 + j], X_mean, im_num), cmap='gray')
    f.savefig('hw1b_{0}.png'.format(im_num))
    plt.close(f)
def plot_top_16(D, sz, imname):
    f, axarr = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            plt.axes(axarr[i, j])
            plt.imshow(D[:, i * 4 + j].reshape(IMG_SIZE, IMG_SIZE), cmap='gray')
    f.savefig(imname)
    plt.close(f)
def get_images_from_file():
    os.chdir(CWD + '/Fei_256')
    X = []
    for filename in os.listdir('.'):
        if filename.endswith('.jpg'):
            img = mpimg.imread(filename, 0)
            X.append(img.flatten())
    return np.array(X)
def train_model(X, num_eig, iteration, step, epsilon):
    n = X.shape[1]
    D = np.zeros((n, n), dtype=np.float32)
    c = np.zeros(n, dtype=np.float32)
    A = T.matrix('A')
    d = T.vector('d')
    d_i = T.vector('d_i')
    l = T.scalar('l')
    f = 2 * T.dot(T.dot(d.T, A.T), A)
    g = l * 2 * T.dot(T.dot(d.T, d_i), d_i.T)
    grad1 = theano.function([d, A], f)
    grad2 = theano.function([l, d, d_i], g)
    for i in range(num_eig):
        dd = np.random.normal(0, 10, n)
        dd_norm = dd / np.linalg.norm(dd)
        print("Obtaining {0}th eigen vector".format(i))
        start = time.time()
        for k in range(iteration):
            gd1 = grad1(dd_norm, X)
            gd2 = np.zeros(n)
            for j in range(i):
                gd2 = gd2 + grad2(c[j], dd_norm, D[:, j])
            gd = (gd1 - gd2)
            y = dd_norm + gd * step
            new_dd = y / np.linalg.norm(y)
            print("{0}th difference: {1}".format(k, np.sum(abs(new_dd - dd_norm))))
            if abs(np.sum(new_dd - dd_norm)) < epsilon:
                dd_norm = new_dd
                break
            dd_norm = new_dd
        print("Time spent: {0} to obtain eigen vector".format(time.time() - start))
        D[:, i] = dd_norm
        c[i] = np.dot(grad1(dd_norm, X) / 2.0, dd_norm)
        print("c: ", np.dot(np.dot(np.dot(dd_norm.T, X.T), X), dd_norm))
        print("c{0} = {1}".format(i, c[i]))
        if i >= 1:
            print("Difference between eigen vectors:", np.sum(abs(D[:, i] - D[:, (i - 1)])))
    return (D, c)
def main():
    images = get_images_from_file()
    images = images.astype(np.float32)
    X_mean = np.mean(images, 0)
    X = images - np.repeat(X_mean.reshape(1, -1), images.shape[0], 0)
    D, v = train_model(X, NUM_EIG, ITERATION, STEP_SIZE, EPSILON)
    c = np.dot(D.T, X.T)
    os.chdir(CWD + '/output')
    for i in range(0, 200, 10):
        plot_reconstructions(D=D, c=c, num_coeff_array=[1, 2, 4, 6, 8, 10, 12, 14, 16], X_mean=X_mean, im_num=i)
    plot_top_16(D, 256, 'hw1b_top16_256.png')
if __name__ == '__main__':
    main()