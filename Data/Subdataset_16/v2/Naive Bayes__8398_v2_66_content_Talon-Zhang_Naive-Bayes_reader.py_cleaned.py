
from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
b1 = PorterStemmer()
b2 = {'aed', 'oed', 'eed'}
def fonk1(directory_path, b18):
    b3 = []
    for file_name in listdir(directory_path):
        b4 = directory_path + file_name
        b5 = []
        with open(b4, 'rb') as file:
            for line in file:
                b5 += line.decode(b6 = 'ignore').split(' ')
        if b18:
            b5 = [b1.stem(word) if word not in b2 else word for word in b5]
        b3.append(b5)
    return b3
def fonk2(b16, b17, b18):
    b7 = fonk1(b16 + '/ham/', b18)
    b8 = fonk1(b16 + '/spam/', b18)
    b9 = b7 + b8
    b10 = np.array([0] * len(b7) + [1] * len(b8))
    b11 = fonk1(b17 + '/ham/', b18)
    b12 = fonk1(b17 + '/spam/', b18)
    b13 = b11 + b12
    b14 = np.array([0] * len(b11) + [1] * len(b12))
    return b9, b10, b13, b14
if b15 = = "__main__":
    b16 = "path/to/train"
    b17 = "path/to/dev"
    b18 = True
    b9, b10, b13, b14 = fonk2(b16, b17, b18)
    print("Training data loaded:")
    print(f"b9: {len(b9)} samples")
    print(f"b10: {len(b10)} labels")
    print("Test data loaded:")
    print(f"b13: {len(b13)} samples")
    print(f"b14: {len(b14)} labels")