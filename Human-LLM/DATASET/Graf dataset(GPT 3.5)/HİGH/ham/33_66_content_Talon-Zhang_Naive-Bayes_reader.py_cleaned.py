
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed','oed','eed'}
def fonk1(name,stemming):
    b3 = []
    a1 = 0
    for f in listdir(name):
        b4 = name+f
        b5 = []
        with open(b4, 'rb') as f:
            for line in f:
                b5 += line.decode(b6 = 'ignore').split(' ')
        if stemming:
            for i in range(len(b5)):
                if b5[i] in b2:
                    continue
                b5[i] = b1.stem(b5[i])
        b3.append(b5)
        a1 = a1 + 1
    return b3
def fonk2(train_dir,dev_dir,stemming):
    b3 = fonk1(train_dir + '/ham/',stemming)
    b7 = fonk1(train_dir + '/spam/',stemming)
    b8 = b3 + b7
    b9 = len(b3) * [0] + len(b7) * [1]
    b9 = np.array(b9)
    b10 = fonk1(dev_dir + '/ham/',stemming)
    b11 = fonk1(dev_dir + '/spam/',stemming)
    b12 = b10 + b11
    b13 = len(b10) * [0] + len(b11) * [1]
    b13 = np.array(b13)
    return b8,b9,b12,b13