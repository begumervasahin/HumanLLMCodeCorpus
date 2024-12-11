
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
from pydataset import b4
b1 = []
b2 = "/home/hosni/Downloads/faces/"
for filename in os.listdir(b2):
    if '.pgm' not in filename:
        b3 = Image.open(os.path.join(b2, filename))
        b4 = list(b3.getdata())
        b5 = np.transpose(b4)
        b1.append(b5)
b6 = []
a1 = 0
for i in range(0, 15):
    for j in range(0, 11):
        b6.append(a1)
    a1 += 1
b7 = decomposition.PCA(n_components=165)
b8 = b7.fit_transform(b1)
x_train, x_test, y_train, b9 = train_test_split(b8, b6, test_size=0.33)
b10 = svm.SVC(kernel='linear', C=1, decision_function_shape='ovr')
b10.fit(x_train, y_train)
b11 = b10.predict(x_test)
b12 = accuracy_score(b9, b11)
print("Accuracy:", b12)