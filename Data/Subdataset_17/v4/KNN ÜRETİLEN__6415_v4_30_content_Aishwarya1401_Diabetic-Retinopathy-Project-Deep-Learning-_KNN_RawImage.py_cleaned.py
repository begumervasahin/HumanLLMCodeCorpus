import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
path = "gray2"
files = []
image_vectors = []
labels = []
names = []
imlist = os.listdir(path)
if imlist:
    imlist = imlist[1:]
df_label = pd.read_csv('trainLabels.csv', index_col=0)
def get_label(filename):
    image_id = filename.split(os.path.sep)[-1].split(".")[0]
    label = df_label.loc[image_id].values[0]
    return int(label)
def imagevector_label():
    for file in os.listdir(path):
        files.append(file)
    files = files[1:]
    image_matrix = np.array([np.array(Image.open(os.path.join(path, file))).flatten() for file in files], 'f')
    for file in files:
        names.append(file)
        labels.append(get_label(file))
    return image_matrix, np.array(labels)
image_vectors, labels = imagevector_label()
trainRI, testRI, trainRL, testRL = train_test_split(image_vectors, labels, test_size=0.25, random_state=42)
for k in [1, 3, 5, 10, 20, 50, 100]:
    print(f"Evaluating raw pixel accuracy for k={k}...")
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(trainRI, trainRL)
    accuracy = model.score(testRI, testRL)
    print(f"Raw pixel accuracy for k={k}: {accuracy * 100:.2f}%")