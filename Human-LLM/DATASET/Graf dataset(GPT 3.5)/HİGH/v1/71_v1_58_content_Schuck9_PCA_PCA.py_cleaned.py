import os
import numpy as np
import struct
from sklearn.decomposition import PCA
from sklearn.metrics import precision_score, accuracy_score
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
    def fonk3(self, samples, b10 = 1):
        b11 = PCA(b10=b10)
        b12 = b11.fit_transform(samples)
        return b12, b11
if b13 = = "__main__":
    b14 = r'D:/Pattern_Recognion/Exp5-10'
    b15 = os.path.join(b14, "b18")
    os.chdir(b14)
    b16 = os.path.join(b15, "mnist")
    b17 = class1()
    b18 = "mnist"
    if b18 = = "mnist":
        x_train, b19 = b17.fonk2(b16, "train")
        x_train, b19 = x_train[:10000], b19[:10000]
        x_test, b20 = b17.fonk2(b16, "t10k")
        x_test, b20 = x_test[:2000], b20[:2000]
        print("Data loaded!")
        x_train_compressed, b11 = b17.fonk3(x_train, b10=50)
        b21 = b11.transform(x_test)
        b22 = KNN(kN=5, method="K_Nearest")
        b22.train(x_train_compressed, b19)
        b23 = b22.predict(b21)
        b24 = accuracy_score(b20, b23)
        b25 = precision_score(b20, b23, average='weighted')
        print("Accuracy:", b24)
        print("Precision:", b25)
    elif b18 = = "normal":
        pass
