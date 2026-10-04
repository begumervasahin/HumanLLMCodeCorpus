import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
path = "gray2"
df_label = pd.read_csv('trainLabels.csv')
def get_label(image_name):
    image_id = image_name.split(os.path.sep)[-1].split(".")[0]
    label = df_label.loc[df_label['id'] == image_id, 'label'].values[0]
    return int(label)
def load_images_and_labels(image_path):
    files = os.listdir(image_path)
    image_vectors = np.array([np.array(Image.open(os.path.join(image_path, file))).flatten() for file in files], 'f')
    labels = np.array([get_label(file) for file in files])
    return image_vectors, labels
img_vectors, labels = load_images_and_labels(path)
train_vectors, test_vectors, train_labels, test_labels = train_test_split(img_vectors, labels, test_size=0.25, random_state=42)
for k in [1, 3, 5, 10, 20, 50, 100]:
    print(f"Evaluating raw pixel accuracy with k = {k}")
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(train_vectors, train_labels)
    accuracy = model.score(test_vectors, test_labels)
    print(f"Raw pixel accuracy: {accuracy * 100:.2f}%")