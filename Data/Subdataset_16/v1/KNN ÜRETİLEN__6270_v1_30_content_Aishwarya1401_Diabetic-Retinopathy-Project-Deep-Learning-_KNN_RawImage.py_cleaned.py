import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pylab
from PIL import Image
import os, sys
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
b1 = "gray2"
b2 = pd.read_csv('trainLabels.csv')
b3 = []
b4 = []
b5 = []
b6 = []
b7 = os.listdir(b1)
b7 = b7[1:]
b8 = np.array(Image.open(b1 + '/' + b7[0]))
m, b9 = b8.shape[0:2]
def fonk1(i):
    b10 = i.split(os.b1.sep)[-1].split(".")[0]
    b11 = b2.loc[[b10]]
    b12 = int(b11.values)
    return b12
def fonk2():
    for file in os.listdir(b1):
        b3.append(file)
    b13 = b3[1:]
    b14 = np.array([np.array(Image.open(b1 + '/' + file)).flatten() for file in b13], 'f')
    for file in b13:
        b6.append(file)
        b5.append(fonk1(file))
    return b14, np.array(b5)
img_vect, b15 = fonk2()
trainRI, testRI, trainRL, b16 = train_test_split(img_vect, b5, test_size=0.25, random_state=42)
for b17 in [1, 3, 5, 10, 20, 50, 100]:
    print("Evaluating raw pixel accuracy with b17 = ", b17)
    b18 = KNeighborsClassifier(n_neighbors=b17)
    b18.fit(trainRI, trainRL)
    b19 = b18.score(testRI, b16)
    print("Raw pixel accuracy: {:.2f}%".format(b19 * 100))