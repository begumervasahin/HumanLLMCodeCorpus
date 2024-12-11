import os
import struct
import numpy as np
from sklearn.decomposition import PCA
from KNN import KNN
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = (128, 128)
    def fonk2(self, path, b3 = 'train'):
        b4 = os.path.join(path, '%s-b7-idx1-ubyte' % b3)
        b5 = os.path.join(path, '%s-b9-idx3-ubyte' % b3)
        with open(b4, 'rb') as lbpath:
            magic, b6 = struct.unpack('>II', lbpath.read(8))
            b7 = np.fromfile(lbpath, dtype=np.uint8)
        with open(b5, 'rb') as imgpath:
            magic, num, rows, b8 = struct.unpack('>IIII', imgpath.read(16))
            b9 = np.fromfile(imgpath, dtype=np.uint8).reshape(len(b7), 784)
        return b9, b7
    def fonk3(self, x, b10 = 0):
        return x.mean(b10 = b10)
    def fonk4(self, matrix):
        eigenvalues, b11 = np.linalg.eig(matrix)
        return eigenvalues, b11
    def fonk5(self, eigenvalues, b13):
        b12 = np.argsort(eigenvalues, b3='quicksort')[::-1]
        return b12[:b13]
    def fonk6(self, b12, b11, b13):
        return b11[:, b12[:b13]]
    def fonk7(self, x, mean):
        return (x - mean).T.dot((x - mean))
    def fonk8(self, samples, b16):
        return np.dot(samples, b16)
    def fonk9(self, x):
        return (x + x.T) * 1.0 / 2
    def fonk10(self, samples, b13 = 1):
        print("PCA decomposition start!")
        b14 = self.fonk3(samples)
        b15 = self.fonk7(samples, b14)
        b15 = b15 * 1.0 / samples.shape[0]
        b15 = self.fonk9(b15)
        eigenvalues, b11 = self.fonk4(b15)
        b12 = self.fonk5(eigenvalues, b13)
        b16 = self.fonk6(b12, b11, b13)
        print("number of components: ", b13)
        b17 = self.fonk8(samples, b16)
        return b17, b16
    def fonk11(self, data, b13 = "mle", svd_solver="full"):
        print("PCA decomposition start!")
        b18 = PCA(b13=b13, svd_solver="full")
        b17 = b18.fit_transform(data)
        print("number of components: ", b18.b13)
        print("explained variance ratio:\b6", b18.explained_variance_ratio_)
        return b17, b18
if b19 = = "__main__":
    b20 = r'D:/Pattern_Recognion/Exp5-10'
    b21 = os.path.join(b20, "b24")
    os.chdir(b20)
    b22 = os.path.join(b21, "mnist")
    b23 = class1()
    b24 = "mnist"
    if b24 = = "mnist":
        x_train, b25 = b23.fonk2(b22, "train")
        x_train, b25 = x_train[:10000], b25[:10000]
        b27, b26 = b23.fonk2(b22, "t10k")
        b27, b26 = b27[:2000], b26[:2000]
        print("data loaded!")
    elif b24 = = "normal":
        print("data loaded!")
    x_train, b16 = b23.fonk10(x_train, b13=50)
    b27 = b23.fonk8(b27, b16)
    b28 = KNN(kN=5, method="b28")
    b28.train(x_train, b25)
    b29 = b28.predict(b27)
    acc, b30 = b28.evaluate(b29, b26)
    print("acc: {} b30:{}".format(acc, b30))