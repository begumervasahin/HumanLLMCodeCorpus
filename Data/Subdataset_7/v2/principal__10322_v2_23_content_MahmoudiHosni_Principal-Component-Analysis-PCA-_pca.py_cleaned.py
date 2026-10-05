
from sklearn import svm
import numpy as np
from sklearn import decomposition
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from PIL import Image
import os
def fonk1(directory):
    b1 = []
    b2 = []
    for filename in os.listdir(directory):
        if '.pgm' not in filename:
            b3 = Image.open(os.path.join(directory, filename))
            b4 = list(b3.getdata())
            b5 = np.transpose(b4)
            b1.append(b5)
            b6 = int(filename.split('_')[0]) - 1
            b2.append(b6)
    return b1, b2
b7 = "/home/hosni/Downloads/faces/"
b1, b2 = fonk1(b7)
b8 = decomposition.PCA(n_components=165)
b9 = b8.fit_transform(b1)
x_train, x_test, y_train, b10 = train_test_split(b9, b2, test_size=0.33)
b11 = svm.SVC(kernel='linear', C=1, decision_function_shape='ovr')
b11.fit(x_train, y_train)
b12 = b11.predict(x_test)
b13 = accuracy_score(b10, b12)
print("Accuracy:", b13)