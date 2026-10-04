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
path = "gray2"
df_label = pd.read_csv('trainLabels.csv')
Files = []
Xlist = []
labels = []
names = []
imlist = os.listdir(path)
imlist = imlist[1:]
im = np.array(Image.open(path + '/' + imlist[0]))
m, n = im.shape[0:2]
def get_labels(i):
    l = i.split(os.path.sep)[-1].split(".")[0]
    st1 = df_label.loc[[l]]
    to_int = int(st1.values)
    return to_int
def imagevector_label():
    for file in os.listdir(path):
        Files.append(file)
    File = Files[1:]
    immatrix = np.array([np.array(Image.open(path + '/' + file)).flatten() for file in File], 'f')
    for file in File:
        names.append(file)
        labels.append(get_labels(file))
    return immatrix, np.array(labels)
img_vect, lab = imagevector_label()
trainRI, testRI, trainRL, testRL = train_test_split(img_vect, labels, test_size=0.25, random_state=42)
for k in [1, 3, 5, 10, 20, 50, 100]:
    print("Evaluating raw pixel accuracy with k =", k)
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(trainRI, trainRL)
    acc = model.score(testRI, testRL)
    print("Raw pixel accuracy: {:.2f}%".format(acc * 100))