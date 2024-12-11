import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
def fonk1(image_name, b8):
    b1 = image_name.split(os.b7.sep)[-1].split(".")[0]
    b2 = b8.loc[[b1]].values.astype(int)[0, 0]
    return b2
def fonk2(b7, b8):
    b3 = os.listdir(b7)[1:]
    b4 = np.array([np.array(Image.open(os.b7.join(b7, file))).flatten() for file in b3], dtype='float32')
    b5 = np.array([fonk1(file, b8) for file in b3])
    return b4, b5
if b6 = = "__main__":
    b7 = "gray2"
    b8 = pd.read_csv('trainLabels.csv')
    img_matrix, b5 = fonk2(b7, b8)
    train_images, test_images, train_labels, b9 = train_test_split(
        img_matrix, b5, b10 = 0.25, random_state=42)
    for b11 in [1, 3, 5, 10, 20, 50, 100]:
        print("Evaluating raw pixel b13 for b11 = ", b11)
        b12 = KNeighborsClassifier(n_neighbors=b11)
        b12.fit(train_images, train_labels)
        b13 = b12.score(test_images, b9)
        print("Raw pixel b13: {:.2f}%".format(b13 * 100))