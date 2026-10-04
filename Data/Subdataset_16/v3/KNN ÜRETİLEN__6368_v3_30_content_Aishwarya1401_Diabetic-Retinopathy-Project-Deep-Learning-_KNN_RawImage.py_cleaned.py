import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
b1 = "gray2"
b2 = 'trainLabels.csv'
b3 = pd.read_csv(b2)
def fonk1(image_name):
    b4 = image_name.split(os.path.sep)[-1].split(".")[0]
    b5 = b3.loc[b3['id'] == b4, 'b5'].values[0]
    return int(b5)
def fonk2(image_path):
    b6 = os.listdir(image_path)
    b7 = []
    b8 = []
    for file in b6:
        b9 = Image.open(os.path.join(image_path, file))
        b10 = np.array(b9).flatten()
        b7.append(b10)
        b5 = fonk1(file)
        b8.append(b5)
    return np.array(b7, b11 = 'float32'), np.array(b8)
def fonk3(train_vectors, train_labels, test_vectors, b15, b16):
    for b12 in b16:
        print(f"Evaluating raw pixel b14 with b12 = {b12}")
        b13 = KNeighborsClassifier(n_neighbors=b12)
        b13.fit(train_vectors, train_labels)
        b14 = b13.score(test_vectors, b15)
        print(f"Raw pixel b14: {b14 * 100:.2f}%")
def fonk4():
    img_vectors, b8 = fonk2(b1)
    train_vectors, test_vectors, train_labels, b15 = train_test_split(img_vectors, b8, test_size=0.25, random_state=42)
    b16 = [1, 3, 5, 10, 20, 50, 100]
    fonk3(train_vectors, train_labels, test_vectors, b15, b16)
if b17 = = "__main__":
    fonk4()