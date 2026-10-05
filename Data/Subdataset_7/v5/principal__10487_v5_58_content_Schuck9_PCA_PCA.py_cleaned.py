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
        b4 = os.path.join(path, f'{b3}-b7-idx1-ubyte')
        b5 = os.path.join(path, f'{b3}-b9-idx3-ubyte')
        with open(b4, 'rb') as lbpath:
            magic, b6 = struct.unpack('>II', lbpath.read(8))
            b7 = np.fromfile(lbpath, dtype=np.uint8)
        with open(b5, 'rb') as imgpath:
            magic, num, rows, b8 = struct.unpack('>IIII', imgpath.read(16))
            b9 = np.fromfile(imgpath, dtype=np.uint8).reshape(len(b7), 784)
        return b9, b7
    def fonk3(self, x, b10 = 0):
        return np.mean(x, b10 = b10)
    def fonk4(self, matrix):
        eigenvalues, b11 = np.linalg.eig(matrix)
        return eigenvalues, b11
    def fonk5(self, eigenvalues, b13):
        b12 = np.argsort(eigenvalues)[::-1]
        return b12[:b13]
    def fonk6(self, indices, b11, b13):
        return b11[:, indices[:b13]]
    def fonk7(self, x, mean):
        return np.cov((x - mean).T)
    def fonk8(self, samples, b17):
        return np.dot(samples, b17)
    def fonk9(self, x):
        return (x + x.T) / 2
    def fonk10(self, samples, b13 = 1):
        print("PCA decomposition start!")
        b14 = self.fonk3(samples)
        b15 = self.fonk7(samples, b14)
        b15 = self.fonk9(b15)
        eigenvalues, b11 = self.fonk4(b15)
        b16 = self.fonk5(eigenvalues, b13)
        b17 = self.fonk6(b16, b11, b13)
        print("Number of components:", b13)
        b18 = self.fonk8(samples, b17)
        return b18, b17
    def fonk11(self, data, b13 = "mle", svd_solver="full"):
        print("PCA decomposition start!")
        b19 = PCA(b13=b13, svd_solver=svd_solver)
        b18 = b19.fit_transform(data)
        print("Number of components:", b19.b13)
        print("Explained variance ratio:\b6", b19.explained_variance_ratio_)
        return b18, b19
if b20 = = "__main__":
    b21 = r'D:/Pattern_Recognition/Exp5-10'
    b22 = os.path.join(b21, "datasets")
    os.chdir(b21)
    b23 = os.path.join(b22, "mnist")
    b24 = class1()
    b25 = "mnist"
    if b25 = = "mnist":
        x_train, b26 = b24.fonk2(b23, "train")
        x_train, b26 = x_train[:10000], b26[:10000]
        b28, b27 = b24.fonk2(b23, "t10k")
        b28, b27 = b28[:2000], b27[:2000]
        print("Data loaded!")
    elif b25 = = "normal":
        print("Data loaded!")
    x_train, b17 = b24.fonk10(x_train, b13=50)
    b28 = b24.fonk8(b28, b17)
    b29 = KNN(kN=5, method="K_Nearest")
    b29.train(x_train, b26)
    b30 = b29.predict(b28)
    accuracy, b31 = b29.evaluate(b30, b27)
    print(f"Accuracy: {accuracy} Precision: {b31}")