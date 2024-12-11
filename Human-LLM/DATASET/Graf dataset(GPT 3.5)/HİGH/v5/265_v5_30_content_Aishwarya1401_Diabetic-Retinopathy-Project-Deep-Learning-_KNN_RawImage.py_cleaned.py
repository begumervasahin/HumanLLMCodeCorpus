import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
b1 = "gray2"
b2 = pd.read_csv('trainLabels.csv')
def fonk1(file):
    b3 = file.split(os.b1.sep)[-1].split(".")[0]
    return int(b2.loc[[b3]].values)
def fonk2():
    b4 = os.listdir(b1)[1:]
    b5 = np.array([np.array(Image.open(b1+'/'+file)).flatten() for file in b4], 'f')
    b6 = np.array([fonk1(file) for file in b4])
    return b5, b6
img_vect, b6 = fonk2()
(trainRI, testRI, trainRL, testRL) = train_test_split(
    img_vect, b6, b7 = 0.25, random_state=42
)
for b8 in [1, 3, 5, 10, 20, 50, 100]:
    print(f"Evaluating raw pixel accuracy for b8 = {b8}")
    b9 = KNeighborsClassifier(n_neighbors=b8)
    b9.fit(trainRI, trainRL)
    b10 = b9.score(testRI, testRL)
    print(f"Raw pixel accuracy for b8 = {b8}: {b10*100:.2f}%")