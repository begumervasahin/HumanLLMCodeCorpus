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
        b4 = os.path.join(path, f'{b3}-b7-idx1-ubyte')
        b5 = os.path.join(path, f'{b3}-b9-idx3-ubyte')
        with open(b4, 'rb') as lb_file:
            _, b6 = struct.unpack('>II', lb_file.read(8))
            b7 = np.fromfile(lb_file, dtype=np.uint8)
        with open(b5, 'rb') as img_file:
            _, num, rows, b8 = struct.unpack('>IIII', img_file.read(16))
            b9 = np.fromfile(img_file, dtype=np.uint8).reshape(len(b7), 784)
        return b9, b7
    def fonk3(self, samples, b10 = 1):
        b11 = PCA(b10=b10)
        b12 = b11.fit_transform(samples)
        return b12, b11
if b13 = = "__main__":
    b14 = r'D:/Pattern_Recognion/Exp5-10'
    b15 = os.path.join(b14, "datasets")
    os.chdir(b14)
    b16 = os.path.join(b15, "mnist")
    b17 = class1()
    b18 = "mnist"
    if b18 = = "mnist":
        x_train, b19 = b17.fonk2(b16, "train")
        x_train, b19 = x_train[:10000], b19[:10000]
        x_test, b20 = b17.fonk2(b16, "t10k")
        x_test, b20 = x_test[:2000], b20[:2000]
        print("MNIST dataset loaded!")
        x_train_compressed, b21 = b17.fonk3(x_train, b10=50)
        b22 = b21.transform(x_test)
        b23 = KNN(kN=5, method="K_Nearest")
        b23.train(x_train_compressed, b19)
        b24 = b23.predict(b22)
        b25 = accuracy_score(b20, b24)
        b26 = precision_score(b20, b24, average='weighted')
        print("Accuracy:", b25)
        print("Precision:", b26)
    elif b18 = = "normal":
        pass