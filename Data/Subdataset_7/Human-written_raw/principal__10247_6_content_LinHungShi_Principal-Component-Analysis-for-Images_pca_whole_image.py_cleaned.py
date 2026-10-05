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
a1 = 256
a2 = 50
a3 = 0.0001
a4 = 0.00001
a5 = 16
b1 = os.getcwd()
'''
Implement the functions that were not implemented and complete the
parts of main according to the instructions in comments.
'''
def fonk1(b13,b14,num_coeffs,b34,im_num):
    '''
    This function reconstructs an image b7 given the number of
    coefficients for each image specified by num_coeffs
    '''
    '''
        Parameters
    ---------------
    b14: np.ndarray
        a b12 x m matrix  representing the coefficients of all the image blocks.
        b12 represents the maximum dimension of the PCA space.
        m is (number of images x n_blocks**2)
    b13: np.ndarray
        an N x b12 matrix representing the basis vectors of the PCA space
        N is the dimension of the original space (number of pixels in a block)
    im_num: Integer
        index of the image to visualize
    b34: np.ndarray
        a matrix representing the mean block.
    num_coeffs: Integer
        an integer that specifies the number of top components to be
        considered while reconstructing
    n_blocks: Integer
        number of blocks comprising the image in each direction.
        For example, for a 256x256 image divided into 64x64 blocks, n_blocks will be 4
    '''
    b2 = b14[:num_coeffs,im_num]
    b3 = b13[:,:num_coeffs]
    b4 = np.dot(b3.T, b34.T)
    b5 = b2 - b4
    b6 = np.dot(b3, b5) + b34
    b7 = b6.reshape(a1, a1)
    return b7
def fonk2(b13,b14,num_coeff_array,b34,im_num):
    '''
    Plots 9 reconstructions of a particular image using b13 as the basis matrix and coeffiecient
    vectors from b14
    Parameters
    ------------------------
        num_coeff_array: Iterable
            an iterable with 9 elements representing the number of coefficients
            to use for reconstruction for each of the 9 plots
        b14: np.ndarray
            a b18 x m matrix  representing the coefficients of all blocks in a particular image
            b18 represents the dimension of the PCA space used for reconstruction
            m represents the number of blocks in an image
        b13: np.ndarray
            an N x b18 matrix representing b18 basis vectors of the PCA space
            N is the dimension of the original space (number of pixels in a block)
        n_blocks: Integer
            number of blocks comprising the image in each direction.
            For example, for a 256x256 image divided into 64x64 blocks, n_blocks will be 4
        b34: basis vectors represent the divergence from the mean so this
            matrix should be added to all reconstructed blocks
        im_num: Integer
            index of the image to visualize
    '''
    b19, b8 = plt.subplots(3,3)
    for a6 in range(3):
        for j in range(3):
            plt.axes(b8[a6,j])
            plt.imshow(fonk1(b13,b14,num_coeff_array[a6*3+j],b34,im_num), b9 = 'gray')
    b19.savefig('hw1b_{0}.png'.format(im_num))
    plt.close(b19)
def fonk3(b13, sz, imname):
    '''
    Plots the top 16 components from the basis matrix b13.
    Each basis vector represents an image block of shape (sz, sz)
    Parameters
    -------------
    b13: np.ndarray
        N x b12 matrix representing the basis vectors of the PCA space
        N is the dimension of the original space (number of pixels in a block)
        b12 represents the maximum dimension of the PCA space (assumed to be atleast 16)
    sz: Integer
        The height and width of each block
    imname: string
        name of file where image will be saved.
    '''
    b19, b8 = plt.subplots(4,4)
    for a6 in range(4):
        for j in range(4):
            plt.axes(b8[a6,j])
            plt.imshow(b13[:,a6*4+j].reshape(a1, a1), b9 = 'gray')
    b19.savefig(imname)
    plt.close(b19)
