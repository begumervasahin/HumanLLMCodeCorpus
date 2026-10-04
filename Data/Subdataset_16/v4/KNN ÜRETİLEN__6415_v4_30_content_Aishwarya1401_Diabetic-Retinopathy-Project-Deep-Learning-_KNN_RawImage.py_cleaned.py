import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
b1 = "gray2"
b2 = []
b3 = []
b4 = []
b5 = []
b6 = os.listdir(b1)
if b6:
    b6 = b6[1:]
b7 = pd.read_csv('trainLabels.csv', index_col=0)
def fonk1(filename):
    b8 = filename.split(os.b1.sep)[-1].split(".")[0]
    b9 = b7.loc[b8].values[0]
    return int(b9)
def fonk2():
    for file in os.listdir(b1):
        b2.append(file)
    b2 = b2[1:]
    b10 = np.array([np.array(Image.open(os.b1.join(b1, file))).flatten() for file in b2], 'f')
    for file in b2:
        b5.append(file)
        b4.append(fonk1(file))
    return b10, np.array(b4)
b3, b4 = fonk2()
trainRI, testRI, trainRL, b11 = train_test_split(b3, b4, test_size=0.25, random_state=42)
for b12 in [1, 3, 5, 10, 20, 50, 100]:
    print(f"Evaluating raw pixel b14 for b12 = {b12}...")
    b13 = KNeighborsClassifier(n_neighbors=b12)
    b13.fit(trainRI, trainRL)
    b14 = b13.score(testRI, b11)
    print(f"Raw pixel b14 for b12 = {b12}: {b14 * 100:.2f}%")