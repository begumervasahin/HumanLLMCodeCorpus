import os
import numpy as np
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
bad_words = {'aed', 'oed', 'eed'}
def load_directory(directory_path, apply_stemming):
    documents = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'rb') as file:
            text = file.read().decode(errors='ignore').split()
            if apply_stemming:
                text = [porter_stemmer.stem(word) if word not in bad_words else word for word in text]
            documents.append(text)
    return documents
def load_dataset(train_directory, dev_directory, apply_stemming):
    train_ham = load_directory(os.path.join(train_directory, 'ham'), apply_stemming)
    train_spam = load_directory(os.path.join(train_directory, 'spam'), apply_stemming)
    X_train = train_ham + train_spam
    Y_train = np.array([0] * len(train_ham) + [1] * len(train_spam))
    dev_ham = load_directory(os.path.join(dev_directory, 'ham'), apply_stemming)
    dev_spam = load_directory(os.path.join(dev_directory, 'spam'), apply_stemming)
    X_dev = dev_ham + dev_spam
    Y_dev = np.array([0] * len(dev_ham) + [1] * len(dev_spam))
    return X_train, Y_train, X_dev, Y_dev
train_directory = 'path_to_train_directory'
dev_directory = 'path_to_dev_directory'
apply_stemming = True
X_train, Y_train, X_dev, Y_dev = load_dataset(train_directory, dev_directory, apply_stemming)
print("Train data:", len(X_train))
print("Dev data:", len(X_dev))
print("Train labels:", len(Y_train))
print("Dev labels:", len(Y_dev))