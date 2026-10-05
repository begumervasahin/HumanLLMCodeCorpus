import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
def get_label(image_name, df_label):
    label_name = image_name.split(os.path.sep)[-1].split(".")[0]
    label_value = df_label.loc[[label_name]].values.astype(int)[0, 0]
    return label_value
def load_images_and_labels(path, df_label):
    files = os.listdir(path)[1:]
    images = np.array([np.array(Image.open(os.path.join(path, file))).flatten() for file in files], dtype='float32')
    labels = np.array([get_label(file, df_label) for file in files])
    return images, labels
path = "gray2"
df_label = pd.read_csv('trainLabels.csv')
img_matrix, labels = load_images_and_labels(path, df_label)
(train_images, test_images, train_labels, test_labels) = train_test_split(
    img_matrix, labels, test_size=0.25, random_state=42)
for k in [1, 3, 5, 10, 20, 50, 100]:
    print("Evaluating raw pixel accuracy for k =", k)
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(train_images, train_labels)
    accuracy = model.score(test_images, test_labels)
    print("Raw pixel accuracy: {:.2f}%".format(accuracy * 100))