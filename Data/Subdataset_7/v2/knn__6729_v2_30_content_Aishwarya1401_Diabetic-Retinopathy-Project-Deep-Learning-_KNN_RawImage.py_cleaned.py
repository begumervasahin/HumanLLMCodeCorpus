import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
def fonk1(image_name, b7):
    b1 = image_name.split(os.b6.sep)[-1].split(".")[0]
    b2 = b7.loc[[b1]].values.astype(int)[0, 0]
    return b2
def fonk2(b6, b7):
    b3 = os.listdir(b6)[1:]
    b4 = np.array([np.array(Image.open(os.b6.join(b6, file))).flatten() for file in b3], dtype='float32')
    b5 = np.array([fonk1(file, b7) for file in b3])
    return b4, b5
b6 = "gray2"
b7 = pd.read_csv('trainLabels.csv')
img_matrix, b5 = fonk2(b6, b7)
(train_images, test_images, train_labels, test_labels) = train_test_split(
    img_matrix, b5, b8 = 0.25, random_state=42)
for b9 in [1, 3, 5, 10, 20, 50, 100]:
    print("Evaluating raw pixel b11 for b9 = ", b9)
    b10 = KNeighborsClassifier(n_neighbors=b9)
    b10.fit(train_images, train_labels)
    b11 = b10.score(test_images, test_labels)
    print("Raw pixel b11: {:.2f}%".format(b11 * 100))