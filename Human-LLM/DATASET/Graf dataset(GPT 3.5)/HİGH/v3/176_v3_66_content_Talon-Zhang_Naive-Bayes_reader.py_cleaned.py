import os
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed', 'oed', 'eed'}
def fonk1(directory_path, b14):
    b3 = []
    for file_name in os.listdir(directory_path):
        b4 = os.path.join(directory_path, file_name)
        with open(b4, 'rb') as file:
            b5 = file.read().decode(errors='ignore').split()
            if b14:
                b5 = [b1.stem(word) if word not in b2 else word for word in b5]
            b3.append(b5)
    return b3
def fonk2(b12, b13, b14):
    def fonk3(directory):
        b6 = fonk1(os.path.join(directory, 'ham'), b14)
        b7 = fonk1(os.path.join(directory, 'spam'), b14)
        b8 = b6 + b7
        b9 = np.array([0] * len(b6) + [1] * len(b7))
        return b8, b9
    X_train, b10 = fonk3(b12)
    X_dev, b11 = fonk3(b13)
    return X_train, b10, X_dev, b11
b12 = 'path_to_train_directory'
b13 = 'path_to_dev_directory'
b14 = True
X_train, b10, X_dev, b11 = fonk2(b12, b13, b14)
print("Train data:", len(X_train))
print("Dev data:", len(X_dev))
print("Train labels:", len(b10))
print("Dev labels:", len(b11))