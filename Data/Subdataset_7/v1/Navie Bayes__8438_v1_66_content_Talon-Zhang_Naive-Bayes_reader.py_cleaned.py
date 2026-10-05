from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed', 'oed', 'eed'}
def fonk1(name, b16):
    b3 = []
    a1 = 0
    for f in listdir(name):
        b4 = name + f
        b5 = []
        with open(b4, 'rb') as file:
            for line in file:
                b5 += line.decode(b6 = 'ignore').split(' ')
        if b16:
            for i in range(len(b5)):
                if b5[i] in b2:
                    continue
                b5[i] = b1.stem(b5[i])
        b3.append(b5)
        a1 = a1 + 1
    return b3
def fonk2(b14, b15, b16):
    b3 = fonk1(b14 + '/ham/', b16)
    b7 = fonk1(b14 + '/spam/', b16)
    b8 = b3 + b7
    b9 = len(b3) * [0] + len(b7) * [1]
    b9 = np.array(b9)
    b10 = fonk1(b15 + '/ham/', b16)
    b11 = fonk1(b15 + '/spam/', b16)
    b12 = b10 + b11
    b13 = len(b10) * [0] + len(b11) * [1]
    b13 = np.array(b13)
    return b8, b9, b12, b13
b14 = 'path_to_train_directory'
b15 = 'path_to_dev_directory'
b16 = True
X_train, Y_train, b12, b13 = fonk2(b14, b15, b16)
print("Train data:", len(X_train))
print("Test data:", len(b12))
print("Train labels:", len(Y_train))
print("Test labels:", len(b13))