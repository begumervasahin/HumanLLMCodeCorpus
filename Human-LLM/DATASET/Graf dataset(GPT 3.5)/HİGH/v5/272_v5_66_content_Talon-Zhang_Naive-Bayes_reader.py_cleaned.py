
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed', 'oed', 'eed'}
def fonk1(directory_name, stemming):
    b3 = []
    for file_name in listdir(directory_name):
        b4 = directory_name + file_name
        b5 = []
        with open(b4, 'rb') as file:
            for line in file:
                b5 += line.decode(b6 = 'ignore').split(' ')
        if stemming:
            b5 = [b1.stem(word) if word not in b2 else word for word in b5]
        b3.append(b5)
    return b3
def fonk2(train_dir, dev_dir, stemming):
    b7 = fonk1(train_dir + '/ham/', stemming)
    b8 = fonk1(train_dir + '/spam/', stemming)
    b9 = b7 + b8
    b10 = np.array([0] * len(b7) + [1] * len(b8))
    b11 = fonk1(dev_dir + '/ham/', stemming)
    b12 = fonk1(dev_dir + '/spam/', stemming)
    b13 = b11 + b12
    b14 = np.array([0] * len(b11) + [1] * len(b12))
    return b9, b10, b13, b14