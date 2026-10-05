import os
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed', 'oed', 'eed'}
def fonk1(directory_path, b16):
    b3 = []
    for file_name in os.listdir(directory_path):
        b4 = os.path.join(directory_path, file_name)
        with open(b4, 'rb') as file:
            b5 = file.read().decode(errors='ignore').split()
            if b16:
                b5 = [b1.stem(word) if word not in b2 else word for word in b5]
            b3.append(b5)
    return b3
def fonk2(b14, b15, b16):
    b6 = fonk1(os.path.join(b14, 'ham'), b16)
    b7 = fonk1(os.path.join(b14, 'spam'), b16)
    b8 = b6 + b7
    b9 = np.array([0] * len(b6) + [1] * len(b7))
    b10 = fonk1(os.path.join(b15, 'ham'), b16)
    b11 = fonk1(os.path.join(b15, 'spam'), b16)
    b12 = b10 + b11
    b13 = np.array([0] * len(b10) + [1] * len(b11))
    return b8, b9, b12, b13
b14 = 'path_to_train_directory'
b15 = 'path_to_dev_directory'
b16 = True
b8, b9, b12, b13 = fonk2(b14, b15, b16)
print("Train data:", len(b8))
print("Dev data:", len(b12))
print("Train labels:", len(b9))
print("Dev labels:", len(b13))