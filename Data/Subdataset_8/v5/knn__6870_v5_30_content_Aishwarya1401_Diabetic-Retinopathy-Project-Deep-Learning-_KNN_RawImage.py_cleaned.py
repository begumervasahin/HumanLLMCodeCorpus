import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
path = "gray2"
df_label = pd.read_csv('trainLabels.csv')
def get_labels(file):
    label = file.split(os.path.sep)[-1].split(".")[0]
    return int(df_label.loc[[label]].values)
def load_images_and_labels():
    files = os.listdir(path)[1:]
    images = np.array([np.array(Image.open(path+'/'+file)).flatten() for file in files], 'f')
    labels = np.array([get_labels(file) for file in files])
    return images, labels
img_vect, labels = load_images_and_labels()
(trainRI, testRI, trainRL, testRL) = train_test_split(
    img_vect, labels, test_size=0.25, random_state=42
)
for k in [1, 3, 5, 10, 20, 50, 100]:
    print(f"Evaluating raw pixel accuracy for k = {k}")
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(trainRI, trainRL)
    acc = model.score(testRI, testRL)
    print(f"Raw pixel accuracy for k = {k}: {acc*100:.2f}%")