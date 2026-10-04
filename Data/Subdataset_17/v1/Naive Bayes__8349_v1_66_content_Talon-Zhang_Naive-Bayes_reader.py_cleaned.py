
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
bad_words = {'aed', 'oed', 'eed'}
def loadDir(name, stemming):
    X0 = []
    for f in listdir(name):
        fullname = name + f
        text = []
        with open(fullname, 'rb') as file:
            for line in file:
                text += line.decode(errors='ignore').split(' ')
        if stemming:
            for i in range(len(text)):
                if text[i] in bad_words:
                    continue
                text[i] = porter_stemmer.stem(text[i])
        X0.append(text)
    return X0
def load_dataset(train_dir, dev_dir, stemming):
    X0 = loadDir(train_dir + '/ham/', stemming)
    X1 = loadDir(train_dir + '/spam/', stemming)
    X = X0 + X1
    Y = len(X0) * [0] + len(X1) * [1]
    Y = np.array(Y)
    X_test0 = loadDir(dev_dir + '/ham/', stemming)
    X_test1 = loadDir(dev_dir + '/spam/', stemming)
    X_test = X_test0 + X_test1
    Y_test = len(X_test0) * [0] + len(X_test1) * [1]
    Y_test = np.array(Y_test)
    return X, Y, X_test, Y_test
if __name__ == "__main__":
    train_dir = "path/to/train"
    dev_dir = "path/to/dev"
    stemming = True
    X_train, Y_train, X_test, Y_test = load_dataset(train_dir, dev_dir, stemming)
    print("Training data loaded:")
    print(f"X_train: {len(X_train)} samples")
    print(f"Y_train: {len(Y_train)} labels")
    print("Test data loaded:")
    print(f"X_test: {len(X_test)} samples")
    print(f"Y_test: {len(Y_test)} labels")