
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
bad_words = {'aed', 'oed', 'eed'}
def load_dir(directory_path, apply_stemming):
    documents = []
    for file_name in listdir(directory_path):
        full_path = directory_path + file_name
        words = []
        with open(full_path, 'rb') as file:
            for line in file:
                words += line.decode(errors='ignore').split(' ')
        if apply_stemming:
            words = [porter_stemmer.stem(word) if word not in bad_words else word for word in words]
        documents.append(words)
    return documents
def load_dataset(train_directory, dev_directory, apply_stemming):
    train_ham = load_dir(train_directory + '/ham/', apply_stemming)
    train_spam = load_dir(train_directory + '/spam/', apply_stemming)
    X_train = train_ham + train_spam
    Y_train = np.array([0] * len(train_ham) + [1] * len(train_spam))
    test_ham = load_dir(dev_directory + '/ham/', apply_stemming)
    test_spam = load_dir(dev_directory + '/spam/', apply_stemming)
    X_test = test_ham + test_spam
    Y_test = np.array([0] * len(test_ham) + [1] * len(test_spam))
    return X_train, Y_train, X_test, Y_test
if __name__ == "__main__":
    train_directory = "path/to/train"
    dev_directory = "path/to/dev"
    apply_stemming = True
    X_train, Y_train, X_test, Y_test = load_dataset(train_directory, dev_directory, apply_stemming)
    print("Training data loaded:")
    print(f"X_train: {len(X_train)} samples")
    print(f"Y_train: {len(Y_train)} labels")
    print("Test data loaded:")
    print(f"X_test: {len(X_test)} samples")
    print(f"Y_test: {len(Y_test)} labels")