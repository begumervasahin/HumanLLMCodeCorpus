
import os
from PIL import Image
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
from sklearn import svm
from sklearn import multiclass
from sklearn import decomposition
from pydataset import data
image_data = []
directory = "/home/hosni/Downloads/faces/"
for filename in os.listdir(directory):
    if '.pgm' not in filename:
        image = Image.open(os.path.join(directory, filename))
        data = list(image.getdata())
        transposed_data = np.transpose(data)
        image_data.append(transposed_data)
labels = []
counter = 0
for i in range(0, 15):
    for j in range(0, 11):
        labels.append(counter)
    counter += 1
pca = decomposition.PCA(n_components=165)
reduced_image_data = pca.fit_transform(image_data)
x_train, x_test, y_train, y_test = train_test_split(reduced_image_data, labels, test_size=0.33)
clf = svm.SVC(kernel='linear', C=1, decision_function_shape='ovr')
clf.fit(x_train, y_train)
predicted_labels = clf.predict(x_test)
accuracy = accuracy_score(y_test, predicted_labels)
print("Accuracy:", accuracy)