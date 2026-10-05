import os
import time
from os import walk
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.image as mpimg
import numpy.linalg as linalg
import os, glob
from PIL import Image
import copy
import theano
import theano.tensor as T
IMG_SIZE = 256
ITERATION = 50
STEP_SIZE = 0.0001
EPSILON = 0.00001
NUM_EIG = 16
CWD = os.getcwd()
'''
Implement the functions that were not implemented and complete the
parts of main according to the instructions in comments.
'''
def reconstructed_image(D,c,num_coeffs,X_mean,im_num):
    '''
    This function reconstructs an image X_recon_img given the number of
    coefficients for each image specified by num_coeffs
    '''
    '''
        Parameters
    ---------------
    c: np.ndarray
        a n x m matrix  representing the coefficients of all the image blocks.
        n represents the maximum dimension of the PCA space.
        m is (number of images x n_blocks**2)
    D: np.ndarray
        an N x n matrix representing the basis vectors of the PCA space
        N is the dimension of the original space (number of pixels in a block)
    im_num: Integer
        index of the image to visualize
    X_mean: np.ndarray
        a matrix representing the mean block.
    num_coeffs: Integer
        an integer that specifies the number of top components to be
        considered while reconstructing
    n_blocks: Integer
        number of blocks comprising the image in each direction.
        For example, for a 256x256 image divided into 64x64 blocks, n_blocks will be 4
    '''
    c_im = c[:num_coeffs,im_num]
    D_im = D[:,:num_coeffs]
    M_coef = np.dot(D_im.T, X_mean.T)
    tmp1 = c_im - M_coef
    X = np.dot(D_im, tmp1) + X_mean
    X_recon_img = X.reshape(IMG_SIZE, IMG_SIZE)
    return X_recon_img
def plot_reconstructions(D,c,num_coeff_array,X_mean,im_num):
    '''
    Plots 9 reconstructions of a particular image using D as the basis matrix and coeffiecient
    vectors from c
    Parameters
    ------------------------
        num_coeff_array: Iterable
            an iterable with 9 elements representing the number of coefficients
            to use for reconstruction for each of the 9 plots
        c: np.ndarray
            a l x m matrix  representing the coefficients of all blocks in a particular image
            l represents the dimension of the PCA space used for reconstruction
            m represents the number of blocks in an image
        D: np.ndarray
            an N x l matrix representing l basis vectors of the PCA space
            N is the dimension of the original space (number of pixels in a block)
        n_blocks: Integer
            number of blocks comprising the image in each direction.
            For example, for a 256x256 image divided into 64x64 blocks, n_blocks will be 4
        X_mean: basis vectors represent the divergence from the mean so this
            matrix should be added to all reconstructed blocks
        im_num: Integer
            index of the image to visualize
    '''
    f, axarr = plt.subplots(3,3)
    for i in range(3):
        for j in range(3):
            plt.axes(axarr[i,j])
            plt.imshow(reconstructed_image(D,c,num_coeff_array[i*3+j],X_mean,im_num), cmap = 'gray')
    f.savefig('hw1b_{0}.png'.format(im_num))
    plt.close(f)
def plot_top_16(D, sz, imname):
    '''
    Plots the top 16 components from the basis matrix D.
    Each basis vector represents an image block of shape (sz, sz)
    Parameters
    -------------
    D: np.ndarray
        N x n matrix representing the basis vectors of the PCA space
        N is the dimension of the original space (number of pixels in a block)
        n represents the maximum dimension of the PCA space (assumed to be atleast 16)
    sz: Integer
        The height and width of each block
    imname: string
        name of file where image will be saved.
    '''
    f, axarr = plt.subplots(4,4)
    for i in range(4):
        for j in range(4):
            plt.axes(axarr[i,j])
            plt.imshow(D[:,i*4+j].reshape(IMG_SIZE, IMG_SIZE), cmap = 'gray')
    f.savefig(imname)
    plt.close(f)
