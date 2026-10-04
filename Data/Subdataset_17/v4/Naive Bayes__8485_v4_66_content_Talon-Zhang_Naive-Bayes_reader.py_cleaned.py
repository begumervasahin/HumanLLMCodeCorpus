
import os
import numpy as np
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
bad_words = {'aed', 'oed', 'eed'}
def loadDir(directory, stemming):
    documents = []
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        words = []
        with open(full_path, 'rb') as file:
            for line in file:
                words += line.decode(errors='ignore').split(' ')
        if stemming:
            words = [porter_stemmer.stem(word) if word not in bad_words else word for word in words]
        documents.append(words)
    return documents
def load_dataset(train_dir, dev_dir, stemming):
    X_ham = loadDir(os.path.join(train_dir, 'ham'), stemming)
    X_spam = loadDir(os.path.join(train_dir, 'spam'), stemming)
    X_train = X_ham + X_spam
    Y_train = np.array([0] * len(X_ham) + [1] * len(X_spam))
    X_test_ham = loadDir(os.path.join(dev_dir, 'ham'), stemming)
    X_test_spam = loadDir(os.path.join(dev_dir, 'spam'), stemming)
    X_test = X_test_ham + X_test_spam
    Y_test = np.array([0] * len(X_test_ham) + [1] * len(X_test_spam))
    return X_train, Y_train, X_test, Y_test
