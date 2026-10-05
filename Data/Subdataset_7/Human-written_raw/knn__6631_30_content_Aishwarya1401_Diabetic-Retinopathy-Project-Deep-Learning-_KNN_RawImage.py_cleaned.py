import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pylab
from PIL import Image
import os, sys
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
b1 = "gray2"
b2 = []
b3 = []
b4 = []
b5 = []
b6 = os.listdir(b1)
b6 = b6[1:]
b7 = np.array(Image.open(b1+'/'+b6[0]))
m,b8 = b7.shape[0:2]
b9 = pd.DataFrame.from_csv('trainLabels.csv' )
def fonk1(i):
    b10 = i.split(os.b1.sep)[-1].split(".")[0]
    b11 = b9.loc[[b10]]
    b12 = int(b11.values)
    return b12
def fonk2():
    for file in os.listdir(b1):
        b2.append(file)
    b13 = b2[1:]
    b14 = np.array([np.array(Image.open(b1+'/'+file)).flatten() for file in b13],'f')
    for file in b13:
        b5.append(file)
        b4.append(fonk1(file))
    return b14, np.array(b4)
img_vect, b15 = fonk2()
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
(trainRI, testRI, trainRL, testRL) = train_test_split(
	img_vect, b4, b16 = 0.25, random_state=42)
for k in [1, 3, 5, 10, 20, 50,100 ]:
    print("evaluating raw pixel accuracy...")
    b17 = KNeighborsClassifier(n_neighbors=k)
    b17.fit(trainRI, trainRL)
    b18 = b17.score(testRI, testRL)
    print("raw pixel accuracy: {:.2f}%".format(b18 * 100))