import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
b1 = "gray2"
b2 = pd.read_csv('trainLabels.csv')
def fonk1(image_name):
    b3 = image_name.split(os.b1.sep)[-1].split(".")[0]
    b4 = b2.loc[b2['id'] == b3, 'b4'].values[0]
    return int(b4)
def fonk2(image_path):
    b5 = os.listdir(image_path)
    b6 = np.array([np.array(Image.open(os.b1.join(image_path, file))).flatten() for file in b5], 'f')
    b7 = np.array([fonk1(file) for file in b5])
    return b6, b7
img_vectors, b7 = fonk2(b1)
train_vectors, test_vectors, train_labels, b8 = train_test_split(img_vectors, b7, test_size=0.25, random_state=42)
for b9 in [1, 3, 5, 10, 20, 50, 100]:
    print(f"Evaluating raw pixel b11 with b9 = {b9}")
    b10 = KNeighborsClassifier(n_neighbors=b9)
    b10.fit(train_vectors, train_labels)
    b11 = b10.score(test_vectors, b8)
    print(f"Raw pixel b11: {b11 * 100:.2f}%")