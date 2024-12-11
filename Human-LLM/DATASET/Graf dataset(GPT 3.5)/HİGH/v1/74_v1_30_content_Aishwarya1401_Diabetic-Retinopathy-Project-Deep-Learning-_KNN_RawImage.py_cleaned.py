import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
def fonk1(i, b11):
    b1 = i.split(os.b9.sep)[-1].split(".")[0]
    b2 = b11.loc[[b1]]
    b3 = int(b2.values)
    return b3
def fonk2(b9, b11):
    b4 = []
    b5 = []
    b6 = []
    for file in os.listdir(b9):
        b4.append(file)
    b7 = b4[1:]
    b8 = np.array([np.array(Image.open(b9+'/'+file)).flatten() for file in b7],'f')
    for file in b7:
        b6.append(file)
        b5.append(fonk1(file, b11))
    return b8, np.array(b5)
b9 = "gray2"
b10 = os.listdir(b9)
b10 = b10[1:]
b11 = pd.read_csv('trainLabels.csv')
img_vect, b5 = fonk2(b9, b11)
(trainRI, testRI, trainRL, testRL) = train_test_split(
    img_vect, b5, b12 = 0.25, random_state=42)
for b13 in [1, 3, 5, 10, 20, 50, 100]:
    print("evaluating raw pixel accuracy for b13 = ", b13)
    b14 = KNeighborsClassifier(n_neighbors=b13)
    b14.fit(trainRI, trainRL)
    b15 = b14.score(testRI, testRL)
    print("raw pixel accuracy: {:.2f}%".format(b15 * 100))