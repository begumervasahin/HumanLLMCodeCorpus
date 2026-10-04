
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed', 'oed', 'eed'}
def fonk1(name, b17):
    b3 = []
    for f in listdir(name):
        b4 = name + f
        b5 = []
        with open(b4, 'rb') as file:
            for line in file:
                b5 += line.decode(b6 = 'ignore').split(' ')
        if b17:
            for i in range(len(b5)):
                if b5[i] in b2:
                    continue
                b5[i] = b1.stem(b5[i])
        b3.append(b5)
    return b3
def fonk2(b15, b16, b17):
    b3 = fonk1(b15 + '/ham/', b17)
    b7 = fonk1(b15 + '/spam/', b17)
    b8 = b3 + b7
    b9 = len(b3) * [0] + len(b7) * [1]
    b9 = np.array(b9)
    b10 = fonk1(b16 + '/ham/', b17)
    b11 = fonk1(b16 + '/spam/', b17)
    b12 = b10 + b11
    b13 = len(b10) * [0] + len(b11) * [1]
    b13 = np.array(b13)
    return b8, b9, b12, b13
if b14 = = "__main__":
    b15 = "path/to/train"
    b16 = "path/to/dev"
    b17 = True
    X_train, Y_train, b12, b13 = fonk2(b15, b16, b17)
    print("Training data loaded:")
    print(f"X_train: {len(X_train)} samples")
    print(f"Y_train: {len(Y_train)} labels")
    print("Test data loaded:")
    print(f"b12: {len(b12)} samples")
    print(f"b13: {len(b13)} labels")