def getImgsFromFile():
    '''Read all images to the matrix X, where X is a Nx256x256 array, N is the number of images'''
    os.chdir(CWD+'/Fei_256')
    length = len([name for name in os.listdir('.') if os.path.isfile(name)])
    X = np.ndarray(shape = (length-1, IMG_SIZE * IMG_SIZE))
    i = 0
    for dirPath, dirNames, fileNames in os.walk(CWD + "/Fei_256"):
    	for f in fileNames:
    		if f.endswith('.jpg'):
    			tmp = mpimg.imread(f, 0)
    			X[i,:] = tmp.flatten()
    			i = i + 1
    return X
def trainModel(X, num_eig, iteration, step, epsilon):
    n = X.shape[1]
    D = np.zeros((n, n), dtype = np.float32)
    c = np.zeros(n, dtype = np.float32)
    A = T.matrix('A')
    d = T.vector('d')
    d_i = T.vector('d_i')
    l = T.scalar('l')
    f = 2 * T.dot(T.dot(d.T, A.T), A)
    g = l * 2 * T.dot(T.dot(d.T, d_i), d_i.T)
    grad1 = theano.function([d, A], f)
    grad2 = theano.function([l, d, d_i], g)
    '''Start training model until get all the eigen vectors'''
    for i in range(num_eig):
        dd = np.random.normal(0,10,n)
        dd_norm = dd / np.linalg.norm(dd)
        print "Get {0}th eigen vector".format(i)
        start = time.time()
        ''' Get the ith eigen vector'''
        for k in range(iteration):
            gd1 = grad1(dd_norm, X)
            gd2 = np.zeros(n)
            for j in range(i):
                gd2 = gd2 + grad2(c[j], dd_norm, D[:, j])
            gd = (gd1 - gd2)
            y = dd_norm + gd * step
            new_dd = y / np.linalg.norm(y)
            print "{0}th difference: {1}".format(k, np.sum(abs(new_dd - dd_norm)))
            if abs(np.sum(new_dd - dd_norm)) < epsilon:
                dd_norm = new_dd
                break
            dd_norm = new_dd
        print "spend {0} getting eigen vector".format(time.time() - start)
        D[:,i] = dd_norm
        c[i] = np.dot(grad1(dd_norm, X)/2.0, dd_norm)
        print "c: ", np.dot(np.dot(np.dot(dd_norm.T, X.T), X), dd_norm)
        print "c{0} = {1}".format(i, c[i])
        if i >= 1:
            print "difference between eigen vector", np.sum(abs(D[:,i] - D[:,(i-1)]))
    return (D, c)
def main():
    '''
    Read here all images(grayscale) from Fei_256 folder and collapse
    each image to get an numpy array Ims with size (no_images, height*width).
    Make sure the images are read after sorting the filenames
    '''
    Ims = getImgsFromFile()
    Ims = Ims.astype(np.float32)
    X_mn = np.mean(Ims, 0)
    X = Ims - np.repeat(X_mn.reshape(1, -1), Ims.shape[0], 0)
    D, v = trainModel(X, NUM_EIG, ITERATION, STEP_SIZE, EPSILON)
    '''
    Use theano to perform gradient descent to get top 16 PCA components of X
    Put them into a matrix D with decreasing order of eigenvalues
    If you are not using the provided AMI and get an error "Cannot construct a ufunc with more than 32 operands" :
    You need to perform a patch to theano from this pull(https:
    Alternatively you can downgrade numpy to 1.9.3, scipy to 0.15.1, matplotlib to 1.4.2
    '''
    c = np.dot(D.T, X.T)
    os.chdir(CWD + '/output')
    for i in range(0, 200, 10):
        plot_reconstructions(D=D, c=c, num_coeff_array=[1, 2, 4, 6, 8, 10, 12, 14, 16] \
                             , X_mean=X_mn, im_num=i)
    plot_top_16(D, 256, 'hw1b_top16_256.png')
if __name__ == '__main__':
    main()