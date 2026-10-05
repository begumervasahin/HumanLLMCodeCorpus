
import pandas as pd
import numpy as np
import os
import math
import csv
import matplotlib.pyplot as plt
import struct
from scipy import stats
from PIL import Image
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,accuracy_score
from sklearn.decomposition import PCA
from KNN import KNN
class class1():
    def fonk1(self,):
        self.b1 = None
        self.b2 = (128,128)
    def fonk2(self,path, b3 = 'train'):
        b4 = os.path.join(path,
                                '%s-b7-idx1-ubyte'
                                % b3)
        b5 = os.path.join(path,
                                '%s-b10-idx3-ubyte'
                                % b3)
        with open(b4, 'rb') as lbpath:
            magic, b6 = struct.unpack('>II',
                                    lbpath.read(8))
            b7 = np.fromfile(lbpath,
                                b8 = np.uint8)
        with open(b5, 'rb') as imgpath:
            magic, num, rows, b9 = struct.unpack('>IIII',
                                                imgpath.read(16))
            b10 = np.fromfile(imgpath,
                                b8 = np.uint8).reshape(len(b7), 784)
        return b10, b7
    def fonk3(self,x,b11 = 0):
        return x.mean(b11 = b11)
    def fonk4(self,matrix):
        '''
        decompose a matrix to eigenvalue,b12 on condition of the matrix is symmetric
        '''
        eigenvalues,b12 = np.linalg.eig(matrix)
        return eigenvalues,b12
    def fonk5(self,eigenvalues,b16):
        '''
        find the most representable eigenvalues as the components
        '''
        b13 = np.argsort(eigenvalues,b3='quicksort')[::-1]
        return b13[:b16]
    def fonk6(self,b13,b12,b16):
        '''
        according to the selected eigenvalues draws b12
        '''
        return b12[:,b13[:b16]]
    def fonk7(self,x,mean):
        '''
        compute the covariance matrix
        spposes the x is in form of col vector
        b14 = sum((xi-mi)*(xi-mi)T)
        '''
        return (x-mean).T.dot((x-mean))
    def fonk8(self,samples,b19):
        return np.dot(samples,b19)
    def fonk9(self,x):
        '''
        b15 = (b15+b15')/2
        '''
        return (x+x.T)*1.0/2
    def fonk10(self,samples,b16 = 1):
        '''
        steps of principal component analasis
        '''
        print("PCA decomposition start!")
        b17 = self.fonk3(samples)
        b18 = self.fonk7(samples,b17)
        b18 = b18*1.0/samples.shape[0]
        b18 = self.fonk9(b18)
        eigenvalues,b12 = self.fonk4(b18)
        b13 = self.fonk5(eigenvalues,b16)
        b19 = self.fonk6(b13,b12,b16)
        print("number of components: ",b16)
        b20 = self.fonk8(samples,b19)
        return b20,b19
    def fonk11(self,data,b16 = "mle",svd_sovler = "full"):
        '''
        implementation of sklearn
        '''
        print("PCA decomposition start!")
        b21 = PCA(b16=b16,svd_solver="full")
        b20 = b21.fit_transform(data)
        print("number of components: ",b21.b16)
        print("explained variance ratio:\b6",b21.explained_variance_ratio_)
        return b20,b21
if b22 = ="__main__":
    b23 = r'D:/Pattern_Recognion/Exp5-10'
    b24 = os.path.join(b23,"b27")
    os.chdir(b23)
    b25 = os.path.join(b24,"mnist")
    b26 = class1()
    b27 = "mnist"
    if b27 = = "mnist":
        b35, b28 = b26.fonk2(b25,"train")
        b35, b28 = b35[:10000],b28[:10000]
        b34, b29 = b26.fonk2(b25,"t10k")
        b34, b29 = b34[:2000],b29[:2000]
        print("data loaded!")
    elif b27 = = "normal":
        b30 = np.array([[0.2331, 2.3385], [1.5207, 2.1946], [0.6499, 1.6730], [0.7757, 1.6365],
            [1.0524, 1.7844], [1.1974, 2.0155], [0.2908, 2.0681], [0.2518, 2.1213],
            [0.6682, 2.4797], [0.5622, 1.5118], [0.9023, 1.9692], [0.1333, 1.8340],
            [-0.5431, 1.8704], [0.9407, 2.2948], [-0.2126, 1.7714], [0.0507, 2.3939],
            [-0.0810, 1.5648], [0.7315, 1.9329], [0.3345, 2.2027], [1.0650, 2.4568],
            [-0.0247, 1.7523], [0.1043, 1.6991], [0.3122, 2.4883], [0.6655, 1.7259],
            [0.5838, 2.0466], [1.1653, 2.0226], [1.2653, 2.3757], [0.8137, 1.7987],
            [-0.3399, 2.0828], [0.5152, 2.0798], [0.7226, 1.9449], [-0.2015, 2.3801],
            [0.4070, 2.2373], [-0.1717, 2.1614], [-1.0573, 1.9235], [-0.2099, 2.2604]])
        b31 = np.array([[1.4010, 1.0298], [1.2301, 0.9611], [2.0814, 0.9154], [1.1655, 1.4901],
                    [1.3740, 0.8200], [1.1829, 0.9399], [1.7632, 1.1405], [1.9739, 1.0678],
                    [2.4152, 0.8050], [2.5890, 1.2889], [2.8472, 1.4601], [1.9539, 1.4334],
                    [1.2500, 0.7091], [1.2864, 1.2942], [1.2614, 1.3744], [2.0071, 0.9387],
                    [2.1831, 1.2266], [1.7909, 1.1833], [1.3322, 0.8798], [1.1466, 0.5592],
                    [1.7087, 0.5150], [1.5920, 0.9983], [2.9353, 0.9120], [1.4664, 0.7126],
                    [2.9313, 1.2833], [1.8349, 1.1029], [1.8340, 1.2680], [2.5096, 0.7140],
                    [2.7198, 1.2446], [2.3148, 1.3392], [2.0353, 1.1808], [2.6030, 0.5503],
                    [1.2327, 1.4708], [2.1465, 1.1435], [1.5673, 0.7679], [2.9414, 1.1288]])
        b32 = np.ones(b30.shape[0])
        b33 = -1*np.ones(b31.shape[0])
        b34 = np.array([[1, 1.5], [1.2, 1.0], [2.0, 0.9], [1.2, 1.5], [0.23, 2.33]])
        b35 = np.vstack((b30,b31))
        b28 = np.hstack((b32,b33))
        print("data loaded!")
    b35,b19 = b26.fonk10(b35,b16=50)
    b34 = b26.fonk8(b34,b19)
    b36 = KNN(kN = 5,method = "b36")
    b36.train(b35,b28)
    b37 = b36.predict(b34)
    acc,b38 = b36.evaluate(b37,b29)
    print("acc: {} b38:{}".format(acc,b38))