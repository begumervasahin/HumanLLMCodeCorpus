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
b5 = pd.read_csv('trainLabels.csv', index_col=0)
def fonk1(filename):
    b6 = filename.split(os.b1.sep)[-1].split(".")[0]
    b7 = b5.loc[b6].values[0]
    return int(b7)
def fonk2():
    b8 = os.listdir(b1)[1:]
    b9 = np.array([np.array(Image.open(os.b1.join(b1, file))).flatten() for file in b8], dtype='float32')
    for file in b8:
        b4.append(file)
        b3.append(fonk1(file))
    return b9, np.array(b3)
b2, b3 = fonk2()
trainRI, testRI, trainRL, b10 = train_test_split(b2, b3, test_size=0.25, random_state=42)
for b11 in [1, 3, 5, 10, 20, 50, 100]:
    print(f"Evaluating raw pixel b13 for b11 = {b11}...")
    b12 = KNeighborsClassifier(n_neighbors=b11)
    b12.fit(trainRI, trainRL)
    b13 = b12.score(testRI, b10)
    print(f"Raw pixel b13 for b11 = {b11}: {b13 * 100:.2f}%")