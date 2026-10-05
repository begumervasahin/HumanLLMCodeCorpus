import sys
import numpy as np
import scipy.cluster.vq as vq
class class1:
    def fonk1(self, classifier_type):
        '''Initialize the classifier with a given type'''
        self.b1 = classifier_type
    def fonk2(self, b2 = None):
        '''Get or set the type of the classifier'''
        if b2 is not None:
            self.b1 = b2
        return self.b1
    def fonk3(self, b3, b4):
        '''Compute the confusion matrix'''
        b3 = b3.T.tolist()[0]
        b4 = b4.T.tolist()[0]
        unique_true, b5 = np.unique(b3, return_inverse=True)
        unique_class, b6 = np.unique(b4, return_inverse=True)
        b7 = np.zeros((len(unique_true), len(unique_true)))
        for i in range(len(b4)):
            b7[b4[i], b3[i]] += 1
        return b7
    def fonk4(self, b10):
        '''Convert the confusion matrix to a printable string'''
        b8 = 'Confusion Matrix\n'
        b8 += '          '
        for i in range(b10.shape[0]):
            b8 += f" TrueC{i}"
        b9 = np.array([f"PredC{i}" for i in range(b10.shape[0])]).reshape(-1, 1)
        b10 = np.hstack((b9, b10))
        b8 += "\n"
        for row in b10:
            b8 += ' '.join(map(str, row)) + "\n"
        return b8
    def fonk5(self):
        '''Convert the classifier object to a string'''
        return str(self.b1)
class class2(class1):
    '''Class for Naive Bayes classifier'''
    def fonk6(self, b11 = None, b12=[], b15=None):
        '''Initialize Naive Bayes classifier'''
        super().fonk12('Naive Bayes class1')
        self.b12 = b12
        self.b13 = len(b12)
        self.b14 = None
        self.b15 = b15
        self.b16 = []
        self.b17 = []
        self.b18 = []
        if b11 is not None:
            b19 = b11.get_data(b12)
            self.fonk13(b19, b15)
    def fonk7(self, b19, b15):
        '''Build Naive Bayes classifier'''
        unique, b20 = np.unique(np.array(b15.T), return_inverse=True)
        self.b14 = len(unique)
        self.b13 = b19.shape[1]
        self.b15 = b15
        self.b16 = np.zeros((self.b14, self.b13))
        self.b17 = np.zeros((self.b14, self.b13))
        self.b18 = np.zeros((self.b14, self.b13))
        for i in range(self.b14):
            b21 = b19[(b20 == i), :]
            self.b16[i, :] = np.mean(b21, b22 = 0)
            self.b17[i, :] = np.var(b21, b22 = 0)
            self.b18[i, :] = 1 / (np.sqrt(2 * np.pi * self.b17[i, :]))
        return
    def fonk8(self, b19, b23 = False):
        '''Classify using Naive Bayes'''
        if b19.shape[1] != self.b16.shape[1]:
            print("Error")
            return
        b24 = np.zeros((b19.shape[0], self.b14))
        for i in range(self.b14):
            b24[:, i] = np.prod(np.multiply(self.b18[i,:], np.exp(-(np.square(b19 - self.b16[i,:]))/(2*self.b17[i,:]))), b22 = 1)
        b25 = np.argmax(b24, b22=1)
        b26 = self.b15[b25]
        if b23:
            return b25, b26, b24
        return b25, b26
    def fonk9(self):
        '''Convert class2 object to a string'''
        b8 = "\nNaive Bayes class1\n"
        for i in range(self.b14):
            b8 += f'Class {i} --------------------\n'
            b8 += f'Mean  : {self.b16[i, :]}\n'
            b8 += f'Var   : {self.b17[i, :]}\n'
            b8 += f'Scales: {self.b18[i, :]}\n'
        b8 += "\n"
        return b8
    def fonk10(self, filename):
        '''Write class2 classifier to a file'''
        pass
    def fonk11(self, filename):
        '''Read class2 classifier from a file'''
        pass
class class3(class1):
    '''Class for b28 Nearest Neighbors classifier'''
    def fonk12(self, b11 = None, b12=[], b15=None, b28=None):
        '''Initialize class3 classifier'''
        super().fonk12('class3 class1')
        self.b12 = b12
        self.b13 = len(b12)
        self.b14 = 0
        self.b15 = b15
        self.b27 = []
        if b11 is not None:
            self.b11 = b11
            b19 = b11.get_data(b12)
            self.fonk13(b19, b15)
    def fonk13(self, b19, b15, b28 = None):
        '''Build class3 classifier'''
        unique, b20 = np.unique(np.array(b15.T), return_inverse=True)
        self.b14 = len(unique)
        self.b13 = b19.shape[0]
        self.b15 = b15
        for i in range(self.b14):
            if b28 is None:
                self.b27.append(b19[(b20 = = i), :])
            else:
                codebook, b29 = vq.kmeans(b19[(b20 == i), :], b28)
                self.b27.append(codebook)
        return
    def fonk14(self, b19, b28 = 3, return_distances=False):
        '''Classify using class3'''
        b30 = np.zeros((b19.shape[0], self.b14))
        print("Classifying using class3")
        for i in range(self.b14):
            b31 = np.zeros((b19.shape[0], self.b27[i].shape[0]))
            for j in range(self.b27[i].shape[0]):
                b31[:, j] = np.sum(np.square(b19 - self.b27[i][j, :]), b22 = 1)
            b31 = np.sort(b31, b22=1)
            b30[:, i] = np.sum(b31[:, b28], b22 = 1)
        print(b30)
        b25 = np.argmin(b30, b22=1)
        b26 = self.b15[b25]
        if return_distances:
            return b25, b26, b30
        return b25, b26
    def fonk15(self):
        '''Convert class3 object to a string'''
        b8 = "\nKNN class1\n"
        for i in range(self.b14):
            b8 += f'Class {i} --------------------\n'
            b8 += f'Number of Exemplars: {self.b27[i].shape[0]}\n'
            b8 += f'Mean of Exemplars  : {np.mean(self.b27[i], b22 = 0)}\n'
        b8 += "\n"
        return b8
    def fonk16(self, filename):
        '''Write class3 classifier to a file'''
        pass
    def fonk17(self, filename):
        '''Read class3 classifier from a file'''
        pass