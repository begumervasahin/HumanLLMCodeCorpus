import numpy as np
import scipy.cluster.vq as vq
class class1:
    def fonk1(self, classifier_type):
        self.b1 = classifier_type
    def fonk2(self, b2 = None):
        if b2 is not None:
            self.b1 = b2
        return self.b1
    def fonk3(self, b3, b4):
        b3 = b3.T.tolist()[0]
        b4 = b4.T.tolist()[0]
        unique_true, b5 = np.unique(b3, return_inverse=True)
        unique_classified, b6 = np.unique(b4, return_inverse=True)
        b7 = np.matrix(np.zeros((len(unique_true), len(unique_true))))
        for i in range(len(b4)):
            b7[b4[i], b3[i]] += 1
        return b7
    def fonk4(self, b10):
        b8 = 'Confusion Matrix\n'
        b8 += '          '
        for i in range(b10.shape[0]):
            b8 += f" TrueC{i}"
        b9 = np.matrix([f"PredC{i}" for i in range(b10.shape[0])]).T
        b10 = np.hstack((b9, b10))
        b8 += "\n"
        for i in range(b10.shape[0]):
            b8 += str((b10[i, :].tolist()[0])).strip('[]') + "\n"
        return b8
    def fonk5(self):
        return str(self.b1)
class class2(class1):
    def fonk6(self, b11 = None, b12=[], b15=None):
        class1.fonk12(self, 'Naive Bayes class1')
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
        unique, b20 = np.unique(np.array(b15.T), return_inverse=True)
        self.b14 = len(unique)
        self.b13 = b19.shape[1]
        self.b15 = b15
        self.b16 = np.zeros((self.b14, self.b13))
        self.b17 = np.zeros((self.b14, self.b13))
        self.b18 = np.zeros((self.b14, self.b13))
        for i in range(self.b14):
            self.b16[i, :] = np.mean(b19[(b20 = = i), :], b23=0)
            self.b17[i, :] = np.var(b19[(b20 = = i), :], b23=0)
            self.b18[i, :] = 1 / (np.sqrt(2 * np.pi * self.b17[i, :]))
        return
    def fonk8(self, b19, b21 = False):
        if b19.shape[1] != self.b16.shape[1]:
            print("Error")
            return
        b22 = np.matrix(np.zeros((b19.shape[0], self.b14)))
        for i in range(self.b14):
            b22[:, i] = np.prod(np.multiply(self.b18[i, :], np.exp(-(np.square(b19 - self.b16[i, :])) / (2 * self.b17[i, :]))), b23 = 1)
        b24 = np.argmax(b22, b23=1)
        b25 = self.b15[b24]
        if b21:
            return b24, b25, b22
        return b24, b25
    def fonk9(self):
        b8 = "\nNaive Bayes class1\n"
        for i in range(self.b14):
            b8 += f'Class {i} --------------------\n'
            b8 += 'Mean  : ' + str(self.b16[i, :]) + "\n"
            b8 += 'Var   : ' + str(self.b17[i, :]) + "\n"
            b8 += 'Scales: ' + str(self.b18[i, :]) + "\n"
        b8 += "\n"
        return b8
    def fonk10(self, filename):
        pass
    def fonk11(self, filename):
        pass
class class3(class1):
    def fonk12(self, b11 = None, b12=[], b15=None, b27=None):
        class1.fonk12(self, 'class3 class1')
        self.b12 = b12
        self.b13 = len(b12)
        self.b14 = 0
        self.b15 = b15
        self.b26 = []
        if b11 is not None:
            b19 = b11.get_data(b12)
            self.fonk13(b19, b15)
    def fonk13(self, b19, b15, b27 = None):
        unique, b20 = np.unique(np.array(b15.T), return_inverse=True)
        self.b14 = len(unique)
        self.b13 = b19.shape[0]
        self.b15 = b15
        for i in range(self.b14):
            if b27 is None:
                self.b26.append(b19[(b20 = = i), :])
            else:
                codebook, b28 = vq.kmeans(b19[(b20 == i), :], b27)
                self.b26.append(codebook)
        return
    def fonk14(self, b19, b27 = 3, return_distances=False):
        b29 = np.matrix(np.zeros((b19.shape[0], self.b14)))
        print("Classifying using class3")
        for i in range(self.b14):
            b30 = np.matrix(np.zeros((b19.shape[0], self.b26[i].shape[0])))
            for j in range(self.b26[i].shape[0]):
                b30[:, j] = np.sum(np.square(b19 - self.b26[i][j, :]), b23 = 1)
            b30 = np.sort(b30, b23=1)
            b29[:, i] = np.sum(b30[:, b27], b23 = 1)
        print(b29)
        b24 = np.argmin(b29, b23=1)
        b25 = self.b15[b24]
        if return_distances:
            return b24, b25, b29
        return b24, b25
    def fonk15(self):
        b8 = "\nKNN class1\n"
        for i in range(self.b14):
            b8 += f'Class {i} --------------------\n'
            b8 += f'Number of Exemplars: {self.b26[i].shape[0]}\n'
            b8 += 'Mean of Exemplars  :' + str(np.mean(self.b26[i], b23 = 0)) + "\n"
        b8 += "\n"
        return b8
    def fonk16(self, filename):
        pass
    def fonk17(self, filename):
        pass