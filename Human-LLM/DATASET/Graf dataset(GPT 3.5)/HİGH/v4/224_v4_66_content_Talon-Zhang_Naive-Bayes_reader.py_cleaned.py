
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed', 'oed', 'eed'}
def fonk1(directory_name, stemming):
    b3 = []
    a1 = 0
    for file_name in listdir(directory_name):
        b4 = directory_name + file_name
        b5 = []
        with open(b4, 'rb') as file:
            for line in file:
                b5 += line.decode(b6 = 'ignore').split(' ')
        if stemming:
            for i in range(len(b5)):
                if b5[i] in b2:
                    continue
                b5[i] = b1.stem(b5[i])
        b3.append(b5)
        a1 += 1
    return b3
def fonk2(train_dir, dev_dir, stemming):
    b7 = fonk1(train_dir + '/ham/', stemming)
    b8 = fonk1(train_dir + '/spam/', stemming)
    b9 = b7 + b8
    b10 = len(b7) * [0] + len(b8) * [1]
    b10 = np.array(b10)
    b11 = fonk1(dev_dir + '/ham/', stemming)
    b12 = fonk1(dev_dir + '/spam/', stemming)
    b13 = b11 + b12
    b14 = len(b11) * [0] + len(b12) * [1]
    b14 = np.array(b14)
    return b9, b10, b13, b14