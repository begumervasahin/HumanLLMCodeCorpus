
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
bad_words = {'aed','oed','eed'}
def loadDir(name,stemming):
    X0 = []
    count = 0
    for f in listdir(name):
        fullname = name+f
        text = []
        with open(fullname, 'rb') as f:
            for line in f:
                text += line.decode(errors='ignore').split(' ')
        if stemming:
            for i in range(len(text)):
                if text[i] in bad_words:
                    continue
                text[i] = porter_stemmer.stem(text[i])
        X0.append(text)
        count = count + 1
    return X0
def load_dataset(train_dir,dev_dir,stemming):
    X0 = loadDir(train_dir + '/ham/',stemming)
    X1 = loadDir(train_dir + '/spam/',stemming)
    X = X0 + X1
    Y = len(X0) * [0] + len(X1) * [1]
    Y = np.array(Y)
    X_test0 = loadDir(dev_dir + '/ham/',stemming)
    X_test1 = loadDir(dev_dir + '/spam/',stemming)
    X_test = X_test0 + X_test1
    Y_test = len(X_test0) * [0] + len(X_test1) * [1]
    Y_test = np.array(Y_test)
    return X,Y,X_test,Y_test