def fonk4():
    '''Read all images to the matrix b6, where b6 is a Nx256x256 array, N is the number of images'''
    os.chdir(b1+'/Fei_256')
    b10 = len([name for name in os.listdir('.') if os.path.isfile(name)])
    b6 = np.ndarray(shape = (b10-1, a1 * a1))
    a6 = 0
    for dirPath, dirNames, fileNames in os.walk(b1 + "/Fei_256"):
    	for b19 in fileNames:
    		if b19.endswith('.jpg'):
    			b11 = mpimg.imread(b19, 0)
    			b6[a6,:] = b11.flatten()
    			a6 = a6 + 1
    return b6
def fonk5(b6, num_eig, iteration, step, epsilon):
    b12 = b6.shape[1]
    b13 = np.zeros((b12, b12), dtype = np.float32)
    b14 = np.zeros(b12, dtype = np.float32)
    b15 = T.matrix('b15')
    b16 = T.vector('b16')
    b17 = T.vector('b17')
    b18 = T.scalar('b18')
    b19 = 2 * T.dot(T.dot(b16.T, b15.T), b15)
    b20 = b18 * 2 * T.dot(T.dot(b16.T, b17), b17.T)
    b21 = theano.function([b16, b15], b19)
    b22 = theano.function([b18, b16, b17], b20)
    '''Start training model until get all the eigen vectors'''
    for a6 in range(num_eig):
        b23 = np.random.normal(0,10,b12)
        b24 = b23 / np.linalg.norm(b23)
        print "Get {0}th eigen vector".format(a6)
        b25 = time.time()
        ''' Get the ith eigen vector'''
        for k in range(iteration):
            b26 = b21(b24, b6)
            b27 = np.zeros(b12)
            for j in range(a6):
                b27 = b27 + b22(b14[j], b24, b13[:, j])
            b28 = (b26 - b27)
            b29 = b24 + b28 * step
            b30 = b29 / np.linalg.norm(b29)
            print "{0}th difference: {1}".format(k, np.sum(abs(b30 - b24)))
            if abs(np.sum(b30 - b24)) < epsilon:
                b24 = b30
                break
            b24 = b30
        print "spend {0} getting eigen vector".format(time.time() - b25)
        b13[:,a6] = b24
        b14[a6] = np.dot(b21(b24, b6)/2.0, b24)
        print "b14: ", np.dot(np.dot(np.dot(b24.T, b6.T), b6), b24)
        print "b14{0} = {1}".format(a6, b14[a6])
        if a6 >= 1:
            print "difference between eigen vector", np.sum(abs(b13[:,a6] - b13[:,(a6-1)]))
    return (b13, b14)
def fonk6():
    '''
    Read here all images(grayscale) from Fei_256 folder and collapse
    each image to get an numpy array b31 with size (no_images, height*width).
    Make sure the images are read after sorting the filenames
    '''
    b31 = fonk4()
    b31 = b31.astype(np.float32)
    b32 = np.mean(b31, 0)
    b6 = b31 - np.repeat(b32.reshape(1, -1), b31.shape[0], 0)
    b13, b33 = fonk5(b6, a5, a2, a3, a4)
    '''
    Use theano to perform gradient descent to get top 16 PCA components of b6
    Put them into a matrix b13 with decreasing order of eigenvalues
    If you are not using the provided AMI and get an error "Cannot construct a ufunc with more than 32 operands" :
    You need to perform a patch to theano from this pull(https:
    Alternatively you can downgrade numpy to 1.9.3, scipy to 0.15.1, matplotlib to 1.4.2
    '''
    b14 = np.dot(b13.T, b6.T)
    os.chdir(b1 + '/output')
    for a6 in range(0, 200, 10):
        fonk2(b13 = b13, b14=b14, num_coeff_array=[1, 2, 4, 6, 8, 10, 12, 14, 16] \
                             , b34 = b32, im_num=a6)
    fonk3(b13, 256, 'hw1b_top16_256.png')
if b35 = = '__main__':
    fonk6()